numb = int(input("Введите число: "))
full_list = []
for i in range(numb, 0, -1):
    if numb % i == 0:
        full_list.append(i)
print(full_list)



