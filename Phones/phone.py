import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import math
import numpy as np

phones = pd.read_csv('dataset_android.csv').drop(['web-scraper-start-url', 'link to phone','link to phone-href'],axis=1)
phones = phones.rename(columns={'web-scraper-order': 'idProduct','maruqe': 'marque'}, inplace = False)

phones.dropna(subset=['price'] ,inplace=True)
phones.drop_duplicates(inplace=True)
phones = phones.fillna(0)
print(phones.duplicated().sum())
#phones['rating'] = phones['rating'].apply(lambda x:str(math.floor(x)) + " out of 5")
phones['tags'] = phones['price'] + phones['caracteristique']

cv = CountVectorizer()
vector = cv.fit_transform(phones['tags']).toarray()
cosinesim = cosine_similarity(vector)

def recommand(product) :
    index = phones[phones['caracteristique'] == product].index[0]
    distance = sorted(list(enumerate(cosinesim[index])), reverse = True, key=lambda x : x[1])
    for i in distance[1:10] :
        print(i[1])

#recommand('Ulefone Note 10 32Go+2Go Octa-Core, 6,52Pouce, 8MP AI Triple Caméra, Fingerprint')

pickle.dump(phones,open('phone_list.pkl','wb'))
pickle.dump(cosinesim,open('similarity_phone.pkl','wb'))

#phones['userId'] = np.random.randint(1, 8, phones.shape[0])
#phones.insert(0, 'userId', phones.pop('userId'))
phones['classe'] = "Phone"

pickle.dump(phones,open('df_phone.csv','wb'))