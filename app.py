"""This is the main file for the Flask App that serves as a web interface for the data processing functions."""
import sys
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
        "1. To count number of people getting arrested by selling drugs please enter: <br>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i>your_url/lowerBoundCount/upperBoundCount</i><br>"
    )

def load_data():
    """Loads the data from the file and returns it."""
    data_processor.make_data_array()
    return data_processor.data

data = load_data()

@app.route('/<lowerBoundCount>/<upperBoundCount>', strict_slashes=False)
def sell_arrests(Lower_Bound_Count, Upper_Bound_Count):
    """Returns the number of subjects arrested on drug charges a number of 
    times in the range lower-upper"""
    try:
        lower = int(Lower_Bound_Count)
        upper = int(Upper_Bound_Count)
        return str(data_processor.drug_sale_arrests(lower, upper)) + " people"
    except ValueError:
        return "Invalid input. Please provide valid integers for lower and upper bounds."

def main():
    """Runs the Program"""
    process_input()

def process_input():
    """Takes in the command line input and calls
    the methods from production code to get the requested info"""
    if len(sys.argv) == 0:
        print_usage_statement()
    elif len(sys.argv) > 1 and sys.argv[1] == "--meeting":
        input_meeting_helper()
    elif len(sys.argv) > 1 and sys.argv[1] == "--sellArrests":
        input_serrest_helper()
    else:
        print_usage_statement()

def input_meeting_helper():
    """Serves as a helper for calling the production code method meeting_frequency/count()"""
    if len(sys.argv) == 3:
        if sys.argv[2] == "frequency" or sys.argv[2] == "freq":
            print(str(data_processor.meeting_frequency()) + "%")
        if sys.argv[2] == "count":
            print(str(data_processor.meeting_count()) + " meetings attended")
    else:
        print_usage_statement()

def input_serrest_helper():
    """Serves as a helper for calling the production code method drug_sale_arrests()"""
    if get_sys_argv_length() == 4:
        try:
            print(
                str(
                    data_processor.drug_sale_arrests(
                        int(sys.argv[2]), int(sys.argv[3])
                    )
                )
                + " people"
            )
        except ValueError:
            print_usage_statement()
    else:
        print_usage_statement()

def get_sys_argv_length():
    """gives the numebr of commands in the comand line input"""
    return len(sys.argv)

def print_usage_statement():
    """Prints the class usage statement when improper input is given"""
    print(
        "Usage:"
        '\npython3 cl.py --meeting ["frequency", "count"]'
        "\npython3 cl.py --sellArrests Lower_Bound_Count Lpper_Bound_Count "
    )

if __name__ == '__main__':
    app.run(port=8000, debug=True)
