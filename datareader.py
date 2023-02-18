import pandas as pd
def get_happines_data(option1, option2):
    df = pd.read_csv("happy.csv")
    return df[option1], df[option2]