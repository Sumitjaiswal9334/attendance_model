import streamlit as st
import base64
from pathlib import Path


def get_base64(image_name):
    image_path = Path(__file__).parent / image_name
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode()


def header_home():

    logo_url = f"data:image/png;base64,{get_base64('attend_logo.png')}"

    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:20px; margin-top:30px">
            <img src='{logo_url}' style='height:200px; width:200px; display:block; margin-bottom:-30px;' />
            <h1 style="
                text-align: center;
                font-family: 'Poppins', sans-serif;
                font-size: 64px;
                font-weight: 800;
                line-height: 1.2;
                letter-spacing: 2px;
                margin: 0px;
            ">
                <span style="color:#FFFFFF;">ATTEND</span><br>
                <span style="color:#FACC15;">AI</span>
            </h1>
        </div>
    """, unsafe_allow_html=True)


def header_dashboard():

    logo_url = f"data:image/png;base64,{get_base64('attend_logo.png')}"

    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center;">
            <img src='{logo_url}' style='height:60px; margin-right:-4px;' />
            <div class="brand">
                <span style="color:#FFFFFF;font-size:42px;font-family:'Poppins',sans-serif;font-weight:800;">ATTEND</span>
                <span style="color:#FACC15;font-size:42px;font-family:'Poppins',sans-serif;font-weight:800;">AI</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
