import requests
import datetime
import tempfile

def get_satellite_image(lat, lon, date_str, buffer_km=10):
    """
    Fetches a free Sentinel-2 image using Microsoft Planetary Computer Open Data.
    No API keys, no accounts, no billing required.
    """
    print(f"Fetching free open-source satellite data for {date_str}...")
    
    # 1. Calculate a rough Bounding Box based on the buffer
    # 1 degree of latitude/longitude is roughly 111 km
    offset = (buffer_km / 111.0)
    bbox = [lon - offset, lat - offset, lon + offset, lat + offset]

    # 2. Format Dates (Search 15 days prior to the target date for a clear image)
    target_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    start_date = (target_date - datetime.timedelta(days=15)).strftime("%Y-%m-%dT00:00:00Z")
    end_date = target_date.strftime("%Y-%m-%dT23:59:59Z")
    time_range = f"{start_date}/{end_date}"

    # 3. Query the Open Data API
    url = "https://planetarycomputer.microsoft.com/api/stac/v1/search"
    payload = {
        "collections": ["sentinel-2-l2a"],
        "bbox": bbox,
        "datetime": time_range,
        "query": {"eo:cloud_cover": {"lt": 20}}, # Less than 20% clouds
        "limit": 1
    }
    
    try:
        response = requests.post(url, json=payload, timeout=15)
        data = response.json()
        
        if "features" not in data or len(data["features"]) == 0:
            print("No clear images found. Try increasing the cloud limit or changing the date.")
            return None, None, bbox, None
            
        item = data["features"][0]
        
        # 4. Get the pre-rendered visual thumbnail link
        img_url = item["assets"]["rendered_preview"]["href"]
        capture_date = item["properties"]["datetime"][:10]
        
        # 5. Download the image locally for YOLO to process
        print("Downloading image for YOLO processing...")
        img_response = requests.get(img_url)
        output_path = tempfile.NamedTemporaryFile(suffix='.png', delete=False).name
        
        with open(output_path, 'wb') as f:
            f.write(img_response.content)
            
        print("Image downloaded successfully!")
        return output_path, img_url, bbox, capture_date
        
    except Exception as e:
        print(f"API Error: {e}")
        return None, None, bbox, None