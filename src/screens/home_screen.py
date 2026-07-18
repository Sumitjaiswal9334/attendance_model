import streamlit as st
import base64
from pathlib import Path

from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home


def get_base64(image_name):
    image_path = Path(__file__).parent / image_name
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode()


def home_screen():

    header_home()
    style_background_home()
    style_base_layout()

    student_img = f"data:image/png;base64,{get_base64('student_side.png')}"
    teacher_img = f"data:image/png;base64,{get_base64('teacher_side.png')}"

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.header("I'm Student")

        st.markdown(f"""
        <div style="display:flex;justify-content:center;">
            <img src="{student_img}" width="120">
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "Student Portal",
            type="primary",
            icon=":material/arrow_outward:",
            icon_position="right",
            key="home_student_portal_btn",
            width="stretch",
        ):
            st.session_state["login_type"] = "student"
            st.rerun()

    with col2:
        st.header("I'm Teacher")

        st.markdown(f"""
        <div style="display:flex;justify-content:center;">
            <img src="{teacher_img}" width="120">
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "Teacher Portal",
            type="primary",
            icon=":material/arrow_outward:",
            icon_position="right",
            key="home_teacher_portal_btn",
            width="stretch",
        ):
            st.session_state["login_type"] = "teacher"
            st.rerun()

    footer_home()
