import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from src import DATAFRAME_INIT
import pandas as pd


def Graph_3D():
    DF_to_plot=pd.concat([DATAFRAME_INIT[DATAFRAME_INIT["Class"]==1].head(400),DATAFRAME_INIT[DATAFRAME_INIT["Class"]==0].head(400)])
    fig = px.scatter_3d(DF_to_plot, x='V11', y='V13', z='V15',
                  color='Class',size_max=12,opacity=0.9)
    st.plotly_chart(fig)

def boxplot_variable(Feature):
    data=DATAFRAME_INIT
    sns.set(rc={'figure.figsize': (10, 10)})
    if Feature=='Amount':
        data=data[data['Amount']<500]
    sns.boxplot(x='Class', y=Feature, data=data, showmeans=True, meanprops={"marker": "_",
                                                                                "markeredgecolor": "black",
                                                                                "markersize": "90"})

    plt.title('Distribution of the {} for Fraud Transactions'.format(Feature))
    plt.xlabel('Class')
    plt.ylabel(Feature)
    st.pyplot(plt)

def Transactions_Timestamp():
    data2=DATAFRAME_INIT.groupby(['Time']).size()
    plt.plot(list(data2.index),data2)
    plt.title('Number of Transaction during time')
    plt.ylabel('Time')
    plt.xlabel('Number of Transaction')
    st.pyplot(plt)


def Fraud_Amount():
    DF_to_plot=DATAFRAME_INIT[DATAFRAME_INIT["Class"]==1].head(500)
    fig1 = px.scatter(DF_to_plot, x="Time", y="Amount", color="Class", marginal_y="violin",
                     marginal_x="box", trendline="ols", template="simple_white")
    st.plotly_chart(fig1)

def data_overview():
    data_to_show=DATAFRAME_INIT.head(5)
    st.dataframe(data_to_show)

def Data_describe():
    Info=pd.DataFrame(DATAFRAME_INIT.describe())
    st.dataframe(Info)

