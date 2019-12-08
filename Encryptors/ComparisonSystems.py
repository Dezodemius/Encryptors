from Encryptors.Caesar import Caesar as c
import random as rand


def factor(m):
    """ Разложить число на простые множители.

    Возвращает массив этих простых чисел."""
    factors = [];
    for i in range(2, m, 1):
        if m % i == 0 and (not test_ferma(i)):
            factors.append(i)
    return factors


def test_ferma(n, is_shown=False):
    """ Тест Ферма на простоту. """
    is_composite = False
    for a in range(1, n-1, 1):
        if 1 not in c.solve_mod(c.mhp(a, n-1, n), 1, n).values():
            is_composite = True

    if is_shown:
        if is_composite:
            print("{0} - составное".format(n))
        else:
            print("{0} - вероятно простое".format(n))
    return is_composite


def compare_system(m1, m2):
    """ Табличка систем сравнений."""
    i = 0
    j = 0
    print(end='a\\b\t')
    for i in range(m2):
        print(i, end='\t')
    print()
    for a in range(0, m1, 1):
        print(str(a), end='\t')
        for b in range(0, m2, 1):
            for t in range(0, m2):
                for l in range(0, m1):
                    x1 = a + t * m1
                    x2 = b + l * m2
                    if x1 == x2:
                        print(x1, end='\t')
        print()


def composite_mhp(a, k, m):
    """ Возведение в степень по модулю сильно составных чисел."""
    factors = factor(m)
    b = [c.mhp(a, k, i) for i in factors]
    res_ = []
    for n in factors:
        res = []
        for b_ in b:
            for t in range(m, step=1):
                res.append(b_ + t * n)
        res_.append(res)

    print(b)


def get_n_simple(n):
    """ Получить первые n простых чисел."""
    j = 0
    number = []
    for i in range(1, 100, 1):
        if not test_ferma(i) and j < n:
            j += 1
            number.append(i)
    return number


def cashiers(n, k):
    """ Задача о кассирах в банке."""
    n_ = n
    start = 0
    is_done = False
    nums = []
    prod_1 = 1
    prod_2 = 1
    while not is_done:
        nums = get_n_simple(n_)[start:n_]
        prod_1 = 1
        for i in range(0, k, 1):
            prod_1 *= nums[i]

        prod_2 = 1
        for i in range(n - k + 1, n, 1):
            prod_2 *= nums[i]
        if prod_2 > prod_1:
            n_ += 1
            start += 1
        else:
            is_done = True
    s = rand.randint(prod_2, prod_1)
    print("s = {0}".format(s))
    for i in nums:
        print("({0}, {1})".format(i, s % i), end='\t')

#compare_system(5, 4)

#composite_mhp(2, 6754, 1155)
cashiers(5, 2)
#print(get_n_simple(11)[5:11])