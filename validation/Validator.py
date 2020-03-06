from domain.Entities import Jucator


class ValidError(Exception):
    def __init__(self,errors):
        
        self.__errors = errors

    def get_errors(self):
        return self.__errors

    errors = property(get_errors, None, None, None)
        

class ValidJucator(object):
    
    def __init__(self):
        pass
    
    def valideazaJucator(self, jucator):
        '''
        Arunca exceptii daca numele sau prenumele sunt stringuri vide, daca postul este string vid sau nu este unul dintre
        posturile de 'fundas', 'extrema' sau pivot sau daca inaltimea nu este un nr intreg strict pozitiv
        '''
        errors=[]
        if jucator.get_prenume()=='':
            errors.append("Prenume invalid!")
        if jucator.get_nume()=='':
            errors.append("Nume invalid!")
        if jucator.get_post()=='' or jucator.get_post() not in ['fundas','extrema', 'pivot']:
            errors.append("Post invalid!")
        if jucator.get_inaltime()<=0:
            errors.append("Inaltime invalida!")
            
        if len(errors)>0:
            raise ValidError(errors)
        
def testValid():
    validator=ValidJucator()
    jucator=Jucator('','',0,'asd')
    
    try:
        validator.valideazaJucator(jucator)
        assert False
    except ValidError as msg:
        assert len(msg.get_errors())==4
        
    jucator2=Jucator('Teo','Mihali',-3,'')
    
    try:
        validator.valideazaJucator(jucator2)
        assert False
    except ValidError as msg:
        assert len(msg.get_errors())==2
        
testValid()
    

