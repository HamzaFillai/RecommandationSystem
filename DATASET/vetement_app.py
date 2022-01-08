import pickle
import streamlit as st

def recommendVetement(product):
    index = vetements[vetements['nom'] == product].index[0]
    distances = sorted(list(enumerate(similarity_vetement[index])), reverse=True, key=lambda x: x[1])
    recommended_vetement_names = []
    for i in distances[1:6]:
        recommended_vetement_names.append(vetements.iloc[i[0]].nom)
    return recommended_vetement_names

vetements = pickle.load(open('vetement_list.pkl','rb'))
similarity_vetement = pickle.load(open('similarity_vetement.pkl','rb'))

vetement_list = vetements['nom'].values

st.header('Clothing Recommender System')

selected_cloth = st.selectbox(
    "Type or select a cloth from the dropdown",
    vetement_list
)

if st.button('Show Recommendation'):
    for i in recommendVetement(selected_cloth):
        st.write(i)