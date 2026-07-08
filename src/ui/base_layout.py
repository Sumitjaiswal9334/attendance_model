import streamlit as st



def style_background_home():

    st.markdown("""
        <style>

                .stApp {
                    background: #5865F2 !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background-color:#E0E3FF !important;
                    padding:2.5rem !important;
                    border-radius: 5rem !important;
                    }
        </style>  

                """
            ,unsafe_allow_html=True)
    

def style_background_dashboard():

    st.markdown("""
        <style>

                .stApp {
                    background: #E0E3FF !important;
                }

        </style>  

                """
            ,unsafe_allow_html=True)
    

    

def style_base_layout():
# asdasd
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

                
         /* Hide Top Bar of streamlit */
                
            #MainMenu, footer, header {
                visibility: hidden;
            }
                
            .block-container {
                padding-top:1.5rem !important;    
            }

            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height:1.1 1important;
                margin-bottom:0rem !important;
            }
                

            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height:0.9 !important;
                margin-bottom:0rem !important;
            }
                
            h3, h4, p {
                font-family: 'Outfit', sans-serif;    
            }
                

           button{
    border-radius:1.5rem !important;
    background:linear-gradient(135deg,#4F46E5,#6366F1) !important;
    color:white !important;
    border:none !important;
    transition:all .3s ease !important;
}

button[kind="secondary"]{
    border-radius:1.5rem !important;
    background:linear-gradient(135deg,#F59E0B,#FACC15) !important;
    color:#1F2937 !important;
    border:none !important;
    transition:all .3s ease !important;
}

button[kind="tertiary"]{
    border-radius:1.5rem !important;
    background:#374151 !important;
    color:white !important;
    border:none !important;
    transition:all .3s ease !important;
}

button:hover{
    transform:translateY(-2px) scale(1.03);
    box-shadow:0 10px 25px rgba(79,70,229,.35);
}
        </style>  

                """
            ,unsafe_allow_html=True)