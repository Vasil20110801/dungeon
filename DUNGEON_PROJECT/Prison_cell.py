from colorama import Fore
from time import sleep
import mydata
from Dog_room_crossroads import room2
inventory = []
def room1 ():
    key = False
    look_at_the_bench = True
    look_at_the_crack = True
    Call_for_help = True
    Open_the_door = True
    Look_the_inscription = True
    sleep(1)
    print(f"{Fore.MAGENTA}Стаята в която си  е малка, с каменни стени и ръждиви железни решетки. ")
    sleep(3)
    print(f"{Fore.MAGENTA}По стената има надраскан с нокти надпис: „Доверието убива“. ")
    sleep(3)
    print(f"{Fore.MAGENTA}Има счупена пейка, железни вериги и тъмна пукнатина в стената.")
    sleep(3)
    print(f"{Fore.MAGENTA}Срещу теб има стара изгнила врата,  която води някаде")
    sleep(3)
    while True:
        sleep(1)
        print(f"{Fore.LIGHTYELLOW_EX}Възможни действия")
        if look_at_the_bench:
            sleep(1)
            print(f"{Fore.GREEN}(1) == Огледай пейката")
        if look_at_the_crack:
            sleep(1)
            print(f"{Fore.GREEN}(2) == Провери пукнатината")
        if Call_for_help:
            sleep(1)
            print(f"{Fore.GREEN}(3) == Извикай за помощ")
        if Open_the_door:
            sleep(1)
            print(f"{Fore.GREEN}(4) == Опитай да отвориш вратата")
        if Look_the_inscription:
            sleep(1)
            print(f"{Fore.GREEN}(5) == Огледай надписа")
        sleep(1)
        player_input = input(f"{Fore.BLUE}Въведете вашият избор: ")
        if player_input == "1":
            sleep(1)
            print(f"{Fore.YELLOW}Намираш счупено парче желязо – можеш да го използваш като лост или оръжие.")
            piece_of_iron = "Счупено парче желязо"
            inventory.append(piece_of_iron)
            look_at_the_bench = False
            sleep(1)
            n = input(f"{Fore.BLUE}Напиши (y) когато искаш да продължиш:")
            if n == "y":
                continue
            else:
                sleep(1)
                print(f"{Fore.RED}Невалиден избор")

        if player_input == "2":
            sleep(1)
            print(f"{Fore.YELLOW}Виждаш малка змия която скача и те ухапва/ - 20 кръв")
            mydata.health -= 20
            look_at_the_crack = False
            sleep(1)
            n = input(f"{Fore.BLUE}Напиши (y) когато искаш да продължиш:")
            if n == "y":
                continue
            else:
                print(f"{Fore.RED}Невалиден избор")
        if player_input == "3":
            sleep(1)
            print(f"{Fore.YELLOW}Никой не отговаря , но чуваш някакво движение от другата стая")
            Call_for_help = False
        if player_input == "4":
            if  key == False :
                sleep(1)
                print(f"Нямаш ключ")
                sleep(1)
                n = input(f"{Fore.BLUE}Напиши (y) когато искаш да продължиш:")
                if n == "y":
                    continue
                else:
                    sleep(1)
                    print(f"{Fore.RED}Невалиден избор")
            if key :
                sleep(1)
                key = False
                Open_the_door = False
                sleep(1)
                room2()
                break

        if player_input == "5":
            sleep(1)
            print(f"{Fore.YELLOW}Намираш някакъв предмет зад надписът ,взимаш го и се оказва че си намери някакъв ключ")
            key = True
            Look_the_inscription = False
            sleep(1)
            n = input(f"{Fore.BLUE}Напиши (y) когато искаш да продължиш:")
            if n == "y":
                continue
            else:
                sleep(1)
                print(f"{Fore.RED}Невалиден избор")



room1()


