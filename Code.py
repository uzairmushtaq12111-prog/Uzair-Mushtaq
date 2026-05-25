# Data Sampling Techniques Dataset Generator
# Author: Uzair Mushtaq

import pandas as pd
import random
from datetime import datetime, timedelta

# Random seed for reproducibility
random.seed(42)

# Sampling techniques data
techniques = [
    ("Simple Random Sampling", "Probability", "Equal chance for every member"),
    ("Systematic Sampling", "Probability", "Selection at fixed intervals"),
    ("Stratified Sampling", "Probability", "Population divided into groups"),
    ("Cluster Sampling", "Probability", "Population divided into clusters"),
    ("Convenience Sampling", "Non-Probability", "Selection based on availability"),
    ("Quota Sampling", "Non-Probability", "Fixed quota from each group"),
    ("Snowball Sampling", "Non-Probability", "Participants recruit others"),
    ("Purposive Sampling", "Non-Probability", "Selection based on purpose/judgment"),
]

# Extra dataset values
fields = ["Healthcare", "Education", "Marketing", "Agriculture", "Sports", "Technology"]
countries = ["India", "USA", "UK", "Canada", "Australia", "Germany"]

# Empty list to store rows
data = []

# Start date
start_date = datetime(2025, 1, 1)

# Generate 100 records
for i in range(1, 101):

    tech = random.choice(techniques)

    dataset = {
        "Dataset_ID": f"DS{i:03}",
        "Sampling_Technique": tech[0],
        "Category": tech[1],
        "Description": tech[2],
        "Sample_Size": random.randint(50, 1000),
        "Population_Size": random.randint(2000, 50000),
        "Accuracy_Percentage": round(random.uniform(70, 99), 2),
        "Research_Field": random.choice(fields),
        "Country": random.choice(countries),
        "Survey_Date": (
            start_date + timedelta(days=random.randint(0, 365))
        ).strftime("%Y-%m-%d")
    }

    data.append(dataset)

# Create DataFrame
df = pd.DataFrame(data)

# Display first 10 rows
print(df.head(10))

# Save dataset files
df.to_csv("data_sampling_techniques_dataset.csv", index=False)
df.to_excel("data_sampling_techniques_dataset.xlsx", index=False)

print("\nDataset created successfully!")
print("CSV File: data_sampling_techniques_dataset.csv")
print("Excel File: data_sampling_techniques_dataset.xlsx")
