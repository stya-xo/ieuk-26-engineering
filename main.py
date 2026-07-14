# AEROGRID HEALTH CHECK
# Quickly identify failing turbines

import pandas as pd

df = pd.read_csv('telemetry_data.csv') # Load CSV into DataFrame

df['avg_temp'] = df.groupby('turbine_id')['temperature_c'].transform('mean') # Add column for average temperature

anomaly = df.loc[
    (df['avg_temp'] > 85.0) | (df['vibration_mm_s'] > 15.0)
] # Set parameters for anomaly: Average temperature over 85.0°C OR vibration over 15.0 mm/s

print("Warning! Anomalies found in Turbine(s) ID:")
print(list(anomaly['turbine_id'].unique())) # Print list of IDs of failing Turbines