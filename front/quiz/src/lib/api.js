export async function getQuestions() {
    const response = await fetch('http://127.0.0.1:8000/perguntas');
    return await response.json();
  }
  