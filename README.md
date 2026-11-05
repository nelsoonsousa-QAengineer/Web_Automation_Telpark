# Automação Telpark Webportal

Testes automatizados com Selenium e Pytest (Page Object) para as funcionalidades de Login e Veículos do portal web.

## ## Testes cobertos

* Login com sucesso
* Login sem sucesso (intencional)
* Adicionar veículo com sucesso para o país "Other"
* Remover veículo com sucesso

## ## Estrutura

* **data.py**: dados de teste (URL, credenciais, matrícula)
* **pages.py**: Page Object com locators e acções
* **main.py**: testes com asserts
* **requirements.txt**: dependências

## ## Como rodar

1. Instale o Python 3 e o Google Chrome.
2. Crie e ative o ambiente virtual.
3. Instale as dependências: `pip install -r requirements.txt`
4. Preencha os dados em `data.py` com uma conta de teste.
5. Execute: `pytest main.py -v`
