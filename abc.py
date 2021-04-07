from scipy.optimize import linear_sum_assignment

G=list()

G.append([])
G[0].append(2)
G[0].append(3)

G.append([])
G[1].append(5)
G[1].append(7)

print(G)
row_ind, col_ind = linear_sum_assignment(G)

print(col_ind)