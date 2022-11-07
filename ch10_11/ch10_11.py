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
    
# def main():
#     # scores = input("Enter scores:")
#     # studentScores = [eval(x) for x in scores.split()]
#     studentScores = [40, 55, 70, 58]
#     bestScore = max(studentScores)
#     for i in range(len(studentScores)):
#         grade = gradeScore(studentScores[i], bestScore)
#         print(f"Student {i} score is {studentScores[i]} and grade is {grade}")

# main()


# 10.8 Find the index of the smallest element

def indexOfSmallestElement(lst = []):
    if len(lst) > 1:
        currSmallestIdx = 0
        for i in range(1, len(lst)):
            if lst[i] < lst[currSmallestIdx]:
                currSmallestIdx = i
        
        return currSmallestIdx

def main():
    userInput = input("Enter a list of numbers (comma separated): ")
    numsLst = [eval(num) for num in userInput.split(",")]
    lowestIdxResult = indexOfSmallestElement(numsLst)

    print(f"Index {lowestIdxResult} holds the lowest number in the list {numsLst}")

main()