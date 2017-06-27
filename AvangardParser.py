import pandas as pd

bank = 'Avangard'
curr = 'RUB'

AvangardFile = 'statics/АВАНГАРД.xlsx'
AvangardOpenFile = pd.read_excel(AvangardFile).astype(str)
AvangardDataFrame = pd.DataFrame(AvangardOpenFile)


print(AvangardDataFrame[AvangardDataFrame.columns[2]])
# acc_pos = 0
# for i in AvangardDataFrame[AvangardDataFrame.columns[0]]:
#     acc_pos+=1
#     if str(i).startswith('ИИК'):
#         acc = i.split()[1]
#
# startPos = 0
# for i in AvangardDataFrame[AvangardDataFrame.columns[0]]:
#     startPos += 1
#     if str(i).startswith('Реттік'):
#         break
#
# finishPos = 0
# for i in AvangardDataFrame[AvangardDataFrame.columns[0]]:
#     finishPos += 1
#     if str(i).startswith('Жиынтығы'):
#         finishPos -= 1
#         break
#
# AvangardDataFrame = AvangardDataFrame.iloc[startPos:finishPos]
# AvangardDataFrame = pd.DataFrame(AvangardDataFrame[['Unnamed: 1', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 11', 'Unnamed: 5']])
# AvangardList = [list(x) for x in AvangardDataFrame.to_records(index=False)]
#
# for i in range(len(AvangardList)):
#     AvangardList[i].insert(0,bank)
#     AvangardList[i].append(acc)
#     AvangardList[i].insert(4,curr)
#
# for i in range(len(AvangardList)):
#     for j in range(len(AvangardList[i])):
#         if str(AvangardList[i][j]) == 'nan':
#             AvangardList[i][j] = 0.0
#         AvangardList[i][j] = str(AvangardList[i][j]).replace(',','')
#
# for i in AvangardList:
#        print(i)
