# 📦 Supply Chain & Inventory Decision Analytics

An end-to-end **Decision Analytics project** that analyzes historical sales, inventory, demand patterns, and supplier performance to support **demand forecasting, inventory planning, replenishment decisions, and supply-chain risk analysis**.

The project combines **Python, SQL, statistical forecasting, inventory analytics, and Power BI** to transform raw operational data into actionable business insights.

---

## 🎯 Project Objective

The main objective is to answer four business questions:

1. **How much demand should we expect in the future?**
2. **How much inventory should we maintain?**
3. **Which products require replenishment?**
4. **Which suppliers may create delivery-related inventory risk?**

The overall decision flow is:

```text
Historical Sales & Inventory Data
            ↓
       Data Cleaning
            ↓
       Exploratory Analysis
            ↓
      Demand Forecasting
            ↓
        SARIMA Model
            ↓
       Safety Stock
            ↓
       Reorder Point
            ↓
   Replenishment Recommendation
            ↓
    Supplier Performance
            ↓
      Power BI Dashboard
```

---

## 🛠️ Technologies Used

| Technology           | Purpose                                     |
| -------------------- | ------------------------------------------- |
| **Python**           | Data processing, analysis, forecasting      |
| **Pandas**           | Data manipulation and aggregation           |
| **NumPy**            | Numerical calculations                      |
| **Matplotlib**       | Data visualization                          |
| **Seaborn**          | Exploratory visualization                   |
| **Scikit-learn**     | Forecast evaluation metrics                 |
| **Statsmodels**      | Exponential Smoothing and SARIMA            |
| **SQL**              | Sales, inventory, and supplier analysis     |
| **Power BI**         | Interactive business intelligence dashboard |
| **Jupyter Notebook** | Analysis and experimentation                |

---

# 📊 Dataset

The project uses a synthetic **5-year supply-chain dataset** covering:

* **2021–2025**
* **50 products**
* **5 warehouses**
* **10 suppliers**
* Daily observations
* Approximately **456,500 records**

### Main fields

```text
Date
Product_ID
Product_Name
Category
Warehouse
Region
Supplier_ID
Supplier_Name
Units_Sold
Unit_Cost
Unit_Price
Revenue
COGS
Gross_Margin
Inventory_Level
Safety_Stock
Reorder_Point
Stockout_Flag
Order_Quantity
Lead_Time_Days
Delivery_Days
Promotion_Flag
```

The dataset was designed to simulate realistic supply-chain conditions such as changing demand, inventory fluctuations, stockouts, supplier lead-time variation, and seasonal demand patterns.

---

# 🔎 Exploratory Data Analysis

The EDA stage analyzes:

* Demand trends
* Monthly and yearly demand
* Product-level demand
* Demand volatility
* Inventory levels
* Inventory value
* Inventory turnover
* Days of inventory
* Stockout frequency
* Supplier delivery performance
* Late deliveries
* Lead-time variation
* Correlation between operational variables

### Key observations

The analysis identified:

* Demand growth across the 2021–2025 period
* Higher demand during November and December
* Different levels of demand volatility across products
* Products experiencing recurring stockouts
* Significant variation in supplier delivery times
* Higher safety-stock requirements for products with greater demand variability

---

# 📈 Demand Forecasting

Three forecasting approaches were evaluated:

1. Moving Average
2. Exponential Smoothing
3. SARIMA

A **30-day holdout period** was used to evaluate forecasting performance.

### Forecast comparison

| Model                 |  Avg. MAE | Avg. RMSE | Avg. MAPE |
| --------------------- | --------: | --------: | --------: |
| Moving Average        |     30.96 |     38.85 |     9.52% |
| Exponential Smoothing |     26.54 |     32.93 |     7.91% |
| **SARIMA**            | **25.63** | **31.96** | **7.71%** |

SARIMA achieved the lowest average MAE, RMSE, and MAPE in the evaluation.

It was the best-performing model for **40 out of 50 products** based on the selected comparison metric.

