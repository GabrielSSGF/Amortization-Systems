package principal;

import java.math.RoundingMode;
import java.text.DecimalFormat;

//Subclasse de Amortizacao Americana para acomodar a captação média
public class AmortizacaoAmericana extends Amortizacao {
    double captacaomedia;

    // Construtor da subclasse
    public AmortizacaoAmericana(double pr, double sa, double txj, double cm) {
        super(pr, sa, txj);
        captacaomedia = cm;
    }

    // Método S.A.A
    public void SAA() {
        DecimalFormat decimalFormat = new DecimalFormat("R$#,##0.00");
        decimalFormat.setRoundingMode(RoundingMode.DOWN);
        double amortizacao=0, jurosPF=0, prestacao=0, deposito, jurosFA=0, 
        	   montante, tam=0, tjpf=0, tp=0, tjfa=0, tm=0, td=0;
        int i = 0;
        
        exibir0(i, saldoatual, amortizacao, jurosPF, prestacao);
        jurosPF = saldoatual * taxajuros;
        prestacao = jurosPF - amortizacao;
        deposito = saldoatual*((captacaomedia)/(potencia((1+captacaomedia),periodo)-1));
        montante = deposito;
        
        System.out.println("\nPLANILHA FINANCEIRA\n");
        
        for(i = 1; i<=periodo; i++) {
            if(i==periodo) {
                amortizacao = saldoatual;
                saldoatual = 0;
                prestacao = amortizacao + jurosPF;
            }
            tam += amortizacao;
            tjpf += jurosPF;
            tp += prestacao;
            exibirSAA1(i, saldoatual, amortizacao, jurosPF, prestacao); 
        }

        System.out.println("Totalizações\t - \tAmortização: "+decimalFormat.format(tam)+"\tJuros:\t"+decimalFormat.format(tjpf)
        +"\tPrestacao:\t"+decimalFormat.format(tp));

        i=0;
        System.out.println("\nFUNDO DE AMORTIZAÇÃO\n");
        exibir1(i, deposito, jurosFA, montante);

        for(i=1; i<=periodo; i++) {
            if(i>1) {
                jurosFA = montante * captacaomedia;
            }
            montante += jurosFA;
            tjfa += jurosFA;
            tm += montante;
            td += deposito;
            exibirSAA2(i, deposito, jurosFA, montante);
        }

        System.out.println("Totalizações -  Depósito:\t"+ decimalFormat.format(td) 
        +"\tJuros:\t"+ decimalFormat.format(tjfa)+"\tMontante:\t"+ decimalFormat.format(tm));
    }
}
