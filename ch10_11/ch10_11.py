# Exercises 10.1, 10.8, 10.13, (11.1)
# Chapters 10 and 11 Exercises
# Carlos Rodriguez Escamilla
# 11/05/2022

# 10.1 Assign Grades

def gradeScore(score, bestScore):
    grade = None
    if score >= bestScore - 10:
        grade = "A"
    elif score >= bestScore - 20:
        grade = "B"
    elif score >= bestScore - 30:
        grade = "C"
    elif score >= bestScore - 40:
        grade = "D"
    else:
        grade = "F"
    
    return grade
    
def main():
    scores = input("Enter scores:")
    studentScores = [eval(x) for x in scores.split()]
    bestScore = max(studentScores)
    for i in range(len(studentScores)):
        grade = gradeScore(studentScores[i], bestScore)
        print(f"Student {i} score is {studentScores[i]} and grade is {grade}")

main()


# 10.8 Find the index of the smallest element

def indexOfSmallestElement(lst = []):
    if len(lst) > 1:
        currSmallestIdx = 0
        for i in range(1, len(lst)):
            if lst[i] < lst[currSmallestIdx]:
                currSmallestIdx = i
        
        return currSmallestIdx
    else:
        return None

def main2():
    userInput = input("Enter a list of numbers: ")
    numsLst = [eval(num) for num in userInput.split()]
    lowestIdxResult = indexOfSmallestElement(numsLst)

    if lowestIdxResult != None:
        print(f"Index {lowestIdxResult} holds the lowest number in the list {numsLst}")
    else:
        print("Next time enter more than one number!")

main2()

# 10.18 Eliminate Duplicates

def eliminateDuplicates(lst):
    newList = []

    for num in lst:
        if num not in newList:
            newList.append(num)
    
    return newList

def main3():
    numInput = input("Enter ten numbers: ")
    userList = [eval(num) for num in numInput.split()]
    nonDupList = eliminateDuplicates(userList)

    print(f"The distinct numbers are: ", end="")
    for num in nonDupList:
        print(num, end=" ")

main3()
