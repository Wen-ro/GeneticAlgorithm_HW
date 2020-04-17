"""""
Problem 4
Maximum f(x,y)= 6 - (sin^2(sqrt((x^2 + y^2)))) / (1 + 0.1 * (x^2 - y^2))^8
-1≤x≤2; -1≤y≤1; x+y≥-1	Maximum=6 at (x,y)=(0,0)

"""

import numpy as np
import math
import matplotlib.pyplot as plt

length_x = 12
length_y = 11
length_ch = 23
population = 100
generation = 1000
CR = 0.9  # Crossover Rate
MR = 0.1  # Mutation Rate
x_con = [-1, 2]
y_con = [-1, 1]

# Initialization

ch = np.random.randint(0, 2, (population, length_ch))
ch = ch.tolist()


# Function Part


def bin_to_dec(str_int):  # 2進位制轉10進位制
    bin_v = [int(n) for n in str_int]
    dec = [bin_v[-i - 1] * math.pow(2, i) for i in range(len(bin_v))]
    return int(sum(dec))


def f(x, y):
    return 6 - ((math.sin(math.sqrt(x ** 2 + y ** 2))) ** 2) / ((1 + 0.1 * (x ** 2 - y ** 2)) ** 8)


# Selection: Roulette Wheel


def selection(ch):
    parent_id_1 = np.random.choice(a=100, size=1, replace=False, p=None)
    parent_id_1 = int(parent_id_1)  # 挑出parent1的位置
    parent_1 = ch[parent_id_1]
    parent_id_2 = np.random.choice(a=100, size=1, replace=False, p=None)
    parent_id_2 = int(parent_id_2)  # 挑出parent2的位置
    parent_2 = ch[parent_id_2]

    return parent_1, parent_2, parent_id_1, parent_id_2


def crossover(parent_1, parent_2):
    z2 = np.random.rand()
    if z2 < CR:  # 隨機變數小於CR時crossover
        cr_location = int(np.ceil(z2 * (length_ch - 1)))
        offspring_1 = parent_1[:cr_location - 1] + parent_2[cr_location - 1:]  # parents crossover for offsprings
        offspring_2 = parent_2[:cr_location - 1] + parent_1[cr_location - 1:]
    return parent_1, parent_2


def mutation(offspring_1, offspring_2):  # chromosome-wise mutation
    z3 = np.random.rand()
    if z3 < MR:  # 隨機變數小於突變率的話突變(for parent_1)
        mu_location = np.random.randint(0, length_ch - 1)  # 找出突變的位置
        offspring_1[mu_location] = 1 if offspring_1[mu_location] == 0 else 1  # 原本是0的話變成1, 反之亦然

    z3 = np.random.rand()
    if z3 < MR:  # 隨機變數小於突變率的話突變(for paren_2)
        mu_location = np.random.randint(0, length_ch - 1)
        offspring_2[mu_location] = 1 if offspring_2[mu_location] == 0 else 1
    return offspring_1, offspring_2


# Main Part

best_fit = []  # for best fitness every time
best_rec_fit = [0]
best_x = 0
best_y = 0
best_ch = []
record_fit = 0
for t in range(generation):
    fit_lst = []
    for i in range(population):

        ch_x = ch[i][:12]  # 取每一列 x 染色體
        ch_y = ch[i][12:]  # 取每一列 y 染色體

        # Evaluation

        x_dec = bin_to_dec(ch_x)
        y_dec = bin_to_dec(ch_y)

        x = -1.0 + (x_dec * 3 / (2 ** length_x - 1))  # 求x值
        y = -1.0 + (y_dec * 2 / (2 ** length_y - 1))  # 求y值

        if (x + y) >= -1:  # 求fitness值
            fit = f(x, y)
        else:
            fit = f(x, y) - ((0.5 * t) ** 5) * ((abs(-1 - f(x, y))) ** 5)  # add penalty: x+y>=-1
        fit_lst.append(fit)  # 產生的100個fit值都放進fit_lst

        if record_fit < max(fit_lst):  # 留住最好的x, y, chromosome, fitness
            record_fit = max(fit_lst)
            best_x = x
            best_y = y
            best_ch = ch[i]

    best_fit.append(max(fit_lst))  # 當代100個fitness中最好的fitness value放入best_lst
    if record_fit > max(best_rec_fit):
        best_rec_fit.append(record_fit)
    else:
        best_rec_fit.append(record_fit)

    for i in range(50):  # 針對100個染色體開始往下作，每次產生兩個子代，故循環50次
        parent_1, parent_2, parent_id_1, parent_id_2 = selection(ch)  # selection 選出2個parent
        offspring_1, offspring_2 = crossover(parent_1, parent_2)  # crossover 出2個子代
        offspring_1, offspring_2 = mutation(offspring_1, offspring_2)  # 對子代突變
        ch[parent_id_1] = offspring_1  # 將parents以offsprings取代掉
        ch[parent_id_2] = offspring_2

print(best_fit)
print(best_rec_fit)
print(best_x)
print(best_y)
print(best_ch)

plt.plot(best_fit)
plt.plot(best_rec_fit)  # 畫出best_rec_fit的演進
plt.ylabel("Fitness")
plt.xlabel("Generation")
plt.title("Evolution History")
plt.show()
