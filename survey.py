import streamlit as st
import xml.etree.ElementTree as ET

# Define the survey questions as a dictionary
survey_questions = {
    "name": "What is your name?",
    "mood": "How are you feeling today?",
    "feedback": "Do you have any feedback for us?"
}

# Define a function to save the responses to an XML document
def save_responses(responses):
    root = ET.Element("survey_responses")
    for key, value in responses.items():
        ET.SubElement(root, key).text = value
    tree = ET.ElementTree(root)
    tree.write("JustinBatt/FusionSurvey/survey_responses.xml")

# Create a Streamlit app that displays the survey questions and saves responses
def main():
    st.title("Survey")
    responses = {}
    for key, value in survey_questions.items():
        responses[key] = st.text_input(value)
    if st.button("Submit"):
        save_responses(responses)
        st.success("Responses saved!")

if __name__ == "__main__":
    main()
