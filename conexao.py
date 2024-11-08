import mysql.connector
from dataclasses import dataclass, field
from mysql.connector import Error

@dataclass
class ConexaoDatabase:
    host: str
    database: str
    user: str
    password: str
    connection: mysql.connector.MySQLConnection = field(init=False, default=None)

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                print('Conexao bem sucessedida!')
        
        except Error as e:
            print(f'Erro ao conectar ao banco de dados {e}')
            self.connection = None

    def disconnect(self):
        if self.connection and self.connection.is_connected:
            self.connection.close()
            print('conexao fechada!')

    def execute_query(self, query: str, parms: tuple = None):
        if not(self.connection and self.connection.is_connected()):
            print('Conexao nao esta ativa!')
            return None

        cursor = self.connection.cursor()
        try:
            cursor.execute(query, parms)
            self.connection.commit()
            print('Consulta executada com sucesso!')
        except Error as e:
            print(f'Error a executar consulta {e}')
        finally:
            cursor.close()

    def fetch_results(self, query: str, parms: tuple = None):
        if not(self.connection and self.connection.is_connected()):
            print('Conexao nao esta ativa!')
            return None

        
        cursor = self.connection.cursor()
        
        try:
            cursor.execute(query, parms)
            resultados = cursor.fetchall()
            return resultados
        except Error as e:
            print(f'Error a executar consulta {e}')
            return None
        finally:
            cursor.close()

