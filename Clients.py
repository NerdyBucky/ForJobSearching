# set up libraries for Use
import numpy as np	
import pandas as pd
from pandas import *
import matplotlib.pyplot as plt


# import data

path = 'HireArt.csv'
df=pd.read_csv(path)


# Rename
df.columns=['Account_Manager','Client_Name','Date_M']
df=DataFrame(df)
#print(df)


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
	#print(str_b)
    # remind to remove the 'and', also ',' and ' ' as a split won't influence the item count 
	if 'and' and "Sons']" in str_b:
		#print(Client_No)
		#print(str_b,':',len(str_b)-2)
		Client_No.append(len(str_b)-2)
	elif "Sons']" not in str_b and 'and' in str_b:	
		#Client_No.append(str_b)	
		#print(str_b,':',len(str_b)-1)
		#print(len(str_b))
		Client_No.append(len(str_b)-1)
	elif 'and' not in str_b:
		# print(str_b,len(str_b))
		if len(str_b) == 2:
			new_str_b = len(str_b) - 1	
			Client_No.append(new_str_b)	
			print(str_b,':',new_str_b)	
		else:
			new_str_b = len(str_b)	
			print(str_b,':',new_str_b)			
			Client_No.append(new_str_b)	


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
#print(df)
#print(df.groupby('DATE').count())
print(df.groupby('DATE').sum()/df['Client_No'].sum())
Perc_res= df.groupby('DATE').sum()/df['Client_No'].sum()



# draw a result

labels = 'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'
sizes = Perc_res
explode=(0,0,0,0,0,0,0,0,0,0.1,0,0)
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
plt.axis('equal')
plt.title("Max Percentage of Client Contact", fontsize='large', fontweight='bold') 
plt.show()




#Per_Result=df.groupby("DATE").apply(lambda x:100 * x / float(x.sum()))
#print(Per_Result)


# Transform Date Pattern into Month_only

#df['DATE'] = [datetime.strftime(x,'%m') for x in df['DATE']]


#Count the highest Volumn and get its index 
#print(df['DATE']) #这里要加一个header 然后才能merge
#print(Series(df['DATE']).value_counts())
Max = Series(df['DATE']).value_counts().max()
Month = Series(df['DATE']).value_counts().idxmax()
		
# Print a result

#print("We had highest record numbers in Month",Month,'in total', 'the number is',Max,'.')


# get the result of highest clients number we had collected in each month in history:
	
	# 1 create a new DataFrame Join those 2 columns: Client_Data ; DATE
#df1=pd.DataFrame({})
#print(df_result=pd.concat(df['DATE'],DataFrame(Client_Data)),axis=1)

	# 2 do the categorize for this dataframe #