# 1. Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

def avrg_profit(list_rec):
    avg_prof = 0
    for i in list_rec:
        avg_prof += i.profit

    return avg_prof / len(list_rec)

# num_fac = 3
num_fac = int(input(f'Enter number of factory: '))
# name_fac = 'Beeline'
# profit_fac = 100345.56

# Beeline =>  100345.56
# MTS => 504567.54
# Megafon => 9348348.43

# avg_profit =

list_fac = []
FacRecord = namedtuple('FacRecord', 'name, profit')

for i in range(num_fac):
    name_fac = input(f'Enter factory name: ', )
    profit_fac = float(input(f'Enter Q profit: '))
    fac_rec: FacRecord = FacRecord(name_fac, profit_fac)
    list_fac.append(fac_rec)

avg_prof = avrg_profit(list_fac)

list_fac_report = {}
list_upper = []
list_below = []

for i in list_fac:
    if i.profit > avg_prof:
        list_upper.append(i.name)
    else:
        list_below.append(i.name)

list_fac_report['upper'] = list_upper
list_fac_report['below'] = list_below

print(f'Factories upper avarage profit:')
print(*list_fac_report['upper'])
print(f'Factories below avarage profit: ')
print(*list_fac_report['below'])
