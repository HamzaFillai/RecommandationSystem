import pickle
import streamlit as st

def recommendAccessoire(product):
    index = accessoires[accessoires['nom'] == product].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_accessoire_names = []
    for i in distances[1:6]:
        recommended_accessoire_names.append(accessoires.iloc[i[0]].nom)
    return recommended_accessoire_names

accessoires = pickle.load(open('accessoire_list.pkl','rb'))
similarity = pickle.load(open('similarity_accessoire.pkl','rb'))

accessoire_list = accessoires['nom'].values

st.header('Accessory Recommender System')

selected_makeup = st.selectbox(
    "Type or select an accessory from the dropdown",
    accessoire_list
)

if st.button('Show Recommendation'):
    for i in recommendAccessoire(selected_makeup):
        st.write(i)