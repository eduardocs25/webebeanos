from __future__ import  absolute_import, unicode_literals
from zen import router
from web.curso.rest import Curso
__author__ = 'eduardo'
#crud = create read update delete

def index(_write_tmpl):
    query = Curso.query().order(Curso.nome)
    dct = {'lista_cursos':query.fetch()}
    _write_tmpl('/templates/curso_listar.html', dct)

#con esto se calcula la url
def form(_write_tmpl):
    path = router.to_path(salvar)
    #se crea un dicionario para conectar el html form con esto
    dct = {'salvar_curso':path}
    _write_tmpl('/templates/curso_form.html', dct)

def salvar(_handler, nome, preco):
    preco = float(preco)
    curso = Curso(nome = nome, preco = preco)
    curso.put()
    path = router.to_path(index)
    _handler.redirect(path)