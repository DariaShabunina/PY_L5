import random


def get_unique_list_numbers() -> list[int]:
    list_numbers = []
    for i in range(15):
        while True:
            c = random.randint(-10, 10)
            if c in list_numbers:
                continue
            else:
                list_numbers.append(c)
                break
    return list_numbers


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
#end
