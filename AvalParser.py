import pandas as pd

bank = 'Aval'

AvalFile = 'statics/АВАЛЬ.xlsx'
AvalOpenFile = pd.read_excel(AvalFile).astype(str)
AvalDataFrame = pd.DataFrame(AvalOpenFile[['Дата операцiї', 'Дебет', 'Кредит', 'Валюта', 'Призначення платежу', 'Кореспондент', 'Рахунок', 'ЄДРПОУ']])
AvalDict = AvalDataFrame.to_dict()


# for i in AvalDict:
#     for j in AvalDict[i]:
#         print(i, j, AvalDict[i][j])


AvalList = [list(x) for x in AvalDataFrame.to_records(index=False)]


for i in range(len(AvalList)):
    AvalList[i][0] = AvalList[i][0].split()[0]
    for j in range(len(AvalList[i])):
        if str(AvalList[i][j]) == 'nan':
            AvalList[i][j] = 0.0

for i in AvalList:
      print(i)
