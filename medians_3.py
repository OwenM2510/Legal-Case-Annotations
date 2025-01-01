import json
import matplotlib.pyplot as plt
import numpy as np

path = '/Users/owen/Desktop/UniDataset/Analysis/'

file2 = 'Domain_vio_stats.json'


with open(path + file2) as access_json:
    read_content = json.load(access_json)
    
factor_of_interest = "Independent and Impartial"

tuples = [v[factor_of_interest] for v in read_content.values()]

# Convert data to NumPy array for easier analysis
np_data = np.array(tuples)

# Exclude tuples where all three values are 0
non_zero_tuples = np_data[~np.all(np_data == 0, axis=1)]

# Check if there are any non-zero tuples
if non_zero_tuples.size > 0:
    # Descriptive statistics
    mean_values = np.mean(non_zero_tuples, axis=0)
    median_values = np.median(non_zero_tuples, axis=0)
    std_dev_values = np.std(non_zero_tuples, axis=0)

print("Mean:", mean_values)
print("Median:", median_values)
print("Standard Deviation:", std_dev_values)

# Scale the mean values so that their sum is 1
sum_of_means = np.sum(mean_values)
scaled_mean_values = mean_values / sum_of_means

print("Scaled Mean:", scaled_mean_values)



# Visualization
fig, axs = plt.subplots(len(tuples[0]), 1, figsize=(8, 6), sharex=True)

for i in range(len(tuples[0])):
    axs[i].hist(np_data[:, i], bins=23, alpha=0.7, label=f'Tuple {i+1}')
    axs[i].set_ylabel(f'Frequency (Tuple {i+1})')

axs[-1].set_xlabel('Values')
plt.legend()
plt.show()
