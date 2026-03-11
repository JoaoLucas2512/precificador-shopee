import streamlit as st


if "historico" not in st.session_state:
    st.session_state.historico = []


st.title("Precificação Shopee")
nome_produto = st.text_input("Nome do Produto")
custo_produto = st.number_input("Custo")
preco = st.number_input("Preço")


#cálculos
custo_total = custo_produto + 1 + 1.07
taxa = (preco * 0.20) + 4
lucro = preco - taxa - custo_total

#exibição dos resultados
st.write(f"Custo total: R$ {custo_total:.2f}")
st.write(f"Taxa Shopee: R$ {taxa:.2f}")
st.write(f"Lucro por venda: R$ {lucro:.2f}")

#lucro ou prejuízo
if lucro >= 0:
    st.markdown(f"<h3 style='color:green'>Lucro: R$ {lucro:.2f}</h3>", unsafe_allow_html=True)
else:
    st.markdown(f"<h3 style='color:red'>Lucro: R$ {lucro:.2f}</h3>", unsafe_allow_html=True)

#Tabela de Histórico
if st.button("Salvar no histórico"):
    st.session_state.historico.append({
        "Produto": nome_produto,
        "Custo Total": custo_total,
        "Preço": preco,
        "Taxa": taxa,
        "Lucro": lucro
    })

if st.session_state.historico:
    st.subheader("Histórico de cálculos")
    st.dataframe(st.session_state.historico)