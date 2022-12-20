from . import database as dbf
from . imports models as mdf

def create_note(text):
    note = mdf.Note(text=text)
    db.session.add(note)
    db.session.commit()
    db.session.refresh(note)


def read_notes():
    return db.session.query(mdf.Note).all()


def update_note(note_id, text, done):
    db.session.query(mdf.Note).filter_by(id=note_id).update({
        "text": text,
        "done": True if done == "on" else False
    })
    db.session.commit()


def delete_note(note_id):
    db.session.query(mdf.Note).filter_by(id=note_id).delete()
    db.session.commit()
