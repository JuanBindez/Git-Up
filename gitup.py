'''
MIT License

Copyright (c) 2022 Juan Carlos Bindez

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
Footer

'''


import os
import time


def up_git():
    header_banner()
    commit = str(input("Comente No Commit >"))
    addressrep = str(input("Insira a Url Do Repositório >"))
    os.system("clear")
    header_banner()
    print(

                       'Fique Tranquilo Vamos Fazer Tudo Pra Você!'
    )
    time.sleep(3)
    os.system("git init")
    os.system("git add .")
    os.system("git status")
    print(

                       'Aparentemente Tudo Ok , Caso Contrario Ctrl + C!'
        
    )
    time.sleep(4)
    os.system('git commit -m "{}"'.format(commit))
    os.system("git branch -M main")
    os.system("git remote add origin {}".format(addressrep))
    os.system("git push -u origin main")
    header_banner()
    print(

                       'Ok, Agora Verifique Se Seu Projeto Esta No Seu Repositório Do Github!'
    )


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

if __name__ == '__main__':
    up_git()

