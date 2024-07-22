# Super Portfólio 🤓

É uma projeto para praticar a criação de models, views e APIs REST, além de testes, autenticação e deploy no framework Django.

<details>
<summary><strong>🧑‍💻 O que foi desenvolvido</strong></summary>

Desenvolvi uma API para gerenciamento de dados de perfil e projetos em um super portfólio.

</details>

<details>
  <summary><strong>:memo: Habilidades desenvolvidas </strong></summary>

Neste projeto, aprendi a:

- Utilizar o _Django REST Framework_ para criar endpoints com entidades aninhadas.
- Utilizar o módulo _Simple JWT_ para implementar autenticação no Django REST Framework.
  
</details>



## Instalando o projeto

1. Este projeto usa dependências que não são funcionais em todas as versões do Python. Por isso, recomendo que seu Python esteja na versão `3.10.0` ou superior. 
  
> ⚠️ **ATENÇÃO: NUNCA REMOVA VERSÕES ANTIGAS INSTALADAS DO PYTHON. SEU SISTEMA OPERACIONAL PODE DEPENDER DELAS!** ⚠️

2. Para conseguir instalar a dependência `mysqlclient` você precisa garantir a existência de algumas bibliotecas no seu sistema operacional:

- **Debian/Ubuntu**

```bash
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config
```

- **Mac**

```bash
brew install mysql pkg-config
```

3. Clone o repositório

- Use o comando: `git clone git@github.com:MandyTrajano90/Super-Portfolio.git`
- Entre na pasta do repositório que você acabou de clonar:
  - `cd Super-Portfolio`

4. Instale as dependências

    - Siga os passos do tópico [**🏕️ Ambiente Virtual**]

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary>
  O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
  python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando `deactivate`. Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

</details>

<details>
  <summary><strong>🏃🏾 Executando o Projeto</strong></summary>
  As notícias estarão armazenadas no nosso banco de dados.

  <strong>MySQL</strong>

  Para a realização deste projeto, utilizei um banco de dados chamado `spotnews_database`.

  Para rodar o MySQL via Docker execute os seguintes comandos na raiz do projeto:

  ```bash
  docker build -t spotnews-db .
  docker run -d -p 3306:3306 --name=spotnews-mysql-container -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=spotnews_database spotnews-db
  ```
  
  Esses comandos irão fazer o build da imagem e subir o container.
  
  Lembre-se de que o MySQL utiliza por padrão a porta 3306. Se já houver outro serviço utilizando esta porta, considere desativá-lo ou mudar a porta no comando acima.

</details>

<details>
<summary><strong>🎛 Linter</strong></summary>

Para garantir a qualidade do código, utilizei nesse projeto o linter `Flake8`. Assim o código fica alinhado com as boas práticas de desenvolvimento, sendo mais legível e de fácil manutenção! Para poder executar o `Flake8`, certifique-se de ter seguido os passos do tópico [**🏕️ Ambiente Virtual**] dentro do repositório.

Para rodá-lo localmente no repositório, execute o comando a seguir:

```bash
python3 -m flake8
```

Se a análise do `Flake8` encontrar problemas no seu código, tais problemas serão mostrados no seu terminal. Se não houver problema no seu código, nada será impresso no seu terminal.

</details>


## 👁️ Dê uma olhada no código



https://github.com/user-attachments/assets/a8302a9b-4190-46f7-9cfe-d23b65b4eed7



<!-- Olá, Tryber!
Esse é apenas um arquivo inicial para o README do seu projeto.
É essencial que você preencha esse documento por conta própria, ok?
Não deixe de usar nossas dicas de escrita de README de projetos, e deixe sua criatividade brilhar!
:warning: IMPORTANTE: você precisa deixar nítido:
- quais arquivos/pastas foram desenvolvidos por você; 
- quais arquivos/pastas foram desenvolvidos por outra pessoa estudante;
- quais arquivos/pastas foram desenvolvidos pela Trybe.
-->
