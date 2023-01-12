package principal;
import java.math.RoundingMode;
import java.text.DecimalFormat;

public class Amortizacao {
    double periodo, saldoatual, taxajuros;
    
    // Construtor inicializador
    public Amortizacao (double pr, double sa, double txj) {
        periodo = pr;
        saldoatual = sa;
        taxajuros = txj;
    }

    // Construtor cópia
    public Amortizacao(Amortizacao A) {
        this.periodo = A.periodo;
        this.saldoatual = A.saldoatual;
        this.taxajuros = A.taxajuros;
    }
        
    // Destrutor de classe
    public void finalize() {}

    // Calculo de expoente
    static double potencia(double n, double power) {
        double res = 1;
        for(double i = 1; i <= power; i++) {
            res = res*n;
        }
        return res;
    }

    // Exibição dos elementos da tabela S.A.C/S.A.F/S.A.M/S.A.Alemão convertidos em Real e Decimal
    public static void exibirTAB(int valor0, double valor1, double valor2, double valor3, double valor4) {
    	
        DecimalFormat decimalFormat = new DecimalFormat("R$#,##0.00");
        decimalFormat.setRoundingMode(RoundingMode.DOWN);
        System.out.println("Período: " + valor0 + "\tSaldo atual:\t" + decimalFormat.format(valor1)
        +" \tAmortização:\t"+ decimalFormat.format(valor2)+"\tJuros: "+ decimalFormat.format(valor3)
        +"\t\tPrestação:\t" + decimalFormat.format(valor4));
    }

    // Exibição os elementos do periodo 0 das tabelas S.A.C/S.A.F/S.A.M/S.A.Alemão convertidos em Real e Decimal
    public static void exibir0(int valor0, double valor1, double valor2, double valor3, double valor4) {
    	
        DecimalFormat decimalFormat = new DecimalFormat("R$#,##0.00");
        decimalFormat.setRoundingMode(RoundingMode.DOWN);
        System.out.println("Período: " + valor0 + "\tSaldo atual:\t" + decimalFormat.format(valor1)
        +"\tAmortização:\t"+decimalFormat.format(valor2)+"\t\tJuros:\t"+decimalFormat.format(valor3)
        +"\t\tPrestação:\t" + decimalFormat.format(valor4));
    }
    
    // Exibição os elementos do periodo 0 do fundo de amortizaçao da tabela S.A.A convertidos em Real e Decimal
    public static void exibir1(int valor0, double valor1, double valor2, double valor3) {
        DecimalFormat decimalFormat = new DecimalFormat("R$#,##0.00");
        decimalFormat.setRoundingMode(RoundingMode.DOWN);
        System.out.println("Período: " + valor0 + "\tDepósito:\t" + decimalFormat.format(valor1)
        +"\tJuros:\t"+decimalFormat.format(valor2)+"\t\tMontante:\t"+decimalFormat.format(valor3));
    }

    // Exibição dos elementos da planilha financeira da tabela S.A.A convertidos em Real e Decimal
    public static void exibirSAA1(int valor0, double valor1, double valor2, double valor3, double valor4) {
    	
        DecimalFormat decimalFormat = new DecimalFormat("R$#,##0.00");
        decimalFormat.setRoundingMode(RoundingMode.DOWN);
        System.out.println("Período: " + valor0 + "\tSaldo atual:\t" + decimalFormat.format(valor1) 
        + "\tAmortização:\t" + decimalFormat.format(valor2) + "\tJuros:\t" + decimalFormat.format(valor3) 
        + "\tPrestação:\t" + decimalFormat.format(valor4));   
    }

    // Exibição os elementos do fundo de amortizaçao da tabela S.A.A convertidos em Real e Decimal
    public static void exibirSAA2(int valor0, double valor1, double valor2, double valor3) {
        DecimalFormat decimalFormat = new DecimalFormat("R$#,##0.00");
        decimalFormat.setRoundingMode(RoundingMode.DOWN);
        System.out.println("Período: " + valor0 + "\tDepósito:\t" + decimalFormat.format(valor1) + "\tJuros:\t" + decimalFormat.format(valor2) 
        + "\tMontante:\t" + decimalFormat.format(valor3));
    }

    // Método S.A.C - Sistema de Amortização Constante
    public void SAC() {
        DecimalFormat decimalFormat = new DecimalFormat("R$#,##0.00");
        decimalFormat.setRoundingMode(RoundingMode.DOWN);
        double amortizacao, juros, prestacao, tam=0, tj=0, tp=0;
        amortizacao = saldoatual/periodo;
        for (int i = 1; i<=periodo; i++) {
            juros = saldoatual*taxajuros;
            prestacao = amortizacao + juros;
            saldoatual -= amortizacao;
            tam = tam + amortizacao;
            tj = tj + juros;
            tp = tp + prestacao;
            exibirTAB(i, saldoatual, amortizacao, juros, prestacao);
        }
        System.out.println("\nTotalizações - \tAmortização: "+decimalFormat.format(tam)+"\tJuros: "+decimalFormat.format(tj)
        +"\tPrestacao: "+decimalFormat.format(tp));
    }

