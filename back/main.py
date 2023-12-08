from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from quiz import QuizFacade
from fastapi.middleware.cors import (
    CORSMiddleware
)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/perguntas")
def loadQuestion():
    data = "jogos.json"
    perguntas = QuizFacade.load_questions_from_json(QuizFacade, data)
    return perguntas