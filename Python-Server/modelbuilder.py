import re
import nltk
import string
import pandas as pda

from nltk.corpus import stopwords #not working
nltk.download('stopwords') #Download stopwords of different languages
nltk.download('punkt') #Download punkt bibliothek of different languages
nltk.download('wordnet') #Download wordnet bibliothek of different languages

from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

#Local Classes Imports
from textprocessor import Textprocessor
from webscraper import WebScraper
from algorithms.naive_bayes import NaiveBayes
from algorithms.random_forest import RandomForest

class ModelBuilder:

    true_dataset: ''
    fake_dataset: ''
    text_processor: ''

    def __init__(self, true_path, false_path):
        self.true_dataset = pda.read_csv(true_path)
        self.fake_dataset = pda.read_csv(false_path)
        self.text_processor = Textprocessor('TextProcessor')

    #Function for removing punctuations in a given text
    def remove_punctuations(self, input_text):
        translation_table = dict.fromkeys(map(ord, string.punctuation), ' ')
        translated_str_value = input_text.translate(translation_table)

        return translated_str_value

    #Function to remove stopwords in a given text
    def remove_stopwords(self, input_text):
        pattern = re.compile(r'\b(' + r'|'.join(stopwords.words('english')) + r')\b\s*')
        stopword_text = pattern.sub(' ', input_text)

        return stopword_text

    #Function for lemmatizing
    def lemmatize_words(self, input_text):
        lemmatizer = WordNetLemmatizer()
        lower_input_text = input_text.lower()
        lemmatized_words = lemmatizer.lemmatize(lower_input_text)

        return lemmatized_words

    def get_array_range(self, array):
        
        return range(len(array))

    def lemmatize_words_array(self, text_array):
        cleared_lemmatizedwords = []
        for index in self.get_array_range(text_array):
            test_data_lemmatized = self.text_processor.lemmatize_words(text_array[index])
            cleared_lemmatizedwords.append(test_data_lemmatized)

        return cleared_lemmatizedwords

    def remove_punctuations_array(self, array):
        array_cleared_punct = []
        for index in self.get_array_range(array):
            test_data_punct = self.text_processor.remove_punctuations(array[index])
            array_cleared_punct.append(test_data_punct)

        return array_cleared_punct

    def remove_stopwords_array(self, array):
        cleared_stopwords = []
        for index in self.get_array_range(array):
            temp_data_stopwords = self.text_processor.remove_stopwords(array[index])
            cleared_stopwords.append(temp_data_stopwords)
        
        return cleared_stopwords

    def create_features_vectors(self, array, max_features_):
        #Creating the bag of words model
        cv = CountVectorizer(max_features = int(max_features_))
        array_vector = cv.fit_transform(array).toarray()
        
        #Creating the TFIDF
        tfidf = TfidfTransformer()
        array_tfidf = tfidf.fit_transform(array_vector).toarray()

        return array_tfidf

    # Function to retrieve processed words
    def feature_extraction(self, full_text, max_features):
        lemmatizedwords = self.lemmatize_words_array(full_text)
        clean_puncts_array = self.remove_punctuations_array(lemmatizedwords)
        clean_stopwds_array = self.remove_stopwords_array(clean_puncts_array)
        data_tfidf = self.create_features_vectors(clean_stopwds_array, max_features)
        
        return data_tfidf

    def get_train_test_data(self, max_features):
        web_scraper = WebScraper(3, 3)
        scraped_false_data = web_scraper.get_false_news()
        scraped_true_data = web_scraper.get_true_news()

        #Adding new column in both dataframe variables ('0' for fake) and ('1' for true)
        self.true_dataset['label'] = 1
        scraped_true_data['label'] = 1
        print(scraped_true_data.head)
        self.fake_dataset['label'] = 0
        scraped_false_data['label'] = 0

        #Concatenation of both dataframe variables
        total_dataset = pda.concat([scraped_false_data, self.true_dataset, self.fake_dataset, scraped_true_data], axis=0)
        
        total_dataset['fullLengthText'] = self.text_processor.parse_title_text(total_dataset.title, total_dataset.text)

        #Creating a new tempory dataframe using 'label' and 'fullLengthText'
        temp_data = total_dataset[['fullLengthText', 'label']]
        #reschefful the data index in dataframe
        temp_data = temp_data.reset_index()
        temp_data.drop(['index'], axis = 1, inplace=True)

        ##ML Model data preparation
        data_x = temp_data.fullLengthText
        data_y = temp_data.label

        #Make sure we have 'String' as type
        data_x = data_x.astype(str)

        # Setting the function with parameters
        final_data_x = self.feature_extraction(data_x, max_features)

        # Preparing training and testing data
        seed = 4353
        train_x, test_x, train_y, test_y = train_test_split(final_data_x, data_y, test_size = 0.25, random_state = seed)

        train_test_obj = {
            'train_x': train_x,
            'test_x': test_x,
            'train_y': train_y,
            'test_y': test_y,
            'seed': seed
        }
        return train_test_obj

    def perform_naive_bayes(self, train_test_data, tfid_to_predict):
        nb_model = NaiveBayes()
        prediction_result = nb_model.predict(train_test_data, tfid_to_predict)

        return prediction_result

    def perform_random_forest(self, train_test_data, tfid_to_predict):
        rf_model = RandomForest(10, int(train_test_data['seed']))
        prediction_result = rf_model.predict(train_test_data, tfid_to_predict)

        return prediction_result

    def predict(self, tfid_to_predict, max_features):
        train_test_data = self.get_train_test_data(max_features)

        #Prediction
        rf_predicted = self.perform_random_forest(train_test_data, tfid_to_predict)
        nb_predicted = self.perform_naive_bayes(train_test_data, tfid_to_predict)

        resJson = {
            'naive_bayes': {
                'prediction': int(nb_predicted["text_prediction"][0]),
                'report': nb_predicted["nb_prediction_report"]
            },
            'random_forest': {
                'prediction': int(rf_predicted["text_prediction"][0]),
                'report': rf_predicted["rf_prediction_report"]
            }
        }

        return resJson