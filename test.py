def revrot(string, sz):
    new_string = ""

    if sz <= len(string) and sz > 0:
        n = len(string) / sz    #number of chunks
        for i in range(n):
            num = []
            sum = 0
            for j in range(sz):
                num.append(int(string[i * sz + j]))
                sum += num[j]**3
                print num[j]
            if  sum % 2 == 0:
                new_string += (string[(i * sz) : ((i + 1) * sz) : -1])
            else:
                new_string += (string[(i * sz + 1) : ((i + 1) * sz)])
                new_string += (string[i * sz])
        return new_string
    else:
        return ""
