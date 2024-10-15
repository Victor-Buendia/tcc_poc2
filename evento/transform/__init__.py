import os
import json
import datetime

from libs import *

curated_path = os.environ.get('CURATED_PATH')

def calculate_age(birth_date):
    return (datetime.datetime.now() - datetime.datetime.strptime(birth_date, "%Y-%m-%d")).days // 365

def transform_pessoas(dir_name: str, file_path: str, thread_id: int) -> None:
    with open(file_path, 'r') as file:
        data = json.load(file)
        transformed_data = [
            {
                'id_pessoa': record['id_pessoa'],
                'nome': record['nome'],
                'cpf': record['cpf'],
                # 'cpf': '*'*len(record['cpf'][:4]) + record['cpf'][4:-3] + '*'*len(record['cpf'][-3:]),
                'data_nascimento': record['data_nascimento'],
                'idade': calculate_age(record['data_nascimento']),
                'genero': record['genero'],
                'telefone': record['telefone'],
                # 'telefone': '*'*(len(record['telefone'])-4) + str(record['telefone'][-4:]),
                'email': record['email'],
                # 'email': '*'*(len(record['email'])-4) + record['email'].split('@')[0][-4:] + '@' + record['email'].split('@')[-1],
                'senha': hash_text(record['senha']),
                'cartao': {
                    # 'numero': '*'*(len(record['cartao']['numero'])-4) + str(record['cartao']['numero'][-4:]),
                    'numero': record['cartao']['numero'],
                    'nome': record['cartao']['nome'],
                    'bandeira': record['cartao']['bandeira'],
                    'validade': record['cartao']['validade'],
                    'cvv': record['cartao']['cvv'],
                    # 'cvv': '*'*len(record['cartao']['cvv']),
                } if record['cartao'] else None,
            } for record in data
        ]
    with open(curated_path.format(dir_name, dir_name, thread_id), 'w') as file:
        file.write(json.dumps(transformed_data, indent=4))
        
def no_transform(dir_name: str, file_path: str, thread_id: int) -> None:
    with open(file_path, 'r') as file:
        data = json.load(file)
        transformed_data = [record for record in data]
    with open(curated_path.format(dir_name, dir_name[:-1], thread_id), 'w') as file:
        file.write(json.dumps(transformed_data, indent=4))

transformation_mapping = {
    'empresas': no_transform,
    'eventos': no_transform,
    'pessoas': transform_pessoas,
    'inscricaos': no_transform,
}