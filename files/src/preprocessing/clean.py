from . import preprocessing_functions as pf
#import preprocessing_functions as pf
from multiprocessing import Pool
import pandas as pd

class CleanUpText:
    
    def __init__(self, dataset):
        self.__dataset: list(str) = dataset
        
    def set_dataset(self, new_dataset):
        self.__dataset = new_dataset
    
    def get_dataset(self):
        return self.__dataset   
        
    def lowercase_data(self):
        for index, post in enumerate(self.__dataset):
            self.__dataset[index] = pf.make_lower_case(post)
    
    def eliminate_stopwords(self):
        for index, post in enumerate(self.__dataset):
            self.__dataset[index] = pf.remove_stopwords(post)
            
    def eliminate_punctuation(self):
        for index, post in enumerate(self.__dataset):
            self.__dataset[index] = pf.remove_stopwords(post)
            self.__dataset[index] = pf.remove_missed_punctuation(self.__dataset[index])
    
    def lemmatize_data(self):
        for index, post in enumerate(self.__dataset):
            self.__dataset[index] = pf.lemmatization(post)
            
    def eliminate_empty_posts(self):
        self.__dataset = list(filter(None, self.__dataset))
        
    def get_tokenized_text(self):
        tokenized_data = list()
        for index, post in enumerate(self.__dataset):
            tokenized_data.append(pf.tokenize(post))
        return tokenized_data
            
    def apply_all(self):
        """
        Apply all methods in class. This is the ideal pipeline designed by the
        author.
        """
        for index, post in enumerate(self.__dataset):
            self.__dataset[index] = pf.make_lower_case(self.__dataset[index])
            self.__dataset[index] = pf.remove_stopwords(self.__dataset[index])
            self.__dataset[index] = pf.remove_missed_punctuation(self.__dataset[index])
            self.__dataset[index] = pf.lemmatization(self.__dataset[index])
        



    
