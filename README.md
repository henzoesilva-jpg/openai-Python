# openai.py — Integração com a API OpenAI

## Descrição

Projeto desenvolvido em Python para realizar requisições à API da OpenAI, permitindo enviar entradas e receber respostas geradas por modelos de inteligência artificial.

## Requisitos

* Python
* Biblioteca `openai`

### Instalação

```bash
pip install openai
```

## Configuração da API

Crie manualmente um arquivo chamado `token.json` na mesma pasta do arquivo `openai.py`.

### Exemplo de estrutura do arquivo token.json:

```json
{
    "api_key": "SUA_CHAVE_DA_API_OPENAI"
}
```

Substitua `SUA_CHAVE_DA_API_OPENAI` pela sua chave de API da OpenAI.

**Importante:** Mantenha sua chave privada e não a publique em repositórios públicos.

## Como executar

Após configurar a chave e o código, execute:

```bash
python openai.py
```

## Funcionalidades

* Integração com a API da OpenAI.
* Envio de textos para processamento.
* Recebimento e exibição das respostas geradas pela IA.

## Tecnologias utilizadas

* Python
* OpenAI API
* JSON
