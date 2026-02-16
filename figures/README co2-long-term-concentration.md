# Carbon dioxide concentration in the atmosphere - Data package

This data package contains the data that powers the chart ["Carbon dioxide concentration in the atmosphere"](https://ourworldindata.org/grapher/co2-long-term-concentration?time=1330..2024&v=1&csvType=filtered&useColumnShortNames=false) on the Our World in Data website. It was downloaded on February 16, 2026.

### Active Filters

A filtered subset of the full data was downloaded. The following filters were applied:
- time: 1330..2024

## CSV Structure

The high level structure of the CSV file is that each row is an observation for an entity (usually a country or region) and a timepoint (usually a year).

The first two columns in the CSV file are "Entity" and "Code". "Entity" is the name of the entity (e.g. "United States"). "Code" is the OWID internal entity code that we use if the entity is a country or region. For most countries, this is the same as the [iso alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) code of the entity (e.g. "USA") - for non-standard countries like historical countries these are custom codes.

The third column is either "Year" or "Day". If the data is annual, this is "Year" and contains only the year as an integer. If the column is "Day", the column contains a date string in the form "YYYY-MM-DD".

The final column is the data column, which is the time series that powers the chart. If the CSV data is downloaded using the "full data" option, then the column corresponds to the time series below. If the CSV data is downloaded using the "only selected data visible in the chart" option then the data column is transformed depending on the chart type and thus the association with the time series might not be as straightforward.


## Metadata.json structure

The .metadata.json file contains metadata about the data package. The "charts" key contains information to recreate the chart, like the title, subtitle etc.. The "columns" key contains information about each of the columns in the csv, like the unit, timespan covered, citation for the data etc..

## About the data

Our World in Data is almost never the original producer of the data - almost all of the data we use has been compiled by others. If you want to re-use data, it is your responsibility to ensure that you adhere to the sources' license and to credit them correctly. Please note that a single time series may have more than one source - e.g. when we stich together data from different time periods by different producers or when we calculate per capita metrics using population data from a second source.

## Detailed information about the data


## Annual concentration of atmospheric carbon dioxide
Measured in parts per million.
Last updated: January 14, 2026  
Next update: March 2026  
Date range: 803719 BCE – 2024 CE  
Unit: parts per million  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
NOAA Global Monitoring Laboratory - Trends in Atmospheric Carbon Dioxide (2026); EPA based on various sources (2022) – with major processing by Our World in Data

#### Full citation
NOAA Global Monitoring Laboratory - Trends in Atmospheric Carbon Dioxide (2026); EPA based on various sources (2022) – with major processing by Our World in Data. “Annual concentration of atmospheric carbon dioxide” [dataset]. NOAA Global Monitoring Laboratory, “Trends in Atmospheric Carbon Dioxide”; United States Environmental Protection Agency, “Climate Change Indicators: Atmospheric Concentrations of Greenhouse Gases” [original data].
Source: NOAA Global Monitoring Laboratory - Trends in Atmospheric Carbon Dioxide (2026), EPA based on various sources (2022) – with major processing by Our World In Data

### What you should know about this data
* Based on ice core studies of historical concentration of greenhouse gases, and recent air monitoring sites around the world.

### How is this data described by its producer - NOAA Global Monitoring Laboratory - Trends in Atmospheric Carbon Dioxide (2026), EPA based on various sources (2022)?
This indicator describes how the levels of major greenhouse gases (GHGs) in the atmosphere have changed over geological time and in recent years. Changes in atmospheric GHGs, in part caused by human activities, affect the amount of energy held in the Earth-atmosphere system and thus affect the Earth's climate. This indicator is highly relevant to climate change because greenhouse gases from human activities are the primary driver of observed climate change since the mid-20th century (IPCC, 2021).

### Sources

#### NOAA Global Monitoring Laboratory – Trends in Atmospheric Carbon Dioxide
Retrieved on: 2026-01-14  
Retrieved from: https://gml.noaa.gov/ccgg/trends/gl_data.html  

#### United States Environmental Protection Agency – Climate Change Indicators: Atmospheric Concentrations of Greenhouse Gases
Retrieved on: 2024-04-17  
Retrieved from: https://19january2025snapshot.epa.gov/climate-indicators/climate-change-indicators-atmospheric-concentrations-greenhouse-gases/  


    