import random
import duckdb
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title='Sales Dashboard', page_icon=':bar_chart', layout='wide')


st.title('Sales Dashboard')

with st.sidebar:
    st.header('Configurations')
    uploaded_file = st.file_uploader('Choose a file')
    
if uploaded_file is None:
    st.info('Upload a file through config')
    st.stop()
    
    
@st.cache_data
def load_data(path: str):
    df = pd.read_excel(path)
    return df

df = load_data(uploaded_file)
all_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

with st.expander('Data Preview'):
    st.dataframe(
        df,
        column_config={'Year': st.column_config.NumberColumn(format='%d')}
    )
    
def plot_metric(label, value, prefix='', suffix='', show_graph=False, color_graph='', text_color='', num_color=''):
    fig = go.Figure()
    
    fig.add_trace(
        go.Indicator(
            value = value,
            gauge={'axis': {'visible': False}},
            number={
                'prefix': prefix,
                'suffix': suffix,
                'font': {'size': 22, 'color': num_color},
            },
            title={
                'text': label,
                'font': {'size': 20,'color':text_color},
            }
        )
    )
    
    if show_graph:
        fig.add_trace(
            go.Scatter(
                y=random.sample(range(0, 101), 30),
                hoverinfo='skip',
                fill='tozeroy',
                fillcolor=color_graph,
                line={
                    'color': color_graph
                }
            )
        )
    fig.update_xaxes(visible=False, fixedrange=True)
    fig.update_yaxes(visible=False, fixedrange=True)
    fig.update_layout(
        margin = dict(t=30, b=0),
        showlegend=False,
        plot_bgcolor='white',
        height=200
    )
    
    st.plotly_chart(fig, use_container_width=True)

    
top_left_column, top_right_column = st.columns((2, 1))
with top_left_column:
    column1, column2 = st.columns(2)
    
    with column1:
        plot_metric(
            'Total Accounts Receivable ',
            6621280,
            prefix='$',
            suffix='',
            show_graph=True,
            color_graph='rgba(0, 104, 201, 0.2)',
            text_color='black',
            num_color='rgba(0, 104, 201, 0.6)'
        )
    
    with column2:
        plot_metric(
            'Total Accounts Payable ',
            1630270,
            prefix='$',
            suffix='',
            show_graph=True,
            color_graph='rgba(255, 0, 0, 0.2)',
            text_color='black',
            num_color='rgba(255, 0, 0, 0.6)'
        )

