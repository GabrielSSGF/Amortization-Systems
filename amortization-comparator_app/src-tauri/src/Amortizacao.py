import os
import pandas as pd
import openpyxl

def padrao_de_colunas(worksheet):
    colunas = ['B', 'C', 'D', 'E', 'F', 'G']
    
    worksheet.column_dimensions['A'].width = 13
    
    for i in range(len(colunas)):
        worksheet.column_dimensions[colunas[i]].width = 30

def exportacao_xlsx(data_frames, path): #, planilhas
    writer = pd.ExcelWriter(path, engine='openpyxl')
    for i, df in enumerate(data_frames):
        df.to_excel(writer, sheet_name=f'Sheet_{i}')  # Ou ajuste o nome da planilha conforme suas necessidades
        workbook = writer.book
        worksheet = workbook[f'Sheet_{i}']  # Ou ajuste o nome da planilha conforme suas necessidades
        padrao_de_colunas(worksheet)
    writer.close()

def SAC(dados_financiamento):
    df = pd.DataFrame(columns=['Período', 'Saldo atual', 'Amortização', 'Juros', 'Prestação'])
    df.loc[0] = [0, dados_financiamento["saldo"], "-", "-", "-"]
    df.loc[0, 'Amortização'] = df.loc[0, 'Saldo atual'] / dados_financiamento["periodo"]

    for i in range(1, dados_financiamento["periodo"] + 1):
        df.loc[i, 'Período'] = i
        df.loc[i, 'Juros'] = df.loc[i-1, 'Saldo atual'] * dados_financiamento["taxajuros"]
        df.loc[i, 'Prestação'] = df.loc[0, 'Amortização'] + df.loc[i, 'Juros']
        df.loc[i, 'Saldo atual'] = df.loc[i-1, 'Saldo atual'] - df.loc[0, 'Amortização']
        df.loc[i, 'Amortização'] = df.loc[0, 'Amortização']

    tam = df['Amortização'].sum()
    tj = df['Juros'].sum()
    tp = df['Prestação'].sum()

    totais = {'Período': 'Total', 'Saldo atual': '', 'Amortização': tam, 'Juros': tj, 'Prestação': tp}
    df_total = pd.DataFrame(totais, index=[df.shape[0]])  # Criar um novo dataframe com os totais

    # Ajustar a coluna "Período" como o índice do dataframe
    df.set_index('Período', inplace=True)
    df_total.set_index('Período', inplace=True)  # Definir a coluna "Período" como índice do dataframe de totais

    # Adicionar a linha de totais no final do dataframe
    df = pd.concat([df, df_total])

    return df

# Método S.A.F - Sistema de Amortização Francês - Tabela Price
    
def SAF(dados_financiamento):
    df = pd.DataFrame(columns=['Período', 'Saldo atual', 'Amortização', 'Juros', 'Prestação'])
    tam, tj, tp, saldodevedor, df.loc[0, 'Saldo atual'], df.loc[0, 'Período'] = 0, 0, 0, 0, dados_financiamento["saldo"], '-'
    coef = (((1+dados_financiamento["taxajuros"])**dados_financiamento["periodo"])*dados_financiamento["taxajuros"])/(((1+dados_financiamento["taxajuros"])**dados_financiamento["periodo"])-1)
    df.loc[0, 'Prestação'] = df.loc[0, 'Saldo atual']*coef
    
    for i in range(1, dados_financiamento["periodo"] + 1):
        df.loc[i, 'Período'] = i
        df.loc[i, 'Juros'] = df.loc[i-1, 'Saldo atual']*dados_financiamento["taxajuros"]
        df.loc[i, 'Amortização'] = df.loc[0, 'Prestação'] - df.loc[i, 'Juros']
        saldodevedor = df.loc[i-1, 'Saldo atual'] + df.loc[i, 'Juros']
        df.loc[i, 'Saldo atual'] = saldodevedor - df.loc[0, 'Prestação']
        df.loc[i, 'Prestação'] = df.loc[0, 'Prestação']
    
    tam = df['Amortização'].sum()
    tj = df['Juros'].sum()
    tp = df['Prestação'].sum()
    
    totais = {'Período': 'Total', 'Saldo atual': '', 'Amortização': tam, 'Juros': tj, 'Prestação': tp}
    df_total = pd.DataFrame(totais, index=[df.shape[0]])  # Criar um novo dataframe com os totais

    # Ajustar a coluna "Período" como o índice do dataframe
    df.set_index('Período', inplace=True)
    df_total.set_index('Período', inplace=True)  # Definir a coluna "Período" como índice do dataframe de totais

    # Adicionar a linha de totais no final do dataframe
    df = pd.concat([df, df_total])
    
    return df

# Método S.A.A
    
