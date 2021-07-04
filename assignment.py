def returnranges(numlist):
    missingrange = []
    prev = numlist[0]
    if prev!=0:
        if prev == 1:
            missingrange.append(0)
        else:
            missingrange.append([0, prev-1])
    for i in range(1, len(numlist)):
        diff = numlist[i]-prev
        if diff > 1:
            if diff==2:
                missingrange.append(prev+1)
            else:
                missingrange.append([prev+1, numlist[i]-1])
        prev = numlist[i]
    
    if prev!=99:
        if prev == 98:
            missingrange.append(99)
        else:
            missingrange.append([prev+1, 99])
    return missingrange


print(returnranges([0, 1, 3, 50, 75]))