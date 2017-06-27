import pandas as pd


file = open('static/АВАНГАРД.xlsx', 'r')

AvangardDataFrame = pd.DataFrame(pd.read_excel('static/АВАНГАРД.xlsx').astype(str))

startPos = 0
for i in AvangardDataFrame[AvangardDataFrame.columns[2]]:
    startPos += 1
    if str(i).startswith('Дата док-та'):
        break

finishPos = 0
for i in AvangardDataFrame[AvangardDataFrame.columns[2]]:
    finishPos += 1
    if str(i).startswith('Итого:'):
        finishPos -= 1
        break

AvangardDataFrame = AvangardDataFrame.iloc[startPos:finishPos]

AvangardDataFrame = pd.DataFrame(
    AvangardDataFrame[['ПАО АКБ "АВАНГАРД"', 'Unnamed: 26', 'Unnamed: 29', 'Unnamed: 31', 'Unnamed: 21']])

writer = pd.ExcelWriter('static/result.xlsx', engine='xlsxwriter')
AvangardDataFrame.to_excel(writer, sheet_name='Sheet1', index=False)
writer.save()


# print(startPos, finishPos)
# print(AvangardDataFrame)
# acc_pos=0
# out=''
# for i in df[df.columns[12]]:
#     acc_pos+=1
#     if str(i).startswith('\d'):
#         out = str(i)
# print(out)



# AvangardDataFrame = pd.DataFrame(df[['Unnamed: 1', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 11', 'Unnamed: 5']])
# AvangardList = [list(x) for x in AvangardDataFrame.to_records(index=False)]
#
# for i in AvangardList:
#     print(i)


# for i in range(len(AvangardList)):
#     for j in range(len(AvangardList[i])):
#         if str(AvangardList[i][j]) == 'nan':
#             AvangardList[i][j] = 0.0
#         AvangardList[i][j] = str(AvangardList[i][j]).replace(',','')
#
# for i in AvangardList:
#        print(i)








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


a = ['nan', 'Дата док-та']
df = AvangardDataFrame[~AvangardDataFrame['ПАО АКБ "АВАНГАРД"'].isin(a)]

print(df)