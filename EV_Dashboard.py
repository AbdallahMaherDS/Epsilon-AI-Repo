# Importing Libraries 
import pandas as pd
import plotly.express as px
import streamlit as st
# Reading CSVs
df1=pd.read_csv('DataFrames/df1.csv')
df2=pd.read_csv('DataFrames/df2.csv')
df3=pd.read_csv('DataFrames/df3.csv')
df4=pd.read_csv('DataFrames/df4.csv')
df5=pd.read_csv('DataFrames/df5.csv')
df6=pd.read_csv('DataFrames/df6.csv')
df7=pd.read_csv('DataFrames/df7.csv')
df8=pd.read_csv('DataFrames/df8.csv')
df9=pd.read_csv('DataFrames/df9.csv')
df10=pd.read_csv('DataFrames/df10.csv')
df11=pd.read_csv('DataFrames/df11.csv')
df12=pd.read_csv('DataFrames/df12.csv')
df13=pd.read_csv('DataFrames/df13.csv')
df14=pd.read_csv('DataFrames/df14.csv')
df15=pd.read_csv('DataFrames/df15.csv')
df16=pd.read_csv('DataFrames/df16.csv')
df17=pd.read_csv('DataFrames/df17.csv')
df18=pd.read_csv('DataFrames/df18.csv')
df19=pd.read_csv('DataFrames/df19.csv')
df20=pd.read_csv('DataFrames/df20.csv')
df21=pd.read_csv('DataFrames/df21.csv')
# Data Visualization
# DF1 Visualization
fig1=px.funnel(data_frame=df1.sort_values('Value',ascending=False),x=df1['Value'],y=df1['Region'],width=1100,height=1100,color='Value')
fig1.update_layout(
    title="Number of Battery Electric Vehicles (BEV) Sold in each Region",
    xaxis_title="Number of EV",
    yaxis_title="Region",
)
# DF2 Visualization
fig2=px.funnel(data_frame=df2.sort_values('Value',ascending=True),x=df2['Value'],y=df2['Region'],width=1000,height=1000,color='Value')
fig2.update_layout(
    title="Number of Plug in Electric Vehicles (PHEV) Sold in each Region",
    xaxis_title="Number of PHEV",
    yaxis_title="Region",
)
# DF3 Visualization
fig3=px.funnel(data_frame=df3.sort_values('Value',ascending=False),x=df3['Value'],y=df3['Region'],width=1000,height=1000,color='Value')
fig3.update_layout(
    title="Number of Fuel Cell Electric Vehicles (FCEV) Sold in each Region",
    xaxis_title="Number of FCEV",
    yaxis_title="Region",
)
# DF4 Visualization
fig4=px.line(data_frame=df4,x=df4['Year'],y=df4['Value'],color_discrete_sequence=['yellow'])
fig4.update_layout(
    title="The rate of Increase in Battery Electric Vehicles (BEV) in The world",
    xaxis_title="Year",
    yaxis_title="Value",
)
# DF5 Visualization
fig5=px.line(data_frame=df5,x=df5['Year'],y=df5['Value'],color_discrete_sequence=['brown'])
fig5.update_layout(
    title="The rate of Increase in Plug in Hybrid Electric Vehicles (PHEV) in The world",
    xaxis_title="Year",
    yaxis_title="Value",
)
# DF6 Visualization
fig6=px.line(data_frame=df6,x=df6['Year'],y=df6['Value'],color_discrete_sequence=['violet'])
fig6.update_layout(
    title="The rate of Increase in Fuel Cell Electric Vehicles (FCEV) in The world",
    xaxis_title="Year",
    yaxis_title="Value",
)
# DF7 Visualization
fig7=px.pie(data_frame=df7,names='Powertrain',values='Value')
fig7.update_layout(title="The percentage of Sales of different types of EV all over the world")
# DF8 Visualization
fig8=px.histogram(data_frame=df8.sort_values('Value',ascending=False),x=df8['Value'],y=df8['Region'],width=800,height=800,color='Value',text_auto=True)
fig8.update_layout(
    title="Number of EV Fast Chargers in each Region",
    xaxis_title="Fast Chargers",
    yaxis_title="Region",
)
# DF9 Visualization
fig9=px.histogram(data_frame=df9.sort_values('Value',ascending=False),x=df9['Value'],y=df9['Region'],width=850,height=850,color='Value',text_auto=True)
fig9.update_layout(
    title="Number of EV Slow Chargers in each Region",
    xaxis_title="Slow Chargers",
    yaxis_title="Region",
)
# DF10 Visualization
fig10=px.line(data_frame=df10,x=df10['Year'],y=df10['Value'],color_discrete_sequence=['green'])
fig10.update_layout(
    title="The rate of Increase in EV Fast Chargers in The world",
    xaxis_title="Year",
    yaxis_title="Value",
)
# DF11 Visualization
fig11=px.line(data_frame=df11,x=df11['Year'],y=df11['Value'],color_discrete_sequence=['blue'])
fig11.update_layout(
    title="The rate of Increase in EV Slow Chargers in The world",
    xaxis_title="Year",
    yaxis_title="Value",
)
# DF12 Visualization
fig12=px.pie(data_frame=df12,names='Powertrain',values='Value',color_discrete_sequence=['skyblue'])
fig12.update_layout(title="The percentage of EV chargers Types installed in all over the world")
# DF13 Visualization
fig13=px.line(data_frame=df13,x=df13['Year'],y=df13['Value'],color_discrete_sequence=['orange'])
fig13.update_layout(
    title="The rate of Increase in EV Cars in The world",
    xaxis_title="Year",
    yaxis_title="Value",
)
# DF14 Visualization
fig14=px.line(data_frame=df14,x=df14['Year'],y=df14['Value'],color_discrete_sequence=['turquoise'])
fig14.update_layout(
    title="The rate of Increase in EV Buses in The world",
    xaxis_title="Year",
    yaxis_title="Value",
)
# DF15 Visualization
fig15=px.line(data_frame=df15,x=df15['Year'],y=df15['Value'],color_discrete_sequence=['pink'])
fig15.update_layout(
    title="The rate of Increase in EV Vans in The world",
    xaxis_title="Year",
    yaxis_title="Value",
)
# DF16 Visualization
fig16=px.line(data_frame=df16,x=df16['Year'],y=df16['Value'],color_discrete_sequence=['gray'])
fig16.update_layout(
    title="The rate of Increase in EV Trucks in The world",
    xaxis_title="Year",
    yaxis_title="Value",
)
# DF17 Visualization
fig17=px.line(data_frame=df17,x=df17['Year'],y=df17['Value'])
fig17.update_layout(
    title="The rate of Increase in Electricity demand in The world",
    xaxis_title="Year",
    yaxis_title="Value",
)
# DF18 Visualization
fig18=px.pie(data_frame=df18,names='Region',values='Value')
fig18.update_layout(title="The percentage of Electricity demand in different regions")
# DF19 Visualization
fig19=px.scatter(data_frame=df19,x=df19['Year'],y=df19['Value'],color_discrete_sequence=['red'])
fig19.update_layout(
    title="The rate of Increase in EV companies Stock shares in The world",
    xaxis_title="Year",
    yaxis_title="Value",
)
# DF20 Visualization
fig20=px.scatter(data_frame=df20,x=df20['Year'],y=df20['Value'],color_discrete_sequence=['black'])
fig20.update_layout(
    title="The rate of Increase in the Percentage of EV sales compared to total vehicle sales in The world",
    xaxis_title="Year",
    yaxis_title="Percent",
)
# DF21 Visualization
fig21=px.scatter(data_frame=df21,x=df21['Year'],y=df21['Value'],color_discrete_sequence=['coral'])
fig21.update_layout(
    title="The rate of Increase in the percentage of shares owned by individuals in EV companies compared to total shares owned by individuals in The world",
    xaxis_title="Year",
    yaxis_title="Percent",
)
st.set_page_config(layout='wide')
# sidebar title
sidebar_title = st.sidebar.title('Data analytics for Electric Vehicles and EV Chargers and EV Market')

