import pandas

# Make a dictionary of data for boot sizes
# and harness size in cm
data = {
    'boot_size': [
        39, 38, 37, 39, 38, 35, 37, 36, 35, 40, 40, 36, 38, 39, 42, 42, 36, 36,
        35, 41, 42, 38, 37, 35, 40, 36, 35, 39, 41, 37, 35, 41, 39, 41, 42, 42,
        36, 37, 37, 39, 42, 35, 36, 41, 41, 41, 39, 39, 35, 39
    ],
    'harness_size': [
        58, 58, 52, 58, 57, 52, 55, 53, 49, 54, 59, 56, 53, 58, 57, 58, 56, 51,
        50, 59, 59, 59, 55, 50, 55, 52, 53, 54, 61, 56, 55, 60, 57, 56, 61, 58,
        53, 57, 57, 55, 60, 51, 52, 56, 55, 57, 58, 57, 51, 59
    ]
}

#* Convert Data to DataFram with Pandas

dataset = pandas.DataFrame(data=data)
print(dataset)

#? First we define our formula usin a special syntax
#? This says that boot_size is explained by harness_size

formula = "boot_size ~ harness_size"

#? CREATE A MODEL

#? Import a Library to do the hard work for us
import statsmodels.formula.api as smf

#? Create the model, but don't gonna train it yet
model = smf.ols(formula=formula, data=dataset)

#! We have created out model but it does not have internal parameters yet.
if not hasattr(model, 'params'):
    print(
        "Model selected but it does not have parameters set. We need to train it!"
    )

#? WE CAN TRAIN OUR MODEL NOW
#? Import some Libraries to do the hard work for us
#! a file downloaded to traing our model <- !wget https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/graphing.py
import graphing

#* Train (fit) the model so that it creates a line that fits our data. This method does the hard work for us. We will look at how this moethod works in a later unit.
fitted_model = model.fit()

#* Print information about our model now it has been fit
print("The following model parameters have been found:\n" +
      f"line slope: {fitted_model.params[1]} \n" +
      f"Line Intercept: {fitted_model.params[0]}")

#? We can interpret the parametes obtained but you can use graphing to look it better

# Show a graph of the result
# Don't worry about how this works for now
graphing.scatter_2D(
    dataset,
    label_x="harness_size",
    label_y="boot_size",
    trendline=lambda x: fitted_model.params[1] * x + fitted_model.params[0])
#! Graphing has problems :S using the pyplot library we can show the point dispersion
from matplotlib import pyplot as plt

x = data['boot_size']
y = data['harness_size']

plt.scatter(x, y)
plt.xlabel('Boot Size')
plt.ylabel('Harness size')
plt.title('Gráfico de dispersión')
plt.show()

#? WE CAN USE OUR MODEL TO PREDICT THE ASWER

#* Harness_size states the size og the harness we are interrested in
harness_size = {'harness_size': [52.5]}

#* Use the model to predict what size of boots the dog will fit
approzimate_boot_size = fitted_model.predict(harness_size)

#? Print the result
print("Estimated approximate_boot_size:")
print(approzimate_boot_size[0])
