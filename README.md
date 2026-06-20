Amazon-Prime-DE-DBT-DLT-Project

Amazon Prime Data Engineering Pipeline (DLT + dbt + PostgreSQL)

Built an end-to-end data engineering pipeline to ingest, transform, and model Amazon Prime dataset using modern ELT tools and a warehouse-centric architecture.

Designed and implemented a modular data pipeline using DLT (data load tool) to extract data from a SQLite source and load it into PostgreSQL, followed by transformation and modeling using dbt.

🔧 Key Components:

Data Ingestion (DLT):

Extracted structured data from SQLite database
Loaded raw data into PostgreSQL with automatic schema handling

Data Warehouse (PostgreSQL):

Organized raw ingestion layer in analytics_raw schema
Managed incremental loads and schema evolution

Transformations (dbt):

Built staging and transformation models using dbt
Implemented incremental models for efficient processing
Created clean analytical layer (analytics) for reporting-ready data
Data Modeling:
Structured data into standardized columns (dates, casts, types, ratings, etc.)
Handled data quality issues like nulls and invalid date formats

⚙️ Tech Stack:

Python
DLT (Data Load Tool)
dbt (Data Build Tool)
PostgreSQL
SQLite
SQL

📊 Outcome:

Fully automated ELT pipeline from raw ingestion to transformed analytics layer
Modular architecture separating ingestion, transformation, and modeling
Production-style dbt project with incremental processing and source tracking
