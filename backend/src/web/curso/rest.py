#coding uft-8 -*-
from __future__ import  absolute_import, unicode_literals
import json
from google.appengine.ext import ndb

__author__ = 'eduardo'

#aqui se crea la base de datos y se manipula para que los ordene alfabeticamente
class Curso(ndb.Model):
    nome = ndb.StringProperty()
    preco = ndb.FloatProperty()

def salvar(nome,preco):
    preco = float(preco)
    curso = Curso(nome = nome, preco = preco)
    curso.put()

def listar(_resp):
    query = Curso.query().order(Curso.nome)

    #esto es para poder ordenar y conservar el key
    def to_dict(c):
        dct=c.to_dict()
        dct['id']=str(c.key.id())
        return dct

#   lista_de_cursos = query.fetch()  aqui lo hacemos diccionario
    lista_de_cursos = [to_dict(c) for c in query.fetch()]
    lista_de_cursos = json.dumps(lista_de_cursos)
    _resp.write(lista_de_cursos)