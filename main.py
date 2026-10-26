import csv
import matplotlib.pyplot as plt

# Данни - точки с X и Y координати
data = []

with open("iris.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        if len(row) > 0:
            try:
                # взимаме само първите 2 числа
                x = float(row[0])
                y = float(row[1])
                data.append([x, y])
            except:
                pass

# Начални центрове на двата клъстера
centroid1 = [1, 2]
centroid2 = [8, 7]

# Функция за намиране на разстояние между две точки
def distance(point, centroid):
    return ((point[0] - centroid[0]) ** 2 + (point[1] - centroid[1]) ** 2) ** 0.5

# Създаваме два празни клъстера
cluster1 = []
cluster2 = []

# Разпределяме точките към най-близкия център
for point in data:
    d1 = distance(point, centroid1)
    d2 = distance(point, centroid2)

    if d1 < d2:
        cluster1.append(point)
    else:
        cluster2.append(point)

# Извеждаме резултата
print("Клъстер 1:", cluster1)
print("Клъстер 2:", cluster2)

# Рисуваме точките
for point in cluster1:
    plt.scatter(point[0], point[1], color="blue")

for point in cluster2:
    plt.scatter(point[0], point[1], color="green")

# Рисуваме центровете
plt.scatter(centroid1[0], centroid1[1], color="red", marker="X", s=150)
plt.scatter(centroid2[0], centroid2[1], color="red", marker="X", s=150)

plt.title("Пример за K-Means Clustering")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show()