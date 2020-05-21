import numpy as np
import pandas as pd
import plotly as py
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from plotly.offline import download_plotlyjs

#Code to read the data from the CSV file
df= pd.read_csv("C:\\Users\\user\\Desktop\\Level 5\\Personal Projects\\covid_19_data.csv")

#Renaming coloumns according to our needs
df= df.rename(columns={'Country/Region':'Country'})
df= df.rename(columns={'ObservationDate':'Date'})

#Manipulating Dataframe
df_countryDate=df[df['Confirmed']>0]
df_countryDate=df_countryDate.groupby(['Date','Country']).sum().reset_index()
df_countryDate

# Manipulate Dataframe
df_countries = df.groupby(['Country', 'Date']).sum().reset_index().sort_values('Date', ascending=False)
df_countries = df_countries.drop_duplicates(subset = ['Country'])
df_countries = df_countries[df_countries['Confirmed']>0]
# Create the Choropleth
fig = go.Figure(data=go.Choropleth(
    locations = df_countries['Country'],
    locationmode = 'country names',
    z = df_countries['Confirmed'],
    colorscale = 'Reds',
    marker_line_color = 'black',
    marker_line_width = 0.5,
))
fig.update_layout(
    title_text = 'Confirmed Cases as of March 28, 2020',
    title_x = 0.5,
    geo=dict(
        showframe = False,
        showcoastlines = False,
        projection_type = 'equirectangular'
    ))
fig.show()
#Creating the Animated Choropleth Map using plotly
figure=px.choropleth(df_countryDate,
                  locations="Country",
                  locationmode="country names",
                  color="Confirmed",
                  hover_name="Country",
                  animation_frame="Date"
                  )

figure.update_layout(
        title_text="Coronavirus Visualization",
        title_x=0.5,
        geo=dict(
                showframe=False,
                showcoastlines=False,
                )
        )

figure.show()