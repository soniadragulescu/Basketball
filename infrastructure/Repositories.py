from domain.Entities import Jucator


class RepoError(Exception):
    pass

class FileRepo(object):
    
    def __init__(self, filename):
        ''' filename - string ce reprezinta numele fisierului
        '''
        self.__filename = filename
#         self.__loadFromFile()
        
    def __loadFromFile(self):
        '''
        returneaza lista cu toti jucatorii din fisier
        arunca IO Error daca nu s-a putut deschide fisierul
        '''
        try:
            f=open(self.__filename, 'r')
        except IOError:
            print("Nu s-a putut deschide fisierul")
            return
        jucatori=[] 
        for line in f:
            if line.strip()=="":
                continue
            jucator=self.__createJucatorFromLine(line)
            jucatori.append(jucator)
            
        f.close()
        return jucatori
    
    def __createJucatorFromLine(self, line):
        '''creeaza un obiect de tip Jucator din linia line si il returneaza
        '''
        params=line.split(" ")
        jucator=Jucator(params[0].strip(),params[1].strip(), int(params[2].strip()),params[3].strip())
        return jucator
    
    def __storeToFile(self, jucatori):
        '''
        toata lista de jucatori in fisierul cu numele filename
        '''
        f=open(self.__filename, 'w')
        for jucator in jucatori:
            line=jucator.get_nume()+" "+jucator.get_prenume()+" "+str(jucator.get_inaltime())+" "+jucator.get_post()+"\n"
            f.write(line)
            
        f.close()
        
    def adauga(self, jucator):
        ''' adauga un obiect de tip jucator la lista cu toti jucatorii
            arunca RepoError daca acesta se afla deja in lista
            '''
        jucatori=self.__loadFromFile()
        if jucator in jucatori:
            raise RepoError("Jucator existent!")
        jucatori.append(jucator)
        self.__storeToFile(jucatori)
        
    def update(self, nume,prenume, inaltime):
        '''updateaza inaltimea jucatorului cu numele si prenumele dat cu inaltimea data ca si parametru
        arunca RepoError jucatorul nu exitsa
        postcond: inaltimea nr nat strict pozitiv
        '''
        jucatori=self.__loadFromFile()
        jucator=Jucator(nume, prenume, 0, 'pivot')
        if jucator not in jucatori:
            raise RepoError("Jucator inexistent!")
        for i in jucatori:
            if i==jucator:
                i.set_inaltime(inaltime)
#                 self.__storeToFile(jucatori)
                
        self.__storeToFile(jucatori)
#         raise RepoError("Jucator inexistent!")
    
    def getAll(self):
        '''returneaza o lista cu toti jucatorii din fisier
        '''
        return self.__loadFromFile()
        
def testRepoFile():
    '''
    testeaza functiile din clasa FileRepo
    '''    
    filename="test.txt"
    file=open(filename,'w') #face fisierul gol
    fileRepo=FileRepo(filename)
    assert len(fileRepo.getAll())==0
    
    jucator=Jucator("Teo","Mihali", 172,"extrema")
    fileRepo.adauga(jucator)
    assert len(fileRepo.getAll())==1
    file.close()
    
testRepoFile()
            
            


