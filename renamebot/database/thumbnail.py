from sqlalchemy import Column, Integer
import threading
from renamebot.database import BASE, SESSION

INSERTION_LOCK = threading.RLock()

class Thumbnail(BASE):
    __tablename__ = "thumbnail"
    id = Column(Integer, primary_key=True)
    msg_id = Column(Integer)
    
    def __init__(self, id, msg_id):
        self.id = id
        self.msg_id = msg_id

Thumbnail.__table__.create(checkfirst=True)

async def df_thumb(id, msg_id):
    with INSERTION_LOCK:
        msg = SESSION.query(Thumbnail).get(id)
        if not msg:
            msg = Thumbnail(id, msg_id)
            SESSION.add(msg)
            SESSION.flush()
        else:
            SESSION.delete(msg)
            file = Thumbnail(id, msg_id)
            SESSION.add(file)
        SESSION.commit()

async def del_thumb(id):
    with INSERTION_LOCK:
        msg = SESSION.query(Thumbnail).get(id)
        SESSION.delete(msg)
        SESSION.commit()

async def thumb(id):
    try:
        t = SESSION.query(Thumbnail).get(id)
        return t
    finally:
        SESSION.close()
