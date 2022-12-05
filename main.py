"""
Projeto Final da Extensão - Introdução ao Python
Modulo Main
Autor: Brunno Henrique Sibin
Data: 05/12/2022
Versão: 0.0.3
"""
import view
import model
import os
import shutil

def main():

    dados=view.entrada()
    files=model.arquivos()

    model.os.rename("DespesasCorrentes.xlsx","Planilhas\\DespesasCorrentes.xlsx")
    model.os.rename("DespesasCorrentes.docx","Documentos\\DespesasCorrentes.docx")
    model.os.rename("DespesasCapital.xlsx","Planilhas\\DespesasCapital.xlsx")
    model.os.rename("DespesasCapital.docx","Documentos\\DespesasCapital.docx")        
    model.os.rename("Relatorio.docx","Documentos\\Relatorio.docx")

if __name__ == "__main__":
    main()
