import requests
import json
import os
from datetime import datetime, date
# from prettytable import PrettyTable
# from rich.pretty import pprint
# from rich.console import Console

# console = Console()

TRUEGRITS_LOCATION_ID = '61f9d7c8a9f13a15d7c1a25e'

date = str(date.today())
url = 'https://api.dineoncampus.com/v1/location/{}/periods?platform=0&date={}'.format(TRUEGRITS_LOCATION_ID, date)
print(url)
init_response = requests.get(url)
json_data = json.loads(init_response.text)

# pprint(json_data)

# horizontal line
print("-" * 50)

periods = ['65b67a48351d5307398fdba3', '65b67a48351d5307398fdb8e','65b67a48351d5307398fdb9f']

output = {}
for period in periods:
    url = 'https://api.dineoncampus.com/v1/location/{}/periods/{}?platform=0&date={}'.format(TRUEGRITS_LOCATION_ID, period, date)
    print(url)
    period_response = requests.get(url)
    json_data = json.loads(period_response.text)

    menu = json_data['menu']
    period_name = menu['periods']['name']
    print(period_name)
    output[period_name] = {}

    categories = menu['periods']['categories']

    for category in categories:
        output[period_name][category['name']] = []
        # print(category['name'])
        for item in category['items']:
            # print("\t", item['name'])
            output[period_name][category['name']].append(item['name'])


timestamp = datetime.now()
formatted_timestamp = timestamp.strftime("%m%d%Y_%H%M%S")
file = open('./menu/menu_{}.json'.format(formatted_timestamp), 'w')
file.write(json.dumps(output))
file.close()
# pprint(output)


