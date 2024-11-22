"""Funções utilitárias para carregar arquivos e integração com Firebase."""

import json
from pathlib import Path
from typing import Any

import firebase_admin
import pandas as pd
import streamlit as st
import toml
from firebase_admin import credentials, firestore
from PIL import Image

# Funções de carregamento de arquivos


def get_project_root() -> str:
    """Retorna o caminho raiz do projeto.

    Returns
    -------
    str
        Caminho raiz do projeto.

    """
    return str(Path(__file__).parent.parent.parent)


def load_image(image_name: str) -> Image:
    """Exibe uma imagem.

    Parameters
    ----------
    image_name : str
        Caminho local da imagem.

    Returns
    -------
    Image
        Imagem a ser exibida.

    """
    return Image.open(
        Path(get_project_root()) / f'src/assets/imgs/{image_name}',
    )


def load_toml(toml_file: str) -> dict[Any, Any]:
    """Carrega o arquivo toml de configuração do sistema de arquivos do usuário
    como um dicionário.

    Parameters
    ----------
    toml_file : str
        Arquivo de configuração toml carregado.

    Returns
    -------
    dict
        Dicionário de configuração carregado.

    """
    toml_loaded = toml.load(
        Path(get_project_root())
        / f'src/assets/lang/{toml_file}.toml',
    )

    return dict(toml_loaded)


@st.cache_data
def load_json(json_name: str) -> dict:
    """Carrega um conjunto de dados de um arquivo json.

    Parameters
    ----------
    json_name : str
        Nome do conjunto de dados a ser carregado.

    Returns
    -------
    dict
        Conjunto de dados carregado.

    """
    json_path = Path(get_project_root()) / f'src/data/{json_name}.json'
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


@st.cache_data
def load_dataset(dataset_name: str) -> pd.DataFrame:
    """Carrega um conjunto de dados de um arquivo csv.

    Parameters
    ----------
    dataset_name : str
        Nome do conjunto de dados a ser carregado.

    Returns
    -------
    pd.DataFrame
        Conjunto de dados carregado.

    """
    return pd.read_csv(
        Path(get_project_root()) / f'src/data/{dataset_name}.csv',
    )


# Funções para Firebase

@st.cache_data
def initialize_firebase(credential_path: str) -> firestore.Client:
    """Inicializa a conexão com o Firebase e retorna o cliente Firestore.

    Parameters
    ----------
    credential_path : str
        Caminho para o arquivo de credenciais JSON do Firebase.

    Returns
    -------
    firestore.Client
        Cliente Firestore autenticado.

    """
    # Verifica se o app já foi inicializado
    if not firebase_admin._apps:
        cred = credentials.Certificate(
            Path(get_project_root()) / credential_path
        )
        firebase_admin.initialize_app(cred)
    return firestore.client()


def initialize_firebase_from_session() -> firestore.Client:
    """Inicializa a conexão com o Firebase usando o conteúdo do arquivo JSON da

    Returns
    -------
    firestore.Client
        Cliente Firestore autenticado.

    """
    if 'firebase_config' in st.session_state:
        # Carrega o JSON como um dicionário
        firebase_config = json.loads(st.session_state['firebase_config'])
        cred = credentials.Certificate(firebase_config)
        if not firebase_admin._apps:
            firebase_admin.initialize_app(cred)
        return firestore.client()
    else:
        st.error(
            "Arquivo JSON de configuração não encontrado. Por favor,"
            "carregue o arquivo na tela de configuração."
        )
        return None


def send_data_to_firestore(
    db: firestore.Client, collection_name: str, data: dict
) -> None:
    """Envia um dicionário de dados para uma coleção específica no Firestore.

    Parameters
    ----------
    db : firestore.Client
        Cliente Firestore autenticado.
    collection_name : str
        Nome da coleção onde os dados serão armazenados.
    data : dict
        Dados a serem enviados para o Firestore.

    """
    try:
        db.collection(collection_name).add(data)
    except Exception as e:
        print(f"Erro ao enviar dados para o Firestore: {e}")


@st.cache_data
def load_csv(csv_file) -> pd.DataFrame:
    """Carrega dados de um arquivo CSV enviado pelo usuário como um DataFrame.

    Parameters
    ----------
    csv_file : _io.TextIOWrapper
        Arquivo CSV carregado pelo usuário.

    Returns
    -------
    pd.DataFrame
        Dados carregados do CSV.

    """
    try:
        return pd.read_csv(csv_file)
    except Exception as e:
        raise ValueError(f"Erro ao carregar o CSV: {e}")
