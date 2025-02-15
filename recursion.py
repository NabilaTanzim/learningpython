def fact(f):
    if f <= 1:
        return(1)
    else:
        s = f * fact(f - 1)
        return s
print(fact(122))