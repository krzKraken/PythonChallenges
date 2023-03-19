import pandas

#load a file containing dog's boot and harness sizes
data = pandas.read_csv('doggy-boot-harness.csv')
print(data.head())

# fit the model with ols from statsmodels.formula.api

import statsmodels.formula.api as smf

model = smf.ols(formula="boot_size ~ harness_size", data=data).fit()

print("Model Trained!")

#? SAVE AND LOAD A MODEL

import joblib

model_filename = './avalanche_dog_boot_model.pkl'
joblib.dump(model, model_filename)

print("Model saved!")

#? LOAD OUR MODEL IS JUST AS EASY

model_loaded = joblib.load(model_filename)

print("We have loaded a model with the folloowing parameters: ")
print(model_loaded.params)
"""#?Put it together
On our website, we'll want to take the harness of our customer's dog, then calculate their dog's boot size using the model that we've already trained.
Let's put everything here together to make a function that loads the model from disk, then uses it to predict our customer's dog's boot size height.
"""

#Let's wrire a function that loads and uses our model


def load_model_and_predict(harness_size):
    '''
    This function loads a pretrained model. It uses the model
    with the customer's dog's harness size to predict the size of
    boots that will fit that dog.

    harness_size: The dog harness size, in cm 
    '''

    #* Load the model from file and print basic information about it

    loaded_model = joblib.load(model_filename)

    print("We've loaded a model with the following parameters:")
    print(loaded_model.params)

    # Prepare data for the model
    inputs = {"harness_size": [harness_size]}

    # Use the model to make a prediction
    predicted_boot_size = loaded_model.predict(inputs)[0]

    return predicted_boot_size


# Practice using our model
predicted_boot_size = load_model_and_predict(45)

print("Predicted dog boot size:", predicted_boot_size)


def check_size_of_boots(selected_harness_size, selected_boot_size):
    '''
    Calculates whether the customer has chosen a pair of doggy boots that 
    are a sensible size. This works by estimating the dog's actual boot 
    size from their harness size.

    This returns a message for the customer that should be shown before
    they complete their payment 

    selected_harness_size: The size of the harness the customer wants to buy
    selected_boot_size: The size of the doggy boots the customer wants to buy
    '''

    # Estimate the customer's dog's boot size
    estimated_boot_size = load_model_and_predict(selected_harness_size)

    # Round to the nearest whole number because we don't sell partial sizes
    estimated_boot_size = int(round(estimated_boot_size))

    # Check if the boot size selected is appropriate
    if selected_boot_size == estimated_boot_size:
        # The selected boots are probably OK
        return f"Great choice! We think these boots will fit your avalanche dog well."

    if selected_boot_size < estimated_boot_size:
        # Selected boots might be too small
        return "The boots you have selected might be TOO SMALL for a dog as "\
               f"big as yours. We recommend a doggy boots size of {estimated_boot_size}."

    if selected_boot_size > estimated_boot_size:
        # Selected boots might be too big
        return "The boots you have selected might be TOO BIG for a dog as "\
               f"small as yours. We recommend a doggy boots size of {estimated_boot_size}."


# Practice using our new warning system
check_size_of_boots(selected_harness_size=55, selected_boot_size=39)
