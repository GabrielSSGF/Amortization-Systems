import os
import pandas as pd
import openpyxl

# tabela[0][0] = periodo        | Planilha financeira (S.A.C, S.A.F, S.A.M, S.ALM e S.A.A)
# tabela[0][1] = saldo atual    | Planilha financeira (S.A.C, S.A.F, S.A.M, S.ALM e S.A.A)
# tabela[0][2] = amortizacao    | Planilha financeira (S.A.C, S.A.F, S.A.M, S.ALM e S.A.A)
# tabela[0][3] = juros          | Planilha financeira (S.A.C, S.A.F, S.A.M, S.ALM e S.A.A)
# tabela[0][4] = prestacao      | Planilha financeira (S.A.C, S.A.F, S.A.M, S.ALM e S.A.A)
# tam = amortização total       | Planilha financeira (S.A.C, S.A.F, S.A.M, S.ALM e S.A.A)
# tj = juros total              | Planilha financeira (S.A.C, S.A.F, S.A.M, S.ALM e S.A.A)
# tp = prestação total          | Planilha financeira (S.A.C, S.A.F, S.A.M, S.ALM e S.A.A)
# tabelaFA[0][0] = depósito     | Fundo de Amortização (S.A.A)
# tabelaFA[0][1] = juros        | Fundo de Amortização (S.A.A)
# tabelaFA[0][2] = montante     | Fundo de Amortização (S.A.A)
# tm = montante total           | Fundo de Amortização (S.A.A)
# tjpf = juros total            | Fundo de Amortização (S.A.A)
# td = depósito total           | Fundo de Amortização (S.A.A)

# Loop infinito do programa

def padrao_de_colunas(worksheet):
    colunas = ['B', 'C', 'D', 'E', 'F', 'G']
    
    worksheet.column_dimensions['A'].width = 13
    
    for i in range(len(colunas)):
        worksheet.column_dimensions[colunas[i]].width = 30

def exportacao_xlsx(data_frames, planilhas):
    writer = pd.ExcelWriter(path, engine='openpyxl')
    for i, df in enumerate(data_frames):
        df.to_excel(writer, sheet_name=planilhas[i])
        workbook = writer.book
        worksheet = workbook[planilhas[i]]
        padrao_de_colunas(worksheet)
    writer._save()

def SAC():
    df = pd.DataFrame(columns=['Período', 'Saldo atual', 'Amortização', 'Juros', 'Prestação'])
    df.loc[0] = [dados_financiamento["periodo"], dados_financiamento["saldo"], 0, 0, 0]
    df.loc[0, 'Amortização'] = df.loc[0, 'Saldo atual'] / df.loc[0, 'Período']
        
    for i in range(1, df.loc[0, 'Período'] + 1):
        df.loc[i, 'Juros'] = df.loc[i-1, 'Saldo atual'] * dados_financiamento["taxajuros"]
        df.loc[i, 'Prestação'] = df.loc[0, 'Amortização'] + df.loc[i, 'Juros']
        df.loc[i, 'Saldo atual'] = df.loc[i-1, 'Saldo atual'] - df.loc[0, 'Amortização']
            
    tam = df['Amortização'].sum()
    tj = df['Juros'].sum()
    tp = df['Prestação'].sum()
        
    totais = {'Período': 'Total', 'Saldo atual': '', 'Amortização': tam, 'Juros': tj, 'Prestação': tp}
    df = df.append(totais, ignore_index=True)

    return df

# Método S.A.F - Sistema de Amortização Francês - Tabela Price
    
def SAF():
    df = pd.DataFrame(columns=['Período', 'Saldo atual', 'Amortização', 'Juros', 'Prestação'])
    tam, tj, tp, saldodevedor, df.loc[0, 'Saldo atual'], df.loc[0, 'Período'] = 0, 0, 0, 0, dados_financiamento["saldo"], dados_financiamento["periodo"]
    coef = (((1+dados_financiamento["taxajuros"])**df.loc[0, 'Período'])*dados_financiamento["taxajuros"])/(((1+dados_financiamento["taxajuros"])**df.loc[0, 'Período'])-1)
    df.loc[0, 'Prestação'] = df.loc[0, 'Saldo atual']*coef
    
    for i in range(1, df.loc[0, 'Período'] + 1):
        df.loc[i, 'Juros'] = df.loc[i-1, 'Saldo atual']*dados_financiamento["taxajuros"]
        df.loc[i, 'Amortização'] = df.loc[0, 'Prestação'] - df.loc[i, 'Juros']
        saldodevedor = df.loc[i-1, 'Saldo atual'] + df.loc[i, 'Juros']
        df.loc[i, 'Saldo atual'] = saldodevedor - df.loc[0, 'Prestação']
        tam += df.loc[i, 'Amortização']
        tj += df.loc[i, 'Juros']
        tp += df.loc[0, 'Prestação']
    
    totais = {'Período': 'Total', 'Saldo atual': '', 'Amortização': tam, 'Juros': tj, 'Prestação': tp}
    df = df.append(totais, ignore_index=True)
    
    return df

