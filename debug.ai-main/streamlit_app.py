import streamlit as st
import time
from helper import *


menu_items = {
	'Get help': 'https://www.linkedin.com/in/oluwaseyi-gbadamosi-41015216b/',
	'Report a bug': 'https://www.linkedin.com/in/oluwaseyi-gbadamosi-41015216b/',
	'About': '''
	## My Custom App

	Some markdown to show in the About dialog.
	'''
}

st.set_page_config(page_title="debug", page_icon="./images/Favicon1.png", layout='centered',menu_items=menu_items)
st.set_option('deprecation.showfileUploaderEncoding', False)



# rule=pred()
def main():
    #loading the model
    model = load_model()
    # hiding the footer text
    hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    
    # header of the app
    image = Image.open('./images/DebugLogo.png')
    st.image(image,width=700)
    st.markdown("<h3 style='text-align: center; color: black;'>Debug: An AI Pest🪲Diagnostic App'</h3>",unsafe_allow_html=True)
    
    # creating tabs for navigation
    tab1, tab2, tab3 = st.tabs(["Home", "About", "Pesticides Education"])
    with tab1:
        file = st.file_uploader("Upload an image of a pest 😃", type=["jpg", "png"])
        if file is None:
            st.markdown("<h5 style='text-align: left; color: black;'>Please upload an image for processing ⏳</h3>",unsafe_allow_html=True)
        else:
            slot = st.empty()
            with st.spinner('Your image is being processed. ⏳⏳⏳⏳'):
                time.sleep(2)

            test_image = Image.open(file).convert('RGB')
            st.image(test_image, caption="Pest Image", width = 400)
            pred = predict_class( test_image, model)
            
            if pred == 0:
                markdown = read_markdown_file("./treatment/aphids.md")
                st.markdown(markdown, unsafe_allow_html=True)
                image = Image.open('./images/aphids/banzo.jpg')
                st.image(image, caption='Banzo',width = 400)
            
            elif pred  == 1:
                markdown = read_markdown_file("./treatment/armyworm.md")
                st.markdown(markdown, unsafe_allow_html=True)
                image = Image.open('./images/armyworm/perfek-315-ec.jpg')
                st.image(image, caption='Perfek-315-ec',width = 400)
            
            
            elif pred  == 2:
                markdown = read_markdown_file("./treatment/beetle.md")
                st.markdown(markdown, unsafe_allow_html=True)
                image = Image.open('./images/beetle/smash.jpg')
                st.image(image, caption='Smash',width = 400)
            
            
            elif pred  == 3:
                markdown = read_markdown_file("./treatment/bollworm.md")
                st.markdown(markdown, unsafe_allow_html=True)
                image = Image.open('./images/bollworm/auzar-25-ec.jpg')
                st.image(image, caption='Auzar-25-ec',width = 400)
            
            
            elif pred  == 4:
                markdown = read_markdown_file("./treatment/grasshopper.md")
                st.markdown(markdown, unsafe_allow_html=True)
                image = Image.open('./images/grasshopper/biostadt-malathion-57-ec.jpg')
                st.image(image, caption='Biostadt-malathion-57-ec',width = 400)
            
            
            elif pred  == 5:
                markdown = read_markdown_file("./treatment/mites.md")
                st.markdown(markdown, unsafe_allow_html=True)
                image = Image.open('./images/mites/bioclaim.jpg')
                st.image(image, caption='Bioclaim',width = 400)
            
            
            elif pred  == 6:
                markdown = read_markdown_file("./treatment/sawfly.md")
                st.markdown(markdown, unsafe_allow_html=True)
                image = Image.open('./images/sawfly/krush.jpg')
                st.image(image, caption='krush',width = 400)
            
            
            elif pred  == 7:
                markdown = read_markdown_file("./treatment/stem_borer.md")
                st.markdown(markdown, unsafe_allow_html=True)
                image = Image.open('./images/stem_borer/cartop.jpg')
                st.image(image, caption='Cartop',width = 400)
            
            
            elif pred  == 8:
                markdown = read_markdown_file("./treatment/thrips.md")
                st.markdown(markdown, unsafe_allow_html=True)
                image = Image.open('./images/thrips/Eagle-Thripan-Bio-Miticide.jpg')
                st.image(image, caption='Eagle-Thripan-Bio-Miticide',width = 400)
            
            
            elif pred  == 9:
                markdown = read_markdown_file("./treatment/whitefly.md")
                st.markdown(markdown, unsafe_allow_html=True)
                image = Image.open('./images/whitefly/reno.jpg')
                st.image(image, caption='Reno',width = 400)
            
            
            else:
                st.write("pest not found in database")
                st.markdown("<h3 style='text-align: center; color: black;'>Sorry Debug does not currently have this pest in database'</h3>",unsafe_allow_html=True)


        with tab2:
            markdown = read_markdown_file("./treatment/about.md")
            st.markdown(markdown, unsafe_allow_html=True)
            
        with tab3:
            markdown = read_markdown_file("./treatment/info.md")
            st.markdown(markdown, unsafe_allow_html=True)

if __name__=='__main__':
    main()
    