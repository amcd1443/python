import requests
import lxml.html as lh
import pandas as pd
pd.set_option('display.max_rows', 150)


url = 'https://pokemondb.net/pokedex/all'

#create a handle page, to handle the contents of the website
page = requests.get(url)

#store the contents of the of the website under doc
doc = lh.fromstring(page.content)

#parse data that are stored between <tr>...</tr> of HTML
tr_elements = doc.xpath('//tr')


#Sanity check: check the length of the first 12 rows
[len(T) for T in tr_elements [:12]]


# Parse Table Header
tr_elements = doc.xpath('//tr')

#create empty list
col = []
i = 0

#for each row, store each first element (header) and an empty list
for t in tr_elements[0]:
	i += 1
	name = t.text_content()
	#print ' %d: "%s" ' % (i, name)
	col.append((name, [] ))

#Creating Pandas DataFrame
#Since out first row is the header, data is stored on the second row, and onwards
for j in range(1,len(tr_elements)):
	#T is our j'th row
	T = tr_elements[j]
	#If row is not of size 10, the //tr data is not from our table
	if len(T) != 10:
		break
	# 'i' is the index of our column
	i = 0
	#Iterate through each element of the row
	for t in T.iterchildren():
		data = t.text_content()
		#check if row is empty
		if i > 0:
		#convert any numerical value to integers 
			try:
				data = int(data)
			except:
				pass
		#append the data to the empty list of the i'th column
		col[i][1].append(data)
		#increment 'i' for the next column
		i += 1

# print [len(C) for (title,C) in col]


#Create the DataFrame
Dict = {
	title: column for (title,column) in col
}
df = pd.DataFrame(Dict)

print df.head(150)

#Questions and Problems to fix:
#1. why is it just 5 rows (fixed see line 4 & 70)...but why is 5 default?
#2. why are: Name, Total, HP, Attack, Defense, and Type; NOT in the correct order
#3. what is everything going on?
#4. why when i set head to head(36) do the names turn into elpisis?
#5. why at 100 does it skip rows 30-69? 
# L> is it a speed thing?








