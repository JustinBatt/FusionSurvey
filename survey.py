import streamlit as st
import xml.etree.ElementTree as ET
from github import Github

# Define the survey questions as a dictionary
survey_questions = {
    "name": "What is your name?",
    "mood": "How are you feeling today?",
    "feedback": "Do you have any feedback for us?"
}

# Define a function to save the responses to an XML document in a GitHub path
def save_responses(responses):
    # Initialize the GitHub repository
    g = Github("YOUR_GITHUB_ACCESS_TOKEN")
    repo = g.get_repo("JustinBatt/FusionSurvey")
    # Create the XML tree
    root = ET.Element("survey_responses")
    for key, value in responses.items():
        ET.SubElement(root, key).text = value
    tree = ET.ElementTree(root)
    # Write the XML file to the GitHub path
    contents = ET.tostring(root, encoding="unicode", method="xml")
    repo.create_file("survey_responses.xml", "Committing survey responses", contents)

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
