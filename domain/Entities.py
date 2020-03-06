

class Jucator(object):
    
    def __init__(self, nume, prenume, inaltime, post):
        '''
        creeaza un obiect de tipul Jucator
        datele introduse: nume, prenume, inaltime, post
        post-conditii: numele si prenumele stringuri nevide, inaltimea numar intreg strict pozitiv
        post trebuie sa fie unul dintre 'fundas','extrema','pivot'
        '''
        self.__nume = nume
        self.__prenume = prenume
        self.__inaltime = inaltime
        self.__post = post

    def __str__(self):
        return self.get_nume()+" "+self.get_prenume()+" "+str(self.get_inaltime())+" "+self.get_post()


    def __eq__(self, value):
        return self.get_nume()==value.get_nume() and self.get_prenume()==value.get_prenume()


    def get_nume(self):
        return self.__nume


    def get_prenume(self):
        return self.__prenume


    def get_inaltime(self):
        return self.__inaltime


    def get_post(self):
        return self.__post


    def set_inaltime(self, value):
        self.__inaltime = value

    nume = property(get_nume, None, None, None)
    prenume = property(get_prenume, None, None, None)
    inaltime = property(get_inaltime, set_inaltime, None, None)
    post = property(get_post, None, None, None)
    
def testJucator():
    '''
    testeaza crearea de obicete de tip Jucator
    '''
    jucator=Jucator("Mihali", "teodora", 172, 'extrema')
    assert jucator.get_inaltime()==172
    assert jucator.get_prenume()=="teodora"
    assert jucator.get_nume()=="Mihali"
    assert jucator.get_post()=='extrema' 
    jucator.set_inaltime(162)
    assert jucator.get_inaltime()==162  
    jucator1=Jucator("Mihali", "teodora", 172, 'extrema')
    assert jucator==jucator1
 
    
testJucator()



