import streamlit as st


def header_home():

    logo_url = "https://www.image2url.com/r2/default/images/1783421673187-6e692f3c-ed9d-482b-ac99-8ad7369f8b5a.png"
    
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

    logo_url = "https://www.image2url.com/r2/default/images/1783421673187-6e692f3c-ed9d-482b-ac99-8ad7369f8b5a.png"
    
    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center;">
            <img src='{logo_url}' style='height:85px; margin-right:-4px;' />
            <div class="brand">
        <span style="color:#FFFFFF;font-size: 44px; font-family: 'Poppins', sans-serif;font-weight: 800;">ATTEND</span><span style="color:#FACC15;font-size: 44px; font-family: 'Poppins', sans-serif; font-weight: 800;">AI</span>
</div>
        </div>     
               """, unsafe_allow_html=True)