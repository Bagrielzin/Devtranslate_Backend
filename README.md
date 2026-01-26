# DevTranslate - Backend

**DevTranslate** é uma aplicação web que permite traduzir trechos de código de uma linguagem de programação para outra com auxílio de modelos de inteligência artificial.

Este repositório contém o backend da aplicação, desenvolvido em **Python + FastAPI**, responsável por processar requisições, validar dados e integrar diferentes provedores de IA.

---

## Decisões Arquiteturais

### Modelo Arquitetural

O backend opera como uma **REST API**, expondo endpoints HTTP para consumo do frontend.

### Organização do Código

- Separação clara por **responsabilidades**, garantindo baixo acoplamento e fácil manutenção.
- Uso de **schemas com Pydantic** para validação de dados de entrada e saída.
- Camada de **services** responsável pela lógica de negócio e integração com provedores externos de IA.
- Utilização do **Factory Pattern** para seleção dinâmica do provedor de IA (OpenAI, Claude ou Gemini).

### Manutenção e Escalabilidade

- Novos provedores de IA podem ser adicionados criando um novo serviço em `services/` e registrando-o na Factory.
- Uso de variáveis de ambiente com `python-dotenv` para garantir segurança das chaves de API.
- Tratamento centralizado de erros para respostas HTTP padronizadas.

---  

## Estrutura do Projeto

```
app/
├── main.py                 # Inicialização e configuração do FastAPI
├── routers/                # Definição das rotas/endpoints
│   └── translate.py        # Endpoint de tradução
├── schemas/                # Modelos Pydantic (Request/Response)
│   └── translation.py
├── services/               # Integração com provedores de IA
│   ├── openai_service.py   # OpenAI (GPT)
│   ├── claude_service.py   # Anthropic Claude
│   ├── gemini_service.py   # Google Gemini
│   └── provider_factory.py # Factory de seleção do provedor
├── utils/                  # Utilitários auxiliares
│   ├── formatters.py       # Limpeza e formatação de respostas
│   └── prompt_builder.py   # Construção dinâmica de prompts
```

---

## Tecnologias Utilizadas

- [Python 3.10+](https://www.python.org)
- [FastAPI](https://fastapi.tiangolo.com)
- [Pydantic](https://docs.pydantic.dev/latest/)
- [OpenAI SDK](https://platform.openai.com/docs/overview)
- [Anthropic SDK](https://www.anthropic.com)
- [Google Generative AI](https://ai.google.dev)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## Instalação e Execução

1. **Clone o repositório:**

```bash
git clone https://github.com/Bagrielzin/Devtranslate_Backend
cd Devtranslate_Backend
```

2. **(Opcional) Crie e ative um ambiente virtual:**
   
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

3. **Instale as dependências**:
   
```bash
pip install -r requirements.txt
```

4. **Rode o servidor em modo de desenvolvimento:**

```bash
uvicorn app.main:app --reload
```

> Por padrão, rodará em: http://localhost:8000
---

## Observações
- Os prompts são construídos dinamicamente para retornar apenas código limpo e explicação, sem markdown desnecessário.
- O utilitário `formatters.py` remove blocos de código `(```)` caso o modelo de IA os inclua na resposta.
- O backend foi projetado para integração direta com o frontend React via HTTP.
---

## Funcionalidades
**Endpoint de Tradução**
**POST** `/translate`
> Responsável por traduzir trechos de código entre linguagens utilizando IA.

**Exemplo de Request**
```json
{
  "code": "print('Hello World')",
  "from": "python",
  "to": "java",
  "model": "gpt-4"
}
```

**Exemplo de Response**
```json
{
  "translated_code": "System.out.println(\"Hello World\");",
  "explanation": "A função print do Python foi substituída por System.out.println em Java, que é a forma padrão de saída no console."
}
```

## Licença

Este projeto está sob a licença [MIT](https://github.com/S204-Inatel-2025-2/cinelist-backend/blob/main/LICENSE).

