list = []

amount = int(input("Syötä kuinka monta numeroa haluat syöttää: "))

for i in range(amount):
    user_input = int(input("Syötä numero: "))
    list.append(user_input)

def list_even(x):
    even_list = [num for num in x if num % 2 == 0]
    print(even_list)
    return even_list

print(list)
list_even(list)