    // Método S.A.F - Sistema de Amortização Francês - Tabela Price
    public void SAF() {
        DecimalFormat decimalFormat = new DecimalFormat("R$#,##0.00");
        decimalFormat.setRoundingMode(RoundingMode.DOWN);
        double coef = ((potencia((1+taxajuros),periodo))*taxajuros)/((potencia((1+taxajuros),periodo))-1);
        double amortizacao=0, juros=0, saldodevedor, prestacao=0, tam=0, tj=0, tp=0;
        int i = 0;
        exibir0(i, saldoatual, amortizacao, juros, prestacao);
        prestacao = saldoatual*coef;
        
        for(i = 1; i<=periodo; i++) {
            juros = saldoatual*taxajuros;
            amortizacao = prestacao - juros;
            saldodevedor = saldoatual + juros;
            saldoatual = saldodevedor - prestacao;
            tam += amortizacao;
            tj += juros;
            tp += prestacao;
            exibirTAB(i, saldoatual, amortizacao, juros, prestacao);
        }
        System.out.println("Totalizações - \t\t\t\t\tAmortização:\t"+decimalFormat.format(tam)+"\tJuros: "+decimalFormat.format(tj)
        +"\t\tPrestacao:\t"+decimalFormat.format(tp));
    }

    
    // Método S.A.M - Sistema de Amortização Misto
    public void SAM() {
        DecimalFormat decimalFormat = new DecimalFormat("R$#,##0.00");
        decimalFormat.setRoundingMode(RoundingMode.DOWN);
        double coef = ((potencia((1+taxajuros),periodo))*taxajuros)/((potencia((1+taxajuros),periodo))-1);
        double amortizacao=0, amortizacaoSAC, juros=0, prestacaoSAF=0, prestacaoSAC, prestacaoSAM=0, saldoatualSAC=saldoatual, tam=0, tj=0, tp=0;
        int i = 0;
        exibir0(i, saldoatual, amortizacao, juros, prestacaoSAM);
        prestacaoSAF = saldoatual*coef;
        amortizacaoSAC=(saldoatual/periodo);
        for(i = 1; i<=periodo; i++) {
            prestacaoSAC = amortizacaoSAC + (saldoatualSAC*taxajuros);
            juros = saldoatual*taxajuros;
            saldoatualSAC -= amortizacaoSAC;
            prestacaoSAM = (prestacaoSAC + prestacaoSAF)/2;
            amortizacao = prestacaoSAM - juros;
            saldoatual -= amortizacao;
            tam += amortizacao;
            tj += juros;
            tp += prestacaoSAM;
            exibirTAB(i, saldoatual, amortizacao, juros, prestacaoSAM);
        }
        System.out.println("Totalizações - \t\t\t\t\tAmortização:\t"+decimalFormat.format(tam)+"\tJuros:\t"+decimalFormat.format(tj)
        +"\tPrestacao:\t"+ decimalFormat.format(tp));
    }

    // Método S.A.Alemão - Sistema de Amortização Alemão
    public void SAALM() {
        DecimalFormat decimalFormat = new DecimalFormat("R$#,##0.00");
        decimalFormat.setRoundingMode(RoundingMode.DOWN);
        double amortizacaok=0, amortizacao1, juros, prestacao=0, tam=0, tj=0, tp=0;
        int i = 0;
        juros = taxajuros*saldoatual;
        exibirTAB(i, saldoatual, amortizacaok, juros, prestacao);
        prestacao = (saldoatual*taxajuros)/(1-potencia((1-taxajuros), periodo));
        amortizacao1 = prestacao * potencia((1-taxajuros),periodo-1);
        amortizacaok = amortizacao1;
        juros = prestacao - amortizacaok;
        saldoatual -= amortizacaok;
        i = 1;
        exibirTAB(i, saldoatual, amortizacaok, juros, prestacao);
        for(i = 2; i<=periodo; i++) {
            amortizacaok = amortizacaok/(1-taxajuros);
            juros = prestacao - amortizacaok;
            saldoatual -= amortizacaok;
            if (i == periodo) {
                amortizacaok = 0;
                juros = 0;
            }
            tam += amortizacaok;
            tj += juros;
            tp += prestacao;
            exibirTAB(i, saldoatual, amortizacaok, juros, prestacao);
        }
        System.out.println("Totalizações - \t\t\t\t\tAmortização:\t"+decimalFormat.format(tam)+"\tJuros:\t"+decimalFormat.format(tj)
        +"\tPrestacao:\t"+ decimalFormat.format(tp));
    }
    
}

