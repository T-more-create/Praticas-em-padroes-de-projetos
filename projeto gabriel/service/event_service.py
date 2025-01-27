from dao.event_dao import EventDAO
from models.event import Event

class EventService:
    @staticmethod
    def create_event(id:int, name:str, date:str):
        if any(e.id == id for e in EventDAO.events):
            raise Exception("Evento com ID já existente!")
        event = Event(id, name, date)
        EventDAO.add_event(event)
        return event

    @staticmethod
    def get_all_events():
        return EventDAO.list_events()
    
    @classmethod
    def search_event(cls,id:int):
        return EventDAO.search_event(id)
    
    @staticmethod
    def delete_event(id: int):
        event = EventDAO.delete_event(id)
        if not event:
            raise Exception(f"Evento com ID {id} não encontrado.")
        return event