import time

print("Running Example Project...")


def gen_randint():
    # Microservice will generate random integer between 0-100 and store it in the randint-service text file
    # You can also send other data within the text file if you wish
    f = open("randint-service.txt", "w")
    f.write("run")
    print("Random number generated and stored in communication pipeline.")
    time.sleep(5)
    f.close()


def get_randint():
    # Example.py will receive data from communication pipeline and store it in rand_num variable
    time.sleep(5)
    f = open("randint-service.txt", "r")
    rand_num = f.read()
    print("Random Number Generated: " + rand_num)
    f.close()
    return rand_num


while True:
    # Prompts user to generate or receive random generated number, this is optional.
    user_input = input("Type 1 to generate random integer or 2 to receive generated integer: ")
    if user_input == "1":
        gen_randint()

    elif user_input == "2":
        get_randint()

    else:
        print("unknown option")