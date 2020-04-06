# cons(a,b) constructs a pair, and car(pair) and cdr(pair)
# returns the first and last element of that pair. 
#implement car and cdr.

#test input
x = 3
y = 4

#Given
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

#implement cdr 
def cdr(pair):
    return pair(lambda a, b: b)

#car
def car(pair):
    return pair(lambda a, b: a)

#test cdr
#test = cdr(cons(x, y))

#test car
test = car(cons(x, y))

print(test)