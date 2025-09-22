
import sqlite3
from organizador import Organizador
from evento import Evento
from kit_de_corrida import KitDeCorrida

class Database:
    def __init__(self, db_file='pacehub.db'): 
        """Inicializa a conexão com o banco de dados e cria as tabelas se não existirem."""
        self.db_file = db_file
        self.conn = sqlite3.connect(db_file)
        self._criar_tabelas()

    def _criar_tabelas(self):
        """Cria as tabelas do banco de dados seguindo o modelo de tabela única 'usuario'."""
        cursor = self.conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuario (
                cpf TEXT PRIMARY KEY,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                senha_hash TEXT NOT NULL,
                perfil TEXT NOT NULL,
                data_nascimento TEXT,
                genero TEXT,
                pcd INTEGER
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Eventos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                data TEXT NOT NULL,
                distancia INTEGER NOT NULL,
                local_largada TEXT,
                tempo_corte TEXT,
                data_limite_cred TEXT,
                organizador_cpf TEXT NOT NULL,
                FOREIGN KEY (organizador_cpf) REFERENCES usuario (cpf) -- MUDANÇA IMPORTANTE AQUI
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS KitsDeCorrida (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                descricao TEXT,
                valor REAL NOT NULL,
                evento_id INTEGER NOT NULL,
                FOREIGN KEY (evento_id) REFERENCES Eventos (id)
            )
        ''')
        
        self.conn.commit()

    def salvar_organizador(self, organizador: Organizador):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT OR IGNORE INTO usuario (cpf, nome, email, senha_hash, perfil) VALUES (?, ?, ?, ?, ?)
        ''', (organizador.cpf, organizador.nome, organizador.email, organizador.senha_hash, 'Organizador')) 
        self.conn.commit()
    
    def carregar_organizadores(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT cpf, nome, email, senha_hash FROM usuario WHERE perfil = 'Organizador'") 
        rows = cursor.fetchall()
        
        organizadores = []
        for row in rows:
            org = Organizador(nome=row[1], cpf=row[0], email=row[2])
            org.senha_hash = row[3]
            organizadores.append(org)
        return organizadores

    def salvar_evento(self, evento: Evento):
        cursor = self.conn.cursor()
        
        cursor.execute('''
            INSERT INTO Eventos (nome, data, distancia, local_largada, tempo_corte, data_limite_cred, organizador_cpf)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (evento.nome, evento.data, evento.distancia, evento.local_largada, evento.tempo_corte, evento.data_limite_cred, evento.organizador_cpf))
        
        evento_id = cursor.lastrowid
        
        for kit in evento.kits:
            cursor.execute('''
                INSERT INTO KitsDeCorrida (nome, descricao, valor, evento_id) VALUES (?, ?, ?, ?)
            ''', (kit.nome, kit.descricao, kit.valor, evento_id))
            
        self.conn.commit()

    def fechar_conexao(self):
        if self.conn:
            self.conn.close()

