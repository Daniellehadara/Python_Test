#the following script should help with the calculation of  missing data on RedCap
#calculating the existed data, fields and the requiered fields and as a result calculates the missing data
# all missing data in general and individual for each record id

import pandas as pd
from itertools import groupby

miss_dict={'record_id':'cis_id'}

df_DICT= pd.read_csv(r'''C:\Users\cohendh\Desktop\PyCharm CSV\Redcap\CIS\CIS_DataDictionary.csv''', sep=',').set_index(['Form Name'])

Fields_to_count=df_DICT.index.tolist()
Field_count=[len(list(group)) for key, group in groupby(Fields_to_count)]
print(Field_count)
new_Field_count=[]
Num_of_fields=pd.Series(new_Field_count)
print(Num_of_fields)


