import random
def generate_list():
    alist= [x for x in range(random.randint(-10,10))]
    return alist
    
#print a generated list

def printIt()
    print(generate_list())

def main():
    printIt()
    
#If this script file is called, it will run main() directly

if __name__ == '__main__':
    print("Test printIT():")
    main()