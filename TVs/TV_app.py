import pickle
import streamlit as st
import pandas as pd


def recommendTV(product,n):
    index = tvs[tvs['caracteristique'] == product].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    L=[]
    for i in distances[1:n+1]:
        L.append([tvs.iloc[i[0]].caracteristique, tvs.iloc[i[0]].price, tvs.iloc[i[0]].rating, tvs.iloc[i[0]].marque, i[1]])
    st.write(pd.DataFrame(L, columns=["Caracteristique", "Price", "Rating", "Marque", "CosineSimularity"]))

tvs = pickle.load(open('TV_list.pkl','rb'))
similarity = pickle.load(open('similarity_tv.pkl','rb'))

tv_list = tvs['caracteristique'].values

st.header('TVs Recommender System')

selected_makeup = st.selectbox(
    "Type or select a TVs from the dropdown",
    tv_list
)

int_val = st.number_input('Seconds', min_value=1, step=1)

if st.button('Show Recommendation'):
    recommendTV(selected_makeup,int_val)