
puzzle= [[0]*9 for i in range(9)]

puzzle = [
            [3, 0, 6, 5, 0, 8, 4, 0, 0],  
            [5, 2, 0, 0, 0, 0, 0, 0, 0],  
            [0, 8, 7, 0, 0, 0, 0, 3, 1],  
            [0, 0, 3, 0, 1, 0, 0, 8, 0],  
            [9, 0, 0, 8, 6, 3, 0, 0, 5],  
            [0, 5, 0, 0, 9, 0, 6, 0, 0],  
            [1, 3, 0, 0, 0, 0, 2, 5, 0],  
            [0, 0, 0, 0, 0, 0, 0, 7, 4],  
            [0, 0, 5, 2, 0, 6, 3, 0, 9]
            ] 

def input_ele():
    print("enter elements:")
    for i in range(1,9):
        for j in range(1,9):
            puzzle[i][j]=int(input())
 
def display(puzz):
    for i in range(len(puzz[0])):
        if i%3==0 and i!=0:
            print("-----------------------")
        for j in range(len(puzz[0])):
            if j%3==0 and j!=0:
                print(" | ",end="")    
            if j == 8:
                print(puzz[i][j])
            else:
                print(str(puzz[i][j]) + " ", end="")        

def empyt_loc(puzz):
    for i in range(len(puzz)):
        for j in range(len(puzz[0])):
            if puzz[i][j] == 0:
                return (i, j)  
                
    return None

def valid(puzz, num, pos):
    # Check row
    for i in range(len(puzz[0])):
        if puzz[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(puzz)):
        if puzz[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if puzz[i][j] == num and (i,j) != pos:
                return False

    return True   
def solver(puzz):
    find = empyt_loc(puzz)
    if not find:
        print("------ SOLUTION FOUND ------")
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(puzz, i, (row, col)):
            puzz[row][col] = i

            if solver(puzz):
                return True

            puzz[row][col] = 0
    
    return False                        


display(puzzle)
solver(puzzle)
print("")
display(puzzle) 

