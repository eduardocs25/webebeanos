from __future__ import  absolute_import, unicode_literals
from zen import router
__author__ = 'eduardo'
#crud = create read update delete

def index():
    pass

def form(_write_tmpl):
    path = router.to_path(salvar)
    dct = {'salvar_curso':path}
    _write_tmpl('/templates/curso_form.html', dct)

def salvar(nome,preco):
    preco = float(preco)
    curso = Curso(nome = nome, preco = preco)
    curso.put()