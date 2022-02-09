import random

def compare(goal,comp):
    score = 0
    for i in range(len(goal)):
        if goal[i] == comp[i]:
            score+=1
    return score/len(goal)

def create(leng):
    allletters = "abcdefghijklmnopqrstuvwxyz ,.1234567890"
    tst = ""
    for i in range(leng):
        tst+=allletters[random.randrange(39)]
    return tst

def main():
    goal = input("Enter the string you want the computer to find: ")
    n = create(len(goal))
    score = compare(goal, n)
    best_score = 0
    while score < 1:
        if score>best_score:
            print(n)
        n = create(len(goal))
        score = compare(goal, n)
    if score == 1:
        print(n)
main()
