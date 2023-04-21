import xml.etree.ElementTree as ET

# Function to create and update the XML file
def update_xml(filename, tag, value):
    try:
        # Load the existing XML file if it exists
        tree = ET.parse(filename)
        root = tree.getroot()
    except FileNotFoundError:
        # If the file does not exist, create a new root element
        root = ET.Element("survey")

    # Create or update the tag with the given value
    elem = root.find(tag)
    if elem is None:
        elem = ET.SubElement(root, tag)
    elem.text = value

    # Write the updated XML back to the file
    tree = ET.ElementTree(root)
    tree.write(filename)

# Ask the user for their response to the first question
response1 = input("Hi, how are you doing? ")

# Store the response in the XML file
update_xml("survey.xml", "response1", response1)

# Ask the user for their response to the second question
response2 = input("What's new? ")

# Store the response in the XML file
update_xml("survey.xml", "response2", response2)
