from textprocessor import Textprocessor
from modelbuilder import ModelBuilder
#import os
import pickle
from db_services.mysql_db import MySqlDB

class RoutesHandler:

    rf_modelfile = ''
    nb_modelfile = ''
    rf_model = ''
    nb_model = ''
    db = None


    def __init__(self, rf_modelfile, nb_modelfile):
        self.rf_modelfile = rf_modelfile
        self.nb_modelfile = nb_modelfile
        """
        self.db = MySqlDB({
            "host" : "localhost",
            "user" : "root",
            "passwd": "root"
        }) """

    #ToDo, Not efficient now
    def load_models(self):
        with open(self.rf_modelfile, 'rb') as rf_file:
            self.rf_model = pickle.load(rf_file)

        with open(self.nb_modelfile, 'rb') as nb_file:
            self.nb_model = pickle.load(nb_file)

    def classify_news(self, posted_data):
        #self.load_models()
        text_processor = Textprocessor('TextProcessor')
        pasted_text = text_processor.parse_title_text(posted_data['title'], posted_data['text'])
        text_to_tfid = text_processor.execute_feature_extration(pasted_text)
        modelbuilders = ModelBuilder('Dataset/True.csv', 'Dataset/Fake.csv')
        predictions = modelbuilders.predict(text_to_tfid['tfid_features'], text_to_tfid['max_features'])

        return predictions
    """
    def get_users(self):
        uu
    """