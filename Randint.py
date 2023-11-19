import time
import random

print("Running Randint Service..")
while True:
    time.sleep(1)
    f = open("randint-service.txt", "r")
    command = f.read()
    if command == "run":
        time.sleep(3)
        randint = random.randint(1, 100)
        f = open("randint-service.txt", "w")
        f.write(str(randint))
        f.close()