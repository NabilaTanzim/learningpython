fact = lambda f: 1 if f<= 1 else f * fact(f-1)
print(fact(5))