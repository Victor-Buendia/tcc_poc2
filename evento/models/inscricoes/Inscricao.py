from models.BaseModel import *
from . import *

class Inscricao(BaseModel):
    def __init__(self, **kwargs):
        nro_eventos = list(range(1, int(os.environ.get('N_EVENTOS'))))
        nro_pessoas = list(range(1, int(os.environ.get('N_PESSOAS'))))

        id_inscricao        = 1 # Se generará com SQL usando ROW_NUMBER()
        id_evento           = int(fake.random_element(elements=nro_eventos))
        id_pessoa           = int(fake.random_element(elements=nro_pessoas))
        preco               = fake.random_int(min=0, max=1200)
        data_compra         = fake.date_this_year().isoformat()
        tipo_ingresso       = fake.random_element(elements=('Pista', 'Camarote', 'VIP', 'Meet & Greet', 'Backstage', 'Outro'))
        forma_pagamento     = fake.random_element(elements=('Crédito', 'Débito', 'PIX', 'Boleto', 'Transferência', 'Dinheiro'))
        pagina_web          = fake.url()

        kwargs.setdefault('id_inscricao',                   id_inscricao)
        kwargs.setdefault('id_evento',                      id_evento)
        kwargs.setdefault('id_pessoa',                      id_pessoa)
        kwargs.setdefault('preco',                          preco)
        kwargs.setdefault('data_compra',                    data_compra)
        kwargs.setdefault('tipo_ingresso',                  tipo_ingresso)
        kwargs.setdefault('forma_pagamento',                forma_pagamento)
        kwargs.setdefault('pagina_web',                     pagina_web)

        super().__init__(**kwargs)
