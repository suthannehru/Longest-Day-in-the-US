import requests
from yaml import safe_load
import csv

with open("config.yml", 'r') as stream:
    api_values = safe_load(stream)

url = api_values["api_url"]

querystring = {"lat":"40.75","lon":"-73.98","date":"2024-03-16"}

headers = {
	"X-RapidAPI-Key": api_values["api_key"],
	"X-RapidAPI-Host": api_values["api_host"]
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()


with open('output.csv','w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(data['sun'].keys())
    writer.writerow(data['sun'][row] for row in data['sun'].keys())

