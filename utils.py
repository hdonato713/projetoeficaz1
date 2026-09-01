import sqlite3

#inicial 

class Note:
    def __init__(self, note_id, title, content):
        self.id = note_id
        self.title = title
        self.content = content

#sobre html e css

def load_template(caminho):
    with open(("templates/" + caminho), "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()

        return conteudo

#carregamento e definição de dados (básico do programa)
def load_data(caminho):
    create_table()

    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT id, title, content, favorite FROM note ORDER BY favorite DESC, id ASC")
    resultados = cursor.fetchall()

    conexao.close()

    notas = []

    for note_id, title, content, favorite in resultados:
        notas.append({
            "id": note_id,
            "titulo": title,
            "detalhes": content,
            "favorite" : favorite
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
            content TEXT NOT NULL,
            favorite INTEGER NOT NULL DEFAULT 0
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

#trabalhando com notas (edição de dados)

def get_note(note_id):
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT id, title, content FROM note WHERE id = ?",
        (note_id,)
    )

    resultado = cursor.fetchone()
    conexao.close()

    if resultado is None:
        return None

    return Note(
        resultado[0],
        resultado[1],
        resultado[2]
    )

def update_note(note_id, titulo, detalhes):
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()

    cursor.execute(
        """
        UPDATE note
        SET title = ?, content = ?
        WHERE id = ?
        """,
        (titulo, detalhes, note_id)
    )

    conexao.commit()
    conexao.close()

def turn_favorite (note_id):
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()

    cursor.execute(
        """
        UPDATE note
        SET favorite = CASE
            WHEN favorite = 1 THEN 0
            ELSE 1
        END
        WHERE id = ?
        """,
        (note_id,)
    )

    conexao.commit()
    conexao.close()