from PIL import Image
import plotly.express as px
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import pairwise_distances, cosine_similarity, cosine_distances
from sklearn.preprocessing import StandardScaler
import streamlit as st
import pickle
import time

from collections import Counter

st.title("Welcome, Digital Nomad!")
image = Image.open('usanew.png')
st.image(image, caption='County clusters accross the US')
st.header("Airton is excited to help you find your next functional destination in the US")
st.subheader("Tell me a county that you love, and I'll give you a list of 5 similar counties that could be a great fit for you to travel/work in, ordered by Euclidean similarity scores")

recommended = pd.read_csv('use_for_recommender1.csv')
attributes = pd.read_csv('county_kmeans_not_encoded.csv')
recommended.drop(columns=['Unnamed: 0'], inplace=True)
reco_names = recommended[['fips', 'state', 'name']]

ss = StandardScaler()
reco_scaled = ss.fit_transform(recommended.drop(columns=['fips', 'name', 'state']))

cs = cosine_similarity(reco_scaled)
recommended = pd.DataFrame(reco_scaled)
recommended = pd.concat([reco_names, recommended], axis=1, ignore_index=True)
recommended = recommended.rename(
    columns={0: 'fips', 1: 'state', 2: 'name', 39: 'bachelors_2019',
             42: 'household_has_broadband_2019', 48: 'households_speak_other_2019', 56: 'median_age_2019',
             58: 'median_individual_income_2019', 64: 'persons_per_household_2019', 65: 'persons_per_household_2019',
             66: 'two_plus_races_2019', 67: 'unemployment_rate_2019'})
    
#countyInput = st.text_input('Enter the county here')
#stateInput = st.text_input('Enter the state here')
###################

countyInput = st.selectbox('Enter the county here', recommended['name'])
stateInput = st.selectbox('Enter the state here', recommended['state'])


##################### median_age_2019 per_capita_income_2019 poverty_2017 bachelors_2019 median_individual_income_2019 two_plus_races_2017 

def similar_county(countyInput, stateInput):
    state = recommended[recommended['state'] == stateInput]
    countyIndex = state[state['name'] == countyInput].index.values[0]
    scores = list(enumerate(cs[int(countyIndex)]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    sorted_scores = sorted_scores[1:]

    j = 0
    bachelor = []
    outputscore = []
    output_place = []
    broadband = []
    pop = []
    age = []
    income = []
    ue = []
    density = []
    english = []
    for item in sorted_scores:
        itemIndex = item[0]
        sim_score = item[1]
        county_ = recommended.iloc[itemIndex][['name', 'state']].values[0]
        state_ = recommended.iloc[itemIndex][['name', 'state']].values[1]
        bachelor_ = attributes.iloc[itemIndex]['bachelors_2019']
        broadband_ = attributes.iloc[itemIndex]['household_has_broadband_2019']
        pop_ = attributes.iloc[itemIndex]['pop_2019']
        age_ = attributes.iloc[itemIndex]['median_age_2019']
        income_ = attributes.iloc[itemIndex]['median_individual_income_2019']
        density_ = attributes.iloc[itemIndex]['persons_per_household_2019']
        ue_ = attributes.iloc[itemIndex]['unemployment_rate_2019']
        english_ = attributes.iloc[itemIndex]['foreign_born_2010']


        output_place.append(county_+', ' + state_)
        outputscore.append(sim_score)
        bachelor.append(bachelor_)
        broadband.append(broadband_)
        pop.append(pop_)
        age.append(age_)
        income.append(income_)
        english.append(english_)
        ue.append(ue_)
        density.append(density_)
        #output = "Based on Cosine Similarities, the 5 most recommended counties to " + countyInput + ',' stateInput + 'is' listed[0]
        j = j+1
        if j > 4:
            break
    return pd.DataFrame({'County': output_place, 'Similarity Score (out of 1)': outputscore, 'Pop': pop, 'Density': density, 'Median age': age, 'Percent international': english, 'Median Income': income, 'Percent with Bachelors': bachelor, 'Broadband connection rate': broadband})

if countyInput and stateInput: 
#    st.balloons()  
    st.table(similar_county(countyInput, stateInput))
video_file = open('airport.mp4', 'rb')
video_bytes = video_file.read()
st.header("Happy remote living!")
st.write("As you plan, you can also explore more county data through this tableau [dashboard](https://public.tableau.com/app/profile/airton.tatoug.kamdem/viz/county_tb/Dashboard1?publish=yes)")
st.video(video_bytes)
