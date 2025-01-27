class ParticipantDAO:
    participants = []

    @staticmethod
    def add_participant(participant):
        ParticipantDAO.participants.append(participant)

    @staticmethod
    def list_participants_by_event(event_id):
        return [p for p in ParticipantDAO.participants if p.event_id == event_id]
    
    @classmethod
    def search_participant(cls, id: int):
        return next((p for p in cls.participants if p.id == id), None)  

    @staticmethod
    def delete_participant(id: int):
        participant = ParticipantDAO.search_participant(id)
        if participant:
            ParticipantDAO.participants.remove(participant)
        return participant