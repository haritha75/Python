li = [[1, 2, 3, 4], [3, 4, 5, 6], [1, 2]]
# # largest row sum 
max_sum = 0
for row in li:
    row_sum = 0  
    for ele in row:
        row_sum += ele  
    if row_sum >= max_sum:
        max_sum = row_sum

print(max_sum)


# largest column sum

def lar_Col_sum(li):
    n = len(li)
    m = len(li[0]) # all column size same
    max_sum = -1
    max_col_index = -1
    for j in range(m):
        sum1 = 0
        for i in range(n):
            sum1 += li[i][j]
        if sum1 > max_sum:
            max_col_index = j
            max_sum = sum1
    return max_col_index, max_sum

li = [[1, 2, 3, 4], [3, 4, 5,1], [1, 1,2,3]]
lar_index, lar_sum = lar_Col_sum(li)
print(lar_index, lar_sum)

# another way


def lar_Col_sum(li):
    n = len(li)
    m = len(li[0]) # all column size same
    max_sum = -1
    max_col_index = -1
    for j in range(m):
        sum1 = 0
        for ele in li: # using list directly
            sum1 += ele[j]
        if sum1 > max_sum:
            max_col_index = j
            max_sum = sum1
    return max_col_index, max_sum

li = [[1, 2, 3, 4], [3, 4, 5,1], [1, 1,2,3]]
lar_index, lar_sum = lar_Col_sum(li)
print(lar_index, lar_sum)

            
# but it work like this only it works like for each menas one by one list comes based on that in first list it takes jth value agaon 2nd list takes same jth value and summing that value

