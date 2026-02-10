# 1. Importamos apenas o necessário para criar a API
from flask import Flask, request, jsonify
from genai_api import client
from estrutura_database import estrutura_db
from vetorizacao_fase1 import vetorizar_banco
from rag_fase2 import processar_pergunta_rag

app = Flask(__name__)

# ENDPOINT vs HTTP Métodos
@app.route("/perguntar", methods=["POST"])
def perguntar_post():
    dados = request.get_json() or {}
    pergunta = dados.get('prompt','Pergunta não enviada')
    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents=pergunta
    )
    return jsonify(
        {
        "pergunta": f"Você perguntou: {pergunta}",
        "resposta_gemini": f"{response.text}"  
        }
    )


@app.route("/perguntar", methods=["GET"])
def perguntar_get():
    return jsonify(
     {"estrutura_db": estrutura_db()}
    )

#ENDPOINT DA FASE 1 
@app.route("/fase_1", methods=["GET", "POST"])
def fase_1():    
    resultado = vetorizar_banco()
    return jsonify(resultado)

# ENPOINT DA FASE 2    
@app.route("/fase_2", methods=["GET", "POST"])
def fase_2():
    """
    Endpoint da Fase 2: RAG (Retrieval-Augmented Generation)
    Chama o processo completo de RAG do arquivo rag_fase2.py
    """
    if request.method == "POST":
        dados = request.get_json() or {}
        resultado = processar_pergunta_rag(
            pergunta=dados.get('pergunta', ''),
            contexto_adicional=dados.get('contexto_adicional', ''),
            top_k=dados.get('top_k', 5)
        )
        return jsonify(resultado)
    else:
        return jsonify({
            "mensagem": "Endpoint da Fase 2 - RAG",
            "instrucoes": "Use POST com: {\"pergunta\": \"sua pergunta aqui\"}"
        })

if __name__ == "__main__":
    print("Iniciando API...") 
    app.run(host='0.0.0.0', port=5000, debug=True)