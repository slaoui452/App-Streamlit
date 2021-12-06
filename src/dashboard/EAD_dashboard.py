import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from src import DATAFRAME_INIT
from src.dashboard.Graphs import boxplot_variable,data_overview,Data_describe, Graph_3D,Transactions_Timestamp, Fraud_Amount


def EDAApp():
    st.header("Exploratory Data Analysis")
    st.info("In this section, you are invited to create insightful graphs "
            "about the card fraud dataset that you were provided.")

    st.subheader("Data overview :")
    data_overview()

    st.subheader("Data Describe :")
    Data_describe()

    st.subheader("Data Visualisation :")

    Liste_Variables=list(DATAFRAME_INIT.columns)
    variable1 = st.selectbox('Variables',Liste_Variables[:-1])
    boxplot_variable(variable1)

    st.subheader("Variables that we use in the prediction:")
    Graph_3D()

    st.subheader("Fraud per Amount")
    Fraud_Amount()

