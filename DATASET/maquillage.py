import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

maquillages = pd.read_csv('dataset_maquillage.csv').drop(['web-scraper-order', 'web-scraper-start-url', 'link to product','link to product-href', 'link to reviews-href', 'image-src'],axis=1)
data = maquillages
print(data)
maquillages = maquillages.rename(columns = {'name': 'nom'}, inplace = False)
maquillages.drop_duplicates(subset='nom', keep="first", inplace=True)
maquillages.dropna( inplace=True)
maquillages['tags'] = maquillages['price'] + maquillages['link to reviews'] +  maquillages['ratings']
maquillages = maquillages.drop(['price', 'link to reviews', 'ratings'],axis=1)

cv = CountVectorizer(max_features=5000,stop_words='english')
vector = cv.fit_transform(maquillages['tags']).toarray()

similarity = cosine_similarity(vector)

def recommend(product):
    index = maquillages[maquillages['nom'] == product].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    for i in distances[1:10]:
        print(maquillages.iloc[i[0]])

recommend('Maybelline New York Maybelline - Palette Master Bronzer et Enlumineur - BRONZE')
print(maquillages)

pickle.dump(maquillages,open('maquillage_list.pkl','wb'))
pickle.dump(similarity,open('similarity_tv.pkl','wb'))