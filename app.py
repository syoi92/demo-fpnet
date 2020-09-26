import numpy as np
import streamlit as st
import os, urllib, cv2


def main():
    st.title("FPNet Demo: The Analysis of Complicated Drawings")
    readme_instruction = st.markdown(get_file_content_as_string("src/instruction.md"), unsafe_allow_html=True)

    st.sidebar.title("Contents")
    app_mode = st.sidebar.selectbox("Choose the app mode",
        ["Instructions", "Run the app (EAIS-fp)", "Run the app (SNU-fp)"])
    if app_mode == "Instruction":
        st.sidebar.success('To continue select "Run the app".')
    elif app_mode == "Run the app (EAIS-fp)":
        readme_instruction.empty()
        run_the_app()
    elif app_mode == "Run the app (SNU-fp)":
        readme_instruction.empty()
        st.markdown("## * Plan to be updated soon...*")




def run_the_app():
    st.sidebar.markdown("### Samples")
    sample_index = st.sidebar.slider("choose a sample index (floorplan testset)", 1, 6, 2, 1)

    image_url = os.path.join(DATA_URL_ROOT, "src/imgs/", str(sample_index) + ".png")

    # parameters
    confidence_threshold, IP_threshold = object_detector_ui()



    return


def object_detector_ui():
    st.sidebar.markdown("### Model parameters")
    st.sidebar.markdown("*DeepLearning*")
    confidence_threshold = st.sidebar.slider("Confidence treshold for the junction candidates", -1.0, 1.0, 0.0, 0.01)
    st.sidebar.markdown("*Integer Programming*")
    IP_threshold = st.sidebar.slider("Ratio of the style to the structure errors in the objective function", 0.0, 20.0, 10.0, 0.5)
    return confidence_threshold, IP_threshold


@st.cache(show_spinner=False)
def get_file_content_as_string(path):
    url = DATA_URL_ROOT + path
    response = urllib.request.urlopen(url)
    return response.read().decode("utf-8")

# path = 'src/imgs/fig1.samples.TIF'
@st.cache(show_spinner=False)
def get_file_content_as_img(path):
    url = DATA_URL_ROOT + path
    response = urllib.request.urlopen(url)

    img = cv.imdecode(response.read(), cv.IMREAD_COLOR)
    return response.read().decode("utf-8")

@st.cache(show_spinner=False)
def load_image(url):
    with urllib.request.urlopen(url) as response:
       image = np.asarray(bytearray(response.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    image = image[:, :, [2, 1, 0]] # BGR -> RGB
    return image

DATA_URL_ROOT = "https://raw.githubusercontent.com/syoi92/demo-fpnet/master/"

if __name__ == "__main__":
    main()



#     readme_text = st.markdown("This *FPNet demo* is able to reconstruct walls \
#                 in areas with overlapping graphics or nonuniform patterns, \
#                 thus allowing the room structures to be recovered even from complicated drawings.")

# #    st.markdown("![aa](https://raw.githubusercontent.com/syoi92/demo-fpnet/master/src/imgs/fig1.samples.TIF){:height=\"36px\" width=\"36px\"}.")
#     fig1 = cv2.imread("src/imgs/fig1.samples.tif", cv2.IMREAD_COLOR)
#     readme_img = st.image(fig1, caption='Fig. (a) input floor plan images and \
#         our results of (b) the style-transferred plans and (c) the vectorized floor plans',
#                        use_column_width=True, channels='BGR')