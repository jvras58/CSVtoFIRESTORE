"""Módulo EntryPoint da aplicação"""

import streamlit as st

# Page config
st.set_page_config(page_title='Playground')

from page import tarefa_3
import page.config_json as config
import page.home as home_page
import page.tarefa_1 as tarefa_1
import page.tarefa_2 as tarefa_2
from utils.load import load_image


def show_page() -> None:
    """Mostra a página HOME e menu do dashboard."""
    st.sidebar.image(load_image('logo_banca.png'), use_container_width=True)

    pages = {
        '🏠 Home': home_page,
        '📄 Simple add Collections': tarefa_1,
        '📄 Complex add Collections': tarefa_2,
        '📄 export csv to firestore': tarefa_3,
        '📄 Config Json conection firestore': config,

    }

    st.sidebar.title('Menu')
    selection = st.sidebar.radio('Go to', list(pages.keys()))

    page = pages[selection]
    page.show_page()


if __name__ == '__main__':
    show_page()
