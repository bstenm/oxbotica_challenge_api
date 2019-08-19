import pandas as pd
import json

store_name = "2017-02-20-14-42-25-outdoor-autonomy-02"

df = pd.read_csv(f"./data/{store_name}.csv")


def extract_telemetry_data(key, start, end):
    # set start timestamp to first one in dataframe if no start passed
    start = start or df.loc[0].timestamp
    # set end timestamp to last one in dataframe if no end passed
    end = end or df.loc[len(df) - 1].timestamp
    # get all dataframe rows corresponding to data
    # taken between start and end timestamps
    rows = df.loc[(df[key] >= start) & (df[key] <= end)]
    # transform data into json array of records
    json_records = json.loads(rows.to_json(orient="records"))
    return json_records
