import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

vetements = pd.read_csv('dataset_vetements.csv').drop(['web-scraper-order', 'web-scraper-start-url', 'link to product','link to product-href', 'link to reviews-href', 'image-src'],axis=1)
vetements = vetements.rename(columns = {'name': 'nom'}, inplace = False)
vetements.drop_duplicates(subset='nom', keep="first", inplace=True)
vetements.dropna( inplace=True)
vetements['tags'] = vetements['price'] + vetements['link to reviews'] +  vetements['rating']
vetements = vetements.drop(['price', 'link to reviews', 'rating'],axis=1)

cv = CountVectorizer(max_features=5000,stop_words='english')
vector = cv.fit_transform(vetements['tags']).toarray()

similarity = cosine_similarity(vector)

def recommend(product):
    index = vetements[vetements['nom'] == product].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    for i in distances[1:6]:
        print(vetements.iloc[i[0]].nom)

pickle.dump(vetements,open('vetement_list.pkl','wb'))
pickle.dump(similarity,open('similarity_vetement.pkl','wb'))