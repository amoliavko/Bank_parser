import re


def file_parser(file):

    BcbOpenFile = open(file, 'r', encoding='cp1251')

    data = debet = credit = curr = purp = acc = ''
    bank = 'BSBBankForeign'
    contr = 'Unknown'
    paymentList = []
    count = 0

    for i in BcbOpenFile:

        parsAcc = re.search('Счет клиента\s+(\d+)', i)
        if parsAcc:
            acc = parsAcc.group(1)

        parser = re.search('\A\d{2}\.\d{2}\.\d{4}\s+\d+', i)
        if parser:
            items = re.split('\s+', i)
            if len(items) == 10:

                if data and debet and credit and curr and purp:
                    paymentList.append([bank, data, debet, credit, curr, purp, contr, acc])
                    data = debet = credit = curr = purp = ''

                data = items[0]
                debet = items[5].replace(',','')
                credit = items[6].replace(',','')
                curr = items[3]
                count = 1

        elif count > 0 and '+-----------------------------' in i:
            if data and debet and credit and curr and purp:
                paymentList.append([bank, data, debet, credit, curr, purp, contr, acc])
                data = debet = credit = curr = purp = ''
            break

        elif count > 0:
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
