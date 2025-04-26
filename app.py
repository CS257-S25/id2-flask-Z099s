"""This is the main file for the Flask App that serves as a web 
interface for the data processing functions."""
from flask import Flask
from ProductionCode import data_processor

app = Flask(__name__)

@app.route('/')
def home():
    """
    Home page for the Flask App.
    Returns:
        str: Welcome message and instructions for using the app.
    """
    return (
        "<strong>Welcome to the Flask App! Below are some example commands:</strong><br>"
        "1. To get all the raw data, please go to:<br>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i>your_url/dataOverview</i><br>"
        "2. To count number of people getting arrested by selling drugs please go to: <br>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
        "<i>your_url/sellArrests/lower_bound_count/upper_bound_count</i><br>"
    )

def load_data():
    """Loads the data from the file and returns it."""
    data_processor.make_data_array()
    return data_processor.data

data = load_data()

@app.route('/dataOverview', strict_slashes=False)
def data_overview():
    """Returns the overview of the data."""
    return data

@app.route('/<lower_bound_count>/<upper_bound_count>', strict_slashes=False)
def sell_arrests(lower_bound_count, upper_bound_count):
    """Returns the number of subjects arrested on drug charges a number of 
    times in the range lower-upper"""
    try:
        lower = int(lower_bound_count)
        upper = int(upper_bound_count)
        return str(data_processor.drug_sale_arrests(lower, upper)) + " people"
    except ValueError:
        return "Invalid input. Please provide valid integers for lower and upper bounds."

if __name__ == '__main__':
    app.run(port=8000, debug=True)
