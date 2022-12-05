"""
Projeto Final da Extensão - Introdução ao Python
Modulo Model - Criação de Arquivos
Autor: Brunno Henrique Sibin
Data: 05/12/2022
Versão: 0.0.3
"""

import os
import shutil

def arquivos:

os.chdir(str(pasta_python))

with open("DespesasCorrentes.xlsx","w") as arquivo_1:
    arquivo_1.write("Despesas Correntes")
with open("DespesasCorrentes.docx","w") as arquivo_2:
    arquivo_2.write("Despesas Correntes")
with open("DespesasCapital.xlsx","w") as arquivo_3:
    arquivo_3.write("Despesas Capital")
with open("DespesasCapital.docx","w") as arquivo_4:
    arquivo_4.write("Despesas Capital")
with open("Relatorio.docx","w") as arquivo_5:
    arquivo_5.write("Relatorio")  

return files