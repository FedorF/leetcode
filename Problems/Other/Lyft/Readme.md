## Lyft
```
One of the most important things we do at Lyft is monitor where and when rides take place, charge customers, and pay drivers the right amount. To do this, we collect latitude and longitude coordinates from the GPS on the driver’s phone every few seconds for the duration of the ride, then use a pricing table to determine a final route and cost. Note: ts is measured in unix time, time in seconds since 1/1/1970

ds_decisions_price_of_a_ride.csv
+---------------+---------+
| ride_id       | varchar |
| ts            | float   |
| lat           | float   |
| lng          | float   |
+---------------+---------+

Business Logic:
costPerMile: price per mile traveled in ride*
costPerMinute: price per minute traveled in ride*
costMinimum: minimum price charged per ride* -- lower values round up to this
pickupCharge: fixed cost added to every ride*
* all prices are in USD


Q1. Which ride_id took the most amount of time?

Q2. Assuming that the GPS information is perfectly accurate, how would you accurately calculate the price we should pay to the driver for each ride

```