from fastapi import APIRouter, Form, HTTPException
from service.participant_service import ParticipantService

participant_router = APIRouter(prefix="/participants", tags=["Participants"])

@participant_router.post("/")
async def register_participant(id: int = Form(...), name: str = Form(...), event_id: int = Form(...)):
    print(f"Recebido: id={id}, name={name}, event_id={event_id}")
    participant = ParticipantService.register_participant(id, name, event_id)
    return {"message": "Participante registrado!", "participant": participant.__dict__}

@participant_router.get("/{event_id}")
async def get_participants_by_event(event_id: int):
    participants = ParticipantService.get_participants_by_event(event_id)
    return [p.__dict__ for p in participants]

@participant_router.get("/{id}/ola")
def search_participante(id: int):
    participant = ParticipantService.search_participant(id)
    if not participant:
        raise HTTPException(status_code=404, detail=f"Participante com ID {id} não encontrado.")
    return participant.__dict__ 

@participant_router.put("/{id}/updated")
async def update_participant(id: int,id_updated:int=Form(...), name: str = Form(...),event_id:int=Form(...)):
    participant = ParticipantService.search_participant(id)
    
    if not participant:
        raise HTTPException(status_code=404, detail=f"Participante com ID {id} não encontrado.")
    
    participant.id=id_updated 
    participant.name = name
    participant.event_id=event_id
    
    return {"message": "Participante atualizado!", "participant": participant.__dict__}

@participant_router.delete("/{id}/delete")
async def delete_participant(id: int):
    try:
        participant = ParticipantService.delete_participant(id)
        return {"message": f"Participante com ID {id} deletado!"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
