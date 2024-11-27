from groq import Groq

client = Groq(api_key='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')

def getresposta(pergunta):
    completion = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=[
            {
            "role": "assistant",
            "content": "Ola eu sou CloneGPT, criado por ghost04 numa aula do youtube entao se vc ghost das aulas do gosta se escreve no canal para nao perder nenhum video e para fortalecer o canal isso e bo , boas aulas no python e flet"
        },
            {
                "role": "user",
                "content": pergunta
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    resposta_completa = ""
    for chunk in completion:
        # Verificar se content não é None antes de concatenar
        if chunk.choices[0].delta.content is not None:
            resposta_completa += chunk.choices[0].delta.content
    
    return resposta_completa
