incomes = []
output = []
rest = dict()

for i in range(7):
    day_incomes = int(input('周' + str(i+1) +'的收入是：'))
    incomes.append(day_incomes)
    
for i in range(7):
    day_output = int(input('周' + str(i+1) +'的支出是：'))
    output.append(day_output)
    
print('7天的收入分别是：')
for i in incomes:
    print(i)

print('7天的支出分别是：')
for i in output:
    print(i)
    
for i in range(7):
    rest[i] = incomes[i] - output[i]
    
print('7天的收支结余是：')
for day,rest in rest.items():
    print('周' ,day+1, '的结余是：',rest)
    
print('最终的结余为：',sum(incomes) - sum(output))