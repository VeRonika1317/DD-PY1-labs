numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

for i, k in enumerate(numbers):
    if k is None:
        numbers[i] = 0
        break
numbers[i] = sum(numbers)/len(numbers)

print("Измененный список:", numbers)
