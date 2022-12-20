from . import database as dbf
from . import models as mdf

def create_note(text):
    note = mdf.Note(text=text)
    dbf.db_session.add(note)
    dbf.db_session.commit()
    dbf.db_session.refresh(note)


def read_notes():
    return dbf.db_session.query(mdf.Note).all()


def update_note(note_id, text, done):
    dbf.db_session.query(mdf.Note).filter_by(id=note_id).update({
        "text": text,
        "done": True if done == "on" else False
    })
    dbf.db_session.commit()


def delete_note(note_id):
    dbf.db_session.query(mdf.Note).filter_by(id=note_id).delete()
    dbf.db_session.commit()
