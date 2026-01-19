import csv
import matplotlib.pyplot as plt




file = []
# * * * User Input: enter path and name of .csv file
csv_path = input("Enter path of .csv file: ")
csv_path = csv_path.replace("\\", "/")
csv_name = input("Enter name of .csv file: ")
# Concatenates whole path to use by 'open' function
file.append(csv_path + "/" + csv_name + ".csv")


# Function to read specific, user given column(s) from .csv file
# Input: file path, specific columns
# Output: 2D list build by user given columns(for ex.: "TimeUS", "GyrX", GyrY", "Roll",...)
def get_columns(file_path, colnames):
    data = [[] for i in colnames]                                   # one empty list per requested column

    for j in range(len(file_path)):
        with open(file_path[j], newline="") as f:
            reader = csv.DictReader(f)                              # header names become dict keys [web:17]
            for row in reader:                                      # row is like {"time": "0.0", "Fx": "10", ...} [web:17]
                for i, name in enumerate(colnames):
                    data[i].append(round(float(row[name]),4))       # values are strings by default [web:15]
    return data

data_labels = []


# * * * User Input: Write labels from .csv file which should be read and plotted
while True:
    user_input = input("Enter data label to be read(q to quit): ")
    if user_input.lower() == "q":
        break
    else:
        data_labels.append(user_input)


print(f"Selected data: {data_labels}")
# * * * User Input:
selected_data = get_columns(file,data_labels)


# Plotter function
def plotter(x_axis, y_axis, x_label, y_label):
    plt.figure()
    plt.title(f"Measured {y_label} against {x_label}")
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.plot(x_axis, y_axis)


# * * * User Input: Choose type of plotting - (1) On separate windows (2) As subplots
type_of_plotting = int(input("Enter type of plotting[(1) - Separate; (2) - Subplots]: "))

if type_of_plotting == 1:
    # Plots will be shown in separate windows
    for i in range(1, len(data_labels)):
        plotter(selected_data[0], selected_data[i], data_labels[0], data_labels[i])
    plt.show()
else:
    # Plots will be shown as a subplots
    fig, axs = plt.subplots(len(data_labels) - 1, 1, sharex=True, figsize=(8, 2 * len(data_labels)))
    for ax, label, y in zip(axs, data_labels[1:], selected_data[1:]):
        ax.plot(selected_data[0], y)
        ax.set_ylabel(label)
    axs[-1].set_xlabel("TimeUS")
    plt.tight_layout()
    plt.show()




