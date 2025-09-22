
import json
import os
from organizador import Organizador
from evento import Evento 

class Database:
    def __init__(self, db_org_file='organizadores.json', db_evt_file='eventos.json'):
        self.db_org_file = db_org_file
        self.db_evt_file = db_evt_file
        
        if not os.path.exists(self.db_org_file):
            with open(self.db_org_file, 'w') as f:
                json.dump([], f)
        if not os.path.exists(self.db_evt_file):
            with open(self.db_evt_file, 'w') as f:
                json.dump([], f)

    def carregar_organizadores(self):
        try:
            with open(self.db_org_file, 'r') as f:
                data = json.load(f)
        except json.JSONDecodeError:
            data = []
        
        organizadores = []
        for org_data in data:
            organizador = Organizador(
                nome=org_data['nome'],
                cpf=org_data['cpf'],
                email=org_data['email']
            )
            organizador.senha_hash = org_data['senha_hash']
            organizadores.append(organizador)
        return organizadores

    def salvar_organizador(self, organizador):
        with open(self.db_org_file, 'r') as f:
            try:
                organizadores_data = json.load(f)
            except json.JSONDecodeError:
                organizadores_data = []

        novo_org_data = {
            'nome': organizador.nome,
            'cpf': organizador.cpf,
            'email': organizador.email,
            'senha_hash': organizador.senha_hash
        }
        organizadores_data.append(novo_org_data)

        with open(self.db_org_file, 'w') as f:
            json.dump(organizadores_data, f, indent=4)


    def carregar_eventos(self):
        try:
            with open(self.db_evt_file, 'r') as f:
                data = json.load(f)
        except json.JSONDecodeError:
            data = []
        
        eventos = []
        for evt_data in data:
            evento = Evento(
                nome=evt_data.get('nome'),
                data=evt_data.get('data'),
                distancia=evt_data.get('distancia'),
                tempo_corte=evt_data.get('tempo_corte'),
                data_limite_cancelamento=evt_data.get('data_limite_cancelamento', ''), 
                kit_corrida=evt_data.get('kit_corrida', '') 
            )
            eventos.append(evento)
        return eventos

    def salvar_evento(self, evento):
        try:
            with open(self.db_evt_file, 'r') as f:
                eventos_data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            eventos_data = []

        novo_evt_data = {
            'nome': evento.nome,
            'data': evento.data,
            'distancia': evento.distancia,
            'local_largada': evento.local_largada,
            'tempo_corte': evento.tempo_corte,
            'data_limite_cred': evento.data_limite_cred,
            'organizador_cpf': evento.organizador_cpf,
            'kits': [vars(kit) for kit in evento.kits]
        }
        
        eventos_data.append(novo_evt_data)

        with open(self.db_evt_file, 'w') as f:
            json.dump(eventos_data, f, indent=4)