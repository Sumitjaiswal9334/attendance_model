import streamlit as st
import base64
from pathlib import Path


def get_base64(image_name):
    image_path = Path(__file__).parent / image_name
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode()


def footer_home():
    logo_url = f"data:image/png;base64,{get_base64('name_banner.png')}"

    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:4px; justify-content:center; align-items:center;">
            <p style="font-weight:bold; color:white;">Created with ❤️ by</p>
            <img src="{logo_url}" style="max-height:40px; margin-left:-5px;" />
        </div>
    """, unsafe_allow_html=True)


def footer_dashboard():
    logo_url = f"data:image/png;base64,{get_base64('name_banner.png')}"

    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:4px; justify-content:center; align-items:center;">
            <p style="font-weight:bold; color:black;">Created with ❤️ by</p>
            <img src="{logo_url}" style="max-height:40px; margin-left:-5px;" />
        </div>
    """, unsafe_allow_html=True)
