import pandas as pd
from matplotlib import pyplot as plt

#? FIGURA 1
df_students = pd.read_csv('grades.csv', delimiter=',', header='infer')

# Remove any rows with missing data
df_students = df_students.dropna(axis=0, how='any')

# Calculate who passed, assuming '60' is the grade needed to pass
passes = pd.Series(df_students['Grade'] >= 60)

# Save who passed to the Pandas dataframe
df_students = pd.concat([df_students, passes.rename("Pass")], axis=1)

# Create a bar plot of name vs grade
plt.bar(x=df_students.Name, height=df_students.Grade)
# Display the plot
# plt.show()

#? FIGURA 2
# Create a bar plop with color bar oranges
fig = plt.figure(figsize=(8, 4))
plt.bar(x=df_students.Name, height=df_students.Grade, color='orange')

# Customize the chart
#! Create a Figure (It create a size of the figure)
# Plop Name: "Student Grades"
plt.title('Student Grades', color='pink')
# Axis X label: "Student"
plt.xlabel('Student', color='blue')
# Axis Y label: Grade
plt.ylabel('Grade', color='blue')
# Grid properties
plt.grid(color='#000000', linestyle='dotted', linewidth=2, axis='y', alpha=0.7)
plt.xticks(rotation=90, color='red')
# plt.yticks(rotation=90)

#? FIGURE 3
#* A figure can contanin multiple subplots
# Create a figure for 2 subplots (1 row, 2 columns)
fig, ax = plt.subplots(1, 2, figsize=(10, 4))

# Create a bar plot of name vs grade on the first axis
ax[0].bar(x=df_students.Name, height=df_students.Grade, color='orange')
ax[0].set_title('Grades')
ax[0].set_xticklabels(df_students.Name, rotation=90)

# Create a pie chart of pass counts on the second axis
pass_counts = df_students['Pass'].value_counts()
ax[1].pie(pass_counts, labels=pass_counts.tolist())
ax[1].set_title('Passing Grades')
ax[1].legend(pass_counts.keys())

# Add a title to the Figure
fig.suptitle('Student Data')

#? FIGURE 4
#! pandas provide their own methods to graph...
df_students.plot.bar(x='Name', y='StudyHours', color='red', figsize=(6, 4))

#? STADISTIC ANALYSIS
#? FIGURE 5 data distribution
# Get the variable to examine
var_data = df_students['Grade']

# Create a Figure
fig = plt.figure(figsize=(10, 4))

# Plot a histogram
plt.hist(var_data)

# Add titles and labels
plt.title('Data Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')

#? FIGURE 6
#? MEASURING THE CENTRAL TENDENCY
# Get the variable to examine
var = df_students['Grade']

# Get statistics
min_val = var.min()
max_val = var.max()
mean_val = var.mean()
med_val = var.median()
mod_val = var.mode()[0]

print(
    'Minimum:{:.2f}\nMean:{:.2f}\nMedian:{:.2f}\nMode:{:.2f}\nMaximum:{:.2f}\n'
    .format(min_val, mean_val, med_val, mod_val, max_val))

# Create a Figure
fig = plt.figure(figsize=(10, 4))

# Plot a histogram
plt.hist(var)

# Add lines for the statistics
plt.axvline(x=min_val, color='gray', linestyle='dashed', linewidth=2)
plt.axvline(x=mean_val, color='cyan', linestyle='dashed', linewidth=2)
plt.axvline(x=med_val, color='red', linestyle='dashed', linewidth=2)
plt.axvline(x=mod_val, color='yellow', linestyle='dashed', linewidth=2)
plt.axvline(x=max_val, color='gray', linestyle='dashed', linewidth=2)

# Add titles and labels
plt.title('Data Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')

#? FIGURE 7
#? DATA DISTRIBUTION
# Get the variable to examine
var = df_students['Grade']

# Create a Figure
fig = plt.figure(figsize=(10, 4))

# Plot a histogram
plt.boxplot(var)

# Add titles and labels
plt.title('Data Distribution')


#? FIGURE 8 - SHOW DISTRIBUTION
# Create a function that we can re-use
def show_distribution(var_data):

    # Get statistics
    min_val = var_data.min()
    max_val = var_data.max()
    mean_val = var_data.mean()
    med_val = var_data.median()
    mod_val = var_data.mode()[0]

    print(
        'Minimum:{:.2f}\nMean:{:.2f}\nMedian:{:.2f}\nMode:{:.2f}\nMaximum:{:.2f}\n'
        .format(min_val, mean_val, med_val, mod_val, max_val))

    # Create a figure for 2 subplots (2 rows, 1 column)
    fig, ax = plt.subplots(2, 1, figsize=(10, 4))

    # Plot the histogram
    ax[0].hist(var_data)
    ax[0].set_ylabel('Frequency')

    # Add lines for the mean, median, and mode
    ax[0].axvline(x=min_val, color='gray', linestyle='dashed', linewidth=2)
    ax[0].axvline(x=mean_val, color='cyan', linestyle='dashed', linewidth=2)
    ax[0].axvline(x=med_val, color='red', linestyle='dashed', linewidth=2)
    ax[0].axvline(x=mod_val, color='yellow', linestyle='dashed', linewidth=2)
    ax[0].axvline(x=max_val, color='gray', linestyle='dashed', linewidth=2)

    # Plot the boxplot
    ax[1].boxplot(var_data, vert=False)
    ax[1].set_xlabel('Value')

    # Add a title to the Figure
    fig.suptitle('Data Distribution')

    # Show the figure
    fig.show()


# Get the variable to examine
col = df_students['Grade']
# Call the function
show_distribution(col)


#? FIGURE 9 - SHOW DENSITY
def show_density(var_data):

    fig = plt.figure(figsize=(10, 4))

    # Plot density
    var_data.plot.density()

    # Add titles and labels
    plt.title('Data Density')

    # Show the mean, median, and mode
    plt.axvline(x=var_data.mean(),
                color='cyan',
                linestyle='dashed',
                linewidth=2)
    plt.axvline(x=var_data.median(),
                color='red',
                linestyle='dashed',
                linewidth=2)
    plt.axvline(x=var_data.mode()[0],
                color='yellow',
                linestyle='dashed',
                linewidth=2)

    # Show the figure
    plt.show()


# Get the density of Grade
col2 = df_students['Grade']
show_density(col2)

# Display the plot
plt.show()
