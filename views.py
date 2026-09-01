from utils import load_data, load_template, add_note, delete_note, get_note, update_note, turn_favorite


def index():
    notes_template = load_template('components/note.html')
    notes_li = [
        notes_template.format(id=dados['id'], title=dados['titulo'], details=dados['detalhes'], 
        favorite_icon="★" if dados["favorite"] else "☆",favorite_class="favorite" if dados["favorite"] else "")
        for dados in load_data('notes.json')
    ]
    notes = '\n' .join(notes_li)

    return load_template('index.html').format(notes=notes)

def submit(titulo, detalhes):
    params = {
        "titulo": titulo,
        "detalhes": detalhes
    }

    add_note(params)

def edit(note_id):
    nota = get_note(note_id)

    if nota is None:
        return "Anotação não encontrada"

    return load_template("update.html").format(
        id=nota.id,
        titulo=nota.title,
        detalhes=nota.content
    )

def update(note_id, titulo, detalhes):
    update_note(note_id, titulo, detalhes)

def favorite(note_id):
    turn_favorite(note_id)

def delete(note_id):
    delete_note(note_id)
