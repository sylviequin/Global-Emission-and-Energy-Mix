# Energy consumption by source - Data package

This data package contains the data that powers the chart ["Energy consumption by source"](https://ourworldindata.org/grapher/energy-consumption-by-source-and-country?v=1&csvType=full&useColumnShortNames=false) on the Our World in Data website.

## CSV Structure

The high level structure of the CSV file is that each row is an observation for an entity (usually a country or region) and a timepoint (usually a year).

The first two columns in the CSV file are "Entity" and "Code". "Entity" is the name of the entity (e.g. "United States"). "Code" is the OWID internal entity code that we use if the entity is a country or region. For normal countries, this is the same as the [iso alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) code of the entity (e.g. "USA") - for non-standard countries like historical countries these are custom codes.

The third column is either "Year" or "Day". If the data is annual, this is "Year" and contains only the year as an integer. If the column is "Day", the column contains a date string in the form "YYYY-MM-DD".

The remaining columns are the data columns, each of which is a time series. If the CSV data is downloaded using the "full data" option, then each column corresponds to one time series below. If the CSV data is downloaded using the "only selected data visible in the chart" option then the data columns are transformed depending on the chart type and thus the association with the time series might not be as straightforward.

## Metadata.json structure

The .metadata.json file contains metadata about the data package. The "charts" key contains information to recreate the chart, like the title, subtitle etc.. The "columns" key contains information about each of the columns in the csv, like the unit, timespan covered, citation for the data etc..

## About the data

Our World in Data is almost never the original producer of the data - almost all of the data we use has been compiled by others. If you want to re-use data, it is your responsibility to ensure that you adhere to the sources' license and to credit them correctly. Please note that a single time series may have more than one source - e.g. when we stich together data from different time periods by different producers or when we calculate per capita metrics using population data from a second source.

### How we process data at Our World In Data
All data and visualizations on Our World in Data rely on data sourced from one or several original data providers. Preparing this original data involves several processing steps. Depending on the data, this can include standardizing country names and world region definitions, converting units, calculating derived indicators such as per capita measures, as well as adding or adapting metadata such as the name or the description given to an indicator.
[Read about our data pipeline](https://docs.owid.io/projects/etl/)

## Detailed information about each time series


## Other renewables (including geothermal and biomass)
Input-equivalent energy, in terawatt-hours, is based on gross generation and does not account for cross-border electricity supply.
Last updated: June 27, 2025  
Next update: June 2026  
Date range: 1965–2024  
Unit: terawatt-hours  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
Energy Institute - Statistical Review of World Energy (2025) – with major processing by Our World in Data

#### Full citation
Energy Institute - Statistical Review of World Energy (2025) – with major processing by Our World in Data. “Other renewables (including geothermal and biomass)” [dataset]. Energy Institute, “Statistical Review of World Energy” [original data].
Source: Energy Institute - Statistical Review of World Energy (2025) – with major processing by Our World In Data

### Source

#### Energy Institute – Statistical Review of World Energy
Retrieved on: 2025-06-27  
Retrieved from: https://www.energyinst.org/statistical-review/  

#### Notes on our processing step for this indicator
* Primary energy consumption is expressed in input-equivalents (using the [substitution method](#dod:substitutionmethod)). For "other renewables", we divide gross electricity generation by a factor of 0.32, which reflects an assumed efficiency of 32% for typical biomass power plants — the dominant source of electricity in this category globally. This approach follows the methodology used by the Statistical Review of World Energy up to the 2024 release. In 2025, the Statistical Review switched to the Physical Energy Content method to calculate Total Energy Supply. For now, we continue to use the substitution method to maintain consistency across our articles and charts.


## Biofuels consumption
Includes biogasoline (such as ethanol) and biodiesel. Volumes have been adjusted for energy content.
Last updated: June 27, 2025  
Next update: June 2026  
Date range: 1965–2024  
Unit: terawatt-hours  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
Energy Institute - Statistical Review of World Energy (2025) – with major processing by Our World in Data

#### Full citation
Energy Institute - Statistical Review of World Energy (2025) – with major processing by Our World in Data. “Biofuels consumption” [dataset]. Energy Institute, “Statistical Review of World Energy” [original data].
Source: Energy Institute - Statistical Review of World Energy (2025) – with major processing by Our World In Data

### Source

#### Energy Institute – Statistical Review of World Energy
Retrieved on: 2025-06-27  
Retrieved from: https://www.energyinst.org/statistical-review/  


## Solar consumption
Input-equivalent energy, in terawatt-hours, is based on gross generation and does not account for cross-border electricity supply.
Last updated: June 27, 2025  
Next update: June 2026  
Date range: 1965–2024  
Unit: terawatt-hours  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
Energy Institute - Statistical Review of World Energy (2025) – with major processing by Our World in Data

#### Full citation
Energy Institute - Statistical Review of World Energy (2025) – with major processing by Our World in Data. “Solar consumption” [dataset]. Energy Institute, “Statistical Review of World Energy” [original data].
Source: Energy Institute - Statistical Review of World Energy (2025) – with major processing by Our World In Data

### Source

#### Energy Institute – Statistical Review of World Energy
Retrieved on: 2025-06-27  
Retrieved from: https://www.energyinst.org/statistical-review/  

#### Notes on our processing step for this indicator
* Primary energy consumption is expressed in input-equivalents (using the [substitution method](#dod:substitutionmethod)). For nuclear, hydro, solar, and wind, we divide gross electricity generation by a time-dependent thermal efficiency factor (around 41% in recent years). This represents the average efficiency of fossil fuel power plants globally and reflects the amount of fuel that would have been required to produce the same electricity in such plants. This approach follows the methodology used by the Statistical Review of World Energy up to the 2024 release. In 2025, the Statistical Review switched to the Physical Energy Content method to calculate Total Energy Supply. For now, we continue to use the substitution method to maintain consistency across our articles and charts.


## Wind consumption
Input-equivalent energy, in terawatt-hours, is based on gross generation and does not account for cross-border electricity supply.
Last updated: June 27, 2025  
Next update: June 2026  
Date range: 1965–2024  
Unit: terawatt-hours  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
Energy Institute - Statistical Review of World Energy (2025) – with major processing by Our World in Data

#### Full citation
Energy Institute - Statistical Review of World Energy (2025) – with major processing by Our World in Data. “Wind consumption” [dataset]. Energy Institute, “Statistical Review of World Energy” [original data].
Source: Energy Institute - Statistical Review of World Energy (2025) – with major processing by Our World In Data

### Source

#### Energy Institute – Statistical Review of World Energy
Retrieved on: 2025-06-27  
Retrieved from: https://www.energyinst.org/statistical-review/  

#### Notes on our processing step for this indicator
* Primary energy consumption is expressed in input-equivalents (using the [substitution method](#dod:substitutionmethod)). For nuclear, hydro, solar, and wind, we divide gross electricity generation by a time-dependent thermal efficiency factor (around 41% in recent years). This represents the average efficiency of fossil fuel power plants globally and reflects the amount of fuel that would have been required to produce the same electricity in such plants. This approach follows the methodology used by the Statistical Review of World Energy up to the 2024 release. In 2025, the Statistical Review switched to the Physical Energy Content method to calculate Total Energy Supply. For now, we continue to use the substitution method to maintain consistency across our articles and charts.


## Hydropower consumption
Input-equivalent energy is based on gross generation and does not account for cross-border electricity supply.
Last updated: June 27, 2025  
Next update: June 2026  
Date range: 1965–2024  
Unit: terawatt-hours  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
Energy Institute - Statistical Review of World Energy (2025) – with major processing by Our World in Data

#### Full citation
Energy Institute - Statistical Review of World Energy (2025) – with major processing by Our World in Data. “Hydropower consumption” [dataset]. Energy Institute, “Statistical Review of World Energy” [original data].
Source: Energy Institute - Statistical Review of World Energy (2025) – with major processing by Our World In Data

### Source

#### Energy Institute – Statistical Review of World Energy
Retrieved on: 2025-06-27  
Retrieved from: https://www.energyinst.org/statistical-review/  

#### Notes on our processing step for this indicator
* Primary energy consumption is expressed in input-equivalents (using the [substitution method](#dod:substitutionmethod)). For nuclear, hydro, solar, and wind, we divide gross electricity generation by a time-dependent thermal efficiency factor (around 41% in recent years). This represents the average efficiency of fossil fuel power plants globally and reflects the amount of fuel that would have been required to produce the same electricity in such plants. This approach follows the methodology used by the Statistical Review of World Energy up to the 2024 release. In 2025, the Statistical Review switched to the Physical Energy Content method to calculate Total Energy Supply. For now, we continue to use the substitution method to maintain consistency across our articles and charts.


## Nuclear consumption
Input-equivalent energy is based on gross generation and does not account for cross-border electricity supply.
Last updated: June 27, 2025  
Next update: June 2026  
Date range: 1965–2024  
Unit: terawatt-hours  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
Energy Institute - Statistical Review of World Energy (2025) – with major processing by Our World in Data

#### Full citation
Energy Institute - Statistical Review of World Energy (2025) – with major processing by Our World in Data. “Nuclear consumption” [dataset]. Energy Institute, “Statistical Review of World Energy” [original data].
Source: Energy Institute - Statistical Review of World Energy (2025) – with major processing by Our World In Data

### Source

#### Energy Institute – Statistical Review of World Energy
Retrieved on: 2025-06-27  
Retrieved from: https://www.energyinst.org/statistical-review/  

#### Notes on our processing step for this indicator
* Primary energy consumption is expressed in input-equivalents (using the [substitution method](#dod:substitutionmethod)). For nuclear, hydro, solar, and wind, we divide gross electricity generation by a time-dependent thermal efficiency factor (around 41% in recent years). This represents the average efficiency of fossil fuel power plants globally and reflects the amount of fuel that would have been required to produce the same electricity in such plants. This approach follows the methodology used by the Statistical Review of World Energy up to the 2024 release. In 2025, the Statistical Review switched to the Physical Energy Content method to calculate Total Energy Supply. For now, we continue to use the substitution method to maintain consistency across our articles and charts.


## Gas consumption
Last updated: June 27, 2025  
Next update: June 2026  
Date range: 1965–2024  
Unit: terawatt-hours  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
Energy Institute - Statistical Review of World Energy (2025) – with major processing by Our World in Data

#### Full citation
Energy Institute - Statistical Review of World Energy (2025) – with major processing by Our World in Data. “Gas consumption” [dataset]. Energy Institute, “Statistical Review of World Energy” [original data].
Source: Energy Institute - Statistical Review of World Energy (2025) – with major processing by Our World In Data

### What you should know about this data
* Excludes natural gas converted to liquid fuels but includes derivatives of coal as well as natural gas consumed in Gas-to-Liquids transformation. The difference between the world consumption figures and the world production statistics is due to variations in stocks at storage facilities and liquefaction plants, together with unavoidable disparities in the definition, measurement or conversion of gas supply and demand data.

### Source

#### Energy Institute – Statistical Review of World Energy
Retrieved on: 2025-06-27  
Retrieved from: https://www.energyinst.org/statistical-review/  


## Coal consumption
Last updated: June 27, 2025  
Next update: June 2026  
Date range: 1965–2024  
Unit: terawatt-hours  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
Energy Institute - Statistical Review of World Energy (2025) – with major processing by Our World in Data

#### Full citation
Energy Institute - Statistical Review of World Energy (2025) – with major processing by Our World in Data. “Coal consumption” [dataset]. Energy Institute, “Statistical Review of World Energy” [original data].
Source: Energy Institute - Statistical Review of World Energy (2025) – with major processing by Our World In Data

### What you should know about this data
* Includes commercial solid fuels only, i.e. bituminous coal and anthracite (hard coal), and lignite and brown (sub-bituminous) coal, and other commercial solid fuels. Excludes coal converted to liquid or gaseous fuels, but includes coal consumed in transformation processes. Differences between the consumption figures and the world production statistics are accounted for by stock changes, and unavoidable disparities in the definition, measurement or conversion of coal supply and demand data.

### Source

#### Energy Institute – Statistical Review of World Energy
Retrieved on: 2025-06-27  
Retrieved from: https://www.energyinst.org/statistical-review/  


## Oil consumption
Last updated: June 27, 2025  
Next update: June 2026  
Date range: 1965–2024  
Unit: terawatt-hours  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
Energy Institute - Statistical Review of World Energy (2025) – with major processing by Our World in Data

#### Full citation
Energy Institute - Statistical Review of World Energy (2025) – with major processing by Our World in Data. “Oil consumption” [dataset]. Energy Institute, “Statistical Review of World Energy” [original data].
Source: Energy Institute - Statistical Review of World Energy (2025) – with major processing by Our World In Data

### What you should know about this data
* Includes inland demand plus international aviation and marine bunkers and refinery fuel and loss. Consumption of biogasoline (such as ethanol) and biodiesel are excluded while derivatives of coal and natural gas are included. Differences between the world consumption figures and world production statistics are accounted for by stock changes, consumption of non-petroleum additives and substitute fuels and unavoidable disparities in the definition, measurement or conversion of oil supply and demand data.

### Source

#### Energy Institute – Statistical Review of World Energy
Retrieved on: 2025-06-27  
Retrieved from: https://www.energyinst.org/statistical-review/  


    