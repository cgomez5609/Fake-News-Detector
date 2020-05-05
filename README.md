# Fake-News-Detector
A machine learning model to predict fake news. This model was developed by using datasets known as Fake.csv and True.csv. The combination of these datasets resulted in 38,729 entries, however, I only used ~40% of it. This resulted in 15,499 entries after preprocessing. For convinience I have already preprocessed the data using Spacy and saved it. However, the files used to preprocess can be found in this repository. The dataset contains 6 columns, but only the 3 following columns were used for testing, 1) the title columns displaying the name of the article, 2) the text column displaying thetext of the article, and 3) the label column displaying whether the entry was fake news or not. For testing, I considered only either the title or the text and their associated label. I tranformed the training data into a bag of words model and used naive Bayes and Support Vector Machine as the algorithms.

Code was made using Python 3.7
Dependencies
scikit-learn: 0.22.1
spacy: 2.2.3
  download en_core_web_sm as well
numpy: 1.18.1
pandas: 1.0.3

I tested for all performance metrics, but given that the dataset used had a ~50/50 ratio of fake vs true news I will only display the results for accuracy below. However the code can be downloaded and tested for the remaining metrics.

Title and Labels Results
Naive Bayes: 92%
Support Vector Machine: 94%

Text and Label Results
Naive Bayes: 93%
Support Vector Machine: 99%


This has shown that when using a portion of the dataset, support vector machine has an accuracy of around 99%.

These datasets were obtained through the kaggle website at https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset. 
