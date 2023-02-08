import pandas as pd
import utils_plot as utpl

# If stress_t < 0.2, fail

# Merge all csvs into a dataframe
all_data = []
result_ids = list(range(1, 10))
for index in result_ids:
    all_data.append(pd.read_csv(f'result_{index}.csv'))
all_data = pd.concat(all_data)

all_data = all_data[all_data.failure_strain < 3]

# Extract s/f data
data_success = all_data[all_data['strength'] > 0.2]
data_fail = all_data[all_data['strength'] < 0.2]
utpl.plot_scatter(data_success, data_fail)

utpl.plot_property(data_success, 'density', 'strength', 'density', 'strength')
utpl.plot_property(data_success, 'density', 'failure_strain', 'density', 'failure_strain')

# Plot
# utpl.plot_hist(data_success['density'], 'well connected', r'density ($\rm mg/cm^3$)')
# utpl.plot_hist(data_fail['density'], 'not connected', r'density ($\rm mg/cm^3$)')
# utpl.plot_hist(data_success['bond_per_atom'], 'well connected', r'$N \rm _{bond/atom}$')
# utpl.plot_hist(data_fail['bond_per_atom'], 'not connected', r'$N \rm _{bond/atom}$')