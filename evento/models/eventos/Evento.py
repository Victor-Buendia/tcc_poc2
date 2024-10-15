from datetime import datetime
from models.BaseModel import *
from . import *

class Evento(BaseModel):
    def __init__(self, **kwargs):
        nro_empresas    = list(range(1, int(os.environ.get('N_EMPRESAS'))))

        id_evento       = 1 # Se generará com SQL usando ROW_NUMBER()
        id_empresa      = int(fake.random_element(elements=nro_empresas))
        titulo          = fake.random_element(elements=event_titles)
        tipo            = fake.random_element(elements=['Festa', 'Show', 'Cultura', 'Cinema', 'Educação', 'Esporte', 'Negócios', 'Tecnologia', 'Saúde', 'Moda', 'Gastronomia', 'Arte', 'Dança', 'Teatro', 'Literatura', 'Outro'])
        modalidade      = fake.random_element(elements=['Online', 'Presencial'])
        lotacao         = fake.random_int(min=1, max=10000)
        localizacao     = fake.estado()
        data_evento     = fake.date_this_year().isoformat()

        kwargs.setdefault('id_evento',      id_evento)
        kwargs.setdefault('id_empresa',     id_empresa)
        kwargs.setdefault('titulo',         titulo)
        kwargs.setdefault('tipo',           tipo)
        kwargs.setdefault('lotacao',        lotacao)
        kwargs.setdefault('modalidade',     modalidade)
        kwargs.setdefault('localizacao',    localizacao)
        kwargs.setdefault('data_evento',    data_evento)
        
        super().__init__(**kwargs)