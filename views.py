from utils import load_data, load_template, add_note, delete_note


def index():
    notes_template = load_template('components/note.html')
    notes_li = [
        notes_template.format(id=dados['id'], title=dados['titulo'], details=dados['detalhes'])
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

def delete(note_id):
    delete_note(note_id)