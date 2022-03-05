import pandas as pd
#<module 'pandas' from 'C:\\Users\\lina9\\anaconda3\\lib\\site-packages\\pandas\\__init__.py'>

#cargar el csv como dataframe de pandas
dfcsv= pd.read_csv('x:/repos/GGReport/scripts/songs.csv')

OldestSong=dfcsv['Anio'].min()

print(OldestSong)