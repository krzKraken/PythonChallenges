import pandas
#! wget https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/Data/doggy-boot-harness.csv <- doggy-boot-hardness.csv

# Read the text file containing data using pandas
dataset = pandas.read_csv('doggy-boot-harness.csv')

# Print the data
# Because there are a lot of data, use head() to only print the first few rows
print(dataset.head())

#? We just need the harness_size and the boot_size so we can remove the sex and age_year column

print("harness_size")
print(dataset.harness_size)

#Remove the sex and age-in-yeads columns
del dataset["sex"]
del dataset["age_years"]

print("Print the columsn names")
print("\nAvailable columns after deleting sex and age informations:")
print(dataset.columns.values)

#Print the data of the top of the table
print("Top of table")
print(dataset.head())
# Print the data at the bottom of the table
print("\n Botton of table")
print(dataset.tail())

# Print how many rows of data we have
print(f"We have {len(dataset)} rows of data")

# Determine whether each avalanche dog's harness size is < 55
# This creates a True or False value for each row where True means
# they are smaller than 55
is_small = dataset.harness_size < 55
print("\nWhether the dog's harness was smaller than size 55:")
print(is_small)

# Now apply this 'mask' to our data to keep the smaller dogs
data_from_small_dogs = dataset[is_small]
print("\nData for dogs with harness smaller than size 55:")
print(data_from_small_dogs)

# Print the number of small dogs
print(
    f"\nNumber of dogs with harness size less than 55: {len(data_from_small_dogs)}"
)

# Make a copy of the dataset that only contains dogs with
# a boot size below size 40
# The call to copy() is optional but can help avoid unexpected
# behaviour in more complex scenarios
data_smaller_paws = dataset[dataset.boot_size < 40].copy()

# Print information about this
print(
    f"We now have {len(data_smaller_paws)} rows in our dataset. The last few rows are:"
)
print(data_smaller_paws.tail())

#! Graph data
# Load and prepare plotly to create our graphs
import plotly.express
import graphing  # this is a custom file you can find in our code on github

# Show a graph of harness size by boot size:
plotly.express.scatter(data_smaller_paws, x="harness_size", y="boot_size")

#? CREATE NEW COLUMNS
# Convert harness sizes from metric to imperial units
# and save the result to a new column
data_smaller_paws[
    'harness_size_imperial'] = data_smaller_paws.harness_size / 2.54

# Show a graph of harness size in imperial units
plotly.express.scatter(data_smaller_paws,
                       x="harness_size_imperial",
                       y="boot_size")
