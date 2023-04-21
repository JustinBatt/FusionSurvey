import streamlit as st
import xml.etree.ElementTree as ET

# Create XML file
root = ET.Element("Responses")

# Add questions to XML file
name = ET.SubElement(root, "Name")
name.text = "What is your name?"
feeling = ET.SubElement(root, "Feeling")
feeling.text = "How are you feeling today?"

# Create Streamlit app
st.title("Survey App")

# Loop through questions in XML file
for question in root:
    st.write(question.text)
    answer = st.text_input("Enter your answer:")
    question.set("Answer", answer)

# Save responses to XML file
tree = ET.ElementTree(root)
tree.write("responses.xml")
