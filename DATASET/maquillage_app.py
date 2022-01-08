import pickle
import streamlit as st

def recommendMaquillage(product):
    index = maquillages[maquillages['nom'] == product].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_maquillage_names = []
    for i in distances[1:6]:
        recommended_maquillage_names.append(maquillages.iloc[i[0]].nom)
    return recommended_maquillage_names

maquillages = pickle.load(open('maquillage_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

maquillage_list = maquillages['nom'].values

st.header('Makeup Recommender System')

selected_makeup = st.selectbox(
    "Type or select a makeup from the dropdown",
    maquillage_list
)

if st.button('Show Recommendation'):
    for i in recommendMaquillage(selected_makeup):
        st.write(i)