# Leitor de CSV

## 📖 Sobre o Projeto
O projeto consiste em uma aplicação Web com Python para resolver um problema específico do Felipe. Mais informações [aqui](docs/CHECK.MD).

## 🚀 Tecnologias e Ferramentas

A aplicação foi desenvolvida em Python com interface Streamlit.

## Stack do Projeto

Este projeto é uma aplicação web simples que utiliza o Streamlit, uma biblioteca open-source em Python que permite a criação de aplicativos web para análise de dados de forma extremamente rápida. O objetivo é demonstrar as capacidades e a integração do Streamlit com a resolução dos desafios propostos.

Essas e outras libs e tecnologias usadas neste projeto são:
|  Lib      | Versão    |
|-----------|-----------|
| **Runtime**           |
| Python    | v3.12.x   |
| **Devtime**           |
| Ruff                          | v0.4.x    |
| Docker Engine                 | vx.x.x    |
| Taskipy                       | v1.12.x   |

### Organização do projeto
```
/
├─📁 .devcontainer     ->  Configurações do devcontainer
├─📁 .vscode           ->  Definições de ambiente para o VSCode
├─📁 docs              ->  Artefatos para documentação do repo
├─📁 src               ->  [Implementação do Desafio]
│ │ ├─🐍 playground.py              -> Entrypoint
│ │ ...
│ ├─📁 assets               ->  [recursos externos]
│ │ │ ├─📁 imgs             ->  [Imagens utilizadas pela Aplicação]
│ │ │ │   ...
│ │ │ ├─📁 lang             ->  [Config TOML utilizado pela Aplicação]
│ │ │ │   ├─⚙️ ui_labels.toml         -> toml para Ui da Aplicação
│ │ │ │   ...
│ │ ├─📁 page               -> [Páginas]
│ │ │     ├─🐍 home.py               -> Página Home
│ │ │     ├─🐍 tarefa_x.py           -> Página de tarefa x
│ │ │     ...
│ │ ├─📁 utils             -> [Configurações/Funções da Aplicação]
│ │ │ │   ├─🐍 load.py              -> Funções utilitárias
│ │ │ ├─📁 functions        ->  [Funções para Aplicação]
│ │ │ │   ├─🐍 xxxx.py              -> Funções para Aplicação
│ │ │ │   ...
│ │ ...
├─📄 .gitignore
├─📄 Makefile          ->  Automações para o ambiente
├─📄 

pyproject.toml

    ->  Definições para o projeto
├─📄 README.md

```

## Montando o ambiente

Este repositório está organizado em um devcontainer.
Para instanciá-lo no VSCode, são recomendadas as seguintes configurações:

#### Extensões recomendadas

- Name: Remote Development
- Id: ms-vscode-remote.vscode-remote-extensionpack
- Description: An extension pack that lets you open any folder in a container, on a remote machine, or in WSL and take advantage of VS Code's full feature set.
- Version: 0.25.0
- Publisher: Microsoft
- VSCode Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack

#### Docker Engine

É obrigatório ter o Docker Engine já instalado e configurado. Para mais informações de como instalar o Docker Engine em seu SO, veja:

- Instruções para instalação do Docker Engine: [Ver o link](https://docs.docker.com/engine/install/)

#### Procedimento para instanciar o projeto no VSCode
1. Com o pack de extensões instalado,
1. Realize o clone/fork deste repositório,
1. Abra o diretório deste repositório no VSCode como um projeto,
1. Use o comando _Dev Containers: Reopen in Container_ da paleta de comandos do VSCode. _(F1, Ctrl+Shift+P)_.

Depois da compilação do container, o VSCode abrirá o repositório em um ambiente encapsulado e executando diretamente de dentro do container conforme configurado nas definições do **/.devcontainer**.

#### Procedimento para iniciar
1. Inicie o ambiente virtual do poetry
```
$> poetry shell
```
2. Instale as dependências definidas no pyproject.toml
```
$> poetry install
```
- Pronto, agora você está pronto para começar a usar!

### Principais comandos:

#### Levantar a aplicação
```
$> make playground
```

### Aviso: é necessário fazer o upload do arquivo .json
### Passos para obter o arquivo de credenciais de conta de serviço:
1. Vá para o [Console do Firebase](https://console.firebase.google.com/).
2. Selecione seu projeto.
3. Vá para "Configurações do projeto" (ícone de engrenagem) > "Contas de serviço".
4. Clique em "Gerar nova chave privada" e baixe o arquivo JSON.

### Exemplo de arquivo JSON de credenciais de conta de serviço:
```json
{
  "type": "service_account",
  "project_id": "test-3ffb9",
  "private_key_id": "some_private_key_id",
  "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-abcde@test-3ffb9.iam.gserviceaccount.com",
  "client_id": "some_client_id",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-abcde%40test-3ffb9.iam.gserviceaccount.com"
}
```

#### Adicionar novas dependências
```
# Adicionar uma nova lib para o runtime do projeto
$> poetry add <<nome_da_lib>>

# Adicionar uma nova lib para o ambiente de desenvolvimento
$> poetry add <<nome_da_lib>> --group dev
```

