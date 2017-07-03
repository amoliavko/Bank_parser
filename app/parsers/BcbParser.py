import re

def file_parser(file):

    BcbOpenFile = open(file, 'r', encoding='cp1251')
    # BcbOpenFile = open(file, 'r', encoding='cp1251')
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

    for i in range(len(paymentList)):
        for j in range(2, 4):
            if str(paymentList[i][j]) == '':
                paymentList[i][j] = '0,00'
            paymentList[i][j] = str(paymentList[i][j]).replace('.', ',')

    for i in range(len(paymentList)):
        for j in range(len(paymentList[i])):
            if str(paymentList[i][j]) == 'nan':
                paymentList[i][j] = ''

    return paymentList
