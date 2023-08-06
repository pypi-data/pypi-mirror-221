def factorial(n):
    """
    实现斐波那契数列
    :param n:
    :return:
    """
    if n == 0 or n == 1:
        return 0
    else:
        return n * factorial(n - 1)