def SAA(dados_financiamento):
    saldo = dados_financiamento["saldo"]
    periodo = dados_financiamento["periodo"]

    df = pd.DataFrame(columns=['Período', 'Saldo atual', 'Amortização', 'Juros', 'Prestação'])
    dfFA = pd.DataFrame(columns=['Período', 'Depósito', 'Juros', 'Montante'])

    df.loc[0, 'Saldo atual'] = saldo

    df.loc[1, 'Juros'] = saldo * dados_financiamento["taxajuros"]
    df.loc[1, 'Prestação'] = df.loc[1, 'Juros']

    captacao_media = dados_financiamento["captacaomedia"]
    dfFA.loc[1, 'Depósito'] = saldo * (captacao_media / (((1 + captacao_media) ** periodo) - 1))
    dfFA.loc[1, 'Montante'] = dfFA.loc[1, 'Depósito']

    tam, tjpf, tp = 0, 0, 0

    for i in range(1, periodo + 1):
        if i == periodo:
            df.loc[i, 'Amortização'] = saldo
            df.loc[i, 'Prestação'] = df.loc[i, 'Amortização'] + df.loc[1, 'Juros']
            tp += df.loc[i, 'Prestação']
        else:
            tp += df.loc[1, 'Prestação']

        tam += df.loc[i, 'Amortização']
        tjpf += df.loc[1, 'Juros']

    total_df = {
        'Amortização': round(tam, 2),
        'Juros': round(tjpf, 2),
        'Prestação': round(tp, 2)
    }

    df.loc[periodo + 1, :] = ['Total'] + [total_df[col] for col in ['Amortização', 'Juros', 'Prestação']]

    tjfa, tm, td = 0, 0, 0

    for i in range(1, periodo + 1):
        if i > 1:
            dfFA.loc[i, 'Depósito'] = dfFA.loc[i - 1, 'Montante'] * captacao_media
            dfFA.loc[i, 'Montante'] = dfFA.loc[i - 1, 'Montante'] + dfFA.loc[i, 'Depósito']

        tjfa += dfFA.loc[i, 'Depósito']
        tm += dfFA.loc[i, 'Montante']
        td += dfFA.loc[1, 'Depósito']

    total_dfFA = {
        'Depósito': round(td, 2),
        'Juros': round(tjfa, 2),
        'Montante': round(tm, 2)
    }

    dfFA.loc[periodo + 1, :] = ['Total'] + [total_dfFA[col] for col in ['Depósito', 'Juros', 'Montante']]

    return df, dfFA

# Método S.A.M - Sistema de Amortização Misto
    
def SAM(dados_financiamento):
    df = pd.DataFrame(columns=['Período', 'Saldo atual', 'Amortização', 'Juros', 'Prestação'])

    periodo = dados_financiamento["periodo"]
    saldo = dados_financiamento["saldo"]
    taxajuros = dados_financiamento["taxajuros"]

    coef = (((1 + taxajuros) ** periodo) * taxajuros) / (((1 + taxajuros) ** periodo) - 1)
    saldoatualSAC, prestacaoSAF, tam, tj, tp = saldo, saldo * coef, 0, 0, 0
    amortizacaoSAC = (saldo / periodo)

    for i in range(1, periodo + 1):
        prestacaoSAC = amortizacaoSAC + (saldoatualSAC * taxajuros)

        df.loc[i, 'Período'] = i
        df.loc[i, 'Saldo atual'] = saldoatualSAC
        df.loc[i, 'Amortização'] = prestacaoSAC - (saldoatualSAC * taxajuros)
        df.loc[i, 'Juros'] = saldoatualSAC * taxajuros
        df.loc[i, 'Prestação'] = (prestacaoSAC + prestacaoSAF) / 2

        saldoatualSAC -= amortizacaoSAC

    tam = df['Amortização'].sum()
    tj = df['Juros'].sum()
    tp = df['Prestação'].sum()
        
    totais = {'Período': 'Total', 'Saldo atual': '', 'Amortização': tam, 'Juros': tj, 'Prestação': tp}
    df_total = pd.DataFrame(totais, index=[df.shape[0]])  # Criar um novo dataframe com os totais

    # Ajustar a coluna "Período" como o índice do dataframe
    df.set_index('Período', inplace=True)
    df_total.set_index('Período', inplace=True)  # Definir a coluna "Período" como índice do dataframe de totais

    # Adicionar a linha de totais no final do dataframe
    df = pd.concat([df, df_total])
    
    return df

# Método S.A.Alemão - Sistema de Amortização Alemão
    
def SAALM(dados_financiamento):
    periodo = dados_financiamento["periodo"]
    saldo = dados_financiamento["saldo"]
    taxajuros = dados_financiamento["taxajuros"]

    df = pd.DataFrame(columns=["Período", "Saldo atual", "Amortização", "Juros", "Prestação"])

    amortizacao0 = saldo * taxajuros / (1 - ((1 - taxajuros) ** periodo))
    amortizacao_list = [amortizacao0 * (1 - taxajuros) ** (periodo - 1)]

    for i in range(1, periodo):
        amortizacao_list.append(amortizacao_list[i-1] / (1 - taxajuros))

    df["Período"] = range(1, periodo + 1)
    df["Saldo atual"] = saldo - pd.Series(amortizacao_list).cumsum()
    df["Amortização"] = pd.Series(amortizacao_list)
    df["Juros"] = saldo * taxajuros - pd.Series(amortizacao_list)
    df["Prestação"] = saldo * taxajuros / (1 - ((1 - taxajuros) ** periodo))
    
    # Print the totalizations
    tam = df["Amortização"].sum()
    tj = df["Juros"].sum()
    tp = df["Prestação"].sum()
    totais = {'Período': 'Total', 'Saldo atual': '', 'Amortização': tam, 'Juros': tj, 'Prestação': tp}
    df = df.append(totais, ignore_index=True)
    
    return df

dados_financiamento = {}
dados_financiamento["saldo"] = 10000
dados_financiamento["periodo"] = 5
dados_financiamento["taxajuros"] = 0.02

print(SAM(dados_financiamento))
# exportacao_xlsx([df_sac], "path")  # Note que agora estamos passando uma lista com o dataframe como argumento"""