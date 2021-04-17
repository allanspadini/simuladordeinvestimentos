import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

st.write('# Simulador de investimentos')




inicial = st.number_input('Valor inicial',value=5000.00)
aporte = st.number_input('Aporte mensal',value=100)
taxa = st.number_input('Taxa mensal',value=0.22)
prazo = st.number_input('Prazo em meses', value=12)
atual = inicial
atual2 = atual
#resultado = pd.DataFrame()
resultado=np.zeros(prazo)
colchao=np.zeros(prazo)
juros=np.zeros(prazo)
eixo_meses = np.linspace(1,prazo,prazo)

if st.button('Simular'):
    for i in range(prazo):
        resultado[i] = atual + (atual*taxa/100) + aporte
        juros[i] = atual*taxa/100
        atual = resultado[i]
        colchao[i] = atual2 + aporte
        atual2 = colchao[i]
    st.write('## Resultado do investimento')
    final = '## '+ 'R$' + str(np.round(resultado[-1],2))
    st.write(final)
    st.write('## De baixo do colchão')
    final = '## '+ 'R$' + str(np.round(inicial + prazo*aporte,2))
    st.write(final)

    
    fig = plt.figure()
    
    plt.style.use(['dark_background'])
    plt.plot(eixo_meses, resultado)
    plt.plot(eixo_meses, colchao)
    
    plt.xlabel('Meses')    
    plt.ylabel('Valor')
    st.pyplot(fig)
    dado = {'Meses': eixo_meses, 'De baixo do colchão': colchao, 'Juros no mês': juros,'Valor acumulado': resultado}
    dtf = pd.DataFrame(data=dado)
    dtf['Valor acumulado']=dtf['Valor acumulado'].round(2)
    dtf['Juros no mês']=dtf['Juros no mês'].round(2)
    
    #dtf.set_index('Meses',inplace=True)
    st.table(dtf.style.format({'Meses': '{:.0f}', 'De baixo do colchão': '{:.2f}', 'Juros no mês': '{:.2f}','Valor acumulado': '{:.2f}'}))

