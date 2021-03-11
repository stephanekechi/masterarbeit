from interface import Interface

class IAlgorithm(Interface):

    def predict(self, tfid_dataset, text_to_predict):
        pass