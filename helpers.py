import pandas as pd
import numpy as np

def get_data_set():
    """
    Get the questions dataset from quoratrain
    """
    data_frame = pd.read_pickle("Data/quoratrain_q1_pos.pkl")
    questions = data_frame["question1"]
    no_of_rows = len(data_frame)
    print("done")
    return data_frame, questions, no_of_rows

def get_user_input():
    """
    Get user input
    """
    print(f"Write your question and press 'enter' ")
    data = input("> ")
    return data

def post_question_to_df():
    """
    Get the question and run against df
    """
    s = get_user_input()
    df = pd.DataFrame({'sentence': [s]})
    return df
