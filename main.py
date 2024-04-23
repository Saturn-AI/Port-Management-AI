import folium
import streamlit as st
from streamlit_folium import st_folium
from streamlit_player import st_player
from datetime import datetime
import pandas as pd
import time
import random

def cook_breakfast():
    msg = st.toast("Gathering informations...")
    time.sleep(1)
    msg.toast("Fetching...")
    time.sleep(1)
    msg.toast("Ready!", icon="🎉")


def generate_number_plate():
    # Define the format of the number plate
    letters = [chr(i) for i in range(65, 91)]  # A-Z
    digits = [str(i) for i in range(10)]  # 0-9

    # Generate the number plate
    number_plate = ""
    for _ in range(3):
        number_plate += random.choice(letters)
    number_plate += "-"
    for _ in range(4):
        number_plate += random.choice(digits)

    return number_plate


def yield_data():
    sample = ["PAID", "UNPAID"]
    i = 1
    for l in list(range(0, 500, 1)):
        yield pd.DataFrame(
            {
                "Number Plate": [generate_number_plate()],
                "Payment Status": [random.choice(sample)],
            },
            index=[f"{i}"],
        )
        i += 1
        time.sleep(3)


# def simulate_vehicles():
#     bus, truck, car = 0, 0, 0
#     bus2, truck2, car2 = 0, 0, 0
#     congestion = [False, True]
#     for _ in list(range(0, 500, 1)):
#         yield pd.DataFrame(
#             {
#                 "Incoming": {
#                     "Bus": bus,
#                     "Truck": truck,
#                     "Car": car,
#                     "Congestion": random.choice(congestion),
#                 },
#                 "Outgoing": {
#                     "Bus": bus2,
#                     "Truck": truck2,
#                     "Car": car2,
#                     "Congestion": random.choice(congestion),
#                 },
#             }
#         )
#         bus += random.choice([0, 1, 2])
#         truck += random.choice([0, 1, 2])
#         car += random.choice([1, 2, 3])
#         bus2 += random.choice([0, 1, 2])
#         truck2 += random.choice([0, 1, 2])
#         car2 += random.choice([1, 2, 3])
#         time.sleep(2)


def main():
    # Title of the app
    # st.title("Port Management Video Feed")
    st.set_page_config(
        page_title="Port Management Video Feed",
        layout="wide",
        page_icon="🧊",
        initial_sidebar_state="auto",
    )
    ms = st.session_state

    if "themes" not in ms:
        ms.themes = {
            "current_theme": "light",
            "refreshed": True,
            "light": {
                # "theme.base": "dark",
                "theme.backgroundColor": "#f0f0f5",
                "theme.primaryColor": "#6eb52f",
                "theme.secondaryBackgroundColor": "#e0e0ef",
                "theme.textColor": "#262730",
                "theme.font": "sans serif",
                "button_face": "🌜",
            },
            "dark": {
                # "theme.base": "light",
                "theme.backgroundColor": "#002b36",
                "theme.primaryColor": "#d33682",
                "theme.secondaryBackgroundColor": "#586e75",
                "theme.textColor": "#fafafa",
                "theme.font": "sans serif",
                "button_face": "🌞",
            },
        }

    def ChangeTheme():
        previous_theme = ms.themes["current_theme"]
        tdict = (
            ms.themes["light"]
            if ms.themes["current_theme"] == "light"
            else ms.themes["dark"]
        )
        for vkey, vval in tdict.items():
            if vkey.startswith("theme"):
                st._config.set_option(vkey, vval)

        ms.themes["refreshed"] = False
        if previous_theme == "dark":
            ms.themes["current_theme"] = "light"
        elif previous_theme == "light":
            ms.themes["current_theme"] = "dark"

    btn_face = (
        ms.themes["light"]["button_face"]
        if ms.themes["current_theme"] == "light"
        else ms.themes["dark"]["button_face"]
    )

    if ms.themes["refreshed"] == False:
        ms.themes["refreshed"] = True
        st.rerun()

    #st._config.set_option("layout", "wide")

    # Sidebar menu
    st.sidebar.image("logo.png", caption="Graaho Technologies", width=150)
    st.sidebar.title("Port Video Feed")
    menu_choice = st.sidebar.radio("Zones", ("Aerial", "Zones",))

    st.button(btn_face, on_click=ChangeTheme)
    st.write(datetime(2024, 4, 10, 10, 30))

    if menu_choice == "Aerial":
        show_aerial_page()
    elif menu_choice == "Zone":
        show_aerial_page()

