from bs4 import BeautifulSoup
import pickle

# Read the HTML file
with open('index.html') as file:
    html_content = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Locate the table element in the html.index file
table = soup.find('table')

# Initialize an empty dictionary
table_data = {}

# Extract the table headers - DAY and COLOURS
headers = [header.text.strip() for header in table.find_all('th')]

# Extract the table rows
rows = table.find_all('tr')[0:]  

# Using a For loop, iterate over the rows and extract the data
for row in rows:
    cells = row.find_all('td')
    day = cells[0].text.strip()
    colours = cells[1].text.strip().split(', ')
    table_data[day] = colours   #using day as key and colors as values in the dictionary

# Print the resulting dictionary
print(table_data)

# Specify the filename for the output file
output_filename = 'table_data.pkl'

# Export the dictionary to a file using pickle
with open(output_filename, 'wb') as file:
    pickle.dump(table_data, file)

print(f"Dictionary exported to {output_filename} successfully.")