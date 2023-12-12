import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("new_file.csv")
desired_country_codes = ['RUS','UKR','ZAF', 'SOM', 'VNM', 'USA','THA', 'SWE', 'SGP', 'QAT', 'PRK']
desired_indicator_codes = ['AG.LND.AGRI.K2' ]
filtered_df = df[df["Country Code"].isin(desired_country_codes)]
filtered_df = filtered_df[filtered_df["Indicator Code"].isin(desired_indicator_codes)]
heatmap_data = filtered_df.pivot(index='Country Code', columns='Indicator Code', values=['1975', '1995', '2015','2016','2017','2018', '2022'])

# Plot the heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data, annot=True, fmt=".2f", cmap='YlGnBu', linewidths=0.1)
plt.title('Heatmap of Indicator Codes for Years 1975, 1995, 2015, 2022')
plt.show()



def get_last_10_years_data(file_path, indicator_name):
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(file_path)

    # Filter rows based on the indicator name
    filtered_df = df[df['Indicator Name'] == indicator_name]

    # Extract the last 10 years' data
    last_10_years = df.columns[-10:]

    # Select only the necessary columns
    result_df = filtered_df[['Country Name', 'Country Code'] + list(last_10_years)]
    
    
    return result_df



def goal_one(file_path, indicator_name, flag_trans):
    print(flag_trans)
    if (flag_trans):
        transposed_df = get_transposed_data_and_save(file_path, indicator_name)
        output_file_path = f'transposed_data_{indicator_name}.csv'
        transposed_df.to_csv(output_file_path, index_label='Year')
        
        return "Transpose file has been created"
    else:
        result_df = get_last_10_years_data(file_path, indicator_name)
        output_file_path = f'last10_normal_data_{indicator_name}.csv'
        result_df.to_csv(output_file_path, index_label='Year')
    
        return "Last 10 years normal file has been cearted"
    #driver code
file_path = 'new_file.csv'
indicator_name = 'CO2 emissions from solid fuel consumption (kt)'
isTranspose = input("enter 1 if you want to get a transpose or else enter 0")

print(goal_one(file_path, indicator_name, int(isTranspose)))



df = pd.read_csv("new_file.csv")
desired_country_codes = ['ZAF', 'SOM', 'VNM', 'USA', 'UKR', 'THA', 'SWE', 'SGP', 'QAT', 'PRK']
filtered_df = df[df["Country Code"].isin(desired_country_codes)]


# Calculate mean for each row and add a 'Mean' column
filtered_df['Mean'] = filtered_df.iloc[:,4:13].mean(axis=1)
df_sorted = filtered_df.sort_values(by='Mean', ascending=False)

# Display the DataFrame with the added 'Mean' column
# Plot the bar chart
plt.figure(figsize=(10, 6))
plt.bar(df_sorted['Country Name'], df_sorted['Mean'], color='skyblue')
plt.title('Mean Values by Country (2013-2022)')
plt.xlabel('Country')
plt.ylabel('Mean Value')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
plt.tight_layout()
plt.show()


df = pd.read_csv("new_file.csv")
desired_country_codes = ['ZAF', 'SOM', 'VNM', 'USA', 'UKR', 'THA', 'SWE', 'SGP', 'QAT', 'PRK']
filtered_df = df[df["Country Code"].isin(desired_country_codes)]
filtered_df['Mean'] = filtered_df.iloc[:,4:7].mean(axis=1)
df_sorted = filtered_df.sort_values(by='Mean', ascending=False)

plt.figure(figsize=(12, 8))
plt.barh(df_sorted['Country Name'], df_sorted['Mean'], color='blue')
plt.title('Mean Values by CO2 Emission (2013-2017)')
plt.xlabel('Mean Value')
plt.ylabel('Country')
plt.grid(axis='x', linestyle='--', alpha=0.6)  # Add grid lines for better readability
plt.show()



df = pd.read_csv("new_file.csv")
desired_country_codes = ['RUS', 'UKR']
desired_indicator_codes = ['SP.POP.TOTL']
filtered_df = df[df["Country Code"].isin(desired_country_codes)]
filtered_df = filtered_df[filtered_df["Indicator Code"].isin(desired_indicator_codes)]
years = ['2019','2020','2021','2022']
plt.figure(figsize=(10, 6))

bar_width = 0.05  # Decrease bar width
gap = 0.05  # Introduce gap between grouped bars
index = range(len(desired_country_codes))

for i, year in enumerate(years):
    plt.bar([pos + i * bar_width for pos in index], filtered_df[year], width=bar_width, label=year)

plt.xlabel('Country')
plt.ylabel('Population')
plt.title('Population Comparison')
plt.xticks([pos + bar_width for pos in index], desired_country_codes)
plt.legend(title='Year')
plt.show()



df = pd.read_csv("new_file.csv")
desired_country_codes = ['RUS', 'UKR']
desired_indicator_codes = ['AG.LND.AGRI.K2']
filtered_df = df[df["Country Code"].isin(desired_country_codes)]
filtered_df = filtered_df[filtered_df["Indicator Code"].isin(desired_indicator_codes)]
years = ['2019','2020','2021','2022']
plt.figure(figsize=(10, 6))

bar_width = 0.05  # Decrease bar width
gap = 0.05  # Introduce gap between grouped bars
index = range(len(desired_country_codes))

for i, year in enumerate(years):
    plt.bar([pos + i * bar_width for pos in index], filtered_df[year], width=bar_width, label=year)

plt.xlabel('Country')
plt.ylabel('Population')
plt.title('Population Comparison')
plt.xticks([pos + bar_width for pos in index], desired_country_codes)
plt.legend(title='Year')
plt.show()




df = pd.read_csv("new_file.csv")
desired_country_codes = ['RUS', 'UKR']
desired_indicator_codes = ['EN.ATM.CO2E.LF.KT']
filtered_df = df[df["Country Code"].isin(desired_country_codes)]
filtered_df = filtered_df[filtered_df["Indicator Code"].isin(desired_indicator_codes)]
years = ['2009','2010','2011','2012']
plt.figure(figsize=(10, 6))

bar_width = 0.05  # Decrease bar width
gap = 0.05  # Introduce gap between grouped bars
index = range(len(desired_country_codes))

for i, year in enumerate(years):
    plt.bar([pos + i * bar_width for pos in index], filtered_df[year], width=bar_width, label=year)

plt.xlabel('Country')
plt.ylabel('Population')
plt.title('Population Comparison')
plt.xticks([pos + bar_width for pos in index], desired_country_codes)
plt.legend(title='Year')
plt.show()


df = pd.read_csv("new_file.csv")
desired_country_codes = ['RUS','UKR','ZAF', 'SOM', 'VNM', 'USA','THA', 'SWE', 'SGP', 'QAT', 'PRK']
desired_indicator_codes = ['AG.LND.AGRI.K2' ]
filtered_df = df[df["Country Code"].isin(desired_country_codes)]
filtered_df = filtered_df[filtered_df["Indicator Code"].isin(desired_indicator_codes)]
heatmap_data = filtered_df.pivot(index='Country Code', columns='Indicator Code', values=['1975', '1995', '2015','2016','2017','2018', '2022'])

# Plot the heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data, annot=True, fmt=".2f", cmap='YlGnBu', linewidths=0.1)
plt.title('Heatmap of Indicator Codes for Years 1975, 1995, 2015, 2022')
plt.show()