# Método S.A.A
    
def SAA():
    tabela[0][1], tabela[0][0], tam, tjpf, tjfa, tp, tm, td = dados_financiamento["saldo"], dados_financiamento["periodo"], 0, 0, 0, 0, 0, 0
    tabela[1][3] = tabela[0][1] * dados_financiamento["taxajuros"]
    tabela[1][4] = tabela[1][3]
    tabelaFA[1][0] = tabela[0][1] * (dados_financiamento["captacaomedia"]/(((1+dados_financiamento["captacaomedia"])**tabela[0][0]) - 1)) 
    tabelaFA[1][2] = tabelaFA[1][0]
        
    print("\nPLANILHA FINANCEIRA\n")
    
    print("Periodo: -Saldo atual: R$%.2f" % round(tabela[0][1],2), "  Amortizacao: - \tJuros: - \tPrestação: -")
    for i in range(1, tabela[0][0]+1):
        if(i==tabela[0][0]):
            tabela[i][2] = tabela[0][1]
            tabela[i][4] = tabela[i][2] + tabela[1][3]
            tp += tabela[i][4]
        else:
            tp += tabela[1][4]
        tam += tabela[i][2]
        tjpf += tabela[1][3]
        if (i!=tabela[0][0]):
            exibe_tab(i, tabela[0][1], tabela[1][2], tabela[1][3], tabela[1][4])
        else:
            print("Período: ", i, "Saldo atual: -  Amortização: R$%.2f" % round(tabela[i][2],2), "  Juros: R$%.2f" % round(tabela[1][3],2), "  Prestação: R$%.2f" % round(tabela[i][4],2))
    print("T O T A L I Z A Ç Õ E S --->", f"\t\t\t{'Amortização: R$%.2f' : ^20}" % round(tam,2), f"{'Juros: R$%.2f' : ^24}" % round(tjpf,2), f"{'Prestacao: R$%.2f' : ^10}" % round(tp, 2))
    
    print("\nFUNDO DE AMORTIZAÇÃO\n")
    
    print("Período:  - \tDepósito: - \tJuros: - \tMontante: -")
    for i in range(1, tabela[0][0]+1):
        if(i>1):
            tabelaFA[i][1] = tabelaFA[i-1][2] * dados_financiamento["captacaomedia"]
            tabelaFA[i][2] = tabelaFA[i-1][2] + tabelaFA[i][1]
        tjfa += tabelaFA[i][1]
        tm += tabelaFA[i][2]
        td += tabelaFA[1][0]
        exibe_tabFA(i, tabelaFA[1][0], tabelaFA[i][1], tabelaFA[i][2])
    print("T O T A L I Z A Ç Õ E S --->", f"\t{'Depósito: R$%.2f' : >20}" % round(td,2), f"\t{'Juros: R$%.2f' : >24}" % round(tjfa,2), f"\t{'Montante: R$%.2f' : >20}" % round(tm, 2))

# Método S.A.M - Sistema de Amortização Misto
    
