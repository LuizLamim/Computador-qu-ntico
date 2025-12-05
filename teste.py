s = input ("enter: ")

try:
    i = int(s)
    print("validar:", i)
except ValueError as err:
    print(err)