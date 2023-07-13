import os

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

while True:

    # Exibe os valores da planilha financeira
    
    def exibe_tab(periodo, saldo, amortizacao, juros, prestacao):
        print("Período: ", periodo, f"\t{'Saldo atual: R$%.2f' : >20}" % round(saldo,2), f"\t{'Amortização: R$%.2f' : >20}" % round(amortizacao,2), f"{'Juros: R$%.2f' : >20}" % round(juros,2), f"\t{'Prestação: R$%.2f' : >20}" % round(prestacao,2))

    # Exibe valores do fundo de amortização
    
    def exibe_tabFA(periodo, deposito, juros, montante):
        print("Periodo: ", periodo, f"{'Depósito: R$%.2f' : ^20}" % round(deposito,2), f"{'Juros: R$%.2f' : ^20}" % round(juros,2), f"{'Montante: R$%.2f' : ^20}" % round(montante,2))

    # Método S.A.C - Sistema de Amortização Constante
    
    def SAC():
        tabela[0][1], tabela[0][0], tam, tj, tp = dados_financiamento["saldo"], dados_financiamento["periodo"], 0, 0, 0
        print("\nPeríodo:  -",f"{'Saldo atual: R$%.2f' : ^30}" % round(tabela[0][1],2), f"{'Amortização:   -' : ^20}", f"\t{'Juros:   -' : ^25}",  f"{'Prestação:   -' : ^15}")
        tabela[0][2] = tabela[0][1]/tabela[0][0]
        for i in range(1, tabela[0][0] + 1):
            tabela[i][3] = tabela[i-1][1]*dados_financiamento["taxajuros"]
            tabela[i][4] = tabela[0][2] + tabela[i][3]
            tabela[i][1] = tabela[i-1][1] - tabela[0][2]
            tam += tabela[0][2]
            tj += tabela[i][3]
            tp += tabela[i][4]
            if (i!=tabela[0][0]):
                exibe_tab(i, tabela[i][1], tabela[0][2], tabela[i][3], tabela[i][4])
            else:
                print("Período: ", i,f"{'Saldo atual: ' : >20}""-\t", f"\t{'Amortização: R$%.2f' : >20}" % round(tabela[0][2],2), f"{'Juros: R$%.2f' : >20}" % round(tabela[i][3],2), f"\t{'Prestação: R$%.2f' : >20}" % round(tabela[i][4],2))
        print("T O T A L I Z A Ç Õ E S --->", f"\t\t\t{'Amortização: R$%.2f' : ^20}" % round(tam,2), f"{'Juros: R$%.2f' : ^24}" % round(tj,2), f"{'Prestacao: R$%.2f' : ^10}" % round(tp, 2))

    # Método S.A.F - Sistema de Amortização Francês - Tabela Price
    
    def SAF():
        tam, tj, tp, saldodevedor, tabela[0][1], tabela[0][0] = 0, 0, 0, 0, dados_financiamento["saldo"], dados_financiamento["periodo"]
        print("\nPeríodo:  -",f"{'Saldo atual: R$%.2f' : ^30}" % round(tabela[0][1],2), f"{'Amortização:   -' : ^20}", f"\t{'Juros:   -' : ^25}",  f"{'Prestação:   -' : ^15}")
        coef = (((1+dados_financiamento["taxajuros"])**tabela[0][0])*dados_financiamento["taxajuros"])/(((1+dados_financiamento["taxajuros"])**tabela[0][0])-1)
        tabela[0][4] = tabela[0][1]*coef
        for i in range(1, tabela[0][0] + 1):
            tabela[i][3] = tabela[i-1][1]*dados_financiamento["taxajuros"]
            tabela[i][2] = tabela[0][4] - tabela[i][3]
            saldodevedor = tabela[i-1][1] + tabela[i][3]
            tabela[i][1] = saldodevedor - tabela[0][4]
            tam += tabela[i][2]
            tj += tabela[i][3]
            tp += tabela[0][4]
            if (i!=tabela[0][0]):
                exibe_tab(i, tabela[i][1], tabela[i][2], tabela[i][3], tabela[0][4])
            else:
                print("Período: ", i, f"{'Saldo atual: ' : >20}""-\t", f"\t{'Amortização: R$%.2f' : >15}" % round(tabela[i][2],2), f"\t{'Juros: R$%.2f' : >20}" % round(tabela[i][3],2), f"\t{'Prestação: R$%.2f' : >20}" % round(tabela[0][4],2))
        print("T O T A L I Z A Ç Õ E S --->", f"\t\t\t{'Amortização: R$%.2f' : ^20}" % round(tam,2), f"{'Juros: R$%.2f' : ^24}" % round(tj,2), f"{'Prestacao: R$%.2f' : ^10}" % round(tp, 2))

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
    simulacao = 0
    sim_comparacao = []
   
    # Função de menu para qual tipo de sistema o usuário selecionará

    def escolha_sistema():
        dados_financiamento["tiposistema"] = input("\nEscolha qual sistema de amortização deseja usar: \n" +
        "<A> Sistema de Amortização Constante (S.A.C)\n" +
        "<B> Sistema de Amortização Francês (S.A.F)\n" +
        "<C> Sistema de Amortização Americano (S.A.A)\n" +
        "<D> Sistema de Amortização Misto (S.A.M)\n" +
        "<E> Sistema de Amortização Alemão (S.A.ALM)\n").upper()
        sim_comparacao.append(dados_financiamento["tiposistema"])
        
    # Função que verifica qual sistema foi escolhido pelo usuário 
    
    def verifica_sistema():
        x = 0
        num_simulacoes = 0
        while x <= simulacoes:
            x += 1
            num_simulacoes += 1
            if ("C" in sim_comparacao):
                dados_financiamento["captacaomedia"] = float(input("Tendo escolhido o S.A.A, insira o valor da captação média: "))
                os.system('cls')
                print("\nSIMULAÇÃO N°", num_simulacoes, " - S.A.A")
                SAA()
                sim_comparacao.remove("C")
            elif ("A" in sim_comparacao):
                print("\nSIMULAÇÃO N°", num_simulacoes, " - S.A.C")
                SAC()
                sim_comparacao.remove("A")
            elif ("B" in sim_comparacao):
                print("\nSIMULAÇÃO N°", num_simulacoes, " - S.A.F - Tabela Price")
                SAF()
                sim_comparacao.remove("B")
            elif ("D" in sim_comparacao):
                print("\nSIMULAÇÃO N°", num_simulacoes, " - S.A.M")
                SAM()
                sim_comparacao.remove("D")
            elif ("E" in sim_comparacao):
                print("\nSIMULAÇÃO N°", num_simulacoes, " - S.A.ALM")
                SAALM()
                sim_comparacao.remove("E")
                
    os.system('cls')
    
    # Menu principal
    
    print("\nOlá, bem vindo ao simulador de sistemas de amortização! Insira os dados de seu financiamento para prosseguir\n")

    dados_financiamento["saldo"] = float(input("Insira o saldo a ser pago: "))
    dados_financiamento["taxajuros"] = float(input("Insira a taxa de juros: "))
    dados_financiamento["periodo"] = int(input("Insira o período: "))

    tabela = [[0 for x in range(5)] for y in range(dados_financiamento["periodo"] + 1)]
    tabelaFA = [[0 for x in range(3)] for y in range(dados_financiamento["periodo"] + 1)]

    opcao = input("\nO que você gostaria de fazer?\n" +
                "<S> - Para Simular um financiamento com um sistema específico\n" +
                "<C> - Para Comparar seu financiamento em diferentes sistemas: \n").upper()
    while opcao=="S" or opcao=="C":
        if opcao=="S":
            os.system('cls')
            print("\nMuito bem, vamos começar a simulação")
            simulacao += 1
            simulacoes = 1
            escolha_sistema()
            verifica_sistema()
            break
        if opcao=="C":
            simulacoes = int(input("\nMuito bem, quantas simulações serão feitas?\n"))
            os.system('cls')
            print("\nMuito bem, vamos começar as simulações")
            for i in range (0,simulacoes):   
                escolha_sistema()
                os.system('cls')
                os.system('cls')
                simulacao += 1
                if simulacao == 1:
                    print("Simulações escolhidas até agora: ", *sim_comparacao)
                elif simulacao > 1:
                    print("Simulações escolhidas até agora: ", ", ".join([str(i) for i in sim_comparacao]))
            os.system('cls')
            os.system('cls')
            verifica_sistema()
            break
    
    # Fim/restart do programa
    
    reiniciar = input("\nObrigado por usar o sistema! Deseja sair ou simular outro financiamento?" +
                    "\n<S> - Sair" +
                    "\n<N> - Simular novamente\n").upper()
    while reiniciar=="S" or reiniciar=="N":
        if reiniciar=="S":
            exit()
        elif reiniciar=="N":
            os.system('cls')
            os.system('cls')
            os.system('cls')
            os.system('cls')
            break