import pandas
# wget https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/graphing.py
# wget https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/Data/dog-training.csv
# wget https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/m1b_gradient_descent.py
data = pandas.read_csv("dog-training.csv", delimiter="\t")
# print(data.head())

#? Lets train our model using the dataset
from m1b_gradient_descent import gradient_descent
import numpy
import graphing

# Train model using Gradient Descent
# This method uses custom code that will print out progress as training advances.
# You don't need to inspect how this works for these exercises, but if you are
# curious, you can find it in out GitHub repository
model = gradient_descent(data.month_old_when_trained,
                         data.mean_rescues_per_year,
                         learning_rate=5E-4,
                         number_of_iterations=8000)

# Plot Data
graphing.scatter_2D(data,
                    "month_old_when_trained",
                    "mean_rescues_per_year",
                    trendline=model.predict)

#! El grafico obtenido no se ajusta correctamente a la dispersion y es porque cortamos el entrenamiento a los 8K interacciones, es por ello que se ve la oportunidad de standarizar los datos

#? Let's use standardization as the form of feature scaling for this model, applying it to the month_old_when_trained feature:
# Add the standardized verions of "age_when_trained" to the dataset.
# Notice that it "centers" the mean age around 0

print(data.head())

data['standardized_age_when_trained'] = (
    data['month_old_when_trained'] - data['month_old_when_trained'].mean()
) / data['month_old_when_trained'].std()
print(data[:5])

print(
    f"mean: {data['month_old_when_trained'].mean()}, std: {data['month_old_when_trained'].std()}"
)

#? As we can see the values standardized_age_when_trained column above are distribuited in a much smaller rangue betwen -2 and 2. and have their mean centered around 0

#* Visualizing scaled features
# Let's use a box plot to compare the original feature values to their standardized versions:

from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px

fig = px.box(data,
             y=["month_old_when_trained", "standardized_age_when_trained"])
fig.show()
'''

Now compare the two features by hovering your mouse over the graph. You will see that:
month_old_when_trained ranges from 1 to 71 and has its median centered around 35.
standardized_age_when_trained ranges from -1.6381 to 1.6798, and is centered exactly at 0.
Training with standardized features
We can now retrain our model using the standardized feature in our dataset:
'''

# Let's retrain our model, this time using the standardized feature
model_norm = gradient_descent(data.standardized_age_when_trained,
                              data.mean_rescues_per_year,
                              learning_rate=5E-4,
                              number_of_iterations=8000)

# Plot the data and trendline again, after training with standardized feature
graphing.scatter_2D(data,
                    "standardized_age_when_trained",
                    "mean_rescues_per_year",
                    trendline=model_norm.predict)
'''

It looks like this model fits the data much better that the first one!
The standardized model shows a larger slope and data now centered on 0 on the X-axis, both factors which should allow the model to converge faster.
But how much faster?
'''
#!Let's plot a comparison between models to visualize the improvements.

cost1 = model.cost_history
cost2 = model_norm.cost_history

# Creates dataframes with the cost history for each model
df1 = pandas.DataFrame({"cost": cost1, "Model": "No feature scaling"})
df1["number of iterations"] = df1.index + 1
df2 = pandas.DataFrame({"cost": cost2, "Model": "With feature scaling"})
df2["number of iterations"] = df2.index + 1

# Concatenate dataframes into a single one that we can use in our plot
df = pandas.concat([df1, df2])

# Plot cost history for both models
fig = graphing.scatter_2D(df,
                          label_x="number of iterations",
                          label_y="cost",
                          title="Training Cost vs Iterations",
                          label_colour="Model")
fig.update_traces(mode='lines')
fig.show()

#! In the last figure we can see how much fast the new model is.
