import streamlit as st
import time
from src.constants import CM_PLOT_PATH
from PIL import Image
from src.training.train_pipeline import TrainingPipeline


def Train(serialize,name):
    with st.spinner('Training model, please wait...'):
        time.sleep(1)
        try:
            tp = TrainingPipeline()
            tp.train(serialize=serialize, model_name=name)
            tp.render_confusion_matrix(plot_name=name)
            accuracy, f1 = tp.get_model_perfomance()
            col1, col2 = st.columns(2)

            col1.metric(label="Accuracy score", value=str(round(accuracy, 4)))
            col2.metric(label="F1 score", value=str(round(f1, 4)))

            st.image(Image.open(CM_PLOT_PATH))

        except Exception as e:
            st.error('Failed to train model!')
            st.exception(e)

def TrainingApp():
    st.header("Model Training")
    st.info("Before you proceed to training your model. Make sure you "
            "have checked your training pipeline code and that it is set properly.")

    name = st.text_input('Model name', placeholder='decisiontree')
    print("ll", name)
    serialize = st.checkbox('Save model')
    train = st.button('Train Model')

    if train:
        if name =='' and serialize:
            st.error('Please enter a valid name for the model')
        else:
            Train(serialize,name)