Therefore, SARIMA was selected as the primary forecasting approach for the inventory-planning stage.

### Important

Model selection was based on **out-of-sample forecasting performance**, rather than choosing the most complex model.

---

# 📦 Inventory Analytics

The inventory analysis uses demand variability and supplier lead time to estimate inventory requirements.

## Safety Stock

The project uses a service-level-based safety-stock calculation:

```text
Safety Stock =
Z × Demand Standard Deviation × √Lead Time
```

For a 95% service level:

```text
Z = 1.65
```

---

## 🔄 Reorder Point

The reorder point is calculated as:

```text
Reorder Point =
Average Daily Demand × Lead Time
+ Safety Stock
```

The inventory position is then compared with the calculated reorder point.

```text
Current Inventory <= Reorder Point
              ↓
           REORDER
```

Otherwise:

```text
Current Inventory > Reorder Point
              ↓
         NO REORDER
```

---

# 🛒 Replenishment Recommendation

The initial inventory recommendation uses a 30-day planning horizon.

The project then incorporates the SARIMA forecast to make the recommendation forecast-driven.

```text
30-Day SARIMA Forecast
          +
      Safety Stock
          ↓
   Target Inventory
          ↓
Target Inventory - Current Inventory
          ↓
Recommended Order Quantity
```

Negative order quantities are clipped to zero.

This converts forecasting results into a practical replenishment decision.

---

# 🚚 Supplier Performance Analytics

Supplier analysis evaluates:

* Average lead time
* Average delivery time
* Maximum delivery time
* Delivery variability
* Late delivery rate
* On-time delivery rate
* Products supplied
* Total units associated with each supplier

### Late delivery calculation

A delivery is classified as late when:

```text
Delivery Days > Lead Time Days
```

The project also creates a delivery-risk classification using project-defined thresholds:

```text
Late Delivery Rate < 10%
        ↓
      LOW

10%–20%
        ↓
     MEDIUM

≥ 20%
        ↓
      HIGH
```

These thresholds are used as **project decision rules**, not as universal industry standards.

---

# 📊 Power BI Dashboard

The Power BI dashboard converts the analytical results into an interactive decision-support interface.

## 🖼️ Dashboard Preview

### Executive Overview

![Supply Chain Decision Analytics Dashboard Preview](dashboard/dashboard_preview.png)

*Interactive Power BI dashboard showing supply-chain KPIs, monthly demand and revenue trends, product reorder status, and supplier delivery risk.*

The dashboard is designed to provide a management-level view of the current supply-chain situation while allowing users to drill into demand, inventory, and supplier performance.

> **Note:** The preview image is a visual representation of the dashboard design. The actual `.pbix` report contains the interactive Power BI visuals connected to the project data.

---

## Page 1 — Executive Overview

Provides a high-level view of the supply chain.

### KPI Cards

* Total Revenue
* Total Units Sold
* Stockout Rate
* Products Requiring Reorder
* Total Recommended Order

### Visualizations

* Monthly Demand / Revenue Trend
* Product Reorder Status
* Supplier Delivery Risk
* Product and warehouse filters
* Date and category filters

---

## Page 2 — Demand Forecast

Shows:

* Historical demand
* SARIMA forecast
* Product-level forecast
* MAE
* RMSE
* MAPE
* Forecast comparison

Users can select individual products to inspect demand behavior and forecast results.

---

## Page 3 — Inventory & Reorder

Focuses on inventory decisions.

### Key metrics

* Current Inventory
* Safety Stock
* Reorder Point
* Forecast Demand
* Recommended Order Quantity
* Reorder Decision

The page provides an actionable table showing which products require replenishment and the estimated order quantity.

---

## Page 4 — Supplier Performance

Analyzes supplier reliability using:

* Average Lead Time
* Average Delivery Days
* Late Delivery Rate
* On-Time Delivery Rate
* Delivery Variability
* Delivery Risk

This helps connect supplier performance with inventory-planning risk.

---

# 📁 Project Structure

