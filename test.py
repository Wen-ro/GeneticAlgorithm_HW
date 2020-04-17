import numpy as np

length_x = 12
length_y = 11
x_con = [-1, 2]
y_con = [-1, 1]

ch_a = np.random.randint(0, 2, (3, 5))
print(ch_a)
ch_b = np.random.randint(0, 2, 11)
print(ch_b)
ch_c = ch_a.tolist()

print(type(ch_a))
print(type(ch_c))

p_lst = []  # 機率
    q_lst = []  # 累積機率
    for i in range(population):
        p = (fit_lst[i] - 6) / sum(fit_lst)  # 避免機率變成負數
        p_lst.append(p)
        q_lst.append(sum(p_lst))  # 計算累積機率

        z1 = np.random.rand()  # 找parent1
        for prob in q_lst:
            if prob > z1:  # z1 較大時停下
                parent_id_1 = q_lst.index(prob) - 1  # 停下來的位置再減一才是挑到的位置
                parent_1 = ch[parent_id_1]  # 挑到parent1
                q_lst.remove(prob)  # 選到後刪掉
            else:
                break

        z1 = np.random.rand()
        for prob in q_lst:
            if prob > z1:  # z1 較大時停下
                parent_id_2 = q_lst.index(prob) - 1  # 停下來的位置再減一才是挑到的位置
                parent_2 = ch[parent_id_2]  # 挑到parent2
            else:
                break