def SAM():
    tabela[0][0], tabela[0][1] = dados_financiamento["periodo"], dados_financiamento["saldo"]
    print("\nPeríodo:  - \tSaldo atual: R$%.2f" % round(tabela[0][1],2), "\tAmortização:\t- \t\tJuros:\t- \t\tPrestação:\t-")
    coef = (((1+dados_financiamento["taxajuros"])**tabela[0][0])*dados_financiamento["taxajuros"])/(((1+dados_financiamento["taxajuros"])**tabela[0][0])-1)
    saldoatualSAC, prestacaoSAF, tam, tj, tp = tabela[0][1], tabela[0][1]*coef, 0, 0, 0
    amortizacaoSAC = (tabela[0][1]/tabela[0][0])
    for i in range(1, tabela[0][0] + 1):
        prestacaoSAC = amortizacaoSAC + (saldoatualSAC*dados_financiamento["taxajuros"])
        tabela[i][3] = tabela[i-1][1]*dados_financiamento["taxajuros"]
        saldoatualSAC -= amortizacaoSAC
        tabela[i][4] = (prestacaoSAC + prestacaoSAF)/2
        tabela[i][2] = tabela[i][4] - tabela[i][3]
        tabela[i][1] = tabela[i-1][1] - tabela[i][2]
        tam += tabela[i][2]
        tj += tabela[i][3]
        tp += tabela[i][4]
        if (i!=tabela[0][0]):
            exibe_tab(i, tabela[i][1], tabela[i][2], tabela[i][3], tabela[i][4])
        else:
            print("Período: ", i, f"{'Saldo atual: ' : >20}""\t-", f"\t{'Amortização: R$%.2f' : >15}" % round(tabela[i][2],2), f"\t{'Juros: R$%.2f' : >20}" % round(tabela[i][3],2), f"\t{'Prestação: R$%.2f' : >20}" % round(tabela[i][4],2))
    print("T O T A L I Z A Ç Õ E S --->", f"\t\t\t{'Amortização: R$%.2f' : ^20}" % round(tam,2), f"{'Juros: R$%.2f' : ^24}" % round(tj,2), f"{'Prestacao: R$%.2f' : ^10}" % round(tp, 2))

# Método S.A.Alemão - Sistema de Amortização Alemão
    
def SAALM():
    tabela[0][0], tabela[0][1], tam, tj, tp, amortizacaok, i = dados_financiamento["periodo"], dados_financiamento["saldo"], 0, 0, 0, 0, 0
    tabela[0][3] = dados_financiamento["taxajuros"]*tabela[0][1]
    tabela[0][4] = tabela[0][3]
    exibe_tab(i, tabela[0][1], amortizacaok, tabela[0][3], tabela[0][4])
    tabela[1][4] = (tabela[0][1]*dados_financiamento["taxajuros"])/(1-((1-dados_financiamento["taxajuros"])**tabela[0][0]))
    amortizacao1 = tabela[1][4] * (1-dados_financiamento["taxajuros"])**(tabela[0][0]-1)
    tabela[1][2] = amortizacao1
    tabela[1][3] = tabela[1][4] - tabela[1][2]
    tabela[1][1] = tabela[0][1] - tabela[1][2]
    exibe_tab(i+1, tabela[1][1], tabela[1][2], tabela[1][3], tabela[1][4])
    tp = tabela[0][4] + tabela[1][4]
    tam = tabela[1][2]
    tj = tabela[0][3]
    for i in range(2, tabela[0][0]+1):
        tabela[i][2] = tabela[i-1][2]/(1-dados_financiamento["taxajuros"])
        tabela[i][3] = tabela[1][4] - tabela[i][2]
        tabela[i][1] = tabela[i-1][1] - tabela[i][2]
        tam += tabela[i][2]
        tp += tabela[1][4]
        if (i == tabela[0][0]):
            tabela[i][3] = 0
        tj += tabela[i][3]
        if (i != tabela[0][0]):
            exibe_tab(i, tabela[i][1], tabela[i][2], tabela[i][3], tabela[1][4])
        else:
            print("Período: ", i, f"{'Saldo atual: ' : >20}""\t-", f"\t{'Amortização: R$%.2f' : >15}" % round(tabela[i][2],2), f"\t{'Juros: ' : >20}""\t-", f"\t{'Prestação: R$%.2f' : >20}" % round(tabela[1][4],2))
    print("T O T A L I Z A Ç Õ E S --->", f"\t\t\t{'Amortização: R$%.2f' : ^20}" % round(tam,2), f"{'Juros: R$%.2f' : ^24}" % round(tj,2), f"{'Prestacao: R$%.2f' : ^10}" % round(tp, 2))

    # Declaração de variáveis

dados_financiamento = {}

# Menu principal
    
print("\nOlá, bem vindo ao simulador de sistemas de amortização! Insira os dados de seu financiamento para prosseguir\n")

dados_financiamento["saldo"] = float(input("Insira o saldo a ser pago: "))
dados_financiamento["taxajuros"] = float(input("Insira a taxa de juros: "))
dados_financiamento["periodo"] = int(input("Insira o período: "))
caminho_relatorio = input('Insira o caminho para o diretório do arquivo: ')
path = f'{caminho_relatorio}/Simulações.xlsx'

tabela = [[0 for x in range(5)] for y in range(dados_financiamento["periodo"] + 1)]
tabelaFA = [[0 for x in range(3)] for y in range(dados_financiamento["periodo"] + 1)]

