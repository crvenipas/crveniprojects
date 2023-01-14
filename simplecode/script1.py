import pandas as pd
from datetime import datetime

df = pd.read_csv('~/crveniprojects/simplecode/table1.csv', sep=';')
#df = pd.DataFrame(columns=['date', 'specialist_name', 'client', 'problem_descr', 'solving_descr'])

print('Введите свое имя')
username = input()

print('Выберите клиента')
client = input()

print('Опишите проблему')
problem_descr = input()

print('Опишите, что было сделано')
solving_descr = input()

value1 = [{'date' : datetime.date(datetime.now()), 'specialist_name' : username, 'client' : client, 'problem_descr' : problem_descr ,  'solving_descr' : solving_descr}]

df2 = pd.DataFrame(value1)
df2.to_csv('~/crveniprojects/simplecode/table1.csv', sep=';')
