#Topic: Classify a New Algorithm

n = int(input("Enter any n ( 5, 10 or 50): "))

input("One Loop - runs once per item. Press ENTER to run. ")
for i in range(n):
    pass
print(" n = ", n, " steps =", n, " -> O(n) linear time ")

input("Two nestedloops - runs n x n times. Press ENTER to run. ")
for i in range(n):
    for ij in range(n):
        pass
print(" n = ", n, " steps = ", n * n, " -> O(n^2) quadratic time " )

input("Rule: count the loops. Press ENTER ")
print(" 0 loops -> O(1)  1 loop -> O(n) 2 nested -> O(n^2) ")
