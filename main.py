import streamlit as st
import plotly.express as px
from backend import get_data

#Add title, text input, slider, selectbox, and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select data to view")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")


if place:
    #Get the temperature / sky data
    try:
        data = get_data(place, days)
        dates = [dict["dt_txt"] for dict in data]
        if option == "Temperature":
            temperatures = [dict["main"]["temp"]/10 for dict in data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)
        elif option == "Sky":
            sky_conditions = [dict["weather"][0]["main"] for dict in data]
            images = {"Clear": "static/clear.png", "Clouds": "static/cloud.png",
                      "Rain": "static/rain.png", "Snow": "static/snow.png"}
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=115, caption=dates)
    except KeyError:
        st.write("That place does not exist.")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')

