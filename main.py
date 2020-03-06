'''
Created on 31 ian. 2019

@author: sonia
'''
from infrastructure.Repositories import FileRepo
from business.Service import Service
from validation.Validator import ValidJucator
from ui.Console import Console



repo=FileRepo("jucatori.txt")
valid=ValidJucator()
serv=Service(repo,valid)
c=Console(serv)
c.run()
