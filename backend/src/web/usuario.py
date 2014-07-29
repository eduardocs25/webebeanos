#coding uft-8 -*-
from __future__ import  absolute_import, unicode_literals
from zen import router
__author__ = 'eduardo'


def index(_handler):
    path=router.to_path(form,"gerardo","castro")
    _handler.redirect(path)

def form(_resp, nome,sobrenome):
    _resp.write("Hola %s %s" %(nome,sobrenome))