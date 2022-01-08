import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

accessoires = pd.read_csv('datatset_accessoire.csv').drop(['web-scraper-order', 'web-scraper-start-url', 'link to product','link to product-href', 'link to reviews-href', 'image-src'],axis=1)
accessoires = accessoires.rename(columns = {'name': 'nom'}, inplace = False)
accessoires.drop_duplicates(subset='nom', keep="first", inplace=True)
accessoires.dropna( inplace=True)
accessoires['tags'] = accessoires['price'] + accessoires['link to reviews'] +  accessoires['rating']
accessoires = accessoires.drop(['price', 'link to reviews', 'rating'],axis=1)

cv = CountVectorizer(max_features=5000,stop_words='english')
vector = cv.fit_transform(accessoires['tags']).toarray()

similarity = cosine_similarity(vector)

def recommend(product):
    index = accessoires[accessoires['nom'] == product].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    for i in distances[1:6]:
        print(accessoires.iloc[i[0]].nom)

recommend('Casquette Bleu Marine + casquette noir')

pickle.dump(accessoires,open('accessoire_list.pkl','wb'))
pickle.dump(similarity,open('similarity_accessoire.pkl','wb'))