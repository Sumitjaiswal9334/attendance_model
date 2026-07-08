import streamlit as st


def footer_home():
    logo_url = "https://www.image2url.com/r2/default/images/1783441882417-3282c0fb-443e-4d8b-923c-4f374f1f89e5.png"
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:4px; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:white;"> Created with ❤️ by </p>  
        <img src='{logo_url}' style='max-height:40px ; margin-left:-5px' />
        </div>
                
                """, unsafe_allow_html=True)


def footer_dashboard():
    logo_url = "https://www.image2url.com/r2/default/images/1783441882417-3282c0fb-443e-4d8b-923c-4f374f1f89e5.png"
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:4px; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:black;"> Created with ❤️ by </p>  
        <img src='{logo_url}' style='max-height:40px; margin-left:-5px;' />
        </div>
                
                """, unsafe_allow_html=True)
