import streamlit as st
from verify import *

# set the title of the web app
st.title("Term Deposit Solution Checker")
st.markdown("### This is a simple web app to check how good is your ML model on the test dataset from "
            "[Term Deposit Prediction Dataset by Brajesh Mahopatra]"
            "(https://www.kaggle.com/brajeshmohapatra/term-deposit-prediction-data-set).")
st.markdown("To check your solution, just upload a CSV file **(without column headers!)** containing your test "
            "predictions using the widget at the sidebar. _Your CSV file should contain 13,564 predictions._")

st.sidebar.markdown("Made for fun and maintained by [yuenhernyu](https://github.com/yuenhernyu), for fun. "
                    "If you encounter any issue, feel free to contact me at [LinkedIn](https://www.linkedin.com/in/yuenhernyu/) "
                    "or file an issue on the repository. ")

# candidate to upload answer in csv format
uploaded_file = st.sidebar.file_uploader("Step 1: Upload your CSV here", type=['csv'])
# uploaded_file = "../test/csvtest-100.csv"
if uploaded_file is not None:

    verify_upload(uploaded_file)
    st.sidebar.success("Valid file uploaded")

    st.write("## __Step 2: Check your classification result.__")
    acc, prec, rec, f1 = verify_solution(uploaded_file)
    st.write("### **Accuracy:** " + str(round(acc, 4)))
    st.write("### **Precision:** " + str(round(prec, 4)))
    st.write("### **Recall:** " + str(round(rec, 4)))
    st.write("### **F1-Score:** " + str(round(f1, 4)))


st.stop()





