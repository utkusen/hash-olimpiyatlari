#Canli yayin sirasinda hashleri kirip istatistikleri hesaplamak icin kullanilan bir script.

import argparse
import subprocess
import os
from termcolor import colored
from shutil import copyfile
import xlsxwriter

os.system('color')


def action(target_file,user_file,hashcount):
    wordlist_path = "olimpiyatlisteler/"+user_file+"_wordlist.txt"
    rule_path = "olimpiyatlisteler/"+user_file+"_rule.txt"
    mask_path = "olimpiyatlisteler/"+user_file+"_mask.txt"
    print(colored('__________________________________________', 'red'))
    print(colored('PAROLA LİSTESİ'))
    print(colored('__________________________________________', 'red'))
    with open(wordlist_path,"r") as wordlist:
        for line in wordlist:
            print(line.replace("\n",""))
    print(colored('__________________________________________', 'red'))
    print(colored('KURAL LİSTESİ'))
    print(colored('__________________________________________', 'red'))
    with open(rule_path,"r") as kurallar:
        for line in kurallar:
            print(line.replace("\n",""))
    print(colored('__________________________________________', 'red'))
    print(colored('MASK LİSTESİ'))
    print(colored('__________________________________________', 'red'))
    with open(mask_path,"r") as kurallar:
        for line in kurallar:
            print(line.replace("\n",""))
    print("")
    input("Bekliyor...")
    copy_file = target_file+".bak"
    copyfile(target_file, copy_file)
    subprocess.call(["hashcat.exe", copy_file, wordlist_path, "-r", rule_path, "--remove"])
    subprocess.call(["hashcat.exe", copy_file, "-a","3",mask_path, "--remove", "-o" "cikti2.txt"])
    total_count = 0
    with open(copy_file,"r") as leftfile:
        left_count = 0
        for line in leftfile:
            left_count += 1

    with open("hashcat.potfile","r") as potfile:
        unique_count = 0
        for line in potfile:
            unique_count += 1

    total_count = hashcount - left_count
    percentage = (total_count*100)/hashcount
    print(colored('__________________________________________', 'red'))
    print(colored('Toplam Kırılan:'+str(total_count), 'cyan'))
    print(colored('__________________________________________', 'red'))
    print(colored('Toplam Unique:'+str(unique_count), 'cyan'))
    print(colored('__________________________________________', 'red'))
    print(colored('Kırılan Yüzdesi:'+str("%.3f" % percentage), 'cyan'))
    print(colored('__________________________________________', 'red'))
    #print_red_on_cyan('Hello, World!')
    os.remove("hashcat.potfile")
    os.remove(copy_file)
    #os.remove("cikti1.txt")
    os.remove("cikti2.txt")

    


parser = argparse.ArgumentParser()
parser.add_argument('-u', action='store', dest='user_file', help='user_file', required=True)
argv = parser.parse_args()

action("veritabaniadi.txt",argv.user_file,573654)
