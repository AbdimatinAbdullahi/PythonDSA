# [2,3,1,1,4]

def JumpGame(jumps):
    goal = len(jumps) - 1

    for i in range(len(jumps) - 1, -1, -1):
        if i + jumps[i]  >= goal:
            goal = i
    
    print(True if goal == 0 else False)

JumpGame([2,3,1,1,4])