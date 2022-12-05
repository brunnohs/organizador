"""
Projeto Final da Extensão - Introdução ao Python
Modulo View - Definição de Diretorios e Criação de Pastas
Autor: Brunno Henrique Sibin
Data: 05/12/2022
Versão: 0.0.3
"""

import os
import shutil

def entrada ():

diretorio="C:\\Users\\Bruno\\Desktop"
pasta_python="C:\\Users\\Bruno\\Desktop\\Pasta Python"

os.chdir(str(diretorio))

pasta_python="Pasta Python/"
if (not os.path.exists(pasta_python)):
    os.mkdir(pasta_python)

os.chdir(str(pasta_python))

documentos="Documentos/"
if (not os.path.exists(documentos)):
    os.mkdir(documentos)

planilhas="Planilhas/"
if (not os.path.exists(planilhas)):
    os.mkdir(planilhas)

return dados