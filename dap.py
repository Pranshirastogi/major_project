import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


years = list(range(1985, 2011))

st.title('Gender Pay Gap')
st.subheader('Data Analytics Project')

st.cache_data()
def load_dataset():
    df=pd.read_csv("work/cleaned_gpg.csv", usecols=['year','region','relate','sex','race','marst','occ','ind','classwkr',
                                                    'hrswork','incwage','annhrs','hrwage','inflate','expendbase10','perconexp',
                                                    'potexp','potexp2','o_occ1990','o_occ1950','o_ind1950','o_ind1990'] )
    df.set_index('year',inplace=True)
    return df

with st.spinner('Loading data...'):
    df = load_dataset()


years = df.index.unique().tolist()
selectyear = st.sidebar.selectbox('Select a year', years)
st.info(f'You selected {selectyear}')

st.write(df.shape)
r = df.race.unique().tolist()
s = df.sex.unique().tolist()
occupation = df.occ.unique().tolist()
industry = df.ind.unique().tolist()

race = st.sidebar.selectbox('select a race', r )
sex = st.sidebar.selectbox('select a sex', s )
occup = st.sidebar.selectbox('select a occupation', occupation )
indus = st.sidebar.selectbox('select a industry', industry )

if st.sidebar.checkbox('Show raw data'):
    st.dataframe(df[(df['race']== race) &  (df['sex'] == sex)][:1000])
    st.dataframe(df[(df['occ']== occup) &  (df['ind'] == indus)][:1000])

df_year = df[df.index == selectyear]

fig1 = px.area(x=df.index, y=df['incwage'], title=f'INCOME WAGE')
fig2 = px.scatter( x=df.index, y=df['occ'], title=f'OCCUPATION')
fig3 = px.bar(x=df.index, y=df['ind'], title=f'INDUSTRY')
fig4 = px.box(x=df.index, y=df['hrswork'], title=f'HOURS WORKED')
if st.checkbox('Show income wage'):
    st.plotly_chart(fig1, use_container_width=True)
if st.checkbox('Show occupation'):
    st.plotly_chart(fig2, use_container_width=True)
if st.checkbox('Show industry'):
    st.plotly_chart(fig3, use_container_width=True)
if st.checkbox('Show hours worked'):
    st.plotly_chart(fig4, use_container_width=True)

fig5 = px.scatter(df, x="incwage", y="hrswork", color="sex", marginal_y="violin", title=f'INCOME WAGE VS HOURS WORKED')
if st.checkbox('Show income wage vs hours worked'):
    st.plotly_chart(fig5, use_container_width=True)

if st.checkbox('Show group analysis'):
    fig7 = px.sunburst(df, path=['classwkr','sex'], values='incwage', title=f'CLASS OF WORKERS AND  THEIR INCOME WAGE')
    st.plotly_chart(fig7, use_container_width=True)
    fig11 = px.sunburst(df,path=['marst','sex'],values='annhrs',title=f'MARITAL STATUS AND NO.OF HOURS WORKED')
    st.plotly_chart(fig11, use_container_width=True)
    fig14 = px.treemap(df,names=[''])
fig8 = px.bar(df, x="incwage", y="expendbase10", color="sex",  title=f'INCOME WAGE VS EXPENDITURE')
if st.checkbox('Show income wage vs expenditure'):
    st.plotly_chart(fig8, use_container_width=True)
fig9 = px.histogram(df,x="o_occ1990",y="sex",title=f'OCCUPATION IN 1990')
fig10 = px.histogram(df,x='o_occ1950',y='sex',title=f'OCCUPATION IN 1950')
if st.checkbox('Show difference in occupation'):
    st.plotly_chart(fig9, use_container_width=True)
    st.plotly_chart(fig10, use_container_width=True)
fig12 = px.violin(df,x='hrswork',y='incwage',title=f'INCOME WAGE VS HOURS WORKED')
fig13 = px.violin(df,x='annhrs',y='hrwage',title=f'HOURLY WAGE VS NO.OF HOURS WORKED')
if st.checkbox('Show comparison between income wage and hours wage'):
    st.plotly_chart(fig12, use_container_width=True)
    st.plotly_chart(fig13, use_container_width=True)

