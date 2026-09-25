#Topic Big-O Notation - each growth pattern has an official name

n= 10

guess = input("Double Loop at n = 10 checks n x n pairs. How many? ")

input("Formula: one calculation, done. Press ENTER to run. ")
steps = 1
print(" steps =", steps, " -> O(1) constant time -> steps never change")

input("Loop: one step per time. Press ENTER to run. ")
steps = 0
for i in range(n):
    steps += 1
print(" steps =", steps, " -> O(n) linear time -> steps grow with n")

input("Double Loop: checks every pair. Press ENTER to run. ")
steps = 0
for i in range(n):
    for j in range(n):
        steps += 1
print(" steps =", steps, " your guess:", guess, " -> O(n^2) quadratic time")

input("Two more notations. Press ENTER. ")
print(" Big Omega -> best case lower bound... ")
print(" Big Theta -> exact boung (worst = best)")
