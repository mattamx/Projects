
```
import pandas as pd
import requests  # Library for sending requests to the server
from bs4 import BeautifulSoup # Library for webpage parsing

URL = 'https://practicum-content.s3.us-west-1.amazonaws.com/data-analyst-eng/moved_chicago_weather_2017.html'
req = requests.get(URL)
#print(req.text)

soup = BeautifulSoup(req.text, 'lxml') # Creating the tree structure and adding the parser

table = soup.find("table",attrs={"id": "weather_records"}) 
#print(table)

heading_table = [] # Storing the names of columns
for row in table.find_all('th'):  # <th> elements = names of columns
    heading_table.append(row.text)  # Appending to empty list above
#print(heading_table)

content = []  # Storing the content from the table
for row in table.find_all('tr'): # <tr> tag = row of content
    if not row.find_all('th'): # Ignoring the first row of the table, 'headings'
        content.append([element.text for element in row.find_all('td')])
        # Content is wrapped in <td> </td> tags, looping through all <td> elements and extracting values # Appending to empty list above
#print(content)

weather_records = pd.DataFrame(content, columns=heading_table)
print(weather_records)
```
