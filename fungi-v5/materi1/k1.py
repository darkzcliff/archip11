# Kegiatan 1

def sum(x, y):
    return x + y

def min(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y != 0:
        return x / y
    else: print("Undefined.")

def tree(node):
    if type(node) in (int, float):
        return node
    elif type(node) is tuple and len(node) == 3:
        ops, left, right = node
        if ops == '+':
            return sum(tree(left), tree(right))
        elif ops == '-':
            return min(tree(left), tree(right))
        elif ops == '*':
            return mul(tree(left), tree(right))
        elif ops == '/':
            return div(tree(left), tree(right))

expression = ('*', ('+', 2, 3), ('-', 5, 1))
print("Hasil {0}".format(tree(expression)))


# def treh(node):
#     if isinstance(node, tuple):
#         left = treh(node[0])
#         operator = node[1]
#         right = treh(node[2])
        
#         if operator == '+':
#             return sum(left, right)
#         elif operator == '-':
#             return min(left, right)
#         elif operator == '*':
#             return mul(left, right)
#         elif operator == '/':
#             return div(left, right)
#     else:
#         return node

# expressioh = ((2, '+', 3), '*', (5, '-', 1))
# print("Hasil {0}".format(treh(expressioh)))
