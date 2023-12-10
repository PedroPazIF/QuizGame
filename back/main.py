from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from quiz import QuizFacade
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

quiz_facade = QuizFacade() 

@app.get("/perguntas")
def loadQuestion(total: int):
    data = "jogos.json"
    perguntas = quiz_facade.load_questions_from_json(data, total)  # Chamar o método na instância
    return perguntas
