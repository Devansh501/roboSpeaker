import os

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.0")
    print('Choose your os')
    osC = input("1.Mac 2.Linux\n")
    if osC != str(1) and osC != str(2):
        exit("Os not supported!")

    while True:
        x = input("Enter text input or ! to quit\n")
        if x == '!':
            print("Bye Bye :)")
            break
        else:
            command = "say " + x
            if osC==str(2):
                command = f"spd-say \"{x}\""
            os.system(command)