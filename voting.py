#voting
age = int(input("enter your age:   "))
voting_criteria= "eligible for vote" if age >= 18 else "not eligible for vote"
print(voting_criteria)
