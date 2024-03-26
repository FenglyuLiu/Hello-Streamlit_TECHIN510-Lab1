import streamlit as st

col1, col2= st.columns(2)

with col1:
    st.header('Hello, I am :orange[Felicity] :sunglasses:')
    st.subheader('a UX Researcher with a background in HCI and UX Design.')
    st.subheader('My passion lies in merging design thinking and research insights to craft meaningful and impactful solutions.')
  

    st.subheader('🐯 About Me')
    st.markdown('''
    - School: University of Washington
    - Major: Science in Technology Innovation
    - Minor: Human Computer Interaction
    - Email: liufl22@uw.edu
    '''
    )
    

    st.subheader('🦒 Skills')
    st.markdown('''
    - Research: usability test, interview, survey, field study, heuristic evaluation
    - Design: wireframe, prototyping, user flow, persona
    - Data: SPSS, SQL, python
    '''
    )


with col2:
    image_path = 'pictures/Felicity.png'
    st.image(image_path, caption='Summer in Yunnan, China', width=300)

    image_path2 = 'pictures/Spring in Tsinghua.png'
    st.image(image_path2, caption='Spring in Tsinghua, China', width=300)