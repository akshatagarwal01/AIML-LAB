def create_magic_square(d):
    magicSquare = [[0 for x in range(d)]
                   for y in range(d)]

    i = d // 2
    j = d - 1

    num = 1
    while num <= (d * d):
        if i == -1 and j == d:  
            j = d - 2
            i = 0
        else:
 
            
            if j == d:
                j = 0
 
            
            if i < 0:
                i = d - 1
 
        if magicSquare[int(i)][int(j)]:  
            j = j - 2
            i = i + 1
            continue
        else:
            magicSquare[int(i)][int(j)] = num
            num = num + 1
 
        j = j + 1
        i = i - 1

        print("Magic Square =", d)
        print("Sum of each row or column",
            d * (d * d + 1) // 2, "\n")
    
        for i in range(0, d):
            for j in range(0, d):
                print('%2d ' % (magicSquare[i][j]), end='')

                if j == d - 1:
                    print()





d = int(input("Enter the dimensions : "))
print(d)
create_magic_square(d)
  