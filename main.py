from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from quiz import QuizFacade
app = FastAPI()

@app.get("/perguntas")
def loadQuestion():
    data = "/home/lab/Documentos/Pedro/QuizGame/jogos.json"
    perguntas = QuizFacade.load_questions_from_json(QuizFacade, data)
    return perguntas