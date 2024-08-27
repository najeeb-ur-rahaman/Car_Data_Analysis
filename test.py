from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

# define URL link variable, get the response to parse the HTML  contents
url = "https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub"
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')

# declare table variable and use soup to find table in HTML
table = soup.find('table')

# iterate over table rows (tr) and append table data (td) to rows list
rows = []
for i, row in enumerate(table.find_all('tr')):
        rows.append([value.text.strip() for value in row.find_all('td')])

# Add the first row as columns and the remaining rows as rows
df = pd.DataFrame(rows[1:], columns=rows[0])

# cast the two coordinate columns to integer
df['x-coordinate'] = df['x-coordinate'].astype(int)
df['y-coordinate'] = df['y-coordinate'].astype(int)
#print(df)

# Initialize the maximum element of x-coordinate and y-coordinate to varibales
x_max = int(df['x-coordinate'].max())
y_max = int(df['y-coordinate'].max())

# Use the variables to create a matirx with spaces. 
# We are doing this because if any element is missing then it will be filled with spaces
output = [[' ' for _ in range(y_max + 1)] for _ in range(x_max + 1)]

#Iterate over the dataframe and insert the characters into the matrix at their respective positions
for _, row in df.iterrows():
    x = int(row['x-coordinate'])
    y = int(row['y-coordinate'])
    output[x][y] = row['Character']

# In-order to print the elements as a Uppercase Alphabet the matrix should be rotated by 90 degreees

rotated_output = np.rot90(output)

# Parse through the matrix and print the elemnts wihtout spaces
for row in rotated_output:
    for element in row:
        print(element, end="")
    print()


