import re


def file_parser(file):
    PaymentSystemOpenFile = open(file, 'r')

    count = 0
    purp = ''
    paymentList = []

    for i in PaymentSystemOpenFile:
        parser = re.search('\A\s{3}\d\.\d\.\d+\s\d+\.\d{2}', i)

        if parser:
            if purp:
                paymentList.append(purp)
                purp = ''
                count = 0

            purp += re.sub('\s+',' ',i.replace('\n',''))
            count += 1

        elif count > 0 and 'Итого: ' in i:
            paymentList.append(purp)
            purp = ''
            break

        elif count > 0:
            purp += re.sub('\s+', ' ', i.replace('\n', ''))

    return paymentList
