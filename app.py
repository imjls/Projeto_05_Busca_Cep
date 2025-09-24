import streamlit as st
import requests
import json
import BuscarCep
import pandas as pd
import BuscarCep

##### TÍTULO DA APLICAÇÃO #####

st.title("Busca CEP")



##### Lista de Opções #####

opcoes = ["Buscar CEP", "Descobrir CEP"]



##### BARRA LATERAL #####
st.sidebar.image("logo.png")

opcao = st.sidebar.selectbox("Selecione Algo", opcoes)

if opcao == "Buscar CEP":
    st.image("principal.png")

    ##### BOTÃO BUSCAR CEP #####
    cep= st.text_input("Digite o CEP")

    if st.button("Buscar CEP"):
     if len(cep) != 8 or not cep.isdigit():
                st.error("Por favor, insira um CEP válido com 8 dígitos numéricos.")
     else:
                try:
                    endereco = BuscarCep.buscar_cep(cep)
                    if endereco:
                        st.success("Endereço encontrado:")
                        st.write(f"CEP: {endereco[0]}")
                        st.write(f"Endereço: {endereco[1]}")
                        st.write(f"Bairro: {endereco[2]}")
                        st.write(f"Cidade: {endereco[3]}")
                        st.write(f"Estado: {endereco[4]}")

                        ## Mapas
                        st.title("Localização no Mapa")
                        df = pd.DataFrame({"latitude": [endereco[5]], "longitude": [endereco[6]]})
                        st.map(df, zoom=15)
                    else:
                        st.error("CEP não encontrado.")
                except Exception as e:
                    st.error(f"Ocorreu um erro ao buscar o CEP: {e}")


                    
elif opcao == "Descobrir CEP":

    st.title("Descubra Seu CEP")
    st.image("principal.png")
    st.text_input("Digite seu endereço")
    st.button("Descobrir CEP")
