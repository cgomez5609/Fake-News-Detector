""" 
    This project will, hopefully, be able to create a model that will predict 
    fake news.
"""

from file_management.get_filepath import FilePath
from dataframe_utils.tools import remove_empty_rows, get_dataframe_sample
from preprocessing.clean import CleanUpText
import pandas as pd
import numpy as np
from collections import Counter

def main():
    # For simplicity the data was preprocessed prior to this script
    filename = "True_Fake_35_preprocessed.tsv"
    subdirectory = "preprocessed"
    
    # Get out file path
    fp = FilePath(filename=filename, subdir=subdirectory)
    
    path = fp.get_path()
    
    # Create DataFrame
    df = pd.read_csv(path, sep="\t")
    
    # Remove any empty rows
    remove_empty_rows(df, "title")
    remove_empty_rows(df, "text")

    # Get the title, text and labels for training and testing
    titles = df.title.values
    text = df.text.values
    labels = df.label.values
    
    # Convert labels to numerical data to be used in algorithms
    labels[labels == "fake"] = int(1)
    labels[labels == "True"] = int(0)
    
    # Convert to numpy arrays
    titles = np.array(titles)
    text = np.array(text)
    labels = np.array(labels, dtype=float) # Cannot be of object type
    
    # Counts the number 
    labels_stats = Counter(labels)
    print()
    print(f"There are {labels_stats[0]} True articles")
    print(f"There are {labels_stats[1]} Fake articles")
    print()
    
    names = ["titles", "text"]
    data = [titles, text]
    
    for i, datum in enumerate(data):
        # Split our data into training and testing (2 way split for this project)
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(datum, labels, test_size=0.20, shuffle=True, random_state=42)
        
        
        # Vectorize our data text data (Bag of Words)
        from sklearn.feature_extraction.text import TfidfVectorizer
        vectorizer = TfidfVectorizer()
        X_train = vectorizer.fit_transform(X_train)
        word_dict = vectorizer.vocabulary_ # All the words found in the training set
        
        # Only transformed X_test 
        X_test = vectorizer.transform(X_test)
            
        # Naive Bayes Algorithm
        from sklearn.naive_bayes import MultinomialNB
        classifier = MultinomialNB()
        classifier.fit(X_train, y_train)
        
        y_pred = classifier.predict(X_test)
        
        from sklearn.metrics import classification_report, confusion_matrix
        cm = confusion_matrix(y_test, y_pred)
        report = classification_report(y_test, y_pred)
        print(f"Naive Bayes for {names[i]}")
        print()
        print(cm)
        print()
        print(report)
        print()
        print()
        
        # Support Vector Machine Algorithm
        from sklearn import svm
        classifier = svm.SVC(kernel='linear')
        classifier.fit(X_train, y_train)
        
        y_pred = classifier.predict(X_test)
        
        cm = confusion_matrix(y_test, y_pred)
        report = classification_report(y_test, y_pred)
        print(f"Support Vector Machine for {names[i]}")
        print()
        print(cm)
        print()
        print(report)
        print()
        print()
        
        print("---------------------------------------------------------")
        print()
        
if __name__ == "__main__":
    main()




