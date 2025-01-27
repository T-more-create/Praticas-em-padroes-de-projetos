from fastapi import APIRouter, HTTPException, Form
from service.event_service import EventService

event_router = APIRouter(prefix="/events", tags=["Events"])

@event_router.post("/")
async def create_event(id: int = Form(...), name: str = Form(...), date: str = Form(...)):
    try:
        event = EventService.create_event(id, name, date)
        return {"message": "Evento criado com sucesso!", "event": event.__dict__}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@event_router.get("/listar")
def list_events():
    events = EventService.get_all_events()
    return [e.__dict__ for e in events]

@event_router.get("/listar/{id}")
def search_evento(id: int):
    event = EventService.search_event(id)
    if not event:
        raise HTTPException(status_code=404, detail=f"Evento com ID {id} não encontrado.")
    return event

@event_router.put("/{id}/updated")
async def update_event(id: int,id_updated:int=Form(...), name: str = Form(...),date:str=Form(...)):
    event = EventService.search_event(id)
    
    if not event:
        raise HTTPException(status_code=404, detail=f"evento com ID {id} não encontrado.")
    
    event.id=id_updated 
    event.name = name
    event.date=date
    
    return {"message": "evento atualizado!", "event": event.__dict__}

@event_router.delete("/{id}/delete")
async def delete_event(id: int):
    try:
        event = EventService.delete_event(id)
        return {"message": f"Evento com ID {id} deletado!"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))