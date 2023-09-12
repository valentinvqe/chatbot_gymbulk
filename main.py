import gradio as gr
import openai

# Charger la clé API depuis un fichier
openai.api_key = open("/Users/valentinvaquie/anaconda3/CHAT GPT/key.txt", "r").read().strip()

message_history = [
    {"role": "user", "content": "Tu es un bot de l'entreprise GymBulk spécialisé dans la transformation physique. Tu es concu pour aider les personnes à trouver des recettes ou encore des équivalences nutritionnelles. Tu commenceras chaque discussion par : Bonjour, je suis l'assistant GymBulk. Comment puis-je t'aider ?"},
    {"role": "assistant", "content": "Ok, je vais faire de mon mieux"}
]

def predict(input):
    message_history.append({"role": "user", "content" : input})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_history,
    )
 
    Reply_content = completion.choices[0].message.content

    message_history.append({"role": "assistant", "content": Reply_content})

    response = [(message_history[i]["content"], message_history[i+1]["content"]) for i in range(2, len(message_history), 2)]
 
    return response

with gr.Blocks() as demo:  
    # Créer une nouvelle instance de chatbot
    chatbot = gr.Chatbot()
  
    with gr.Row():
        txt = gr.Textbox(show_label=False, placeholder="Envoyer votre message", style="container: flash")
 
    txt.submit(predict, txt, chatbot)
 
    txt.submit(None, None, _js="()=>{}")
 
demo.launch(share=True)



