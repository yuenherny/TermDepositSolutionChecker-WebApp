"""
Copyright (c) 2021 Yuen Hern, Yu

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

   SPDX-License-Identifier: Apache-2.0
"""

import streamlit as st
from verify import *

# to run the app, use command "streamlit run streamlit_app.py in the terminal"

# set the title of the web app
st.title("Term Deposit Solution Checker")
st.markdown("### This is a simple web app to check how good your ML model is on the test dataset from "
            "[Term Deposit Prediction Dataset by Brajesh Mohapatra]"
            "(https://www.kaggle.com/brajeshmohapatra/term-deposit-prediction-data-set).")
st.markdown("To check your solution, just upload a CSV file **(without column headers!)** containing your test "
            "predictions using the widget at the sidebar. "
            """_Your CSV file should contain 13,564 predictions with "no" as "0" and "yes" as "1"._""")
st.markdown("Visit the [project GitHub repo](https://github.com/yuenherny/TermDepositSolutionChecker-WebApp) for more information.")

st.sidebar.markdown("Made and maintained by [yuenherny](https://github.com/yuenherny), for fun. "
                    "If you encounter any issues, feel free to contact me at "
                    "[LinkedIn](https://www.linkedin.com/in/yuenhernyu/) or file an issue at the repository. ")

# candidate to upload answer in csv format
uploaded_file = st.sidebar.file_uploader("Step 1: Upload your CSV here", type=['csv'])
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





