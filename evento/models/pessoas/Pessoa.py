from models.BaseModel import *
from . import *

class Pessoa(BaseModel):
    def __init__(self, **kwargs):
        nro_pessoas = list(range(1, int(os.environ.get('N_PESSOAS'))))

        id_pessoa       = 1 # Se generará com SQL usando ROW_NUMBER()
        nome            = fake.name()
        cpf             = fake.cpf()
        data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=60).isoformat()
        genero          = fake.random_element(elements=('Masculino', 'Feminino', 'Outro'))
        telefone        = fake.cellphone_number()
        while regex.match(pattern=r'^.\d{2} \(\d{2}\) \d{5}-\d{4}$', string=telefone) == None:
            telefone    = fake.cellphone_number()
        email           = regex.sub(pattern=r'@example\....', repl=fake.random_element(elements=['@gmail.com', '@hotmail.com', '@yahoo.com', '@outlook.com']), string=fake.ascii_safe_email())
        cartao          = {
            'numero'    : fake.credit_card_number(card_type=None),
            'nome'      : fake.name() if random.random() < 0.2 else nome,
            'bandeira'  : fake.credit_card_provider(card_type=None),
            'validade'  : fake.credit_card_expire(),
            'cvv'       : fake.credit_card_security_code(card_type=None)
        } if random.random() < 0.7 else None
        senha           = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)

        kwargs.setdefault('id_pessoa',                  id_pessoa)
        kwargs.setdefault('nome',                       nome)
        kwargs.setdefault('cpf',                        cpf)
        kwargs.setdefault('data_nascimento',            data_nascimento)
        kwargs.setdefault('genero',                     genero)
        kwargs.setdefault('telefone',                   telefone)
        kwargs.setdefault('email',                      email)
        kwargs.setdefault('senha',                      senha)
        kwargs.setdefault('cartao',                     cartao)

        super().__init__(**kwargs)
