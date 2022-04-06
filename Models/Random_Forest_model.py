import nltk
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import string
import numpy as np

#create data sets
data = pd.read_excel('uniq.xlsx')
data_t = pd.read_excel('testing.xlsx')

# Create function to clean data
def clean_text(text):
  text=[hausa_stem(sent) for sent in text]
  text = "".join([word.lower() for word in text] 
  tokens = re.split('\W+', text)
  text = tokens
  return text
  
# create TF Idf object for Training
tfidf_vect = TfidfVectorizer(analyzer=clean_text)
X_tfidf = tfidf_vect.fit_transform(data['Hausa'])
X_train= pd.DataFrame(X_tfidf.toarray())

y_train=data['Polarity']
y_train = y_train.astype(np.int8)

# create TF Idf object for Testing
tfidf_vect_test = TfidfVectorizer(analyzer=clean_text)
y_tfidf = tfidf_vect.transform(data_t['Hausa'].values.astype('U'))
X_test= pd.DataFrame(y_tfidf.toarray())

y_test=data_t['Polarity']
y_test = y_test.astype(np.int8)

#Training process
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_recall_fscore_support as score
from sklearn.model_selection import train_test_split

rf = RandomForestClassifier(n_estimators=100, max_depth=None, n_jobs=-1)
rf_model = rf.fit(X_train, y_train)

y_pred = rf_model.predict(X_test)
precision, recall, fscore, support = score(y_test, y_pred, average='weighted')

print('Precision: {} / Recall: {} / Accuracy: {}'.format(round(precision, 3),round(recall, 3), round((y_pred==y_test).sum() / len(y_pred),3)))
