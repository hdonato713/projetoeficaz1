import sqlite3

def load_template(caminho):
    with open(("templates/" + caminho), "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()

        return conteudo

def load_data(caminho):
    create_table()

    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT id, title, content FROM note")
    resultados = cursor.fetchall()

    conexao.close()

    notas = []

    for note_id, title, content in resultados:
        notas.append({
            "id": note_id,
            "titulo": title,
            "detalhes": content
        })

    return notas

def add_note(nova_anotacao):
    create_table()

    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()

    cursor.execute(
        """
        INSERT INTO note (title, content)
        VALUES (?, ?)
        """,
        (
            nova_anotacao["titulo"],
            nova_anotacao["detalhes"]
        )
    )

    conexao.commit()
    conexao.close()

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

def delete_note(note_id):
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM note WHERE id = ?",
        (note_id,)
    )

    conexao.commit()
    conexao.close()