h = [2,3,5,7,11,13]
k=9

for i in h:
    if i>k:
        h.insert(h.index[i], k)
        break

print(h)