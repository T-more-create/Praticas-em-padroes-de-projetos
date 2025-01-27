from fastapi import FastAPI
from controllers.event_controller import event_router
from controllers.participant_controller import participant_router

app = FastAPI()

# Adicionando rotas ao aplicativo
app.include_router(event_router)
app.include_router(participant_router)

@app.get("/")
def root():
    return {"message": "Sistema de Organização de Eventos ativo!"}
