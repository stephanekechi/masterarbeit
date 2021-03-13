from interface import implements
from algorithms.interface_algorithm import IAlgorithm
from sklearn.metrics import classification_report #,confusion_matrix

#Naive Bayes algorithm
from sklearn.naive_bayes import MultinomialNB

class NaiveBayes(implements(IAlgorithm)):

    NB = None
    def __init__(self):
        self.NB = MultinomialNB()
    
    def predict(self, tfid_dataset, text_to_predict):

        self.NB.fit(tfid_dataset['train_x'], tfid_dataset['train_y'])
        nb_predictions = self.NB.predict(tfid_dataset['test_x'])
        text_prediction = self.NB.predict(text_to_predict)

        #Model evaluation
        nb_classification_report = classification_report(tfid_dataset['test_y'], nb_predictions)
        print(nb_classification_report)
        #print(confusion_matrix(train_test_data['test_y'], nb_predictions))

        return {
            "text_prediction": text_prediction,
            "nb_prediction_report": nb_classification_report
        }
    
