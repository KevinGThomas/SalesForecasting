# SalesForecasting
Consumer Packaged Goods Sales Forecasting project for ReconAI

# Overview
This is the full code for 'CPG Sales Forecasting'. This code helps to identify current sales and predict the forecast for the rest of the year with the current sales numbers. It also identifies the GAP between Actual Sales+forecast versus the initial yearly plan. It identifies the market share in the retailers, products and regions perspective.

# Dependencies
* Database ReconAI in MySQL
* pandas
* matplotlib
* pymysql
* os
* datetime
* decimal
* PyAF (git+git://github.com/antoinecarme/pyaf.git)

# Concept
## Hierarchical Forecasting
Time series can often be naturally disaggregated by various attributes of
interest. For example, the total number of products sold by a
manufacturer can be disaggregated by Retailers such as SuperMart,
BigCo and Rx. Each of these can be disaggregated into finer categories.
For example, SuperMart can be divided into North region, East region,
South region, and West region. These categories are nested within the
larger group categories, and so the collection of time series follow a
hierarchical aggregation structure. Therefore, we refer to these as
“hierarchical time series”.
Here, we use forecasting of large collections of time series that must add
up in some way. The challenge is that we require forecasts that
are coherent across the aggregation structure. That is, we require
forecasts to add up in a manner that is consistent with the aggregation
structure of the collection of time series.

## The Bottom-up Approach
A simple method for generating coherent forecasts is the bottom-up
approach. This approach involves first generating forecasts for each
series at the bottom-level, and then summing these to produce forecasts
for all the series in the structure.

![bigco_graph](https://user-images.githubusercontent.com/20180559/48884364-3345c080-ee4a-11e8-9ac9-614931e6c1b7.png)

For example, for the hierarchy given above, we first generate h-step-ahead
forecasts for each of the bottom-level series:
<p align="center"><b>𝑦̂<sub>𝐵𝐶_𝑁_𝑈𝑃𝐶1,h</sub> , 𝑦̂<sub>𝐵𝐶_𝑁_𝑈𝑃𝐶2,ℎ</sub> , 𝑦̂<sub>𝐵𝐶_𝐸_𝑈𝑃𝐶1,ℎ</sub> , 𝑦̂<sub>𝐵𝐶_𝐸_𝑈𝑃𝐶2,ℎ</sub> , 𝑦̂<sub>𝐵𝐶_𝑆_𝑈𝑃𝐶1,ℎ</sub> , 𝑦̂<sub>𝐵𝐶_𝑆_𝑈𝑃𝐶2,ℎ</sub> , 𝑦̂<sub>𝐵𝐶_𝑊_𝑈𝑃𝐶1,ℎ</sub> , 𝑦̂<sub>𝐵𝐶_𝑊_𝑈𝑃𝐶2,ℎ</sub></b></p>

Summing these, we get h-step-ahead coherent forecasts for the rest of
the series:

<p align="center"><b>𝑦̃<sub>ℎ</sub> = 𝑦̂<sub>𝐵𝐶_𝑁_𝑈𝑃𝐶1,ℎ</sub> + 𝑦̂<sub>𝐵𝐶_𝑁_𝑈𝑃𝐶2,ℎ</sub> + 𝑦̂<sub>𝐵𝐶_𝐸_𝑈𝑃𝐶1,ℎ</sub> + 𝑦̂<sub>𝐵𝐶_𝐸_𝑈𝑃𝐶2,ℎ</sub> + 𝑦̂<sub>𝐵𝐶_𝑆_𝑈𝑃𝐶1,ℎ</sub> + 𝑦̂<sub>𝐵𝐶_𝑆_𝑈𝑃𝐶2,ℎ</sub> + 𝑦̂<sub>𝐵𝐶_𝑊_𝑈𝑃𝐶1,ℎ</sub> + 𝑦̂<sub>𝐵𝐶_𝑊_𝑈𝑃𝐶2,ℎ</sub></b></p>
<p align="center"><b>𝑦̃<sub>𝑁,ℎ</sub> =𝑦̂<sub>𝐵𝐶_𝑁_𝑈𝑃𝐶1,ℎ</sub> +𝑦̂<sub>𝐵𝐶_𝑁_𝑈𝑃𝐶2,ℎ</sub></b></p>
<p align="center"><b>𝑦̃<sub>𝐸,ℎ</sub> =𝑦̂<sub>𝐵𝐶_𝐸_𝑈𝑃𝐶1,ℎ</sub> +𝑦̂<sub>𝐵𝐶_𝐸_𝑈𝑃𝐶2,ℎ</sub></b></p>
<p align="center"><b>𝑦̃<sub>𝑆,ℎ</sub> =𝑦̂<sub>𝐵𝐶_𝑆_𝑈𝑃𝐶1,ℎ</sub> +𝑦̂<sub>𝐵𝐶_𝑆_𝑈𝑃𝐶2,ℎ</sub></b></p>
<p align="center"><b>𝑦̃<sub>𝑊,ℎ</sub> =𝑦̂<sub>𝐵𝐶_𝑊_𝑈𝑃𝐶1,ℎ</sub> +𝑦̂<sub>𝐵𝐶_𝑊_𝑈𝑃𝐶2,ℎ</sub></b></p>

(We use the “tilde” notation (~) to indicate coherent forecasts).
  
  
## Results
* <h4>Retailer Forecast</h4>
![retailer_total](https://user-images.githubusercontent.com/20180559/48884401-67b97c80-ee4a-11e8-93b0-ce6ddb0cdd51.png)

* <h4>PlanVsActual</h4>
![retailerplanvsactual](https://user-images.githubusercontent.com/20180559/48884424-81f35a80-ee4a-11e8-9056-b1632c414c7c.png)

* <h4>Product Category</h4>
![category_bar](https://user-images.githubusercontent.com/20180559/48884458-a2231980-ee4a-11e8-9642-0ff7275cad0d.png)

* <h4>Retailer Region</h4>
![region_bar](https://user-images.githubusercontent.com/20180559/48884492-bd8e2480-ee4a-11e8-8451-4d65fd079ffb.png)

* <h4>Retailers</h4>
![retailer_bar](https://user-images.githubusercontent.com/20180559/48884518-d4cd1200-ee4a-11e8-9dcd-54bbf9fef26d.png)

* <h4>Products</h4>
![upc_bar](https://user-images.githubusercontent.com/20180559/48884532-eca49600-ee4a-11e8-8658-78e093b0fbe3.png)
