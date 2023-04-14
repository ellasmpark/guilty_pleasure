import streamlit as st

import numpy as np
import pandas as pd

st.markdown("""# Welcome to Guilty Pleasure""")

# tbd more introductory text and a picture 

# User's age, gender, weight, activity level, goal 

age = st.number_input('How old are you?')
gender = st.radio('Your Gender?',('Male','Female'))
weight = st.number_input('Your Weight?')
activity_level = st.radio(
    'Which one best describes your activity level?'
    ,( 
      'Sedentary',
        'Light activity',
        'Moderate activity',
        'Very Active' 
        )
    )
goal = st.radio(
        'Which one best describes your personal goal?'
    , ( 'Weight loss',
        'Maintain',
        'Weight gain'
        )
    )
