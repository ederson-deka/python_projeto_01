import streamlit as st

def main():

    st.title("Monitoria Descomplicada")
    menu=["Inicio", "Entrar", "Inscrever"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Início":
        st.subheader("Início")

    elif choice == "Entrar":
        st.subheader("Entrar na seção")
        username = st.sidebar.text_input("Nome de usuário")
        password = st.sidebar.text_input("Senha", type='password')
        if st.button("Entrar"):
            if password == "123456":

                st.success("Logged In as {}".format(username))

                task = st.selectbox("Task",["Adicionar Postagem", "Análises", "Perfis"])
                if task == "Adicionar Postagem":
                    st.subheader("Adicione a sua postagem")
                    st.title("Etapa 01 - 14/03/2023")
                    st.video("projeto_01.mp4")
                    st.title("Etapa 02 - 15/03/2023")
                    st.video("projeto_02.mp4")
                elif task == "Análises":
                    st.subheader("Análises")
                elif task == "Perfis":
                    st.subheader("Usar perfil")
            else:
                st.warning("Usuário ou senha incorretos")

    elif choice == "Inscrever":
        st.subheader("Criar nova conta")
    
if __name__ == "__main__":
    main()

