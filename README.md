# Satellite-Validation-1
Preparing the data for validation 



The data is a time series of ground observations for a variable called Aerosol Optical Depth (AOD). We want to use this to validate the satellite data. 

The AOD observations are typically taken every 15 min, while the satellite overpass time is 10-11.
To make sure that we are not comparing Apples to Oranges, we need to aggregate the ground measurement data (i.e File) and take only the observation near the overpass time of the satellite. 
![ ](https://github.com/RawanAloula/Satellite-Validation-1/blob/master/agg%20viz.png)

This is done in two steps:

* first the ground measurement data (i.e File) is aggregated and saved for exploratory analysis. 
* second, we filter the data to the overpass time. 
