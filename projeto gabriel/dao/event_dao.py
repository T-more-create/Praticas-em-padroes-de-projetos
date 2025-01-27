class EventDAO:
    events = []

    @staticmethod
    def add_event(event):
        EventDAO.events.append(event)

    @staticmethod
    def list_events():
        return EventDAO.events

    @classmethod
    def search_event(cls, id: int):
        return next((e for e in cls.events if e.id == id), None)
    
    @staticmethod
    def delete_event(id: int):
        event = EventDAO.search_event(id)
        if event:
            EventDAO.events.remove(event)
        return event