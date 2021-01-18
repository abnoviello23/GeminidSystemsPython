import csv
import json

peopleCSV = open('people.csv')
reader3 = csv.reader(peopleCSV, delimiter=',')
final_csv2 = list(reader3)
region_list = []
found = -1
state_to_region = open('state_to_region.json')
state_data =  json.load(state_to_region)

for x in range(len(final_csv2)):
	for i in state_data:
		found = final_csv2[x][3].find(i)
		if found != -1:
			region_list.append(state_data[i])
			final_csv2[x][4] = state_data[i]
			break


