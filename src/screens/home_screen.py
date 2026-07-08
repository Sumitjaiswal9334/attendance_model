import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home
def home_screen():


    header_home()
    style_background_home()
    style_base_layout()


    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.header("I'm Student")

        st.markdown("""
        <div style="display:flex;justify-content:center;">
            <img src="https://www.image2url.com/r2/default/images/1783455367872-a809cec1-3dbd-4742-8f6a-abcd3369e9ce.png" width="120">
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

        st.markdown("""
        <div style="display:flex;justify-content:center;">
            <img src="https://www.image2url.com/r2/default/images/1783455656536-01669d28-8760-4c7a-b4fa-4de0d1acd215.png" width="120">
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