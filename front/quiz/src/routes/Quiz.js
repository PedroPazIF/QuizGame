export const load = async ({fetch}) => {
    const perguntasRes = await fetch('http://127.0.0.1:8000/perguntas')
    const perguntasData = await perguntasRes.json()
    const perguntas = perguntasData.perguntas

    return  {
        perguntas: perguntas
    }
}   