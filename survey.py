import xml.etree.ElementTree as ET
import tkinter as tk

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

# Create the GUI
root = tk.Tk()
root.title("Survey")

# Function to handle the submission of the form
def submit_form():
    # Get the values from the form
    response1 = entry1.get()
    response2 = entry2.get()

    # Store the responses in the XML file
    update_xml("survey.xml", "response1", response1)
    update_xml("survey.xml", "response2", response2)

    # Clear the form
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)

    # Show a message indicating that the form was submitted
    tk.messagebox.showinfo("Survey", "Thank you for your response!")

# Add the form elements
label1 = tk.Label(root, text="Hi, how are you doing?")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="What's new?")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

button = tk.Button(root, text="Submit", command=submit_form)
button.pack()

# Run the GUI
root.mainloop()
