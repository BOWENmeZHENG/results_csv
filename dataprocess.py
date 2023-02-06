import pandas as pd
import utils_plot as utpl

# If stress_t < 0.2, fail

# Merge all csvs into a dataframe
all_data = []
result_ids = [1, 2, 3, 4]
for index in result_ids:
    all_data.append(pd.read_csv(f'result_{index}.csv'))
all_data = pd.concat(all_data)

# Extract s/f data
data_success = all_data[all_data['strength'] > 0.2]
data_fail = all_data[all_data['strength'] < 0.2]


# Plot
utpl.plot_hist(data_success['density'], 'well-connected', r'density ($\rm mg/cm^3$)')