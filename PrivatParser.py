import pandas as pd

bank = 'Privat'

PrivatFile = 'statics/ПРИВАТ.xlsx'
PrivatOpenFile = pd.read_excel(PrivatFile).astype(str)
PrivatDataFrame = pd.DataFrame(PrivatOpenFile)
PrivatDataFrame = pd.DataFrame(PrivatOpenFile[['Unnamed: 1', 'Unnamed: 4', 'Unnamed: 3', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 8', 'Unnamed: 11', 'Unnamed: 7' ]])[2:-1]

PrivatList = [list(x) for x in PrivatDataFrame.to_records(index=False)]

for i in range(len(PrivatList)):
    PrivatList[i].insert(0,bank)

for i in range(len(PrivatList)):
    PrivatList[i][1] = PrivatList[i][1].split()[0]
    for j in range(len(PrivatList[i])):
        if str(PrivatList[i][j]) == 'nan':
            PrivatList[i][j] = 0.0
#
for i in PrivatList:
       print(i)
