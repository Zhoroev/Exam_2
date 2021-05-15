def func(*args):
    count = 0
    for i in args:
        try:
            count += i
        except:
            pass
    return count