#coding: UTF-8
from graphics import *
from time import *
from random import *
from math import *
from ctypes import *

Bibliotecac = CDLL("./Biblioteca.so")


def main():
    win = GraphWin("E-STUDY",1050,700)              #Cria a janela de login
    continuando = True
    winopen = True
    while continuando==True and winopen==True:
        req = win.checkKey()
        if req=="Escape":                           #Checando se a tecla Esc foi pressionada
            continuando = False 
                                     
        bemvindo = Text(Point(525,150),"OLÁ, BEM VINDO AO CHORIS!!!\n FAÇA O LOGIN, SE AINDA NÃO ESTIVER SE REGISTRE!!!")
        bemvindo.setSize(20)
        bemvindo.draw(win)
        logintx = Text(Point(435,300),"LOGIN:")
        logintx.setSize(12)
        logintx.draw(win)
        entradalogin = Entry(Point(545,300),15)
        entradalogin.draw(win)
        login = entradalogin.getText()
        senhatx = Text(Point(435,350),"SENHA:")
        senhatx.setSize(12)
        senhatx.draw(win)
        entradasenha = Entry(Point(545,350),15)
        entradasenha.draw(win)    
        senha = entradasenha.getText()
        registrotx = Text(Point(555,370),"REGISTRE-SE")
        registrotx.draw(win)
        continua = Text(Point(685,325),"CONTINUAR")
        continua.setSize(12)
        continua.draw(win)
        
        clique = win.getMouse()
        x = clique.getX()
        y = clique.getY()
             
        def conferindo(): 
            dados = open("dadosdeusuarios.txt","r")
            loginesenhaconf = (login+"\n",senha+"\n")
            conf = str(loginesenhaconf)
            confere= dados.readline()
            

            if conf in confere:        
                winopen = False
                    
            
            elif conf not in confere:
                invalidlogin = Text(Point(540,300),"Usuário ou senha inválidos, tente novamente :(")
                invalidlogin.setSize(12)
                invalidlogin.draw(win)
                
            dados.close()
        
        if x>510 and x<600 and y>360 and y<381:
            winopen = False
            win.close()
            janelaopen = True
            continuandoj = True
            janela = GraphWin("REGISTRE-SE",1050,700)
            while continuandoj==True and janelaopen==True:
                checkesc = janela.checkKey()
                if checkesc=="Escape":                           #Checando se a tecla Esc foi pressionada
                    continuandoj = False 
            
                registertxt = Text(Point(525,150),"REGISTRE-SE ABAIXO")
                registertxt.setSize(20)
                registertxt.draw(janela)    
                loginrtxt = Text(Point(400,300),"LOGIN DESEJADO:")
                loginrtxt.setSize(12)
                loginrtxt.draw(janela)
                entradaloginr = Entry(Point(545,300),15)
                entradaloginr.draw(janela)
                senhartx = Text(Point(400,350),"SENHA DESEJADA:")
                senhartx.setSize(12)
                senhartx.draw(janela)
                entradasenhar = Entry(Point(545,350),15)
                entradasenhar.draw(janela)

            
            
                confirma = Text(Point(685,330),"CONTINUAR")
                confirma.setSize(12)
                confirma.draw(janela)
                cliqueregistro = janela.getMouse()
                xr = cliqueregistro.getX()
                yr = cliqueregistro.getY()
            

                if xr>630 and xr<730 and yr>321 and yr<340:     #Verifica se deve registrar o novo login
                    loginr = entradaloginr.getText()
                    senhar = entradasenhar.getText()
                    loginesenhanovos = (loginr+"\n",senhar+"\n")
                    dados = open("dadosdeusuarios.txt", "r")
                    conferindologin = dados.readline()
                    loginconfere = str(loginr+"\n")

                    if loginr in conferindologin:
                        loginutilizado = Text(Point(510,380),"Este login já está em uso, tente novamente :(")
                        loginutilizado.setSize(12)
                        loginutilizado.draw(janela)

                        dados.close()
                    elif loginr not in conferindologin:
                        dados = open("dadosdeusuarios.txt", "a+")
                        dados.write(str(loginesenhanovos))
                        janelaopen = False
                        janela.close()
                        dados.close()
                        main()  
                elif checkesc=="Escape": 
                    janelaopen = False                         #Checando se a tecla Esc foi pressionada
                    continuandoj = False
                    janela.close()
    
        
              
        
        

                
        
                  
                
              
          

    
            
        
main()

