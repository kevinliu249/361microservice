# 361microservice
# Clear instructions for how to programmatically REQUEST data from the microservice you implemented. Include an example call.
To request data from the random number generator microservice, you may implement a gen_randint() function.  
Once the function is called, a command will be written to the text file,  
the microservice that receives the command will generate and store a randomly generated number in the text file communication pipeline.  
  
example call:
> def gen_randint():  
>> f = open("randint-service.txt", "w")  
>> f.write("run")  
>> print("Random number generated and stored in communication pipeline.")  
>> time.sleep(5)  
>> f.close()  
  
# Clear instructions for how to programmatically RECEIVE data from the microservice you implemented.

def get_randint():
    # Example.py will receive data from communication pipeline and store it in rand_num variable
    time.sleep(5)
    f = open("randint-service.txt", "r")
    rand_num = f.read()
    print("Random Number Generated: " + rand_num)
    f.close()
# UML sequence diagram showing how requesting and receiving data works. Make it detailed enough that your partner (and your grader) will understand
