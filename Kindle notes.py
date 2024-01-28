from bs4 import BeautifulSoup
import os

# Extract text from HTML file
with open('index.html', 'r') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')
text_content = soup.get_text()

# Write text content to 'output.txt'
with open('output.txt', 'w') as output_file:
    output_file.write(text_content)

# Read lines from 'output.txt', skip the first 10 lines, filter and remove blank lines
with open('output.txt', 'r') as file:
    lines = file.readlines()[10:]

filtered_lines = [line for line in lines if 'Highlight' not in line.strip()]

# Write filtered lines to 'output_file.txt'
with open('output_file.txt', 'w') as file:
    file.writelines(filtered_lines)

# Remove 'output.txt' file
os.remove("output.txt")

with open('index.html', 'w') as file:
    file.write('')
