# Doc: https://learn.microsoft.com/es-mx/training/modules/test-machine-learning-models/5-exercise-test-training-datasets

import pandas

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
                    trendline=lambda x: model.params[1] * x + model.params[0])
