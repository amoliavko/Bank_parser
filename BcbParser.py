import pandas as pd
import re

#file ='/media/a_m/Wdisk/Python/Projects/Bank_parser/example/clean (copy)/УКРЭКСИМ.xlsx'
#bcb_file ='/media/a_m/Wdisk/Python/Projects/Bank_parser/example/txt.txt'
#Avangard_file ='/media/a_m/Wdisk/Python/Projects/Bank_parser/example/clean (copy)/АВАНГАРД.xlsx'

#open_file = pd.read_excel(file)
# open_BCB = pd.read_table(bcb_file, encoding='cp1251')
#open_BCB = pd.read_table(bcb_file, encoding='cp1251')
#open_Avangard = pd.read_excel(Avangard_file)

#df = pd.DataFrame({'a':[1], 'b':[2]})
# df = pd.DataFrame(open_file)
# BCB_df = pd.DataFrame(open_BCB)
# Avangard_df = pd.DataFrame(open_Avangard)

# df.to_csv('/media/a_m/Wdisk/Python/Projects/Bank_parser/example/clean (copy)/out_УКРЭКСИМ.xlsx')
# BCB_df.to_excel('/media/a_m/Wdisk/Python/Projects/Bank_parser/example/clean (copy)/out_БСБ банк.xlsx')

# print(open_file,'\n')


# test_df = pd.DataFrame(columns=('Банк', 'Дата', 'Дебет', 'Кредит', 'Валюта', 'Назначение', 'Агент', 'Счет'))
#
#
#
# test_df.loc['test'] = [1,2,3,4,5,6,7,8]
#
# print(test_df)
#
#
# test_df

BcbFile = '/media/a_m/Wdisk/Python/Projects/Bank_parser/example/clean (copy)/БСБ банк.txt'
BcbOpenFile = open(BcbFile, 'r', encoding='cp1251')


data = contr = debet = credit = curr = purp = acc = edrp = ''
bank = 'BSBBank'
count = 0
paymentList = []

for i in BcbOpenFile:

    pars_account = re.search('Счет клиента\s+(\d+)\s+(\w+)', i)
    if pars_account:
        acc = pars_account.group(1)
        curr = pars_account.group(2)

    parser = re.search('\A\d{2}\.\d{2}\.\d{4}\s+\d+', i)
    if parser:

        items1 = re.split('\s+', i)
        if len(items1) == 9:
            if data and debet and credit and curr and purp and contr and acc and edrp:
                paymentList.append([bank, data, debet, credit, curr, purp, contr, acc, edrp])
                data = debet = credit = purp = contr = edrp =''

            data = items1[0]
            debet = items1[5].replace(',','')
            credit = items1[6].replace(',','')
            edrp = items1[7]
            count = 1

    elif count == 1:
        contr = i.strip()
        count += 1

    elif '+-------------------------------------' in i and count >= 2:
        if data and debet and credit and curr and purp and contr and acc and edrp:
            paymentList.append([bank, data, debet, credit, curr, purp, contr, acc, edrp])
            data = debet = credit = purp = contr = edrp = ''
        break

    elif count > 1:
        if i:
            purp += i.strip('\n')
        count += 1


BcbOpenFile.close()


for i in paymentList:
    print(i)