# sidebar radio 
sidebar_radio = st.sidebar.radio('Categories' , ['Introduction' , 'EV Powertrain Sales in the world' , 'EV Chargers Spread in the world' , 'EV types Sales in the world' , 'Electricity demand in the world', 'EV World Market'])
if sidebar_radio == 'Introduction':
    st.header('Introduction to Electric Vehicle (EV) Data Analysis')
    # markdown
    st.markdown('As the world increasingly shifts towards sustainable transportation solutions, electric vehicles (EVs) have emerged as a pivotal component in reducing carbon emissions and promoting energy efficiency. The analysis of EV data is essential for understanding market trends, consumer behavior, and the overall impact of electric vehicles on the environment and economy.')
    st.markdown('This EV Data Analysis focuses on various dimensions of the electric vehicle market, including sales figures, vehicle types, charging infrastructure, and regional adoption rates. By examining these factors, we can gain insights into the growth trajectory of the EV market, identify challenges and opportunities, and inform stakeholders such as manufacturers, policymakers, and consumers.')
if sidebar_radio == 'EV Powertrain Sales in the world':
    st.subheader('EV Powertrain Sales in the world')
    tab1 , tab2 , tab3 = st.tabs(['EV Powertrain Sales in each Region','EV powertrain Sales From 2011 to 2023','EV Powertrain Percent'])
    with tab1:
            st.plotly_chart(fig1)
            st.plotly_chart(fig2)
            st.plotly_chart(fig3)
    with tab2:
            st.plotly_chart(fig4)
            st.plotly_chart(fig5)
            st.plotly_chart(fig6)
    with tab3:
            st.plotly_chart(fig7)
if sidebar_radio =='EV Chargers Spread in the world':
    st.subheader('EV Chargers Spread in the world')
    tab1 , tab2 , tab3 = st.tabs(['Fast Chargers','Slow Chargers','The percentage of Public EV Chargers types Installed'])
    with tab1:
            st.plotly_chart(fig8)
            st.plotly_chart(fig10)
    with tab2:
            st.plotly_chart(fig9)
            st.plotly_chart(fig11)
    with tab3:
            st.plotly_chart(fig12)
if sidebar_radio =='EV types Sales in the world':
    st.subheader('EV types Sales in the world')
    tab1 , tab2 , tab3 , tab4= st.tabs(['Electric Cars','Electric Buses','Electric Vans','Electric Trucks'])
    with tab1:
            st.plotly_chart(fig13)
    with tab2:
            st.plotly_chart(fig14)
    with tab3:
            st.plotly_chart(fig15)
    with tab4:
            st.plotly_chart(fig16)
if sidebar_radio =='Electricity demand in the world':
    st.subheader('Electricity demand in the world')
    st.plotly_chart(fig17)
    st.plotly_chart(fig18)
if sidebar_radio =='EV World Market':
    st.subheader('EV World Market')
    tab1 , tab2 = st.tabs(['EV companies Stock shares from 2010 to 2023','EV sales percentage compared to total vehicle sales from 2011 to 2023'])
    with tab1:
            st.plotly_chart(fig19)
            st.plotly_chart(fig21)
    with tab2:
            st.plotly_chart(fig20)
