export async function getQuestions(total) {
    const response = await fetch(`http://127.0.0.1:8000/perguntas?total=${total}`);
    return await response.json();
  }
  