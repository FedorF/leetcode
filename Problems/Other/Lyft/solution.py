from math import radians, cos, sin, asin, sqrt
import pandas as pd
import numpy as np

pricing = {
    'costPerMile': 1.35,
    'costPerMinute': 0.27,
    'costMinimum': 5,
    'pickupCharge': 2.25
}

df = pd.read_csv("./data/ds_decisions_price_of_ride.csv")


# feel free to modify
def haversine(lat1, lng1, lat2, lng2):
    '''computes distance in miles between two lat-long pairs'''
    R = 3959.87433  # this is the Earth’s radius in miles.

    dLat = radians(lat2 - lat1)
    dLon = radians(lng2 - lng1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    a = sin(dLat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dLon / 2) ** 2
    c = 2 * asin(sqrt(a))

    return R * c


# Question 1
def calculate_longest_duration(df):
    df_dur = calc_duration(df)
    longest_ride = df_dur.loc[df_dur["duration"] == df_dur["duration"].max(), "ride_id"].values[0]
    return longest_ride


def calc_distance(df):
    df = df.sort_values(["ride_id", "ts"])
    df["lat_prev"] = df.groupby("ride_id").lat.shift(1)
    df["lng_prev"] = df.groupby("ride_id").lng.shift(1)
    df = df[df["lng_prev"].notna() & df["lat_prev"].notna()]
    df["dist"] = (
        df
        .apply(lambda x: haversine(x["lat"], x["lng"], x["lat_prev"], x["lng_prev"]), axis=1)
    )
    df_dist = df.groupby("ride_id").dist.sum().reset_index()
    df_dist.columns = ["ride_id", "dist"]
    return df_dist


def calc_duration(df):
    df_ride = (
        df
        .groupby("ride_id")
        .agg({"ts": ["min", "max"]})
        .reset_index()
    )
    df_ride.columns = ["ride_id", "ts_min", "ts_max"]
    df_ride["duration"] = df_ride["ts_max"] - df_ride["ts_min"]
    return df_ride


# Question 2
def calculate_trip_price(df):
    df_dist = calc_distance(df)
    df_dur = calc_duration(df)
    df = df_dist.merge(df_dur)
    df["price"] = (
            pricing["costPerMile"] * df["dist"]
            + pricing["costPerMinute"] * df["duration"]
            + pricing["pickupCharge"]
    )
    df["price"] = np.where(df["price"] < pricing["costMinimum"], pricing["costMinimum"], df["price"])
    return df
