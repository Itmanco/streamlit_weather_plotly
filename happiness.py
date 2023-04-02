import streamlit as st
import plotly.express as px
from datareader import get_happines_data


st.title("In search for Happines")
option1 = st.selectbox("Select the data for the X-axis", ("gdp", "freedom_to_make_life_choices", "corruption"))
option2 = st.selectbox("Select the data for the Y-axis", ("happiness", "social_support", "generosity"))
st.subheader(f"{option1} and {option2}")

d, t = get_happines_data(option1,option2)
figure = px.scatter(x=d, y=t, labels={"x": f"{option1}", "y": f"{option2} (C)"})
st.plotly_chart(figure)
