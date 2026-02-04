# NAUTILUS: Neural Analysis of Unlawful Trawling & Illegal Underwater Surveillance

**NAUTILUS** is an AI-powered maritime surveillance system that fuses multi-source satellite data (Synthetic Aperture Radar, optical imagery, Automatic Identification System) with oceanographic data to detect, classify, and predict illegal fishing activities in near real-time. It transforms disparate, raw data streams into actionable intelligence for maritime authorities and environmental agencies.

## The Problem 
Illegal, Unreported, and Unregulated (IUU) fishing represents 20-30% of global catch (worth $10-23 billion annually), leading to:
1. Ecological Collapse: Overfishing, bycatch mortality, and habitat destruction
2. Economic Loss: Legitimate fisheries lose revenue; coastal communities suffer
3. Security Threats: IUU vessels often engage in trafficking and slavery
4. Food Security: Depletes protein sources for 3 billion people

### Current Limitations
- Manual Monitoring: Analysts manually review AIS data and satellite imagery
- Data Silos: SAR, optical, AIS, and environmental data aren't integrated
- Reactive Response: Detection occurs weeks/months after the event
- "Dark Vessels": Vessels that disable AIS transponders become invisible
- High False Positives: Weather conditions mimic vessel signatures in SAR

## Key Features & System Components
### 1. Detection Module
1. Dark Vessel Detection
2. Identify vessels in SAR imagery when AIS is turned off
3. Differentiate vessels from ocean clutter, wind farms, islands
4. Multi-Sensor Fusion
5. Correlate SAR detections with optical imagery (Sentinel-2)
6. Cross-reference with historical AIS patterns of known vessels

### 2. Classification Module
Vessel Type Classification
Distinguish between fishing vessels, cargo ships, tankers
Sub-classify fishing vessels (trawlers, longliners, purse seiners)
Behavior Classification
Detect fishing patterns: transshipment, loitering, pair trawling
Identify rendezvous events (potential illegal transfers)

C. Prediction & Risk Assessment
Risk Scoring Engine

Assign risk scores to vessels based on multiple factors

Prioritize high-risk targets for limited patrol resources

Predictive Hotspot Mapping

Forecast high-probability IUU zones 24-72 hours in advance

Incorporate environmental factors (chlorophyll, sea temp)

D. Intelligence Dashboard
Interactive Web Interface

Real-time vessel tracking with risk overlays

Historical pattern analysis and anomaly alerts

Evidence packages for law enforcement

Automated Reporting

Daily intelligence briefs

Monthly compliance reports for regulatory bodies


## The Tech Stack:

Primary Domain: Geospatial ML + Computer Vision + Time Series.

## Model Architecture: 
A two-stage multimodal model. 
### Stage 1: A Vision Transformer (ViT) or U-Net processes Sentinel-1 (SAR) and Sentinel-2 (optical) imagery to detect vessel presence in "dark" areas (AIS off). 
### Stage 2: A Temporal Fusion Transformer (TFT) ingests sequential AIS data, historical IUU reports, and oceanographic data (sea temp, chlorophyll) to classify vessel behavior (loitering, transshipment) and predict high-risk zones.

**[Subject to change]**

## The Data Strategy:

Satellite Imagery: Copernicus Open Access Hub (Sentinel-1 SAR, Sentinel-2 optical).

Vessel Tracking: Global Fishing Watch's public AIS data.

Ocean Context: NOAA ERDDAP servers for sea surface temperature, chlorophyll-a.

Ground Truth: Global IUU vessel lists from NGOs like Trygg Mat Tracking.
