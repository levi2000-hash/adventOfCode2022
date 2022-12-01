with open('input.txt') as f:
    lines = f.readlines()

    mostCalories = []
    total = 0

    for line in lines:
        if line != "\n" and line != '' and line != "":
            total += int(line.strip())
        else:
            mostCalories.append(total)
            total = 0
mostCalories.sort(reverse=True)

total = 0
for num in mostCalories[:3]:
    total += num
print(total)