Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
import csv
>>> with open('people.csv', newline='') as peopleCSV:
	reader1 = csv.reader(peopleCSV, delimiter=' ')
	for row in reader1:
		print(', '.join(row))

		
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    with open('people.csv', newline='') as peopleCSV:
FileNotFoundError: [Errno 2] No such file or directory: 'people.csv'
>>> ls
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    ls
NameError: name 'ls' is not defined
>>> peopleCSV = open('people.csv)
		 
SyntaxError: EOL while scanning string literal
>>> peopleCSV = open('people.csv')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    peopleCSV = open('people.csv')
FileNotFoundError: [Errno 2] No such file or directory: 'people.csv'
>>> peopleCSV = open('C:/Users/alex8/Desktop/python/people.csv')
>>> 
>>> reader1 = csv.reader(peopleCSV, delimiter=' ')
>>> for row in reader1:
	print(', '.join(row))

	
ï»¿Name,Title,City,State,Region
John,Dr,New, York,NY,
Sarah,Mrs,Denver,CO,
David,,Washington,,
William,Mr,,WI,
,None,None,None,
>>> import json
>>> state_to_region = open('C:/Users/alex8/Desktop/python/state_to_region.json')
>>> state_data =  json.load(state_to_region)
>>> print(state_data)
{'WA': 'West', 'OR': 'West', 'CA': 'West', 'ID': 'West', 'NV': 'West', 'MT': 'West', 'UT': 'West', 'AZ': 'West', 'NM': 'West', 'CO': 'West', 'WY': 'West', 'AK': 'West', 'HI': 'West', 'ND': 'Midwest', 'SD': 'Midwest', 'NE': 'Midwest', 'KS': 'Midwest', 'MN': 'Midwest', 'IA': 'Midwest', 'MO': 'Midwest', 'WI': 'Midwest', 'IL': 'Midwest', 'IN': 'Midwest', 'OH': 'Midwest', 'MI': 'Midwest', 'TX': 'South', 'OK': 'South', 'AR': 'South', 'LA': 'South', 'MS': 'South', 'AL': 'South', 'TN': 'South', 'KY': 'South', 'GA': 'South', 'FL': 'South', 'SC': 'South', 'NC': 'South', 'VA': 'South', 'WV': 'South', 'MD': 'South', 'DE': 'South', 'PA': 'Northeast', 'NY': 'Northeast', 'NJ': 'Northeast', 'CT': 'Northeast', 'MA': 'Northeast', 'VT': 'Northeast', 'NH': 'Northeast', 'RI': 'Northeast', 'ME': 'Northeast'}
>>> print(state_data['WA'])
West
>>> print(state_data[0])
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print(state_data[0])
KeyError: 0
>>> reader1[0]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    reader1[0]
TypeError: '_csv.reader' object is not subscriptable
>>> for t in reader1:
	print(', '.join(row[3]))

>>> 
>>> for t in reader1:
	print(', '.join(t[3]))

	
>>> t
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    t
NameError: name 't' is not defined
>>> for row in reader1:
	print(', '.join(row))

	
>>> print(state_data)
{'WA': 'West', 'OR': 'West', 'CA': 'West', 'ID': 'West', 'NV': 'West', 'MT': 'West', 'UT': 'West', 'AZ': 'West', 'NM': 'West', 'CO': 'West', 'WY': 'West', 'AK': 'West', 'HI': 'West', 'ND': 'Midwest', 'SD': 'Midwest', 'NE': 'Midwest', 'KS': 'Midwest', 'MN': 'Midwest', 'IA': 'Midwest', 'MO': 'Midwest', 'WI': 'Midwest', 'IL': 'Midwest', 'IN': 'Midwest', 'OH': 'Midwest', 'MI': 'Midwest', 'TX': 'South', 'OK': 'South', 'AR': 'South', 'LA': 'South', 'MS': 'South', 'AL': 'South', 'TN': 'South', 'KY': 'South', 'GA': 'South', 'FL': 'South', 'SC': 'South', 'NC': 'South', 'VA': 'South', 'WV': 'South', 'MD': 'South', 'DE': 'South', 'PA': 'Northeast', 'NY': 'Northeast', 'NJ': 'Northeast', 'CT': 'Northeast', 'MA': 'Northeast', 'VT': 'Northeast', 'NH': 'Northeast', 'RI': 'Northeast', 'ME': 'Northeast'}
>>> for row in reader1:
	print(', '.join(row))

	
>>> 
>>> print(reader1)
<_csv.reader object at 0x0000024FD76BAA58>
>>> reader2 = csv.reader(peopleCSV, delimiter=' ')
>>> for row in reader2:
	print(', '.join(row))

	
>>> 
>>> reader1.seek(0)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    reader1.seek(0)
AttributeError: '_csv.reader' object has no attribute 'seek'
>>> final_csv = list(reader1)
>>> final_csv
[]
>>> print(final_csv)
[]
>>> peopleCSV.seek(0)
0
>>> for row in reader1:
	print(', '.join(row))

	
ï»¿Name,Title,City,State,Region
John,Dr,New, York,NY,
Sarah,Mrs,Denver,CO,
David,,Washington,,
William,Mr,,WI,
,None,None,None,
>>> peopleCSV.seek(0)
0
>>> final_csv = list(reader1)
>>> print(final_csv)
[['ï»¿Name,Title,City,State,Region'], ['John,Dr,New', 'York,NY,'], ['Sarah,Mrs,Denver,CO,'], ['David,,Washington,,'], ['William,Mr,,WI,'], [',None,None,None,']]
>>> len(final_csv)
6
>>> for x in state_data:
	print(x[1])

	
A
R
A
D
V
T
T
Z
M
O
Y
K
I
D
D
E
S
N
A
O
I
L
N
H
I
X
K
R
A
S
L
N
Y
A
L
C
C
A
V
D
E
A
Y
J
T
A
T
H
I
E
>>> for x in range(len(final_csv)):
	print(final_csv[x][3])

	
Traceback (most recent call last):
  File "<pyshell#69>", line 2, in <module>
    print(final_csv[x][3])
IndexError: list index out of range
>>> 
>>> final_csv[0][2]
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    final_csv[0][2]
IndexError: list index out of range
>>> final_csv[0]
['ï»¿Name,Title,City,State,Region']
>>> final_csv[1]
['John,Dr,New', 'York,NY,']
>>> final_csv[1][1]
'York,NY,'
>>> x = 1
>>> for x in range(len(final_csv)):
	print(final_csv[x][1])

	
Traceback (most recent call last):
  File "<pyshell#78>", line 2, in <module>
    print(final_csv[x][1])
IndexError: list index out of range
>>> for x in range(1, len(final_csv)):
	print(final_csv[x][1])

	
York,NY,
Traceback (most recent call last):
  File "<pyshell#81>", line 2, in <module>
    print(final_csv[x][1])
IndexError: list index out of range
>>> final_csv[2]
['Sarah,Mrs,Denver,CO,']
>>> final_csv[3]
['David,,Washington,,']
>>> final_csv[4]
['William,Mr,,WI,']
>>> final_csv[5]
[',None,None,None,']
>>> peopleCSV.seek(0)
0
>>> for row in reader1:
	print(row)

	
['ï»¿Name,Title,City,State,Region']
['John,Dr,New', 'York,NY,']
['Sarah,Mrs,Denver,CO,']
['David,,Washington,,']
['William,Mr,,WI,']
[',None,None,None,']
>>> row[1][0]
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    row[1][0]
IndexError: list index out of range
>>> row[1]
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    row[1]
IndexError: list index out of range
>>> final_csv[1]
['John,Dr,New', 'York,NY,']
>>> final_csv[1][0]
'John,Dr,New'
>>> shape(final_csv)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    shape(final_csv)
NameError: name 'shape' is not defined
>>> len(final_csv[1])
2
>>> len(final_csv[2])
1
>>> found = 0
>>> found = -1
for x in range(len(final_csv)):
	for i in state_data:
		found = final_csv[x][len(final_csv[x]-1)].find(i[:1])
		
SyntaxError: multiple statements found while compiling a single statement
>>> found = -1
>>> region_list = []
>>> for i in state_data:
	print(i[1:])

	
A
R
A
D
V
T
T
Z
M
O
Y
K
I
D
D
E
S
N
A
O
I
L
N
H
I
X
K
R
A
S
L
N
Y
A
L
C
C
A
V
D
E
A
Y
J
T
A
T
H
I
E
>>> for i in state_data:
	print(i)

	
WA
OR
CA
ID
NV
MT
UT
AZ
NM
CO
WY
AK
HI
ND
SD
NE
KS
MN
IA
MO
WI
IL
IN
OH
MI
TX
OK
AR
LA
MS
AL
TN
KY
GA
FL
SC
NC
VA
WV
MD
DE
PA
NY
NJ
CT
MA
VT
NH
RI
ME
>>> for i in state_data[1]:
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    for i in state_data[1]:
KeyError: 1
>>> state_data
{'WA': 'West', 'OR': 'West', 'CA': 'West', 'ID': 'West', 'NV': 'West', 'MT': 'West', 'UT': 'West', 'AZ': 'West', 'NM': 'West', 'CO': 'West', 'WY': 'West', 'AK': 'West', 'HI': 'West', 'ND': 'Midwest', 'SD': 'Midwest', 'NE': 'Midwest', 'KS': 'Midwest', 'MN': 'Midwest', 'IA': 'Midwest', 'MO': 'Midwest', 'WI': 'Midwest', 'IL': 'Midwest', 'IN': 'Midwest', 'OH': 'Midwest', 'MI': 'Midwest', 'TX': 'South', 'OK': 'South', 'AR': 'South', 'LA': 'South', 'MS': 'South', 'AL': 'South', 'TN': 'South', 'KY': 'South', 'GA': 'South', 'FL': 'South', 'SC': 'South', 'NC': 'South', 'VA': 'South', 'WV': 'South', 'MD': 'South', 'DE': 'South', 'PA': 'Northeast', 'NY': 'Northeast', 'NJ': 'Northeast', 'CT': 'Northeast', 'MA': 'Northeast', 'VT': 'Northeast', 'NH': 'Northeast', 'RI': 'Northeast', 'ME': 'Northeast'}
>>> for i in state_data:
	print(state_data[i])

	
West
West
West
West
West
West
West
West
West
West
West
West
West
Midwest
Midwest
Midwest
Midwest
Midwest
Midwest
Midwest
Midwest
Midwest
Midwest
Midwest
Midwest
South
South
South
South
South
South
South
South
South
South
South
South
South
South
South
South
Northeast
Northeast
Northeast
Northeast
Northeast
Northeast
Northeast
Northeast
Northeast
>>> for x in range(len(final_csv)):
	for i in state_data:
		found = final_csv[x][len(final_csv[x]-1)].find(i)
		if found != -1:
			region_list.append(state_data[i])
			break

		
Traceback (most recent call last):
  File "<pyshell#124>", line 3, in <module>
    found = final_csv[x][len(final_csv[x]-1)].find(i)
TypeError: unsupported operand type(s) for -: 'list' and 'int'
>>> for x in range(len(final_csv)):
	for i in state_data:
		found = final_csv[x][len(final_csv[x])-1].find(i)
		if found != -1:
			region_list.append(state_data[i])
			break

		
>>> region_list
['Northeast', 'West', 'Midwest']
>>> peopleCSV[0]
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    peopleCSV[0]
TypeError: '_io.TextIOWrapper' object is not subscriptable
>>> test_csv = final_csv
>>> test_csv
[['ï»¿Name,Title,City,State,Region'], ['John,Dr,New', 'York,NY,'], ['Sarah,Mrs,Denver,CO,'], ['David,,Washington,,'], ['William,Mr,,WI,'], [',None,None,None,']]
>>> test_csv[1][len(test_csv[1])-1].append(region_list[0])
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    test_csv[1][len(test_csv[1])-1].append(region_list[0])
AttributeError: 'str' object has no attribute 'append'
>>> test_csv[1].append(region_list[0])
>>> test_csv[1]
['John,Dr,New', 'York,NY,', 'Northeast']
>>> for x in range(len(final_csv)):
	for i in state_data:
		found = final_csv[x][len(final_csv[x])-1].find(i)
		if found != -1:
			region_list.append(state_data[i])
			final_csv[x].append(state_data[i])
			break

		
>>> final_csv
[['ï»¿Name,Title,City,State,Region'], ['John,Dr,New', 'York,NY,', 'Northeast'], ['Sarah,Mrs,Denver,CO,', 'West'], ['David,,Washington,,'], ['William,Mr,,WI,', 'Midwest'], [',None,None,None,']]
>>> peopleCSV.seek(0)
0
>>> reader3 = csv.reader(peopleCSV, delimiter=',')
>>> final_csv2 = list(reader3)
>>> final_csv2
[['ï»¿Name', 'Title', 'City', 'State', 'Region'], ['John', 'Dr', 'New York', 'NY', ''], ['Sarah', 'Mrs', 'Denver', 'CO', ''], ['David', '', 'Washington', '', ''], ['William', 'Mr', '', 'WI', ''], ['', 'None', 'None', 'None', '']]
>>> for x in range(len(final_csv2)):
	for i in state_data:
		found = final_csv2[x][3].find(i)
		if found != -1:
			region_list.append(state_data[i])
			final_csv2[x][4] = state_data[i]
			break

		
>>> final_csv2
[['ï»¿Name', 'Title', 'City', 'State', 'Region'], ['John', 'Dr', 'New York', 'NY', 'Northeast'], ['Sarah', 'Mrs', 'Denver', 'CO', 'West'], ['David', '', 'Washington', '', ''], ['William', 'Mr', '', 'WI', 'Midwest'], ['', 'None', 'None', 'None', '']]
>>> writer1 = csv.writer(peopleCSV)
>>> writer1.writerows(final_csv2)
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    writer1.writerows(final_csv2)
io.UnsupportedOperation: not writable
>>> with open('C:/Users/alex8/Desktop/python/people.csv', 'wb') as peopleCSVwrite:
	writer1 = csv.writer(peopleCSVwrite)
	writer1.writerows(final_csv2)

	
Traceback (most recent call last):
  File "<pyshell#149>", line 3, in <module>
    writer1.writerows(final_csv2)
TypeError: a bytes-like object is required, not 'str'
>>> with open('C:/Users/alex8/Desktop/python/people.csv', 'w', newline="") as peopleCSVwrite:
	writer1 = csv.writer(peopleCSVwrite)
	writer1.writerows(final_csv2)

	
>>> 
