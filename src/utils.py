import numpy as np
import itertools
import matplotlib.pyplot as plt
import streamlit as st


class PlotUtils:
    @staticmethod
    def plot_confusion_matrix(cm, classes, title, normalize=False, cmap=plt.cm.Blues):
        title = 'Confusion Matrix of {}'.format(title)

        if normalize:
            cm = cm.astype(float) / cm.sum(axis=1)[:, np.newaxis]

        plt.imshow(cm, interpolation='nearest', cmap=cmap)
        plt.title(title)
        plt.colorbar()
        tick_marks = np.arange(len(classes))
        plt.xticks(tick_marks, classes, rotation=45)
        plt.yticks(tick_marks, classes)

        fmt = '.2f' if normalize else 'd'
        thresh = cm.max() / 2.
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            plt.text(
                j,
                i,
                format(cm[i, j], fmt),
                horizontalalignment='center',
                color='white' if cm[i, j] > thresh else 'black'
            )

        plt.tight_layout()
        plt.ylabel('True label')
        plt.xlabel('Predicted label')



class MultiPage:

    def __init__(self) -> None:
        self.pages = []

    def add_page(self, title, func) -> None:
        """Class Method to Add pages to the project
        Args:
            title ([str]): The title of page which we are adding to the list of apps

            func: Python function to render this page in Streamlit
        """

        self.pages.append(
            {
                "title": title,
                "function": func
            }
        )

    def run(self):
        # Drodown to select the page to run
        page = st.sidebar.selectbox(
            'Options',
            self.pages,
            format_func=lambda page: page['title']
        )

        # run the app function
        page['function']()