def pascaltriangle(n):
    if n == 1:
        return[1]
    else:
        current = []
        current.append(1)
        prev = pascaltriangle(n-1)
        for i in range(len(prev)-1):
            temp = prev[i] + prev[i+1]
            current.append(temp)
        current.append(1)
    return current
print(pascaltriangle(10))
