def number_pattern():
    n = int(input("Enter the nth value: "))
    for x in range(1, n+1):
        for y in range(1, x+1):
            print(y, end=' ')
        print()
#number_pattern()

def reverse_pyramid():
    n = int(input("Enter the nth value: "))
    
    for x in range(n + 1, 0, -1):
        for y in reversed(range(x + 1, 0, -1)):
            print("*", end=" ")
        print()
#reverse_pyramid()

