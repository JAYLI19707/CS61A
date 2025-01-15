print(True and 13)
print(False or 0)
print(-1 or 5)
print((1 + 1) and 1)

def cake():
    print('beets')
    def pie():
        print('sweets')
        return 'cake'
    return pie
chocolate = cake()
more_chocolate, more_cake = chocolate(), cake
print(more_chocolate)
print(cake)

def snake(x, y):
    if cake == more_cake:
        return chocolate
    else:
        return x + y
    
print(snake(10, 20))


print(snake(10, 20)())


cake = 'cake'
print(snake(10, 20))
