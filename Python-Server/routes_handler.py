from textprocessor import Textprocessor
from modelbuilder import ModelBuilder
#import os
import pickle
from sklearn.externals import joblib

class RoutesHandler:
    rf_modelfile = ''
    nb_modelfile = ''
    rf_model = ''
    nb_model = ''


    def __init__(self, nf_path, rf_path):
        self.rf_modelfile = nf_path
        self.nb_modelfile = rf_path

    #ToDo
    def load_models(self):
        with open(self.rf_modelfile, 'rb') as rf_file:
            self.rf_model = pickle.load(rf_file)

        with open(self.nb_modelfile, 'rb') as nb_file:
            self.nb_model = pickle.load(nb_file)

    def classify_news(self, posted_data):
        #self.load_models()
        text_processor = Textprocessor('TextProcessor')
        pasted_text = text_processor.parse_title_date(posted_data["title"], posted_data["text"])
        text_to_tfid = text_processor.execute_feature_extration(pasted_text)
        modelbuilders = ModelBuilder('Dataset/True.csv', 'Dataset/Fake.csv')
        predictions = modelbuilders.predict(text_to_tfid["tfid_features"], text_to_tfid["max_features"])

        return predictions