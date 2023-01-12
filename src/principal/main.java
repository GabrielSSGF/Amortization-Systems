package principal;

import java.util.Locale;
import java.util.Scanner;


public class Main {

	public static void main(String[] args) {
		Locale.setDefault(Locale.US);
		Scanner entrada = new Scanner(System.in);

		System.out.println("Quantidade de parcelas: ");
		double qtdMeses = entrada.nextDouble();

		System.out.println("Valor a ser pago: ");
		double valorPag = entrada.nextDouble();

		System.out.println("Valor do juros (formato decimal): ");
		double valorJuros = entrada.nextDouble();
		while (valorJuros <= 0 || valorJuros > 1) {

			valorJuros = entrada.nextDouble();

		}

		System.out.println("Escolha o número da amortização que será utilizada:\n"
				+ "(1) Sistema de Amortizacao Americano\n"
				+ "(2) Sistema de Amortizacao Frances\n"
				+ "(3) Sistema de Amortizacao Alemao\n"
				+ "(4) Sistema de Amortizacao Misto\n"
				+ "(5) Sistema de Amortizacao Constante\n");
		int tipoAmort = entrada.nextInt();
		while (tipoAmort <= 0 || tipoAmort > 5) {
			System.out.println("Valor invalido! Por favor, digite um valor correto.");
			tipoAmort = entrada.nextInt();
		}
		Amortizacao calculo = new Amortizacao(qtdMeses, valorPag, valorJuros);

		switch (tipoAmort) {

			case 1:
				System.out.println("Digite o valor da captacao media: \n");
				double capMed = entrada.nextDouble();
				while (capMed < 0 || capMed > 1) {
					System.out.println("Valor invalido! Por favor, digite um valor correto (entre 0 e 1).");
					capMed = entrada.nextDouble();
				}
				AmortizacaoAmericana calc = new AmortizacaoAmericana(qtdMeses, valorPag, valorJuros, capMed);
				calc.SAA();
				break;

			case 2:
				calculo.SAF();
				break;

			case 3:
				calculo.SAALM();
				break;

			case 4:
				calculo.SAM();
				break;

			case 5:
				calculo.SAC();
				break;
		}
		System.out.println("Fim do programa.");
		entrada.close();
	}

}
