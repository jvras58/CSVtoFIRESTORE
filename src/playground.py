"""Módulo EntryPoint da aplicação"""

import streamlit as st

import page.config_json as config
import page.home as home_page
from page import tarefa_1, tarefa_2, tarefa_3, tarefa_4, tarefa_5
from utils.load import load_image

# Page config
st.set_page_config(page_title='Playground')


def show_page() -> None:
    """Mostra a página HOME e menu do dashboard."""
    st.sidebar.image(load_image('logo_banca.png'), use_container_width=True)

    pages = {
        '🏠 Home': home_page,
        '📄 Simple add Collections': tarefa_1,
        '📄 Complex add Collections': tarefa_2,
        '📄 Complex add Collections 2': tarefa_3,
        '📄 export csv to firestore': tarefa_4,
        '📄 export json to firestore': tarefa_5,
        '📄 Config Json conection firestore': config,

    }

    st.sidebar.title('Menu')
    selection = st.sidebar.radio('Go to', list(pages.keys()))

    page = pages[selection]
    page.show_page()


if __name__ == '__main__':
    show_page()
