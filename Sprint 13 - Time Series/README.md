# TripleTen Sprint 13 - Time Series

### What we learned throughout the sprint:

- Analyze time series and find the trends and seasonality;
- Create features for time series;
- Train models using time series.

### Project - Taxi Service Forecasting

An taxi company would like to attract more drivers during peak hours, utilizing historical data on taxi orders at airports. 

#### Task

Build a model to predict the amount of taxi orders for the next hour. Targeting an RMSE metric of no more than 48 on our test dataset.

#### The Data

The data is spread across one file with two features:

- `datetime`: our DF index, time feature
- `num_orders`: number of orders, target feature

#### The Process

Performed exploratory data analysis to make conclusions on any perceived issues, resample the data by one hour and futher preprocess the data for modeling.

Further levarging our `datetime` feature, we break out charts to take a look at seasonality, trends and residuals to get a wider understanding of our DF.

We then train various models with different hyperparameters in order to find our most optimal results. Our test dataset for evaluation was manipulated to be 10% of the initial dataset.

#### Results

After training various models and tuning their hyperparameters we found the gradient boosting techniques gave us better RMSE results in comparison to the regression models initially deployed. We selected the LightGBM model as our ideal model due to the overall advantages of LGBM parameter tuning (e.g., boosting) and the flexibility from introducing of more features/pattern complexity.Our achieved RMSE value was that of ~44. This was partially achieved by tuning the `max_lag` and `rolling_mean` parameters crafted from feature creation. These parameters seem to have played a significant role (compared to some of the hyperparameters) in getting the RMSE near the target value.

# Chart Examples

![Alt text](newplot1.png)

![Alt text](newplot2.png)

![Alt text](newplot3.png)

![Alt text](newplot4.png)

Included is the full Notebook which breaks out the description of our results.

# Plans for updates

Nothing at the moment.