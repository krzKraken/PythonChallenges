# Doc: https://learn.microsoft.com/es-mx/training/modules/test-machine-learning-models/5-exercise-test-training-datasets

import pandas
import numpy
from matplotlib import pyplot as plt

plt.style.use('seaborn-whitegrid')
'''
!pip install statsmodels
!wget https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/graphing.py
!wget https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/Data/dog-training.csv
!wget https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/Data/dog-training-switzerland.csv
'''
data = pandas.read_csv("dog-training.csv", delimiter="\t")

print(data.shape)
print(data.head())

#We are interested in the relationship between a dog's weight and the amount of rescues it performed in the previous year. Let's begin by plotting rescues_last_year as a function of weight_last_year:

import graphing
import statsmodels.formula.api as smf

# First, we define our formula using a special syntax
# This says that rescues_last_year is explained by weight_last_year
formula = "rescues_last_year ~ weight_last_year"

model = smf.ols(formula=formula, data=data).fit()

graphing.scatter_2D(data,
                    "weight_last_year",
                    "rescues_last_year",
                    size_multiplier=4,
                    trendline=lambda x: model.params[1] * x + model.params[0])

#! grafico de dispersion y funcion de tendencia
# Weight_last_year vs rescues last years and trendline = params[1]X + model.params[0]

plt.scatter(x=data['weight_last_year'],
            y=data['rescues_last_year'],
            edgecolors='violet',
            s=300,
            linewidths=0,
            alpha=0.5)
x = numpy.linspace(data['weight_last_year'].min(),
                   data['weight_last_year'].max(), 26)
print(x)
y = model.params[1] * x + model.params[0]
plt.plot(x, y, 'r')
#! Uncomment
#! plt.show()
'''There seems to be a pretty clear relationship between a dog's weight and the number of rescues it's performed. That seems pretty reasonable, as we would expect heavier dogs to be bigger and stronger and thus better at saving lives!'''

#? TRAIN/TEST SPLIT
'''This time, instead of fitting a model to the entirety of our dataset, we're going to separate our dataset into two smaller partitions: a training set and a test set.
The training set is the largest of the two, usually made up of between 70-80% of the overall dataset, with the rest of the dataset making up the test set. By splitting our data, we're able to gauge the performance of our model when confronted with previously unseen data.
Notice that data on the test set is never used in training. For that reason it's commonly referred to as unseen data or data that is unknown by the model.'''

from sklearn.model_selection import train_test_split

# Obtain the label and feature from the original data
dataset = data[['rescues_last_year', 'weight_last_year']]

# Split the dataset in an 70/30 train/test ratio. We also obtain the respective corresponding indices from the original dataset.
train, test = train_test_split(dataset, train_size=0.7, random_state=21)
datasetTrain = pandas.DataFrame(train)
datasetTest = pandas.DataFrame(test)
print("Train")
print(datasetTrain.head())
print(datasetTrain.shape)

print("Test")
print(datasetTest.head())
print(datasetTest.shape)

#We can see that these sets are different, and that the training set and test set contain 70% and 30% of the overall data respectively.
# Let's have a look at how the training set and test set are separated out:

#? Concatenate training and test so they can be graphed
#! This create a set for training and other one to test
plot_set = pandas.concat([datasetTrain, datasetTest])
plot_set["Dataset"] = ["train"] * len(datasetTrain) + ["test"
                                                       ] * len(datasetTest)

plt.scatter(x=plot_set['weight_last_year'],
            y=plot_set['rescues_last_year'],
            edgecolors='violet',
            s=300,
            linewidths=0,
            alpha=0.5)
x = numpy.linspace(data['weight_last_year'].min(),
                   data['weight_last_year'].max(), 26)
print(x)
y = model.params[1] * x + model.params[0]
plt.plot(x, y, 'r')
#! Uncomment
plt.show()

#? TRAINING SET
import statsmodels.formula.api as smf
from sklearn.metrics import mean_squared_error as mse

# First, we define our formula using a special syntax
# This says that rescues_last_year is explained by weight_last_year
formula = "rescues_last_year ~ weight_last_year"

# Create and train the model
model = smf.ols(formula=formula, data=train).fit()

# Graph the result against the data
graphing.scatter_2D(dataset,
                    "weight_last_year",
                    "rescues_last_year",
                    trendline=lambda x: model.params[1] * x + model.params[0])
