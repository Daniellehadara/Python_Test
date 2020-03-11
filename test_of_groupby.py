#the following script should help with the calculation of  missing data on RedCap
#calculating the existed data, fields and the requiered fields and as a result calculates the missing data
# all missing data in general and individual for each record id

import pandas as pd
from itertools import cycle

miss_dict={'record_id':'cis_id'}

#create an empty dataframe
column_result=["Record_id", "Redcap_event_name", "Form","visit_date", "Num_of_fields", "Requiered_fields", "entered_values", "entered_NaN_values", "Calculated_miss_data"]
df_result= pd.DataFrame(columns=column_result)

#importing all the necessary data from Redcap

#patients data
df_Data= pd.read_csv(r'''C:\Users\cohendh\Desktop\PyCharm CSV\Redcap\CIS\CIS_DATA_TEST.csv''', sep=',').set_index([miss_dict['record_id']])
#data dictionary of the study
df_DICT= pd.read_csv(r'''C:\Users\cohendh\Desktop\PyCharm CSV\Redcap\CIS\CIS_DataDictionary.csv''', sep=',').set_index(['Form Name'])
#all the forms of the different visits
df_Forms= pd.read_csv(r'''C:\Users\cohendh\Desktop\PyCharm CSV\Redcap\CIS\CIS_FORMS.csv''', sep=',').set_index(['unique_event_name', 'form'])
#print(df_Data.head())
#print(df_DICT.head())
#print(df_Forms.head())
Num_Forms=df_Forms.groupby(level=0).sum()
#print(Num_Forms)
#-----------------------------------------
#building and designing the dataframe result
record_ids=df_Data.index.tolist()
Redcap_events=df_Data['redcap_event_name'].tolist()
Visit_dates=df_Data['visit_date'].tolist()
record_ids=[i for n, i in enumerate(record_ids) if i not in record_ids[:n]]
print(record_ids)
print(len(record_ids))
df_Forms=df_Forms.reset_index()
column_length = len(df_Forms['unique_event_name'])
new_list_records=[]
new_list_dates=[]
for item in record_ids:
    new_list_records.extend([item]*column_length)
#print(len(new_list_records))
Redcap_event_name=cycle(df_Forms['unique_event_name'])
Form=cycle(df_Forms['form'])
#print(Form)
events_range=len(record_ids)*column_length
df_result['Redcap_event_name']= [next(Redcap_event_name) for event in range(events_range)]
df_result['Form']=[next(Form) for event in range(events_range)]
new_list_records=pd.Series(new_list_records)
df_result['Record_id']=new_list_records
#print(len(df_result['Record_id']))
#print(df_result)

#drop all rows with no visit date
#df_visits['visit_date'].fillna("no Value", inplace=True)

df_result=df_result.set_index(['Record_id', 'Redcap_event_name'])
print(df_result)
#print(df_result.groupby(['Record_id']))
df_result.to_csv('check_df_result.csv')
