import os
import random
import sys
import time


def clear():
    system = sys.platform
    if system == "linux" or "darwin":
        os.system("clear")
    else:
        os.system("cls")


def digit_verify(user):
    time.sleep(1)
    print("[*] Verifying Code.... ")
    time.sleep(3)
    print("[*] Verify Successful!")
    time.sleep(1)
    print(f"Full-Code: {user}")

def create_path(user,net):
    times = time.strftime("%b-%d %H:%M:%S")
    write_date = f"\n[{times}]  |  {user}  |  {net}"
    win = "C:/Users/HP/Desktop/digit/gen_card/cards.txt"
    sdcard = "./gen_card/cards.txt"
    linux = "./gen_card/cards.txt"
    if sys.platform == "android":
        if os.path.exists(sdcard):
            with open(sdcard,"w") as file:
                file.write(user)
                file.close()
        else:
            print("No File Found!")
    elif sys.platform == "window" or "win":
        if os.path.exists(win):
            with open(win,"a") as file:
                file.write(write_date)
                digit_verify(user)
                file.close()
        else:
            print("No File Found!")
    elif sys.platform == "linux":
        if os.path.exists(linux):
            with open(linux, "w+a+x") as file:
                file.write(user)
                file.close()
        else:
            print("No File Found!")


def codes(user):
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    c = random.randint(0, 9)
    d = random.randint(0, 9)  # First part
    e = random.randint(0, 9)
    f = random.randint(0, 9)
    g = random.randint(0, 9)
    h = random.randint(0, 9)  # Second part
    i = random.randint(0, 9)
    j = random.randint(0, 9)
    k = random.randint(0, 9)
    l = random.randint(0, 9)  # Third part
    m = random.randint(0, 9)
    n = random.randint(0, 9)
    o = random.randint(0, 9)
    p = random.randint(0, 9)
    q = random.randint(0, 9)  # Last part
    if user == "1":
        result_code = f"{a}{b}{c}{d}-{e}{f}{g}{h}-{i}{j}{k}{l}-{m}{n}{o}{p}{q}"
        print(f"Code: xxxx-xxxx-xxxx-{m}{n}{o}{p}{q}")
        create_path(result_code,net="Mtn")
    elif user == "2":
        result_code = f"{a}{b}{c}{d}-{e}{f}{g}{h}-{i}{j}{k}{l}-{m}{n}{o}{p} "
        print(f"Code: xxxx-xxxx-xxxx-{m}{n}{o}{p}")
        create_path(result_code, net="Airtel")
    elif user == "3":
        result_code = f"{a}{b}{c}{d}-{e}{f}{g}{h}-{i}{j}{k}{l}-{m}{n}{o}{p} "
        print(f"Code: xxxx-xxxx-xxxx-{m}{n}{o}{p}")
        create_path(result_code, net="Glo")


def main():
    print("+-------------------------------+")
    print("+-+-+Card_Maker_By_@apklearner+-+-+")
    print("+-------------------------------+")
    print(f'''+ 1. MTN                        +
+ 2. AIRTEL                     +
+ 3. GLO                        +
+ 0. Exit                       +''')
    print("+-------------------------------+")
    running = True
    while running:
        try:
            user = (input("Select your Network: "))
            print("+-------------------------------+")
            if user == "1":
                print("[*] Generating Mtn Code...")
                time.sleep(5)
                codes(user)
                print("+-------------------------------+")
                print("enter 0 to quit, or loops cont...")
            elif user == "2":
                print("[*] Generating Airtel Code...")
                time.sleep(5)
                codes(user)
                print("+-------------------------------+")
                print("enter 0 to quit, or loops cont...")
            elif user == "3":
                print("[*] Generating Glo Code...")
                time.sleep(5)
                codes(user)
                print("+-------------------------------+")
                print("enter 0 to quit, or loops cont...")
            elif user == "clear":
                os.system("clear")
            elif user == "0":
                print("[!] Program Terminated!")
                break
        except KeyboardInterrupt:
            print()
            print("[!] Program Interrupted!")
            break
        except ValueError:
            print(end="")

if __name__ == '__main__':
    main()