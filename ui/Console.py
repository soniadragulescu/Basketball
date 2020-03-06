from business.Service import Service
from validation.Validator import ValidError
from infrastructure.Repositories import RepoError

class Console(object):
    
    def __init__(self, servJucator):
        self.__servJucator = servJucator
        self.__commands={"1":self.__uiAdaugaJucator,
                         "2":self.__uiPrint,
                         "3":self.__uiActualizeaza,
                         "4":self.__uiEchipa,
                         "5":self.__uiImporta
                         }
    
    def run(self):
        meniu="1Adauga\n2Vizualizeaza\n3Actualizeaza\n4Echipa\n5Importa\nExit"
        
        while True:
            print(meniu)
            comanda=input("Comanda:")
            cmds=comanda.split(" ")
            if cmds=="Exit":
                return
            elif cmds[0] in self.__commands:
                try:
                    self.__commands[cmds[0]](cmds[1:])
                except ValueError:
                    print("Valoare invalida!")
                except RepoError as re:
                    print(re)
                except ValidError as ve:
                    print(ve)
                
            else:
                print("Comanda invalida!")

    def __uiAdaugaJucator(self,cmds):
        if len(cmds)!=4:
            print("Numar invalid de parametrii!")
            return
        nume=cmds[0].strip()
        prenume=cmds[1].strip()
        post=cmds[3].strip()
        inaltime=int(cmds[2].strip())
#         prenume=input("prenume:")
#         nume=input("nume:")
#         post=input("post:")
#         inaltime=int(input("inaltime:"))
        self.__servJucator.adauga(nume, prenume,inaltime,post)
    
    def __uiPrint(self, cmds):
        if len(cmds)>0:
            print("Numar invalid de parametrii!")
            return
        else:
            jucatori=self.__servJucator.getAll()
            if len(jucatori)<1:
                print("Nu exista jucatori!")
            else:
                for jucator in jucatori:
                    print(jucator)
                    
            
    def __uiActualizeaza(self, cmds):
        if len(cmds)!=3:
            print("Numar invalid de parametrii!")
            return
        else:
            nume=str(cmds[0].strip())
            prenume=str(cmds[1].strip())
            inaltime=int(cmds[2].strip())
            self.__servJucator.update(nume,prenume, inaltime)
            
    def __uiEchipa(self, cmds):
        if len(cmds)>0:
            print("Numar invalid de parametrii!")
            return
        echipa=self.__servJucator.echipa()
        if echipa==[]:
            return
        print("Echipa:")
        for jucator in echipa:
            print(jucator)
            
    def __uiImporta(self, cmds):
        if len(cmds)!=1:
            print("Numar invalid de parametrii!")
            return
        filename=cmds[0].strip()
        print(filename)
        self.__servJucator.importa(filename)
