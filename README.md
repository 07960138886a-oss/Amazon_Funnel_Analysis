<h1 align="center">Amazon Funnel Analysis</h1>

1. Project Introduction                 
An end-to-end e-commerce funnel analytics project that uses Python to analyze Amazon user behavior data, track stage-to-stage session drop-offs, analyze multi-dimensional drop-off drivers, and deliver strategic recommendations to boost conversion rates and sales.

2. Executive Summary & Key Metrics
Analytic overview across a customer interaction base of 10,000 sessions (21,676 event records) during 2026-07-15 to 2026-08-14:              
(1) Key Metrics:                      
1,068 Total Orders | 10.68% Overall Conversion Rate | $1,179,313.12 Total Revenue | $1,104.23 Average Order Value (AOV).        
(2) Primary Funnel Bottlenecks:       
The Purchases stage experienced the highest drop-off rate (70.11% drop-off from Basket Adds to Purchases overall), representing significant cart abandonment across the user journey.
 <img width="917" height="365" alt="截屏2026-08-14 20 10 51" src="https://github.com/user-attachments/assets/a8081f53-e452-4325-9cb3-3075bc59ef04" />.       
This pattern also occurs across each segmented dimension (channels, devices, regions, and product categories).        
(3) Performance Highlights:       
    <table border="0">
  <tr>
    <td align="center" width="33%">
      <b>Sponsored Brands</b><br>
      <sub>Top Marketing Channel (11.10% CVR)</sub>
    </td>
    <td align="center" width="33%">
      <b>HomeDecor</b><br>
      <sub>Best Product Category (11.85% CVR)</sub>
    </td>
    <td align="center" width="33%">
      <b>Northern Ireland</b><br>
      <sub>Leading Regional Market (11.26% CVR)</sub>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top">
      <img src="https://github.com/user-attachments/assets/52f2f5f9-bce3-480e-b28f-29d326a3eec1" width="100%" />
    </td>
    <td align="center" valign="top">
      <img src="https://github.com/user-attachments/assets/8d53f270-92fc-4c41-87c2-e3031ce1ff7b" width="100%" />
    </td>
    <td align="center" valign="top">
      <img src="https://github.com/user-attachments/assets/acf662f4-ca14-4f43-b768-c1d4f22530a8" width="100%" />
    </td>
  </tr>
</table>           




        
3\. Pipeline Architecture & Tech Stack           
[ Raw Data Generation ] ──> [ Session Aggregation (Pandas) ] ──> [ Funnel & KPI Modeling ] ──> [ Multi-Dimensional Analysis ] ──> [ Interactive Visualization & Insights ]             
(1) Data Preparation & Data Cleaning: Python (Pandas, Numpy, Datetime)                 
(2) Behavioral & Funnel Analytics: Python (Pandas, Aggregation, Time-series modeling)               
(3) Data Visualization: Python (Matplotlib, Seaborn, Plotly), Power BI.                  

4\. User Funnel Performance Dashboards & Drop-off Diagnostics               
<table border="0" width="100%">
  <tr>
    <td align="center" width="50%"><b>(1) User Funnel Performance Dashboard</b></td>
    <td align="center" width="50%"><b>(2) Funnel Drop-off Diagnostics</b></td>
  </tr>
  <tr>
    <td align="center" width="50%">
      <img src="https://github.com/user-attachments/assets/99e64e24-9aed-4f8d-ba50-a06189971b7f" style="width:100%;" />
    </td>
    <td align="center" width="50%">
      <img src="https://github.com/user-attachments/assets/f72c2a22-5d76-4d8a-8249-c7d9a9c18ae8" style="width:100%;" />
    </td>
  </tr>
</table>
<a href="./1funnel%20analysis.pbix">Click here to download the interactive Power BI report (.pbix)</a>.          
 

5\. Python Code & Analytical Implementation           
(1) Synthetic Data Generation & Data Cleaning         
Generated 10,000 user session records using Faker with custom event conditional probabilities.       
Data quality checks, timestamp transformations, and duration calculations were executed seamlessly.       
View simulated raw dataset: [amazon_funnel_analysis_data.csv](./amazon_funnel_analysis_data.csv).       
(2) Session-Level Aggregation & Multi-Dimensional EDA         
Aggregated raw event logs into session-level records (`session_summary`) to evaluate conversion rates, drop-off rates, and Revenue per Session (RPS) across channels, devices, product categories, regions, and time periods.        
View the full analysis & Python implementation and outputs: [Amazon_Funnel_Analysis.ipynb](./Amazon_Funnel_Analysis.ipynb)

6\. Strategic Recommendations       
(1) Cart Abandonment Recovery: Address the 70.11% drop-off at the Purchases stage by streamlining checkout UX and launching automated cart abandonment email campaigns, unlocking an estimated $2,766,724.01 in potential revenue recovery.       
(2) Budget Optimization: Reallocate marketing spend toward high-ROI channels, prioritizing Sponsored Brands (11.10% CVR) and Sponsored Products.       
(3) Regional Strategy Replication: Benchmark and replicate successful promotional strategies from Northern Ireland (11.26% CVR) across lower-performing markets such as England (10.26% CVR).        
(4) Category Promotion: Increase homepage visibility and ad placements for top-converting categories like HomeDecor (11.85% CVR) and Bedding (11.35% CVR).           
