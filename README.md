# ETL Data Pipeline 
  E-commerce Data Processing


## Description
This project is a simple end-to-end ETL pipeline built using Python. It takes raw data from an external API, stores it in a raw (Bronze) layer, then cleans and transforms it into structured datasets in the Silver layer. Finally, it creates aggregated business-ready tables in the Gold layer for analysis.

The idea behind this project was to understand how real-world data pipelines work and how raw data is gradually converted into useful insights.


## Benefit
The main benefit of this pipeline is that it automates the entire flow from data extraction to final reporting tables. It reduces manual work, keeps the data structured, and makes it easier to track changes using batch IDs.

It also helps in building a clear understanding of how data engineering systems are structured in real companies.


## Outcome
At the end of the pipeline, raw API data gets converted into clean datasets and finally into business-level summary tables. These Gold tables can be directly used for analysis or dashboards.

So instead of dealing with raw messy data, we get clean and meaningful outputs like category summaries and top products.


## Achievement
Through this project, I was able to build a working ETL system that includes:
- API data extraction
- Data cleaning and transformation
- Layered storage (Bronze, Silver, Gold)
- Final aggregation into SQL-ready tables

It helped strengthen my understanding of how data flows through different stages in a pipeline.


## Architecture
The pipeline follows a simple layered structure:

Raw data is first fetched from an API and stored in JSON format in the Bronze layer. This data is then cleaned and converted into structured CSV files in the Silver layer. Finally, the Silver data is used to generate aggregated business insights, which are stored as Gold tables.

So the flow looks like:

API → Bronze → Silver → Gold → SQL Tables


## Modules Used
Python, Pandas, Requests, JSON, YAML, Pathlib, MySQL Connector