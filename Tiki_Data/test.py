import ijson
'''
# read JSON file and parse contents
with open('/home/dunhan/PycharmProjects/Tiki_Crawling/tiki_data/tiki_products_12.json', 'r') as file:
    python_obj = json.load(file)
print(python_obj)
'''

with open('/home/dunhan/PycharmProjects/Tiki_Crawling/tiki_data/tiki_products_12.json', 'r') as file:
    for item in ijson.items(file, 'item'):
        print(item)  # Process each JSON item individually

