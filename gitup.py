import os
import time


def up_git():
    header_banner()
    commit = str(input("Comente No Commit >"))
    addressrep = str(input("Insira a Url Do Repositório >"))
    header_banner()
    print(

                       'Fique Tranquilo Vamos Fazer Tudo Pra Você!'
    )
    time.sleep(3)
    os.system("git init")
    os.system("git add .")
    os.system('git commit -m "{}"'.format(commit))
    os.system("git branch -M main")
    os.system("git remote add origin {}".format(addressrep))
    os.system("git push -u origin main")
    header_banner()


def header_banner():
    print(

                      '''
                       ____ _ _   _   _       
                      / ___(_) |_| | | |_ __  
                     | |  _| | __| | | | '_ \ 
                     | |_| | | |_| |_| | |_) |
                      \____|_|\__|\___/| .__/ 
                                       |_|    
                            
                      '''
    )


up_git()

