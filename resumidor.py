import os
from google import genai
from google.genai import types

# Configuração da API do Google Gemini
# Certifique-se de configurar sua chave de API no terminal antes de rodar:

def analisar_mercado():
    try:
        client = genai.Client(api_key="SUA_CHAVE_DE_API_AQUI")
        
        prompt = """
        Atue como um analista de mercado automotivo na América do Sul.
        Liste as inovações em infraestrutura de carregamento e serviços conectados que concorrentes asiáticos (ex: BYD, GWM) estão desenvolvendo na região nos últimos 2 anos.
        Separe o que já é fato consumado do que ainda é projeto piloto ou promessa.
        """
        
        print("Iniciando análise de mercado com Google Gemini API...")
        print("Enviando prompt estruturado (CTCEV)...\n")
        
        response = client.models.generate_content(
            model='gemini-3.6-flash',
            contents=prompt,
        )
        
        print("--- RESULTADO DA ANÁLISE ---")
        print(response.text)
        print("\n[Atenção]: O resultado acima deve ser validado criticamente (checar fontes) conforme as diretrizes do projeto.")
        
    except Exception as e:
        print(f"Erro ao conectar com a API: {e}")
        print("Dica: Verifique se a variável de ambiente GEMINI_API_KEY está configurada corretamente.")

if __name__ == "__main__":
    analisar_mercado()
