# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r"C:\Users\HP\Downloads\COVID clinical trials.csv" # Adjust the path if needed
data = pd.read_csv(file_path)
# Display basic information about the dataset
print("Dataset Info:")
print(data.info())
# Display the first few rows of the dataset
print("\nFirst few rows of the dataset:")
print(data.head())
# Check for missing values and duplicates
missing_values = data.isnull().sum()
duplicates = data.duplicated().sum()
print("\nMissing values in each column:")
print(missing_values)
print(f"\nNumber of duplicate rows: {duplicates}")
# Cleaning: Drop duplicates and handle missing values
data_cleaned = data.drop_duplicates()
threshold = 0.5 * data_cleaned.shape[1]  # Drop rows with more than 50% missing values
data_cleaned = data_cleaned.dropna(thresh=threshold)
# Filling remaining missing values
data_cleaned = data_cleaned.fillna(method='ffill').fillna(method='bfill')
# Display cleaned data info
print("\nCleaned Dataset Info:")
print(data_cleaned.info())
# Summarize key statistics
summary_stats = data_cleaned.describe(include='all')
print("\nSummary statistics:")
print(summary_stats)
# Convert date columns to datetime if present
if 'Start Date' in data_cleaned.columns:
    data_cleaned['Start Date'] = pd.to_datetime(data_cleaned['Start Date'], errors='coerce')
if 'Completion Date' in data_cleaned.columns:
    data_cleaned['Completion Date'] = pd.to_datetime(data_cleaned['Completion Date'], errors='coerce')
# EDA - Trends over time
if 'Start Date' in data_cleaned.columns:
    trials_over_time = data_cleaned.groupby(data_cleaned['Start Date'].dt.year).size()
    # Plot number of clinical trials over years
    plt.figure(figsize=(10, 6))
    trials_over_time.plot(kind='line', marker='o', color='blue')
    plt.title("Number of Clinical Trials Over Time", fontsize=16)
    plt.xlabel("Year", fontsize=14)
    plt.ylabel("Number of Trials", fontsize=14)
    plt.grid(True)
    plt.show()
# EDA - Study types and sponsors
if 'Study Type' in data_cleaned.columns:
    study_type_counts = data_cleaned['Study Type'].value_counts()
    # Plot study type distribution
    plt.figure(figsize=(8, 5))
    study_type_counts.plot(kind='bar', color='skyblue')
    plt.title("Distribution of Study Types", fontsize=16)
    plt.xlabel("Study Type", fontsize=14)
    plt.ylabel("Count", fontsize=14)
    plt.xticks(rotation=45)
    plt.show()
if 'Sponsor/Collaborators' in data_cleaned.columns:
    top_sponsors = data_cleaned['Sponsor/Collaborators'].value_counts().head(10)
    # Plot top sponsors
    plt.figure(figsize=(8, 5))
    top_sponsors.plot(kind='bar', color='orange')
    plt.title("Top 10 Sponsors of Clinical Trials", fontsize=16)
    plt.xlabel("Sponsor", fontsize=14)
    plt.ylabel("Number of Trials", fontsize=14)
    plt.xticks(rotation=45)
    plt.show()
# Distribution of enrollment
if 'Enrollment' in data_cleaned.columns:
    enrollment = data_cleaned['Enrollment']
    # Plot enrollment distribution
    plt.figure(figsize=(8, 5))
    plt.hist(enrollment.dropna(), bins=20, color='purple', edgecolor='black')
    plt.title("Distribution of Enrollment Numbers", fontsize=16)
    plt.xlabel("Enrollment", fontsize=14)
    plt.ylabel("Frequency", fontsize=14)
    plt.grid(True)
    plt.show()
# Save cleaned data to a new file
# cleaned_file_path = 'cleaned_COVID_clinical_trials.csv'
# data_cleaned.to_csv(cleaned_file_path, index=False)
# print(f"Cleaned data has been saved to {cleaned_file_path}.")
