# Sentinel for Sustainable Fisheries
# NAUTILUS: Neural Analysis of Unlawful Trawling & Illegal Underwater Surveillance

The "One-Liner": Use satellite imagery (SAR, optical) and AIS data with multimodal deep learning to detect and predict illegal, unreported, and unregulated (IUU) fishing activity in near real-time.

## The Problem 
IUU fishing accounts for ~20% of global catch, devastating marine ecosystems, economies, and food security; current monitoring is sparse, reactive, and relies on manual analysis of disconnected data streams.

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
