import requests
import lxml.html as lh
import pandas as pd
from pandas.tools.plotting import scatter_matrix


pd.set_option('display.max_rows', 200)


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
	print ' {}: {} '.format(i, name)
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




def str_bracket(word):
	# Add brackets around the second term
	for_list = [x for x in word]
	for char_ind in range(1,len(for_list)):
		if for_list[char_ind].isupper():
			for_list[char_ind] = ' ' + for_list[char_ind]
	fin_list = ''.join(for_list).split(' ')
	length = len(fin_list)
	if length > 1: 
		fin_list.insert(1,'(' )
		fin_list.append( ')' )
	return ' '.join(fin_list)

def str_break(word):
	#breaks the string at upper case
	for_list = [ x for x in word]
	for char_ind in range(1, len(for_list)):
		if for_list[char_ind].isupper():
			for_list[char_ind] = ' ' + for_list[char_ind]
	fin_list = ''.join(for_list).split(' ')
	return fin_list
print "break"


df['Name'] = df["Name"].apply(str_bracket)
df['Type'] = df["Type"].apply(str_break)

def max_stats(df, col_list):
	#Get highest pokemon value of the column in the DataFrame
	max_message = ''
	for col in col_list:
		max_stat = df[col].max()
		name = df[df[col] == df[col].max()]['Name'].values[0]
		max_message += name + ' has the greatest ' + col + ' of ' + str(max_stat) + '.\n'
	return max_message

def min_stats(df, col_list):
	#get minimum value for each pokemon in the DataFrame
	min_message = ''
	for col in col_list:
		min_stat = df[col].min()
		name = df[df[col] == df[col].min()]['Name'].values[0]
		min_message += name + ' has the lowest ' + col + ' of ' + str(min_stat) + '.\n'
	return min_message

stats = ['Attack', 'Defense', 'HP', 'Sp. Atk', 'Sp. Def', 'Speed', 'Total']
print max_stats(df, stats)
print min_stats(df, stats)


#see line 4 for import
scatter_matrix(df[stats[:-1]], alpha = 0.2, figsize = (10,10), diagonal = 'kde')

#creating a new DataFrame where the Type values are separated
newDict = {}
stats_col = ['#', 'Name', 'Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
# collecting the list of Type for each Pokemon
Dict['Type'] = df['Type'].values
# creating an empty list for each key aka column
for col in stats_col:
	newDict[col] = []
	newDict['Type'] = []
# populating each of the dictionary value (aka empty list) with data
for row in range(len(Dict['#'])):
	for t in Dict['Type'][row]:
		for col in stats_col:
			# Append all columns except Type to the new Dictionary
			newDict[col].append(Dict[col][row])
			# append the Type separately for each pokemon in the dict
		newDict['Type'].append(t)

# conver dictionary to data Frame
new_df = pd.DataFrame(newDict)
print new_df.head(200)


#new_df['Name'] = new_df["Name"].apply(str_bracket)
#new_df['Type'] = new_df["Type"].apply(str_break)





#print df.head(150)

#Questions and Problems to fix:
#1. why is it just 5 rows (fixed see line 4 & 70)...but why is 5 default?
#2. why are: Name, Total, HP, Attack, Defense, and Type; NOT in the correct order
#3. what is everything going on?