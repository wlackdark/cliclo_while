print("Escriba un programa que cuente del numero 1000 al cero")
import time

i = 1000

while i >= 0:
    print(i)
    i -= 1
    time.sleep(0.001)