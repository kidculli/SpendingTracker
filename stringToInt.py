import functools 

def add(x,y):
    return x + y 

def stringToInt(s):
    intList = list(map(ord,s))
    return  functools.reduce(add ,intList)

def stringToFloat(s):
    return stringToInt(s) / len(s)


if __name__ == '__main__':
    food = "Staples"
    print(stringToInt(food))
    food2 = "Foodtruck"
    print(stringToInt(food2))
