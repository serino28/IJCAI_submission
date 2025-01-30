# -*- coding: utf-8 -*-
"""Untitled33.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GAbWpFsGGfSLPnqnZZmgtWDT10CSJsAK
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import gdown

# Set page configuration
st.set_page_config(page_title="IJCAI submission", layout="wide")

# Load dataset from Google Drive
# Load dataset from Google Drive
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/serino28/IJCAI_submission/refs/heads/main/data_submission.csv"  # Sostituisci con il tuo link RAW
    df = pd.read_csv(url, sep=",", encoding="utf-8-sig", on_bad_lines="skip")
    #st.success("Dataset caricato con successo!")
    return df


df = load_data()

# Ensure correct data types
#df['soc2d'] = df['soc2d'].astype('category')

# Compute median values for quadrant lines
mean_x = df['te_score_all_percentage'].median()
mean_y = df['te_score_engagement_percentage'].median()

# Create scatter plot
fig = px.scatter(
    df,
    x='te_score_all_percentage',
    y='te_score_engagement_percentage',
    color='Occupation group',
    labels={'te_score_all_percentage': 'Exposure Rate (TEAI)',
            'te_score_engagement_percentage': 'Replacement Rate (TRAI)'},
    hover_data=['Title']
)

# Add quadrant reference lines
fig.add_hline(y=mean_y, line_dash="dot", line_color="red")
fig.add_vline(x=mean_x, line_dash="dot", line_color="red")

# Add custom layout settings
fig.update_traces(
    textposition='top center',
    marker=dict(size=10, opacity=0.7)
)
fig.update_layout(
    xaxis=dict(
        title='Exposure Rate (TEAI)',
        range=[0, 100],
        zeroline=False,
        showgrid=True,
        gridcolor='lightgray',
        gridwidth=0.3,
        title_font=dict(size=18, color="black"),  # Cambiato colore titolo
        tickfont=dict(size=16, color="black")
    ),
    yaxis=dict(
        title='Replacement Rate (TRAI)',
        range=[0, 100],
        zeroline=False,
        showgrid=True,
        gridcolor='lightgray',
        gridwidth=0.3,
        title_font=dict(size=18, color="black"),  # Cambiato colore titolo
        tickfont=dict(size=16, color="black")  # Cambiato colore etichette
    ),
    showlegend=True,
    legend=dict(
        orientation="h",
        y=-0.2,
        x=0.5,
        xanchor='center',
        title_text=None,
        font=dict(size=18, color="black")
    ),
    plot_bgcolor='#f9f9f9',
    paper_bgcolor='#f9f9f9',
    width=1600,
    height=600
)

# Add quadrant annotations
annotations = [
    dict(x=mean_x * 0.35, y=mean_y * 0.035, text="Low Exposure, Low Automation", showarrow=False, font=dict(size=18), color = 'black'),
    dict(x=mean_x * 0.35, y=mean_y * 1.85, text="Low Exposure, High Automation", showarrow=False, font=dict(size=18), color='black'),
    dict(x=mean_x * 1.65, y=mean_y * 1.85, text="High Exposure, High Automation", showarrow=False, font=dict(size=18), color='black'),
    dict(x=mean_x * 1.65, y=mean_y * 0.035, text="High Exposure, Low Automation", showarrow=False, font=dict(size=18), color= 'black')
]
fig.update_layout(annotations=annotations)

# Display title and plot in Streamlit
st.title("Towards the Terminator Economy: Assessing Job Exposure to AI through LLMs")
st.plotly_chart(fig, use_container_width=True)