```text
supply-chain-decision-analytics/
│
├── data/
│   ├── raw/
│   │   └── supply_chain_master.csv
│   │
│   └── processed/
│       ├── forecast_model_comparison.csv
│       ├── inventory_reorder_analysis.csv
│       └── supplier_performance.csv
│
├── sql/
│   ├── sales_analysis.sql
│   ├── inventory_analysis.sql
│   └── supplier_analysis.sql
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_demand_forecasting.ipynb
│   └── 03_supplier_analysis.ipynb
│
├── src/
│   ├── forecasting.py
│   ├── inventory.py
│   ├── safety_stock.py
│   ├── reorder.py
│   └── supplier.py
│
├── dashboard/
│   ├── supply_chain_dashboard.pbix
│   └── dashboard_preview.png
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone <your-github-repository-url>
cd supply-chain-decision-analytics
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 📓 Run the Analysis

Start Jupyter Notebook:

```bash
jupyter notebook
```

Run the notebooks in the following order:

```text
01_eda.ipynb
       ↓
02_demand_forecasting.ipynb
       ↓
03_supplier_analysis.ipynb
```

The notebooks perform:

```text
Data Loading
    ↓
EDA
    ↓
Forecast Model Evaluation
    ↓
SARIMA Forecast
    ↓
Inventory Calculations
    ↓
Reorder Recommendations
    ↓
Supplier Analysis
```

---

# 🧮 Example Reorder Calculation

For a product with:

```text
Average Daily Demand = 30 units
Lead Time = 5 days
Demand Std = 10 units
Z = 1.65
```

Safety stock:

```text
1.65 × 10 × √5
≈ 36.90 units
```

Reorder point:

```text
30 × 5 + 36.90
≈ 186.90 units
```

If current inventory is below the reorder point, the system recommends replenishment.

---

# 💡 Business Value

The project demonstrates how operational data can be converted into business decisions.

Instead of simply reporting:

```text
"Inventory is low."
```

the system provides:

```text
Product
   ↓
Expected Future Demand
   ↓
Required Safety Stock
   ↓
Reorder Point
   ↓
Current Inventory
   ↓
Recommended Order Quantity
```

Similarly, instead of simply reporting supplier delivery times, the analysis identifies suppliers with higher late-delivery rates and delivery variability that may contribute to replenishment risk.

---

# 🚀 Future Improvements

The current project can be extended with:

* Product + Warehouse-level inventory optimization
* Forecasting by warehouse
* More advanced safety-stock calculations incorporating lead-time variability
* Dynamic service-level optimization
* Economic Order Quantity (EOQ)
* ABC inventory classification
* Slow-moving and dead-stock analysis
* Promotion-aware demand forecasting
* Automated Power BI refresh
* SQL database integration
* Real-time inventory feeds
* Cost-based optimization of reorder quantities
* Scenario analysis for changes in lead time and demand
* Automated alerts for high-risk products and suppliers

---

# 📌 Key Learning Outcomes

This project demonstrates practical experience with:

* Business problem formulation
* Data cleaning and transformation
* Exploratory data analysis
* Time-series forecasting
* Model evaluation
* Inventory optimization concepts
* Safety-stock calculation
* Reorder-point analysis
* Supplier performance analytics
* SQL-based analysis
* Business KPI development
* Power BI dashboard development
* Translating analytical results into business decisions

---

# 👨‍💻 Project Focus

**Primary Area:** Decision Analytics

**Business Domains:**

```text
Supply Chain
Inventory Management
Demand Forecasting
Procurement
Supplier Analytics
Business Intelligence
```

**Core Technologies:**

```text
Python | SQL | Power BI | Pandas | NumPy | Statsmodels | Scikit-learn
```

---

## 📌 Project Summary

> **Supply Chain & Inventory Decision Analytics** is an end-to-end analytics solution that combines demand forecasting, inventory planning, supplier performance analysis, and Power BI visualization to support data-driven replenishment decisions.

The project demonstrates the complete journey from **raw operational data → analytical models → business recommendations → interactive decision dashboard**.
