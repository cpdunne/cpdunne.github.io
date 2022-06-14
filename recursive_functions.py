def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def sum_recursively(n):
    if n == 0:
        return 0
    else:
        return n + sum_recursively(n-1)

def sumlist_recursively(l):
    if len(l) == 1:         #bingus
        return l[0]
    else:
        return l[0] + sumlist_recursively(l[1:])

def reverse_recursively(l):
    if len(l) == 0:         #Yo moomma
        return []
    else:
        return [l.pop()] + reverse_recursively(l)


#EXTRA CREDIT
def multiply_recursively(n, m):
    if m == 0:
        return 0
    else:
        return n + multiply_recursively(n, m-1)
    pass    # replace this line with your lines of recursive code
