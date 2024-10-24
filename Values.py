from Simplify import a_join
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(a_join)

feature_names = vectorizer.get_feature_names_out()
tfidf_scores = tfidf_matrix.toarray().flatten()

tfidf_df = pd.DataFrame({'word': feature_names, 'tfidf': tfidf_scores})

tfidf_df = tfidf_df.sort_values(by='tfidf', ascending=False)

tfidf_df.to_csv('tfidf_results.csv', index=False)

