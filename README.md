# End-to-End ETL Pipeline: Excel → Python → PostgreSQL → Power BI


This project demonstrates a complete data workflow starting from multiple Excel flat files, transforming them using Python ETL scripts, storing them in a PostgreSQL Data Warehouse, and finally visualizing the results in Power BI.

---

## 📊 Tables Included

The pipeline processes **five different datasets**, each stored as separate Excel files:

| Table Name     | Description                                     | File Type |
|----------------|-------------------------------------------------|-----------|
| **AHT**        | Average Handle Time performance data            | Excel     |
| **CSAT**       | Customer Satisfaction scores                    | Excel   
| **Productivity** | Agent productivity metrics                    | Excel     |
| **Roster**     | Agent schedule / staffing information           | Excel     |
| **SLA**        | Service Level Agreement performance             | Excel     |

Each dataset goes through its own dedicated ETL pipeline written in Python.

---

## 🛠️ ETL Process (Python)

Every table has a **separate ETL script**:

```
etl/
├── AHT.py
├── CSAT.py
├── Prod.py
├── Roster.py
└── SLA.py
```

### 🚀 ETL Steps
1. **Extract** raw Excel data  
2. **Clean/Transfor** Basic data cleaning and transformation
4. **Load** the final cleaned dataset into PostgreSQL

Python libraries used:

- `pandas`
- `sqlalchemy`
- `psycopg2-binary`
- `openpyxl`
- `numpy`

---

## 🗄️ Data Warehouse (PostgreSQL)

A PostgreSQL database is used as the **central data warehouse**.

All 5 tables are loaded into structured relational tables.  


```


## 📈 Power BI Visualization

After the data is stored in PostgreSQL, Power BI connects directly to the database to build:

- KPIs  
- Time-series trends  
- SLA performance  
- Productivity dashboards  
- CSAT visualizations  
- Workforce management insights (Roster)


```
dashboards/BPO Dashboard.pbix
```

---

## ⚙️ How to Run

### 1️⃣ Install dependencies
```
pip install -r requirements.txt
```

### 2️⃣ Set up environment variables  
Create a `.env` file using `config_example.env` as a guide (PostgreSQL credentials).

### 3️⃣ Run ETL scripts
Example:
```
python etl/AHT.py
python etl/CSAT.py
...
```

### 4️⃣ Load data into PostgreSQL  
Ensure your database is running, then the ETL scripts will insert records automatically.

### 5️⃣ Connect Power BI to PostgreSQL  
Use the **PostgreSQL connector** and build your visual dashboards.

---

## 📬 Contact

If you have questions or want to collaborate, feel free to reach out!

