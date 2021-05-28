poem = open("lepanto.txt", encoding='utf8')
lines = poem.read().splitlines()
poem.close()
i = 0
k = 0
lines2 = []
for line in lines:
    
    
    if len(line) != 0:
        lines2.append(line)
        
    k+=1

    

def levenshteindistance(source,target):
    
    rows = len(source)+1
    cols = len(target)+1
    
    dist = [[0 for x in range(cols)] for y in range(rows)]
    
    
    for i in range(1,rows):
        dist[i][0] = i
    for i in range(1,cols):
        dist[0][i] = i
    
    for col in range(1,cols):
        for row in range(1,rows):
            if source[row-1] == target[col-1]:
                cost = 0
            else:
                cost = 1
            dist[row][col] = min(dist[row-1][col] + 1,
                                 dist[row][col-1] + 0.01,
                                dist[row-1][col-1] + cost)
    return dist[row][col]
    
minm = 999999
strng = "Failure"
val = input("Input your best guess of a line \n")
for line in lines2:
        tmp = levenshteindistance(val, line)
        
        if tmp < minm:
            minm = tmp
            strng = line
            

            
            
print(strng)
