from dao.event_dao import EventDAO 
from dao.participant_dao import ParticipantDAO
from models.participant import Participant

class ParticipantService:
    @staticmethod
    def register_participant(id: int, name: str, event_id: int):

        events = EventDAO.list_events()
        event_exists = any(e.id == event_id for e in events)
        
        if not event_exists:
            raise Exception(f"Evento com ID {event_id} não existe. Registre-se em um evento válido.")
        
        participant = Participant(id, name, event_id)
        ParticipantDAO.add_participant(participant)
        return participant

    @staticmethod
    def get_participants_by_event(event_id):
        return ParticipantDAO.list_participants_by_event(event_id)
    
    @classmethod
    def search_participant(cls, id: int):
        return ParticipantDAO.search_participant(id)  

    @staticmethod
    def delete_participant(id: int):
        participant = ParticipantDAO.delete_participant(id)
        if not participant:
            raise Exception(f"Participante com ID {id} não encontrado.")
        return participant