import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


years = list(range(1985, 2011))

st.title('DATA ANALYSIS MAJOR PROJECT')
st.subheader('GENDER PAY GAP ANALYSIS')

st.cache_data()
def load_dataset():
    df=pd.read_csv("cleaned_gpg_v2.csv", usecols=['year','region','relate','sex','race','marst','occ','ind','classwkr',
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


if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.dataframe(df[:1000])

df_year = df[df.index == selectyear]

if st.sidebar.checkbox('Show distribution of sex and race'):
    fig1 = px.pie(df,'sex')
    st.plotly_chart(fig1, use_container_width=True)
    st.write('''ANALYSIS -
            No. of males are more than female by 2.2%''')
    fig2 = px.pie(df,'race')
    st.plotly_chart(fig2, use_container_width=True)
    st.write('''ANALYSIS -
             No. of people distributed according to their race are as follows :
             Hispanic- 14.3% ,
             White non hispanic- 69.8%,
             Black non hispanic- 9.16%,
             Others- 6.26%''')
    fig3 = px.pie(df,'race',facet_col='sex')
    st.plotly_chart(fig3, use_container_width=True)
    st.write('''ANALYSIS -
             Male : Hispanic- 15.6% , White non hispanic - 70.1% , Black non hispanic- 8.13% , Others- 6.14% ;
             FEMALE : Hispanic- 13% , White non hispanic - 69.5% , Black non hispanic- 11.2% , Others- 6.38% ;
             Conluding that hispanic and white non hispanic male are more in number than female oncs and black non hispanic and others male are less in number than female ones.''')
fig4 = px.scatter(df, x="incwage", y="hrswork", color="sex", marginal_y="violin", title=f'INCOME WAGE VS HOURS WORKED')
if st.sidebar.checkbox('Show income wage vs hours worked'):
    st.plotly_chart(fig4, use_container_width=True)
    st.write('''ANALYSIS -
            Upper limit of male employees working is 60 hours where as female employees working is 52 hours.
            75% of male workers work 48 hours where as female workers work 40 hours.
            50% of male workers work for 40 hours same as female workers.
            25% of male workers work for 40 hours where as female workers work for 32 hours.
            Lower limit of male employees working is 28 hours where as female employees working is 24 hours.
            And we can conlude that male workers are paid more that female workers by the figure.''')
    
if st.sidebar.checkbox('Show group analysis'):
    fig5 = px.sunburst(df, path=['classwkr','sex'], values='incwage', title=f'CLASS OF WORKERS AND  THEIR INCOME WAGE')
    st.plotly_chart(fig5, use_container_width=True)
    st.write('''ANALYSIS -
             We can conclude that private workers are paid more than government workers.
             Also male workers earn more than female workers in private sector , fedral govt and govt sector where as in local govt and state govt female workers have higher pay offs.''')

    fig6 = px.sunburst(df,path=['marst','sex'],values='annhrs',title=f'MARITAL STATUS AND NO.OF HOURS WORKED')
    st.plotly_chart(fig6, use_container_width=True)
    st.write('''ANALYSIS -
             We can conclude that married people work more than unmarried people.''')

fig7 = px.bar(df, x="incwage", y="expendbase10", color="sex",  title=f'INCOME WAGE VS EXPENDITURE')
if st.sidebar.checkbox('Show income wage vs expenditure'):
    st.plotly_chart(fig7, use_container_width=True)
    st.write('''ANALYSIS -
             We can conclude that female expenses are higher than male expenses as per their incomes.''')

fig8 = px.histogram(df,x="o_occ1990",y="sex",title=f'OCCUPATION IN 1990')

fig9 = px.histogram(df,x='o_occ1950',y='sex',title=f'OCCUPATION IN 1950')

if st.sidebar.checkbox('Show difference in occupation'):
    st.plotly_chart(fig8, use_container_width=True)
    st.write('Working females in 1990 were approx 50M and working males in 1990 were approx 70M')

    st.plotly_chart(fig9, use_container_width=True)
    st.write('Working females in 1950 were approx 60M and working males were in 1950 approx 80M')
    st.write('''ANALYSIS -
             As we compare working strength of males and females we can conclude that by the given figures the numbers of workers reduced from an average of 70M to 60M in 1950 to 1990 respectively.''')

fig10 = px.violin(df,x='hrswork',y='incwage',facet_col='sex',title=f'INCOME WAGE VS HOURS WORKED')

fig11 = px.histogram(df,x='perconexp',y='expendbase10',facet_col='sex',title=f'PERSONAL CONSUMPTION EXPENDITURE')

if st.sidebar.checkbox('Show comparison between income wage and hours wage'):
    st.plotly_chart(fig10, use_container_width=True)
    st.write('''ANALYSIS -
             We can conclude that male workers income in subsequently more than female workers at the specific working hours.''')
    
if st.sidebar.checkbox('Show personal consumption expenditure'):
    st.plotly_chart(fig11, use_container_width=True)
    st.write('''ANALYSIS -
             We can concluse that personal consumption expenditure of males is more than females but there is a slightest difference between the two. ''')    

fig12 = px.area(x=df.index, y=df['incwage'], title=f'INCOME WAGE')
if st.sidebar.checkbox('Show income wage'):
    st.plotly_chart(fig12, use_container_width=True)
    st.write('')

fig13 = px.scatter( x=df.index, y=df['occ'], title=f'OCCUPATION')

fig14 = px.bar(x=df.index, y=df['ind'], title=f'INDUSTRY')

fig15= px.box(x=df.index, y=df['hrswork'], title=f'HOURS WORKED')

if st.sidebar.checkbox('Show occupation'):
    st.plotly_chart(fig13, use_container_width=True)
    st.write('')

if st.sidebar.checkbox('Show industry'):
    st.plotly_chart(fig14, use_container_width=True)
    st.write('')

if st.sidebar.checkbox('Show hours worked'):
    st.plotly_chart(fig15, use_container_width=True)
    st.write('')