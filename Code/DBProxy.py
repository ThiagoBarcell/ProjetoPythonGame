import sqlite3


class DBProxy:
    def __init__(self, db_name:str):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.connection.execute('''
                                   CREATE TABLE IF NOT EXISTS PlayerPontos(
                                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                                   Player_name TEXT NOT NULL,
                                   Player_pts INTEGER NOT NULL,
                                   Player_data TEXT NOT NULL)
                                '''
                                )
        pass

    def insere_dados(self, score_dict: dict):
        self.connection.execute('INSERT INTO PlayerPontos (Player_data, Player_name, Player_pts) VALUES ( :date, :name, :score )', score_dict)
        self.connection.commit() #faz o commit do insert, salva no BD

    def retorna_top10(self) -> list:
        #Traz os 10 maiores registros da tabela
        return self.connection.execute('SELECT * FROM PlayerPontos ORDER BY Player_pts DESC LIMIT 10').fetchall()


    def close(self): #Fecha a conexão com o BD( Boas práticas )
        return self.connection.close()