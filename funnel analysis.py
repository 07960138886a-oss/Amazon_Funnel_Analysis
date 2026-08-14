!pip install Faker
import pandas as pd
import random
from faker import Faker
from datetime import timedelta

## Generated a synthetic Amazon e-commerce dataset simulating customer interactions across the purchasing funnel
# Initialize Faker and empty list for records
fake = Faker()
data = []
# Funnel Stages and Conditional Probabilities
stages = ['Impressions', 'Clicks', 'Basket Adds', 'Purchases']
probabilities = {
    'Impressions': 1.0,
    'Clicks': 0.7,
    'Basket Adds': 0.5,
    'Purchases': 0.3
}
# Supporting data for randomization
devices = ['Mobile', 'Desktop', 'Tablet']
regions = ['England', 'Scotland', 'Wales', 'Northern Ireland']
channels = ['Organic Search', 'Sponsored Products', 'Sponsored Brands', 'Sponsored Display']
categories = ['Kitchenware', 'HomeDecor', 'Bedding', 'Storage', 'Appliances']
# Generate data for 10,000 users / sessions
for i in range(1, 10001):
    user_id = f"USR{i:05d}"
    session_id = f"SES{i:05d}"
    event_time = fake.date_time_between(start_date='-30d', end_date='now')
    # Assign session-level attributes in the outer loop 
    # to maintain data consistency across events within the same session
    session_device = random.choice(devices)
    session_region = random.choice(regions)
    session_channel = random.choice(channels)
    session_category = random.choice(categories)
    # Stage progression
    for stage in stages:
        # Decide if the user continues to the next stage
        if random.random() < probabilities[stage]:
            # Generate record for the stage
            record = {
                'User_ID': user_id,
                'Session_ID': session_id,
                'Event': stage,
                'Timestamp': event_time.strftime('%Y-%m-%d %H:%M:%S'),
                'Device': session_device,
                'Region': session_region,
                'Channel': session_channel,
                'Product_Category': session_category,
                'Revenue': round(random.uniform(200, 2000), 2) if stage == 'Purchases' else 0,    
            }
            data.append(record)
            # Add 2-5 minutes between each stage event
            event_time += timedelta(minutes=random.randint(2, 5))
        else:
            # If user drops off, stop further stages
            break
# Create DataFrame
df = pd.DataFrame(data)
# Sort values by Session_ID and Timestamp to ensure correct chronological sequence
df = df.sort_values(by=['Session_ID', 'Timestamp']).reset_index(drop=True)
# Save to CSV
df.to_csv("amazon_funnel_analysis_data.csv", index=False)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
df = pd.read_csv("amazon_funnel_analysis_data.csv")  
df
print("Top 5 data\n")
display(df.head())
df.tail()
df.sample()
print(df.columns)
print(f"\nTotal Number of Columns {df.columns.nunique()}")
type(df)
df.dtypes
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
print(df.dtypes)
df.info()
df.describe()
df.describe(include = "object")
df.shape
pd.set_option("display.max_rows", None)
df
# check for the null and duplicate values

print("\n---Finding Null Values---\n")
null_values = df.isnull().sum()
print(null_values)

print("\n---Finding Duplicate Values---\n")
duplicate_values = df.duplicated().sum()
print(f"Total numbers of duplicate values in this dataset is {duplicate_values}")

print("\n---Total Unique Data---\n")
unique_data = df.nunique()
print(unique_data)


