import streamlit as st
from src.utils import MultiPage
from src.dashboard import EAD_dashboard, Inference_dashboard, Traning_dashboard

if __name__ == '__main__':
    app = MultiPage()
    st.title("Card Fraud Detection Dashboard")
    st.sidebar.title("Data Themes")
    app.add_page("EDA", EAD_dashboard.EDAApp)
    app.add_page("Training", Traning_dashboard.TrainingApp)
    app.add_page("Inference", Inference_dashboard.InferenceApp)
    app.run()
