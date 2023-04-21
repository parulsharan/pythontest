def outer_loop(a, b):
    square = a**2
    def inner_loop(a, b):
        add = a+b
        return add+5

print(outer_loop(5,6))    