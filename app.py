import streamlit as st 
from functionality import * 
from intro import * 
from about import * 

st.title('Emotion Detection!')

selectbox = st.sidebar.selectbox(
    "Where do you want to go?",
    ("Introduction", "run_app>", "about")
)

if selectbox == 'Introduction': 
    run_intro()
elif selectbox == 'run_app>':
    run_app()
elif selectbox == 'about':
    show_about()

if app_mode == "Show instructions":
       run_intro()
        st.sidebar.success('To continue select "Run the app".')
    elif app_mode == "Source code":
        t1 = st.title("Code:")
        m1 = st.markdown(
            "## [github link](https://github.com/tanupunjani/Emotion-Detection)"
        )
        code1 = st.code(get_file_content_as_string("app.py"))
        title_1 = st.title("Functionality")
        code2 = st.code(get_file_content_as_string("functionality.py"))
    elif app_mode == 'Run the app':
        # st.balloons()
        run_the_app()

