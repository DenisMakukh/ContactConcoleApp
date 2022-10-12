import datetime

file = open('array.txt', 'r')
sp1 = list(map(int, file.read().split()))
print('Количество элементов в файле:', len(sp1))

a = datetime.datetime.now()

def _min(num):
    mini = 1000000^10000
    if len(num) != 0:
        for _ in range(len(num)):
            if num[_] <= mini:
                mini = num[_]
        return mini
    else:
        return None

def _max(num):
    maxi = -(1000000^10000)
    if len(num) != 0:
        for j in range(len(num)):
            if num[j] >= maxi:
                maxi = num[j]
        return maxi
    else:
        return None


def _sum(num):
    counter = 0
    if len(num) != 0:
        for i in num:
            counter += i
        return counter
    else:
        return None

def _mult(num):
    total = 1
    if len(num) != 0:
        for i in num:
            total *= i
        return total
    else:
        return None

def minef(num):
    if len(num) != 0:
        maxi = -(1000000 ^ 10000)
        for j in range(len(num)):
            if num[j] >= maxi:
                maxi = num[j]
        mini = 1000000 ^ 10000
        for _ in range(len(num)):
            if num[_] <= mini:
                mini = num[_]
        return maxi*mini
    else:
        return None


print('Минимальное:', _min(sp1))
print('Максимальное:', _max(sp1))
print('Сумма:', _sum(sp1))
print('Произведение:', _mult(sp1))
b = datetime.datetime.now()
c = b - a