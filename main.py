import folium
import streamlit as st
from streamlit_folium import st_folium
from streamlit_player import st_player
from datetime import datetime
import pandas as pd
import time
import random

def main():
    # Title of the app
    st.set_page_config(
        page_title= "Port Management Video Feed",
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
    menu_choice = st.sidebar.radio("Zones", ("Aerial", "Cam List",))

    st.button(btn_face, on_click=ChangeTheme)
    st.write(datetime(2024, 4, 10, 10, 30))

    if menu_choice == "Aerial":
        show_aerial_page()
    elif menu_choice == "Zone":
        show_aerial_page()


def show_aerial_page():
    MAPPER = {
        "Aerial View": {"video": "https://www.youtube.com/embed/70_7sgajbZg"},
        "Jetty 8 View": {"video": "https://www.youtube.com/embed/iXklAkaUJSk"},
        "Jetty 7 View": {"video": "https://www.youtube.com/embed/Ngrz8Jt_jQA"},
        "Jetty 6 View": {"video": "https://www.youtube.com/embed/1Z-Fnu2k9T0"},
        "WareHouse 1": {"video": "https://www.youtube.com/embed/BbCJDMPOXdE"},
        "WareHouse 2": {"video": "https://www.youtube.com/embed/XSQa-hJJyYw"},
        
    }
    
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
    with col2:
        # All The Markers On map
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
            
        if st_data["last_object_clicked_tooltip"]:   
            st.session_state["VIDEO_URL"] = MAPPER[
                st_data["last_object_clicked_tooltip"]
            ]["video"]
            cook_breakfast()

def cook_breakfast():
    msg = st.toast("Connecting...")
    time.sleep(1)
    msg.toast("Fetching video...")
    time.sleep(1)
    msg.toast("Ready!", icon="🎉")

if __name__ == "__main__":
    main()
