# TripleTen Sprint 6 - Data Collection and Storage (SQL)

### What we learned throughout the sprint:

- About relationships between tables.
- How to join and unite tables.
- How to search for substrings using regular expressions.
- How to search for empty values in a table.
- What RDDs and PySpark DataFrames are.
- How to create and manipulate PySpark DataFrames.
- How to use SQL queries in PySpark.

### Project - Taxi Ride Weather Impact 

As an employee of a new ride-sharing company launching in Chicago, you want to understand passenger preferences and the impact of external factors on rides.

#### Task

Find patterns in the available information, analyzing data from competitors and testing a hypothesis about the impact of weather on ride frequency.

- Test the hypothesis: "The average duration of rides from the Loop to O'Hare International Airport changes on rainy Saturdays." 

#### The Data

The data is spread across 3 files:

`neighborhoods` table: data on city neighborhoods
- `name`: name of the neighborhood
- `neighborhood_id`: neighborhood code
`cabs` table: data on taxis
- `cab_id`: vehicle code
- `vehicle_id`: the vehicle's technical ID
- `company_name`: the company that owns the vehicle
`trips` table: data on rides
- `trip_id`: ride code
- `cab_id`: code of the vehicle operating the ride
- `start_ts`: date and time of the beginning of the ride (time rounded to the hour)
- `end_ts`: date and time of the end of the ride (time rounded to the hour)
- `duration_seconds`: ride duration in seconds
- `distance_miles`: ride distance in miles
- `pickup_location_id`: pickup neighborhood code
- `dropoff_location_id`: dropoff neighborhood code
`weather_records` table: data on weather
- `record_id`: weather record code
- `ts`: record date and time (time rounded to the hour)
- `temperature`: temperature when the record was taken
- `description`: brief description of weather conditions, e.g. "light rain" or "scattered clouds"

Schema
![Alt text](<Image (3).png>)

Additional features:
- `company_name`: taxi company name
- `trips_amount`: the number of rides for each taxi company on November 15-16, 2017
- `dropoff_location_name`: Chicago neighborhoods where rides ended
- `average_trips`: the average number of rides that ended in each neighborhood in November 2017

#### The Process

This project was broken out into three parts: 

1) [Parsing Data](https://github.com/mattamx/TripleTen_projects/blob/7189fe6b04a31b5ffd0aaf27e420c1bd802820c5/Sprint%206%20-%20Data%20Collection%20and%20Storage%20(SQL)/Parsing%20Data.md)
    - Developing code to parse through data on weather conditions from a website
    - Leveraging libraries for sending request to a server and for webpage parsing (`requests` and `bs4 - BeautifulSoup`)
2) [Working with Databases](https://github.com/mattamx/TripleTen_projects/blob/53ca403f2e8244b8ba72f6dcdabbdbe546d159f8/Sprint%206%20-%20Data%20Collection%20and%20Storage%20(SQL)/Working%20with%20Databases.md)
    - Retrieving data using SQL (leveraging operators like `Case`, `Inner Join`, `Extract`) to later perform exploratory data analysis and test the hypothesis
3) Exploratory data analysis and hypothesis testing using Python drawing conclusions from our analysis and explaining the results

#### Results

We conclude that 2 taxi companies hold strong market share based on the amount of trips and 4 locations are the major hubs based on drop-off location data. Ultimately, weather does in fact affect rides as we see 1) higher volume of trips during good weather conditions paired with longer ride duration and 2) an inverse relationship of average trip duration during bad weather conditions. 

There was significant evidence to reject the null hypothesis stating that there is no difference in average duration of rides between weather conditions on each Saturday of November 2017.

# Chart Examples

![](https://github.com/mattamx/TripleTen_projects/blob/9fb19f3da3e8c499b72d65f0fbba6efd833bc764/Sprint%206%20-%20Data%20Collection%20and%20Storage%20(SQL)/images/newplot.png)

![](https://github.com/mattamx/TripleTen_projects/blob/9fb19f3da3e8c499b72d65f0fbba6efd833bc764/Sprint%206%20-%20Data%20Collection%20and%20Storage%20(SQL)/images/newplot1.png)

![](https://github.com/mattamx/TripleTen_projects/blob/9fb19f3da3e8c499b72d65f0fbba6efd833bc764/Sprint%206%20-%20Data%20Collection%20and%20Storage%20(SQL)/images/newplot2.png)

Included is the full Notebook which breaks out the description of our results.

# Plans for updates

Nothing at the moment.
