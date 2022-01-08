import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import math
import numpy as np

tvs = pd.read_csv('dataset_TV.csv').drop(['web-scraper-start-url', 'link to TV','link to TV-href'],axis=1)
tvs = tvs.rename(columns={'web-scraper-order': 'idProduct'}, inplace = False)

tvs.dropna(subset=['price'] ,inplace=True)
tvs.drop_duplicates(inplace=True)
tvs = tvs.fillna(0)

#tvs['rating'] = tvs['rating'].apply(lambda x:str(math.floor(x)) + " out of 5")
tvs['tags'] = tvs['price'] + tvs['caracteristique']

cv = CountVectorizer()
vector = cv.fit_transform(tvs['tags']).toarray()
cosinesim = cosine_similarity(vector)

def recommand(product) :
    index = tvs[tvs['caracteristique'] == product].index[0]
    distance = sorted(list(enumerate(cosinesim[index])), reverse = True, key=lambda x : x[1])
    print(distance)
    for i in distance[1:10] :
        print(i[1])

#recommand('Samsung 32" Smart Tv LED SERIE 5 Récepteur WIFI TNT USB HDMI')

pickle.dump(tvs,open('TV_list.pkl','wb'))
pickle.dump(cosinesim,open('similarity_tv.pkl','wb'))

#tvs['userId'] = np.random.randint(1, 8, tvs.shape[0])
#tvs.insert(0, 'userId', tvs.pop('userId'))
tvs['classe'] = "TV"

pickle.dump(tvs,open('df_TV.csv','wb'))


