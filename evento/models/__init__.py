import os

from models.BaseModel import BaseModel
from models.empresas.Empresa import Empresa
from models.eventos.Evento import Evento
from models.pessoas.Pessoa import Pessoa
from models.inscricoes.Inscricao import Inscricao

models = [
    (
        Empresa, 
        int(os.environ.get('N_EMPRESAS'))//int(os.environ.get('PROCESSES_NO'))
    ), 
    (
        Evento,
        int(os.environ.get('N_EVENTOS'))//int(os.environ.get('PROCESSES_NO'))
    ),
    (
        Pessoa,
        int(os.environ.get('N_PESSOAS'))//int(os.environ.get('PROCESSES_NO'))
    ),
    (
        Inscricao,
        int(os.environ.get('N_INSCRICOES'))//int(os.environ.get('PROCESSES_NO'))
    )
]
