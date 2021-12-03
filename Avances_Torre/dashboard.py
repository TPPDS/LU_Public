#======================================================================================
#======================================================================================
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pandas.api.types import CategoricalDtype
#======================================================================================
#======================================================================================
st.set_page_config(layout="wide")
hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html = True)
#======================================================================================
#======================================================================================
st.image("https://drive.google.com/drive/folders/1lVDygOAzeQSZyBpBvyhsnzpKXRPeQxyJ")
st.title("Avances Data Science - La Torre")
st.markdown("### **25/11 - 03/12**")
#======================================================================================
#======================================================================================
st.markdown("#### Insights")
st.markdown("###### Cuentas FB")
df = pd.DataFrame({"ID Cuenta":["act_10155844865285071","act_10155783000695071","act_1999023726787340","act_707332219645336"],"Nombre":["La Torre Express","La Torre","La Torre Express_TPP","SupermercadosLaTorre_TPP_BMGT_T2"]})
st.dataframe(df.tail(1))
#======================================================================================
#======================================================================================
st.sidebar.title("Explorar gráficas")
breakdown = st.sidebar.selectbox("Desglose", ["age", "gender","publisher_platform", "platform_position", "region"])
seleccion = st.sidebar.selectbox("Seleccionar", ["impressions","clicks","cpc","cpm","ctr","spend"])
#======================================================================================
#======================================================================================
def chart_3(week_df, x_data, y_data):
    week_df = week_df.sort_values(by=[y_data], ascending=False)
    fig = px.bar(week_df, x=x_data, y=y_data, color=y_data, hover_data=['date', y_data])
    return fig

#======================================================================================
#======================================================================================

sheet_url = "https://docs.google.com/spreadsheets/d/1pRZjn77HMTt446XgH-8p9y0faYO0NXA6k7GRD_CNeOI/edit#gid=550136453"
url_age_gender = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
sheet_url = "https://docs.google.com/spreadsheets/d/1ekcF85yOVxfgUzjvE_qOImAlnAs4DCyYOCLx2msy1c8/edit#gid=398951"
url_platform = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
sheet_url = "https://docs.google.com/spreadsheets/d/1b2hSL0BlhDYlmV7S7mcm9M03y1FIuk3yrwRxyeBGTFQ/edit#gid=1315078865"
url_position = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
sheet_url = "https://docs.google.com/spreadsheets/d/1lXGDmgFcK-m09N5VfgwMBcKJINluohE1aiVGnPFms90/edit#gid=851556317"
url_region = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
df_age_gender = pd.read_csv(url_age_gender, error_bad_lines=False)
df_platform = pd.read_csv(url_platform)
df_position = pd.read_csv(url_position)
df_region = pd.read_csv(url_platform)
#======================================================================================
#======================================================================================
if breakdown == "age" or breakdown == "gender":
    df_general = df_age_gender
elif breakdown == "publisher_platform":
    df_general = df_platform
elif breakdown == "region":
    df_general = df_region[df_region["country"]=="GT"]
else:
    df_general = df_position
#======================================================================================
#======================================================================================
st.title("Insights por mes")
#======================================================================================
df_general["date"] = pd.to_datetime(df_general["date"], errors='coerce')
cat_size_order = CategoricalDtype(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','Jul','Aug','Sep','Oct','Nov','Dec'], ordered=True)
month = df_general.groupby([df_general['date'].dt.strftime('%b'),breakdown]).mean().sort_values(by = "date")
month = month.reset_index()
month['date'] = month['date'].astype(cat_size_order)
month = month.sort_values("date")
month = month.replace({pd.NA: 0})
st.dataframe(month)
#======================================================================================
fig = px.bar(month, x="date", y=seleccion,
             color=breakdown, barmode='group')
st.plotly_chart(fig)
#======================================================================================
fig = px.scatter(month, x="date", y=seleccion, color=breakdown,
                 size=seleccion)
st.plotly_chart(fig)
#======================================================================================
st.plotly_chart(chart_3(month, breakdown,seleccion))
#======================================================================================
#======================================================================================
st.title("Insights por día de la semana")
week_df = df_general
week_df["date"] = pd.to_datetime(week_df["date"], errors='coerce')
#======================================================================================
week_df = week_df.groupby([week_df['date'].dt.day_name(), breakdown]).mean()
week_df = week_df.reset_index()
week_df = week_df.replace({pd.NA: 0})
st.dataframe(week_df)
fig = px.bar(week_df, x="date", y=seleccion,
             color=breakdown, barmode='group')
st.plotly_chart(fig)

fig = px.scatter(week_df, x="date", y=seleccion, color=breakdown,
                 size=seleccion)
st.plotly_chart(fig)


st.plotly_chart(chart_3(week_df, breakdown,seleccion))





#======================================================================================
#======================================================================================
#======================================================================================
def chart_2(df_rangos, y_data):
    fig = px.line(df_rangos, x='date', y=y_data, title='Time Series')
    fig.update_xaxes(rangeslider_visible=True, rangeselector=dict(buttons=list([dict(count=1, label="1m", step="month", stepmode="backward"), dict(count=6, label="6m", step="month", stepmode="backward"), dict(count=1, label="YTD", step="year", stepmode="todate"), dict(count=1, label="1y", step="year", stepmode="backward"), dict(step="all")])))
    return fig



def chart_time_series(df, n_chart):
    if n_chart == "spent":
        n_c = "spend"
    else:
        n_c = n_chart
    fig = go.Figure()
    fig.add_trace(go.Bar(
        name = n_c,
        x = df["date"], y = df[n_c],
        xperiod = "M1",
        xperiodalignment="end"))
    fig.update_layout(title_text = 'Time Series - ' + n_c, barmode = "stack")
    fig.update_traces(marker_color = 'rgb(255,0,0)')
    fig.update_xaxes(showgrid = True, ticklabelmode = "period", rangeslider_visible = True)
    return fig

st.title("Por todo el año")
df_df = df_general.groupby("date")[seleccion].sum()
st.plotly_chart(chart_2(df_general, seleccion))
st.plotly_chart(chart_time_series(df_general, seleccion))