def show_aerial_page():
    MAPPER = {
        "Mongla Aerial ": {"video": "https://www.youtube.com/embed/70_7sgajbZg"},
    }
    # st_player("https://www.youtube.com/embed/70_7sgajbZg")
    

    col1, col2 = st.columns([2, 1])

    with col1:
        with st.container(height=450):
            if "VIDEO_URL" in st.session_state:
                playlist_id = st.session_state["VIDEO_URL"].split("/")[-1]
                url_style = """
                    <style>
                    .iframe-container {
                        overflow: hidden;
                        width: 100%;
                        height: 430px;
                    }
                    .iframe-container iframe {
                        position: absolute;
                        top: 0;
                        left: 0;
                        width: 100%;
                        height: 430px;
                        padding-bottom: 5px;
                    }
                    </style>
                    """
                url = f"""
                    <div class="iframe-container">
                        <iframe src="{st.session_state["VIDEO_URL"]}?rel=0&amp;&amp;controls=0&amp;showinfo=0&amp;loop=1&autoplay=1&mute=1&playlist={playlist_id}" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
                    </div>
                    """
                url = url_style + url
                st.write(
                    str(url),
                    unsafe_allow_html=True,
                )
            else:
                st.session_state["VIDEO_URL"] = list(MAPPER.values())[0]["video"]
        

        # with st.container(height=270):
        #     m = folium.Map(
        #         location=[22.4905296250758, 89.59160985318405], zoom_start=16
        #     )
        #     folium.Marker(
        #         [22.4905296250758, 89.59160985318405], popup="Mongla Aerial 1"
        #     ).add_to(m)
        #     # folium.Marker(
        #     #     [23.836842165760064, 90.47714944282039], popup="Toll Plaza B"
        #     # ).add_to(m)

        #     st_data = st_folium(m, width=1050, height=240)
            
            
    with col2:
        with st.container(height=550):
            m = folium.Map(
                location=[22.4904881836411, 89.59180332769601], zoom_start=16.5
            )
            folium.Marker(
                [22.4904881836411, 89.59180332769601], popup="Aerial View", tooltip="Aerial View"
            ).add_to(m)
            folium.Marker(
                [22.491882669402884, 89.590738638717], popup="Jetty 8 View", tooltip="Jetty 8 View"
            ).add_to(m)
            folium.Marker(
                [22.49032603322455, 89.5909433865976], popup="Jetty 7 View", tooltip="Jetty 7 View"
            ).add_to(m)
            folium.Marker(
                [22.48876094551518, 89.59111541374799], popup="Jetty 6 View", tooltip="Jetty 6 View"
            ).add_to(m)
            folium.Marker(
                [22.4904745061418, 89.5926692724233], popup="WareHouse 1", tooltip="WareHouse 1"
            ).add_to(m)
            folium.Marker(
                [22.489058669926866, 89.59297001926369], popup="WareHouse 2", tooltip="WareHouse 2"
            ).add_to(m)
            st_data = st_folium(m, width=400, height=500)

    # with col2:
    #     with st.container(height=735):
    #         if st_data["last_object_clicked_popup"]:
    #             st.session_state["VIDEO_URL"] = MAPPER[
    #                 st_data["last_object_clicked_popup"]
    #             ]["video"]
    #             cook_breakfast()
    #             message = st.chat_message("assistant")
    #             message.write(
    #                 f"Real Time Stream for {st_data['last_object_clicked_popup']}"
    #             )
    #             message.write_stream(yield_data)
    #         else:
    #             message = st.chat_message("assistant")
    #             message.write(f"Real Time Stream for {list(MAPPER.keys())[0]}")
    #             message.write_stream(yield_data)


# def show_zone1_page():
#     MAPPER = {
#         "Aerial": {"video": "https://www.youtube.com/embed/70_7sgajbZg"},
#         "Toll Plaza B": {"video": "https://www.youtube.com/embed/aTJVDGKHAHU"},
#     }

#     col1, col2 = st.columns([3, 1])

#     with col1:
#         with st.container(height=450):
#             if "VIDEO_URL" in st.session_state:
#                 playlist_id = st.session_state["VIDEO_URL"].split("/")[-1]
#                 url_style = """
#                     <style>
#                     .iframe-container {
#                         overflow: hidden;
#                         width: 100%;
#                         height: 430px;
#                     }
#                     .iframe-container iframe {
#                         position: absolute;
#                         top: 0;
#                         left: 0;
#                         width: 100%;
#                         height: 430px;
#                         padding-bottom: 10px;
#                     }
#                     </style>
#                     """
#                 url = f"""
#                     <div class="iframe-container">
#                         <iframe src="{st.session_state["VIDEO_URL"]}?rel=0&amp;&amp;controls=0&amp;showinfo=0&amp;loop=1&autoplay=1&mute=1&playlist={playlist_id}" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
#                     </div>
#                     """
#                 url = url_style + url
#                 st.write(
#                     str(url),
#                     unsafe_allow_html=True,
#                 )
#             else:
#                 st.session_state["VIDEO_URL"] = list(MAPPER.values())[0]["video"]

#         with st.container(height=270):
#             m = folium.Map(
#                 location=[23.828725716729313, 90.44034752339583], zoom_start=13
#             )
#             folium.Marker(
#                 [23.828725716729313, 90.44034752339583], popup="Toll Plaza A"
#             ).add_to(m)
#             folium.Marker(
#                 [23.836842165760064, 90.47714944282039], popup="Toll Plaza B"
#             ).add_to(m)

#             st_data = st_folium(m, width=1050, height=240)

#     with col2:
#         with st.container(height=735):
#             if st_data["last_object_clicked_popup"]:
#                 st.session_state["VIDEO_URL"] = MAPPER[
#                     st_data["last_object_clicked_popup"]
#                 ]["video"]
#                 cook_breakfast()
#                 message = st.chat_message("assistant")
#                 message.write(
#                     f"Real Time Stream for {st_data['last_object_clicked_popup']}"
#                 )
#                 message.write_stream(simulate_vehicles)
#             else:
#                 message = st.chat_message("assistant")
#                 message.write(f"Real Time Stream for {list(MAPPER.keys())[0]}")
#                 message.write_stream(simulate_vehicles)


if __name__ == "__main__":
    main()
