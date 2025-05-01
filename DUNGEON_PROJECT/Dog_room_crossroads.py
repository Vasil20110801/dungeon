from colorama import Fore
from time import sleep
import mydata
key1 = False
def room2 ():
    sleep(3)
    print(f"{Fore.YELLOW}Когато излизаш от килията, попадаш в тъмен коридор, който се разклонява на три посоки. ")
    sleep(3)
    print(f"{Fore.YELLOW}Стените са влажни и покрити с мъх, а въздухът е тежък и застоял.")
    sleep(3)
    print(f"{Fore.YELLOW} Докато се чудиш накъде да поемеш, до теб се чува слабо ръмжене.")
    sleep(3)
    print(f"{Fore.MAGENTA}В ъгъла, полускрит зад счупена статуя, лежи голямо куче, вързано с ръждива верига за железен пръстен в стената. ")
    sleep(3)
    print(f"{Fore.MAGENTA}Очите му блестят в тъмното — наблюдава те внимателно.")
    sleep(3)
    print(f"{Fore.MAGENTA}В началото ръмжи, но не изглежда агресивно. ")
    sleep(3)
    print(f"{Fore.MAGENTA}По-скоро е уплашено.")
    sleep(3)
    print(f"{Fore.MAGENTA}Козината му е разчорлена, ребрата се виждат — очевидно не е хранено от дни.")
    sleep(3)
    attack = True
    ignore = True
    love = True
    while True:
        sleep(1)
        print(f"{Fore.LIGHTYELLOW_EX}Възможни действия :")
        if love :
            sleep(1)
            print(f"{Fore.GREEN}(1) == Ще се доближа и ще се опитам да погаля кучето")
        if ignore:
            sleep(1)
            print(f"{Fore.GREEN}(2) == Ще го подмина")
        if attack:
            sleep(1)
            print(f"{Fore.GREEN}(3) == Ще се опитам да го нападна")
        sleep(1)
        player_input = input(f"{Fore.BLUE}Въведете вашият избор: ")
        if player_input == "1":
            sleep(1)
            print(f"{Fore.YELLOW}Сприятеляваш се със кучето и намираш под него ключ")
            key1 = True
            sleep(1)
            love = False
            n = input(f"{Fore.BLUE}Напиши (y) когато искаш да продължиш:")
            if n == "y":
                continue
            else:
                sleep(1)
                print(f"{Fore.RED}Невалиден избор")
        elif player_input == "2":
            sleep(1)
            print(f"{Fore.YELLOW}Подминаваш го ,но ти става жал за него и се връщаш да провериш")
            sleep(1)
            ignore = False
            n = input(f"{Fore.BLUE}Напиши (y) когато искаш да продължиш:")
            if n == "y":
                continue
            else:
                sleep(1)
                print(f"{Fore.RED}Невалиден избор")
        elif player_input == "3":
            sleep(1)
            print(f"{Fore.YELLOW}Изваждаш желязото и се опитваш да го нападнеш ,но то те захапва първо по кръка  , и решаваш да спреш./ - 20 кръв")
            mydata.health -= 20
            sleep(1)
            attack = False
            n = input(f"{Fore.BLUE}Напиши (y) когато искаш да продължиш:")
            if n == "y":
                continue
            else:
                sleep(1)
                print(f"{Fore.RED}Невалиден избор")
