from interface import implements, Interface
from algorithms.interface_algorithm import IAlgorithm
from sklearn.metrics import classification_report

#RandomForest algorithm
from sklearn.ensemble import RandomForestClassifier

class NaiveBayes(implements(IAlgorithm)):

    RF = None

    def __init__(self, estimators, r_state):
        self.RF = RandomForestClassifier(n_estimators = estimators, random_state = r_state)
    
    def predict(self, tfid_dataset, text_to_predict):

        self.RF.fit(tfid_dataset['train_x'], tfid_dataset['train_y'])
        rf_predictions = self.RF.predict(tfid_dataset['test_x'])
        text_prediction = self.RF.predict(text_to_predict)

        #Model Evaluation
        rf_classification_report = classification_report(tfid_dataset['test_y'], rf_predictions)
        print(rf_classification_report)

        return {
            "text_prediction": text_prediction,
            "rf_prediction_report": rf_classification_report
        }
    
