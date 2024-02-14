# TripleTen Sprint 12 - [Numerical Methods](Numerical%20Methods.ipynb)

### What we learned throughout the sprint:

- Calculate an algorithm's computational complexity.
- Train models using the gradient descent algorithm.
- Use the gradient boosting technique.

### Brief

An used car sales service is developing an app to attract new customers. In that app, you can quickly find out the market value of your car. You have access to historical data: technical specifications, trim versions, and prices. 

The sales service is interested in:
1. the quality of the prediction
2. the speed of the prediction
3. the time required for training

#### Task

Build a model to determine the market value of used cars, leveraging the RMSE metric to evaluate the models and analyzing the speed, and quality.

#### The Data

The data is contained in one file:

- `DateCrawled`: date profile was downloaded from the database
- `VehicleType`: vehicle body type
- `RegistrationYear`: vehicle registration year
- `Gearbox`: gearbox type
- `Power`: power (hp)
- `Model`: vehicle model
- `Mileage`: mileage (measured in km due to dataset's regional specifics)
- `RegistrationMonth`: vehicle registration month
- `FuelType`: fuel type
- `Brand`: vehicle brand
- `NotRepaired`: vehicle repaired or not
- `DateCreated`: date of profile creation
- `NumberOfPictures`: number of vehicle pictures
- `PostalCode`: postal code of profile owner (user)
- `LastSeen`: date of the last activity of the user
- `Price`: price (Euro), our target

#### The Process

We first performed exploratory data analysis to create notes on any perceived issues and how we will tackle them to get all the data clean/ready as proper model inputs.

Following our data clean-up, we leverage a function to encode our dataframe and its multiple feature columns. This allows the data to be properly dissemniated by the boosting methods we incorporated after initializing the benchmark regressor models.

We then train 3 regressor models with different hyperparameters to attain our best RMSE possible. Once this is performed, we then move to boosting methods/techniques which included LightGBM, CatBoost and XGBoost. 

#### Results

From our base regressor models, we find that the RandomForestRegressor attains the best quality for our RMSE metric but performs the worst when it comes to speed. Taking into account some of the needs of the used car sales service, we take a closer look at the boosting methods and come to the conclusion that these models yield the best results with much better speed numbers. 

Our RMSE metrics from utilizing boosting techniques were from a range of ~1700-1800. The suggestion is to use LightGBM as the base model given its speed and quality results but at the end of the day, the car sales service will have to come to a compromise between their 3 wants (speed, quality and time).

# Chart Examples

*To be updated*

Included is the full Notebook which breaks out the description of our results.

# Plans for updates

Create a few visualizations from our dataframe.
