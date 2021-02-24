import re
import nltk
import string
from nltk.corpus import stopwords, wordnet
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import numpy

nltk.download('stopwords')

class Textprocessor:
    name = ''
    
    def __init__(self, name):
        self.name = name

    def parse_title_date(self, title, text):
            return title + ' ' + text
    
    
    def remove_punctuations(self, input_text):
        translation_table = dict.fromkeys(map(ord, string.punctuation), ' ')
        translated_str_value = input_text.translate(translation_table)

        return translated_str_value
    
    def remove_stopwords(self, input_text):
        pattern = re.compile(r'\b(' + r'|'.join(stopwords.words('english')) + r')\b\s*')
        stopword_text = pattern.sub(' ', input_text)

        return stopword_text
    
    def lemmatize_words(self, input_text):
        lemmatizer = WordNetLemmatizer()
        lower_input_text = input_text.lower()
        lemmatized_words = lemmatizer.lemmatize(lower_input_text)

        return lemmatized_words
    
    def execute_data_cleaning(self, input_text):
        lemmatized_text = self.lemmatize_words(input_text)
        punctuated_text = self.remove_punctuations(lemmatized_text)
        stoped_text = self.remove_stopwords(punctuated_text)
        
        return stoped_text
     
    def convert_to_countvectorizer(self, input_text):
        cv = CountVectorizer()
        input_text_vector = cv.fit_transform(numpy.array([input_text])).toarray()
        model_max_features = len(cv.get_feature_names())

        vectorizered_obj = {
            "vector": input_text_vector,
            "max_features": model_max_features
        }
        
        return vectorizered_obj
    
    def execute_tfid_transformer(self, input_text):
        tfidf = TfidfTransformer()
        full_data_tfidf = tfidf.fit_transform(input_text).toarray()

        return full_data_tfidf
                
    def execute_feature_extration(self, input_text):
        cleaned_input_text = self.execute_data_cleaning(input_text)
        vectorizered_text = self.convert_to_countvectorizer(cleaned_input_text)

        tfid_transformed_text = {
            "tfid_features": self.execute_tfid_transformer(vectorizered_text["vector"]),
            "max_features": vectorizered_text["max_features"]
        }

        return tfid_transformed_text