import sqlite3

def load_data(caminho):
    with open(("static/data/" + caminho), "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
    return dados

def load_template(caminho):
    with open(("templates/" + caminho), "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()

        return conteudo

def add_note(nova_anotacao):
    anotacoes = load_data("notes.json")

    anotacoes.append(nova_anotacao)

    with open("static/data/notes.json", "w", encoding="utf-8") as arquivo:
        json.dump(
            anotacoes,
            arquivo,
            ensure_ascii=False,
            indent=4
        )

def create_table():
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS note (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()