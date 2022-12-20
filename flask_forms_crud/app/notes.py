from . import database as dbf
from . import models as mdf

def create_note(text):
    note = mdf.Note(text=text)
    dbf.Base.session.add(note)
    dbf.Base.session.commit()
    dbf.Base.session.refresh(note)


def read_notes():
    return dbf.Base.session.query(mdf.Note).all()


def update_note(note_id, text, done):
    dbf.Base.session.query(mdf.Note).filter_by(id=note_id).update({
        "text": text,
        "done": True if done == "on" else False
    })
    db.session.commit()


def delete_note(note_id):
    dbf.Base.session.query(mdf.Note).filter_by(id=note_id).delete()
    dbf.Base.session.commit()
