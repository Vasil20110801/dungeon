from colorama import Fore
from time import sleep
from Prison_cell import  room1


def situation_01():
    sleep(3)
    print(f"{Fore.YELLOW}Събуждаш се в тъмнина. Мирише на влага, метал и кръв. Чува се капене на вода и далечен метален шум, сякаш верига се влачи по камъка. Главата ти бучи. Не помниш нищо – нито как се озова тук, нито кой си.")
    sleep(10)
    print(f"{Fore.YELLOW}Единственото, което усещаш, е студеният каменен под под себе си… и слаб полъх, който идва от някъде вляво.")
    sleep(3)
    print(f"{Fore.YELLOW}Мисълта ти е ясна – трябва да избягаш.")
    room1()
situation_01()