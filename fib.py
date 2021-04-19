'''Реализовать функцию вычисления i-го числа Фибоначчи.'''

def fib(n):
    if type(n)!=int:
<<<<<<< HEAD
        raise TypeError("n must be int")
=======
        raise ValueError("n must be int")
>>>>>>> 674761220449047da736249a835d822e0534edad
    elif n <= 0:
        raise ValueError("n must be >= 0")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    return fib(n-1)+fib(n-2)


if __name__ == '__main__':
    print(fib(10))    