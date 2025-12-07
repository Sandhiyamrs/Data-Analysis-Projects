# Power BI Dashboards
Upload `.pbix` visual dashboards here.

# 📊 Power BI Reports

This folder contains Power BI report guidance & artifacts for the project.  
**Note:** `.pbix` binary files are not included here (build them in Power BI Desktop). This README contains instructions, data schemas, DAX examples and recommended visuals to reproduce the reports.

## Reports planned
- `customer_churn.pbix` — Customer retention & churn analysis
- `marketing_campaign.pbix` — Campaign performance and ROI

## How to reproduce
1. Open Power BI Desktop.
2. Load the prepared data files (CSV, Excel, SQL query, or direct DB).
3. Build the data model (relationships) according to the schema below.
4. Create measures using the example DAX measures provided.
5. Add visuals and format pages as described.
6. Save the file as `customer_churn.pbix` and `marketing_campaign.pbix`.
7. (Optional) Publish to Power BI Service and set scheduled refresh.

## Data sources / schemas
Place dataset files in `/powerbi/data/` or connect to your DB.

### Customer table (customers.csv)
- CustomerID (string/int)
- SignupDate (date)
- Country (string)
- Segment (string)

### Orders table (orders.csv)
- OrderID
- CustomerID
- OrderDate
- Revenue (decimal)
- Cost (decimal)
- ProductCategory

### Campaign table (campaigns.csv)
- CampaignID
- CampaignName
- StartDate
- EndDate
- Spend (decimal)
- Channel (string)

### CampaignPerformance table (campaign_perf.csv)
- CampaignID
- Date
- Impressions
- Clicks
- Conversions
- RevenueAttributable

## Suggested report pages & visuals

### `customer_churn.pbix` pages
1. Overview
   - KPI cards: Total Customers, Active Customers (period), New Customers (period), Churn Rate (period)
   - Line chart: Customers over time (cumulative)
   - Donut: Customers by Segment or Country
2. Churn Analysis
   - Cohort chart (heatmap) showing retention by signup month
   - Bar chart: Churn rate by segment / country
   - Table with top churn reasons (if survey data available)
3. Revenue Impact
   - Waterfall: Revenue lost due to churn vs revenue gained from new
   - Trend chart: ARPU by cohort
4. Actionable Insights
   - Recommendation list (text box)
   - Drill-through to specific customer lists (table)

### `marketing_campaign.pbix` pages
1. Campaign Overview
   - KPI cards: Total Spend, Total Conversions, Total Revenue, ROAS (Return on ad spend)
   - Bar/stacked bar: Spend by Channel
   - Line chart: Spend vs Revenue over time
2. Channel Performance
   - Table: Campaign, Channel, Spend, Impressions, Clicks, Conversions, CTR, CVR, ROAS
   - Scatter: Impressions vs Conversions (size = Spend)
3. Funnel / Attribution
   - Funnel visual: Impressions → Clicks → Conversions
   - Attribution (if multi-touch data exists): compare attribution models
4. ROI & Recommendations
   - What-if slicer for spend increase and projected conversions
   - Top performing campaigns list

## Example DAX measures
(see `dax_examples.txt` for copy/paste)

## Automation & Publishing
- Publish each `.pbix` to Power BI Service workspace.
- Configure dataset scheduled refresh (Gateway if on-prem).
- Use Power BI REST API or Power BI Export to File API to automate PDF exports.
- Embed reports to internal web app or Streamlit with iframe (Power BI Embedded).

## Files in this folder
- `dax_examples.txt` — ready-to-copy DAX measures
- `data/` — place CSV/Excel data here
- `powerbi_build_instructions.md` — step-by-step build guide
