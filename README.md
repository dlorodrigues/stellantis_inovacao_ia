# Desafio Stellantis: Inovação e IA 🚗⚡

Este repositório contém a documentação e os scripts desenvolvidos para o Desafio de Estágio da Stellantis, focado na aplicação prática de Inteligência Artificial para análise estratégica de mercado.

## 🎯 Objetivo (Cenário 2 - Oportunidades de Inovação Futura)
Analisar como concorrentes asiáticos (especialmente BYD e GWM) estão se posicionando em relação à infraestrutura de carregamento e serviços conectados na América do Sul, e propor uma solução competitiva e inovadora para a Stellantis.

## 🛠️ Ferramentas Utilizadas
* **Google Gemini (Interface Web):** Ideação e estruturação de comandos (Prompts).
* **Python (SDK `google-genai`):** Automação e refinamento das consultas via API utilizando o modelo **Gemini 3.6-flash**.
* **Python (`qrcode`):** Geração automatizada de QR Code para a apresentação final.

## 🧠 Metodologia de Prompts (CTCEV)
Para garantir respostas analíticas e não genéricas, utilizei a metodologia **CTCEV** (Contexto, Tarefa, Critérios, Entrega, Validação) e a técnica dos 4 Papéis:

**Prompt 1: Exploração (Papel: Pesquisadora)**
> "Atue como um analista de mercado automotivo na América do Sul. Liste as inovações em infraestrutura de carregamento e serviços conectados que marcas chinesas estão desenvolvendo na região. Foque em ações dos últimos 2 anos, destacando parcerias locais. Responda em tópicos curtos. Separe o que já é fato consumado do que ainda é projeto piloto."

**Prompt 2: Estruturação (Papel: Organizadora)**
> "Com base na pesquisa anterior, quero estruturar uma solução competitiva para a Stellantis. Compare as lacunas deixadas por eles com as fortalezas da Stellantis (capilaridade de concessionárias). Responda em uma tabela comparativa com: Ameaça, Oportunidade e Ideia de Ação."

## 🕵️‍♂️ Validação Crítica e Correção Humana
A IA apresentou uma limitação ao superestimar a presença atual de infraestrutura de recarga rápida no interior do Brasil, tratando promessas futuras como fatos consumados. Realizei uma checagem cruzada com fontes externas (portais de negócios automotivos) e ajustei a análise para refletir a realidade do mercado: as lacunas de infraestrutura ainda são enormes e representam a principal dor do consumidor.

## 💡 A Proposta: Stellantis Energy Hub & Connect
Aproveitando a nossa maior fortaleza física frente aos novos entrantes, proponho transformar a vasta rede de concessionárias da Stellantis (Fiat, Jeep, Peugeot, etc.) em polos capilares de serviço e energia.

* **A Solução:** Venda de uma "Assinatura de Mobilidade Híbrida/Elétrica". O cliente adquire o veículo e assina um plano que garante acesso prioritário a carregadores rápidos na rede Stellantis e um software preditivo para manutenção preventiva automática.
* **O Diferencial:** Construímos uma barreira competitiva imediata usando um ativo que já possuímos (capilaridade física), solucionando a maior dor do consumidor sul-americano: a ansiedade de autonomia.

## ⚙️ Como executar os scripts deste projeto
1. Clone este repositório.
2. Instale as dependências: `pip install -r requirements.txt`
3. Para rodar a análise via API do Gemini (usando o modelo `gemini-3.6-flash`): `python resumidor.py`
4. Para gerar o QR Code da apresentação: `python app.py`