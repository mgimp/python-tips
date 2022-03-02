import interactive_module as im

def main():
    print("main() is running\n")
    you = input("What is your name?\n")
    im.hello(you)
    im.goodbye(you)

if __name__ == '__main__':
    main()