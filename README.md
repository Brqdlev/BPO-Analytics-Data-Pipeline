# BPO Performance Analytics Data Warehouse Project

## 📌 Project Overview

This project showcases a foundational **ETL-based analytics pipeline** built to analyze **Business Process Outsourcing (BPO)** performance metrics.

The pipeline ingests data from **Excel flat files**, performs basic transformations using **Python**, loads the processed data into **PostgreSQL as a data warehouse**, and delivers insights through **Power BI dashboards**.  
The project focuses on transforming operational metrics into actionable business insights.

---

## 🏗️ Architecture

**High-level flow:**


---

## 🗂️ Data Sources (BPO Domain)

The dataset represents common **BPO operational and workforce performance metrics**, including:

- **AHT (Average Handle Time)** – Average time to resolve customer interactions  
- **CSAT (Customer Satisfaction)** – Customer satisfaction scores  
- **SLA (Service Level Agreement)** – Compliance with service targets  
- **Productivity** – Agent efficiency and output metrics   

---

## 🔄 Data Pipeline Details

### 1. Source Data – Flat Files
- Excel spreadsheets used as the raw data source
- Simulates real-world reporting and operational exports
- Multiple metrics across different time periods and teams

---

### 2. Python ETL
- Extracts data from Excel files
- Performs basic transformations:
  - Data cleaning and formatting
  - Column renaming and standardization
- Loads transformed data into PostgreSQL

---

### 3. PostgreSQL – Data Warehouse
- Centralized storage for analytics
- Structured tables optimized for reporting
- Acts as the single source of truth
- Enables SQL-based analysis and BI integration

---

## 📊 Business Intelligence (Power BI)

- Power BI connected directly to PostgreSQL
- Dashboards provide visibility into:
  - Operational performance trends
  - SLA compliance
  - Customer satisfaction metrics
  - Workforce productivity
- Designed for managers and operations stakeholders

---

## 🛠️ Tech Stack Summary

| Layer | Tools |
|-----|------|
| Data Source | Excel (Flat Files) |
| ETL | Python |
| Data Warehouse | PostgreSQL |
| BI | Power BI |
| Programming | Python, SQL |

---

## 🎯 Key Learnings & Outcomes

- Built a complete **ETL pipeline** from flat files
- Designed a basic **data warehouse schema**
- Gained hands-on experience with **PostgreSQL**
- Created **business-focused dashboards**
- Translated operational metrics into actionable insights

---

## 🚀 Future Improvements

- Automate file ingestion
- Add incremental loads
- Introduce data quality checks
- Implement dimensional modeling (star schema)
- Add historical snapshotting for trend analysis

---

## 📎 Author

**Bradley Alojado**  
Soon to be Data Engineer / Analytics Engineer  
Portfolio Project #1

---

