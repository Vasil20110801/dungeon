from colorama import Fore
from time import sleep
import mydata
from mydata import health


def room3():
    print("Поемаш на някаде и стигаш до една стая в която е студено,мрачно, влажно,мирише лошо .")
    print('На земята пред теб има стар метален съндък, а на стената  има надпис" Не вярвай на сянката"')
    print("В дъното на стаята има врата")
    print("Възможни действия")
    chest = True
    inscription = True
    door = True
    key2 = False
    while True:
        print(f"{Fore.LIGHTYELLOW_EX}Възможни действия :")
        if chest:
            sleep(1)
            print(f"{Fore.GREEN}(1) == Ще се доближа и ще се опитам да отворя съндъка")
        if inscription:
            sleep(1)
            print(f"{Fore.GREEN}(2) == Ще отида да проверя надписа")
        if door:
            sleep(1)
            print(f"{Fore.GREEN}(3) == Ще се опитам да отворя вратата")

        sleep(1)
        player_input = input(f"{Fore.BLUE}Въведете вашият избор: ")
        if player_input == "1":
            sleep(1)
            print(f"{Fore.YELLOW}Намираш злато и  ключ в него")
            key2 = True
            sleep(1)
            chest = False
            n = input(f"{Fore.BLUE}Напиши (y) когато искаш да продължиш:")
            if n == "y":
                continue
            else:
                sleep(1)
                print(f"{Fore.RED}Невалиден избор")
        elif player_input == "2":
            sleep(1)
            print(f"{Fore.YELLOW}Проверяваш надписа  но там се раняваш /-20 hp")
            mydata.health -= 20
            sleep(1)
            inscription = False
            n = input(f"{Fore.BLUE}Напиши (y) когато искаш да продължиш:")
            if n == "y":
                continue
            else:
                sleep(1)
                print(f"{Fore.RED}Невалиден избор")
        elif player_input == "3":
            sleep(1)
            if key2 :
                sleep(1)
            print(f"{Fore.YELLOW}Излизаш от тъмното и миризливо подземие и се намираш точно под старата къща на дядо Гошо ,който е починал преди 5 години")
            print(f"{Fore.RED}КРАЙ НА 1-ВА ЧАСТ")
