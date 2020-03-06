from infrastructure.Repositories import FileRepo, RepoError
from domain.Entities import Jucator
from validation.Validator import *
from lib2to3.tests.data.infinite_recursion import FILE
import random

class Service(object):
    
    def __init__(self, repo, valid):
        self.__repo = repo
        self.__valid=valid
        
    def adauga(self, nume, prenume,inaltime,post):
        jucator=Jucator(nume, prenume, inaltime, post)
        self.__valid.valideazaJucator(jucator)
        self.__repo.adauga(jucator)
        
    def update(self, nume, prenume, inaltime):
        ''' Jucatorul cu numele si prenumele date va avea inaltimea noua cea data.
        post cond: nume, prenume stringuri nevide
                    inaltimea nr intreg strict pozitiv
        '''
#         jucator=Jucator(nume,prenume,11,'extrema')
        if inaltime<=0:
            raise ValueError("Inaltimea trebuie sa fie nr strct pozitiv!")
        self.__repo.update(nume,prenume, inaltime)
        
    def getAll(self):
        '''
        returneaza o lista cu toti jucatorii
        '''
        return self.__repo.getAll()
    
    def echipa(self):
        ''' 
        returneaza o lista cu 5 jucatori, 2 fundasi, 1 pivot si 2 extreme
        care vor avea medie de inaltimea cea mai mare din toti jucatorii din fisier
        '''
        jucatori=self.__repo.getAll()
        fundasi=[]
        extreme=[]
        pivoti=[]
        for jucator in jucatori:
#             print(jucator)
            if jucator.get_post()=='fundas':
                fundasi.append(jucator)
            elif jucator.get_post()=='extrema':
                extreme.append(jucator)
            else:
                jucator.get_post()=='pivot'
                pivoti.append(jucator)
#         if len(fundasi)<2 or len(pivoti)<1 or len(extreme)<2:
#             print("Nu sunt destui jucatori pentru a forma o ehipa!")
#             return []
        fundasi.sort( key=lambda x:x.get_inaltime(), reverse=True)
        extreme.sort( key=lambda x:x.get_inaltime(), reverse=True)
        pivoti.sort( key=lambda x:x.get_inaltime(), reverse=True)
        echipa=[]
        echipa.append(fundasi[0])
        echipa.append(fundasi[1])
        echipa.append(pivoti[0])
        echipa.append(extreme[0])
        echipa.append(extreme[1])
        return echipa
    
    def importa(self, filename):
        
        try:
            f=open(filename,'r')
        except IOError:
            print("Nu s-a gasit fisierul!")
            return
        posturi=['extrema','fundas','pivot']
        jucatori2=self.__repo.getAll()
        jucatori=[]
        for line in f:
            if line.strip()=="":
                continue
            params=line.split(" ")
            nume=params[0].strip()
            prenume=params[1].strip()
            inaltime=random.randint(1,230)
            i=random.randint(0,2)
            post=posturi[i]
            jucator=Jucator(nume,prenume,inaltime,post)
            #(jucator)
            jucatori.append(jucator)
            
        f.close()
        for i in jucatori:
            if i not in jucatori2:
                self.__repo.adauga(i)
        
        
        
    
def testService():
    '''
    testeaza functiile din clasa Service
    '''
    valid=ValidJucator()
    repo=FileRepo("testServ.txt")
    file=open("testServ.txt",'w')
    file.close()
    serv=Service(repo, valid)
    
    try:
        serv.adauga('','',0,'asd')
        assert False
    except ValidError:
        assert True
        
    jucator1=Jucator('Mihali', 'Teo', 172, 'pivot')
    jucator2=Jucator('Alex','Pop',180,'extrema')
    jucator3=Jucator('Mihali', 'Teo', 172, 'pivot')
    
    assert len(serv.getAll())==0
    serv.adauga('Mihali', 'Teo', 172, 'pivot')
    assert len(serv.getAll())==1
    serv.adauga('Alex','Pop',180,'extrema')
    assert len(serv.getAll())==2
    try:
        serv.adauga('Mihali', 'Teo', 172, 'pivot')
        assert False
    except RepoError:
        assert True
#     serv.update("Mihali", "Teo", 160)
#     assert jucator1.get_inaltime()==160
    jucator4=Jucator('Navickas','Gediminas',190,'fundas')
    jucator5=Jucator('Nikolic','Niksa',192,'fundas')
    jucator6=Jucator('Dragusin','Ionut',220,'pivot')
    jucator7=Jucator('Graham','Paul',200,'extrema')
    jucator8=Jucator('Dumitrescu','Tudor',186,'extrema')
    serv.adauga('Navickas','Gediminas',190,'fundas')
    serv.adauga('Nikolic','Niksa',192,'fundas')
    serv.adauga('Dragusin','Ionut',220,'pivot')
    serv.adauga('Graham','Paul',200,'extrema')
    serv.adauga('Dumitrescu','Tudor',186,'extrema')
    echipa=[]
    echipa=serv.echipa()
    assert jucator4 in echipa
    assert jucator5 in echipa
    assert jucator6 in echipa
    assert jucator7 in echipa
    assert jucator8 in echipa
#     assert echipa==[jucator4,jucator5,jucator6,jucator7,jucator8]
#     print(echipa)
    f=open("testImporta.txt",'w')
    #repo2=FileRepo("testImporta.txt")
    line="ala bala\n"
    f.write(line)
    f.close()
    serv.importa("testImporta.txt")
    assert len(serv.getAll())==8
    
    
#     serv.importa("importa.txt")
testService()
    
    
    