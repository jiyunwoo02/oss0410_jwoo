# get two integer parameters
# return sum
def plus(x, y):
    return x+y

def mul(x, y):
    return x*y

def sub(x, y):
    return x-y

def div(x, y):
    return x//y

# main function
def main():
    check = 1
    print("Welcome to calcuator")
    while check >= 1:        
        print("0: exit, 1: plus")
        check = int(input())
        if check == 1:
            print("First Number")
            x = int(input())
            print("Second Number")
            y = int(input())
            print("answer : ", plus(x,y))
            print("mul answer : ", mul(x,y))
            print("sub answer : ", sub(x,y))
            print("div answer : ", div(x,y))
        elif check > 1:
            print("Unsupported")
        else:
            print("Thank you")

if __name__ == "__main__":
    main()