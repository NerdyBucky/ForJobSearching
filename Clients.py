# ForJobSearching

# ZhenZhang


# For Python Version 

# <1> Import Libraries for Use
import numpy as np	
import pandas as pd
from pandas import *
import matplotlib.pyplot as plt


# <2> Import Data File
path = 'HireArt.csv'
df=pd.read_csv(path)
  # Rename
df.columns=['Account_Manager','Client_Name','Date_M']
df=DataFrame(df)
#print(df)

# <3> Process Data

   # change date type to Month only
df['DATE']=pd.to_datetime(df['Date_M'])


   # count clients no
   # 1 turn the column of client_name from a dataframe into a Array
Client_Array = np.array(pd.read_csv(path,usecols=[1]))
   # 2 turn array into list
Client_List = Client_Array.tolist()
   # 3 count how many clients in each row 
Client_No = []

for a in Client_List:
	str_a = str(a)
	str_b = str_a.split(' ')

   # remind to remove the 'and', also ',' and ' ' as a split won't influence the item count 
	if 'and' and "Sons']" in str_b:
		Client_No.append(len(str_b)-2)
	elif "Sons']" not in str_b and 'and' in str_b:	
		Client_No.append(len(str_b)-1)
	elif 'and' not in str_b:
		if len(str_b) == 2:
			new_str_b = len(str_b) - 1	
			Client_No.append(new_str_b)	
			print(str_b,':',new_str_b)	
		else:
			new_str_b = len(str_b)	
			print(str_b,':',new_str_b)			
			Client_No.append(new_str_b)	

# Deal with Months 
Index=[]
for i in range(len(Client_No)):
	Index.append(i)
#print(Index)

# Transform Date Pattern into Month_only
df['DATE'] = [datetime.strftime(x,'%m') for x in df['DATE']]
DATE = []
for i in df['DATE']:
	DATE.append(i)
#print(DATE)
	
# merge a new dataframe
RESULT={'DATE':DATE,'Client_No':Client_No}
df=DataFrame(RESULT)

# print(df.groupby('DATE').count()) // this is the number of  Contacts
# print(df.groupby('DATE').sum()) // this is a groupby of Sum of Clients 

# Result
Perc_res= df.groupby('DATE').sum()/df['Client_No'].sum()

# Visualization 

labels = 'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'
sizes = Perc_res
explode=(0,0,0,0,0,0,0,0,0,0.1,0,0)
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
plt.axis('equal')
plt.title("Max Percentage of Client Contact", fontsize='large', fontweight='bold') 
plt.show()


