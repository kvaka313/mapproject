def area(massive,i,j):
     massive[i][j]=2
     if (j+1<len(massive) and massive[i][j+1]==1):
        area(massive,i,j+1)
     if (i-1>=0 and massive[i-1][j]==1):
         area(massive,i-1,j)
     if(i+1<len(massive) and massive[i+1][j]==1):
         area(massive,i+1,j)
     if(j-1>=0 and massive[i][j-1]==1):
         area(massive,i,j-1)

def move(massive):
    count=0
    for i in range(0,len(massive)):
        for j in range(0,len(massive)):
            if(massive[i][j]==1):
               count+=1
               area(massive,i,j)

    return count

mas=[[0,0,0,0,0],
     [0,1,1,0,0],
     [1,1,0,0,0],
     [0,0,0,0,0],
     [1,1,0,0,1]]

print(move(mas))
