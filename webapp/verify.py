import numpy as np
import streamlit as st
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


def verify_upload(uploaded_file):

    df_uploaded = pd.read_csv(uploaded_file, header=None)
    sol_value = pd.DataFrame(st.secrets["value"])

    if len(df_uploaded) != len(sol_value):
        # print("Not OK")
        st.write("Uploaded file contains " + str(len(df_uploaded)) + " answers, but " +
                 str(len(sol_value)) + " answers are required.")
        raise ValueError("Opps! The number of instances in the uploaded file is not aligned with our database.")


def verify_solution(uploaded_file):

    """
    Since we have used pd.read_csv in the previous function, we need to reset the buffer before we can use the
    uploaded file again. We can do this using uploaded_file.seek(0) as pointed out in the Streamlit forum.
    Link: https://discuss.streamlit.io/t/emptydataerror-no-columns-to-parse-from-file/6247/3
    """
    uploaded_file.seek(0)
    df_uploaded = pd.read_csv(uploaded_file, header=None)
    candidate_answer = np.array(df_uploaded.iloc[:])

    solution = np.array(st.secrets["value"])
    acc = accuracy_score(solution, candidate_answer)
    prec = precision_score(solution, candidate_answer, zero_division=1)
    rec = recall_score(solution, candidate_answer, zero_division=1)
    f1 = f1_score(solution, candidate_answer, zero_division=1)

    return acc, prec, rec, f1