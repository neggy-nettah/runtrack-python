
for iter in range(2, 1001):
    for i in range(2, iter):
        if iter % i == 0:
            break
    else:
        print(iter)