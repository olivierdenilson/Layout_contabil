import streamlit as st
import streamlit.components.v1 as components
import base64

# Função para converter imagem em base64
@st.cache_data  # Atualizado de st.cache para st.cache_data
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Função para definir background
def set_background():
    bin_str = get_base64_of_bin_file('contabil.png')
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{bin_str}");
            background-size: cover;
        }}
        .stSidebar {{
            background-color: white;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Configuração da página deve ser a primeira chamada Streamlit
st.set_page_config(
    layout="wide"
)

def main():
    # Aplicar background
    set_background()
    
    # Configuração do sidebar
    with st.sidebar:

        # Produção
        if st.sidebar.button("📊 Dashboard"):
            st.session_state.page = "Dashboard"

        # Produção
        with st.sidebar.expander("📅 Produção"):
            if st.button("📈 Analitico - Brasilia"):
                st.session_state.page = "Analitico - Brasilia"
            if st.button("📊 Sintetico - Brasilia"):
                st.session_state.page = "Sintetico - Brasilia"
            if st.button("📈 Analitico-Goiania"):
                st.session_state.page = "Analitico-Goiania"
            if st.button("📊 sintetico-Goiania"):
                st.session_state.page = "Sintetico-Goiania"

        # Recebimentos
        with st.sidebar.expander("📋 Recebimentos vs Produção"):
            if st.button("💰 Mvsoul - Brasilia"):
                st.session_state.page = "Mvsoul - Brasilia"
            if st.button("💰 Mv2000 - Brasilia"):
                st.session_state.page = "Mv2000 - Brasilia"
            if st.button("💰 Mvsoul-Goiania"):
                st.session_state.page = "Mvsoul-Goiania"
            if st.button("💰 Mv2000-Goiania"):
                st.session_state.page = "Mv2000-Goiania"
            
        # Notas Fiscais
        with st.sidebar.expander("📑 Notas Fiscais vs Produção"):
            if st.button("🧾 Nota Fiscal Mvsoul"):
                st.session_state.page = "Nota Fical Mvsoul"
            if st.button("🧾 Nota Fiscal Mv2000"):
                st.session_state.page = "Nota Fiscal Mv2000"
            if st.button("🧾 Nota Fiscal Goiania"):
                st.session_state.page = "Nota Fiscal Goiania"

        # Relatório Posicional
        with st.sidebar.expander("📋 Relatório Posicional"):
            if st.button("📌 Posicional - Brasilia"):
                st.session_state.page = "Posicional - Brasilia"
                if st.button("📌 Posicional - Goiania"):
                 st.session_state.page = "Posicional - Goiania"
                    
      
    # Conteúdo principal
    if 'page' not in st.session_state:
        st.session_state.page = "producao"

    # Renderização do conteúdo principal
    if st.session_state.page == "producao":
        # Adiciona espaço antes dos títulos
        st.markdown("<div style='height: 20vh'></div>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; color: white;'>Relatório de Produção</h1>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; color: white;'>Contabilidade</h2>", unsafe_allow_html=True)
        # Adicione aqui o conteúdo específico da página de produção
        
    elif st.session_state.page == "recebimentos":
        st.title("Recebimentos")


# Adicione CSS personalizado
def local_css():
    st.markdown("""
        <style>
        /* Centralizar vertical e horizontalmente os títulos */
        .main .block-container {
            padding-top: 20vh;
        }
        
        h1, h2, h3 {
            text-align: center !important;
            color: white !important;
        }
        
        /* Ajuste para o sidebar com fundo preto */
        .stSidebar {
            background-color: rgba(0, 0, 0, 0.9) !important;
        }
        .stSidebar .sidebar-content {
            background-color: transparent;
        }
        
        /* Ajuste para todos os textos no sidebar */
        .stSidebar * {
            color: white !important;
        }
        
        /* Ajuste para botões no tema escuro e claro */
        .stButton button {
            width: 100%;
            text-align: left !important;
            padding: 10px;
            background-color: transparent;
            border: none;
            color: white !important;
            transition: all 0.3s ease;
        }
        .stButton button:hover {
            background-color: rgba(255, 255, 255, 0.1);
            transform: translateX(10px);
            padding-left: 15px;
        }
        
        /* Ajuste específico para expanders */
        .streamlit-expanderHeader {
            color: white !important;
            transition: all 0.3s ease;
            border-radius: 5px;
            padding: 5px;
        }
        .streamlit-expanderHeader:hover {
            background-color: rgba(255, 255, 255, 0.1);
            transform: translateX(10px);
            padding-left: 15px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        /* Ajuste para textos dentro dos expanders */
        .streamlit-expanderContent {
            color: white !important;
        }
        
        /* Ajuste para headers no sidebar */
        .stSidebar .sidebar-content h1,
        .stSidebar .sidebar-content h2,
        .stSidebar .sidebar-content h3,
        .stSidebar .sidebar-content h4 {
            color: white !important;
        }
        
        /* Efeito de destaque ao expandir */
        details[open] > summary {
            background-color: rgba(255, 255, 255, 0.1);
            margin-bottom: 10px;
        }
        
        /* Remove 'Made with Streamlit' */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    local_css()
    main()