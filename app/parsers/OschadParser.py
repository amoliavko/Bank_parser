import pandas as pd
#
# def file_parser(file):
#
#     bank = 'Oshchad'
#     curr = 'RUB'
#
#     OshchadOpenFile = pd.read_excel(file).astype(str)
#     OshchadDataFrame = pd.DataFrame(OshchadOpenFile)
#
#     acc = OshchadDataFrame[OshchadDataFrame.columns[12]][0]
#
#     startPos = 0
#     for i in OshchadDataFrame[OshchadDataFrame.columns[2]]:
#         startPos += 1
#         if str(i).startswith('Дата док-та'):
#             break
#
#     finishPos = 0
#     for i in OshchadDataFrame[OshchadDataFrame.columns[2]]:
#         finishPos += 1
#         if str(i).startswith('Итого:'):
#             finishPos -= 1
#             break
#     del_list = ['nan', 'Дата док-та']
#     OshchadDataFrame = OshchadDataFrame.iloc[startPos:finishPos]
#     OshchadDataFrame = pd.DataFrame(OshchadDataFrame[['ПАО АКБ "АВАНГАРД"', 'Unnamed: 26', 'Unnamed: 29', 'Unnamed: 31', 'Unnamed: 21']])
#     OshchadDataFrame = OshchadDataFrame[~OshchadDataFrame['ПАО АКБ "АВАНГАРД"'].isin(del_list)]
#
#     OshchadList = [list(x) for x in OshchadDataFrame.to_records(index=False)]
#
#     for i in range(len(OshchadList)):
#         OshchadList[i].insert(0,bank)
#         OshchadList[i].append(acc)
#         OshchadList[i].insert(4,curr)
#
#
#
#     for i in range(len(OshchadList)):
#         OshchadList[i][1] = OshchadList[i][1].split()[0]
#         for j in range(len(OshchadList[i])):
#             if str(OshchadList[i][j]) == 'nan':
#                 OshchadList[i][j] = ''
#             OshchadList[i][j] = str(OshchadList[i][j]).replace(',','')
#
#
#
#     return OshchadList

OshchadList = []

file = '/home/user/Playground/Projects/BankParser/Bank_parser/app/static/Ощад.xlsx'

readFile = pd.read_excel(file)

df = pd.DataFrame(readFile)

oshadDf = df[df.columns[2:6]]
oshadDf = oshadDf.drop(oshadDf.columns[1:3], axis=1)



print(oshadDf)