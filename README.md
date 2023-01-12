# Sistemas de Amortização

# Sobre o Projeto
O projeto foi desenvolvido com o objetivo de automatizar os cálculos que são necessários realizar ao adotar um sistema de amortização para pagar uma dívida e/ou empréstimo por prestações.

# **Descrição do projeto**
O projeto consiste no desenvolvimento da classe **'Amortização'**, no qual realiza o cálculo de um empréstimo, financiamento ou dívida a partir de um dos sistemas de amortizações existentes. Ao passar como entrada as informações de valor total a ser pago, a quantidade de parcelas e o valor do juros, o usuário poderá escolher o tipo de sistema de amortização que será utilizado para o pagamento e o código realizará os cálculos necessários, exibindo os valores das prestações, das amortizações e dos juros de cada período, exibindo saldo atual após o pagamento ser realizado, ou seja, o valor que ainda falta ser pago. Na imagem abaixo, é possível visualizar um exemplo de saída apresentada pelo programa.

<a href="https://imgur.com/zIj4Egq"><img src="https://i.imgur.com/zIj4Egq.png" title="source: imgur.com" align="middle"/></a>

A seguir, serão apresentados os tipos de sistemas de amortizações presentes na classe.

## **Sistema de Amortização Americano**
Nesse sistema, a devolução do principal é feita de uma só vez no final do período de amortização. Não são previstas amortizações intermediárias durante a vigência dos pagamentos, sendo os juros pagos periodicamente. Devido ao impacto financeiro que o próprio sistema concebe visando o pagamento único da dívida, faz se necessária a constituição de um fundo de amortização, o qual irá financiar tal quantia. O fundo é constituído concomitantemente aos pagamentos de juros do principal através do uso do fator de acumulação de capital por operação múltipla.
  
  

## **Sistema de Amortização Francês**
Também conhecido como Tabela *Price*, o Sistema de Amortização Francês Sistema de Amortização Francês é um dos modelos mais conhecidos e adotados atualmente. Através dele, o pagamento é feito através de um conjunto de prestações sucessivas e constantes, geralmente com parcelas pagas mensalmente em valores iguais, já com juros embutidos. O cálculo é feito da seguinte maneira:

![](https://www.maxieduca.com.br/blog/wp-content/uploads/2018/03/resposta-da-quest%C3%A3o-02.jpg "Fórmula utilizada no Sistema de Amortização Francês")


## **Sistema de Amortização Alemão**
O Sistema Alemão consiste em liquidar uma dívida onde os juros são pagos antecipadamente com prestações iguais, exceto o primeiro pagamento que corresponde aos juros cobrados no momento da operação financeira.
Nesse sistema, a última amortização deve coincidir com o pagamento, uma vez que todos os juros são cobrados antecipadamente nas prestações anteriores, assim como todos os pagamentos, com exceção do primeiro, devem ser iguais. 

## **Sistema de Amortização Misto**
O Sistema Misto é um sistema de amortização  que apresenta características intermediárias entre os outros dois principais sistemas de amortização, o Sistema de Amortização Constante (SAC) e o Sistema de Amortização Francês (SAF).
Logo, no sistema de amortização misto, o tomador do empréstimo irá pagar uma parcela que é a média entre o SAC e o Sistema Price. Para realizar esse cálculo, é necessário somar a parcela do SAC e do Sistema Price e dividir por dois. Portanto, pode-se dizer que as parcelas do SAM possuem uma lógica intermediária entre os dois sistemas.

## **Sistema de Amortização Constante**
Consiste no pagamento constante da dívida com base em pagamentos periódicos decrescentes. Ou seja, quanto mais o tempo passa, menores ficam as parcelas de quitação do saldo devedor enquanto o valor é amortizado de maneira constante em todos os períodos.
De forma geral, os juros e o capital são calculados uma única vez e divididos para o pagamento em várias parcelas durante o prazo de quitação. O valor da amortização é calculado através da divisão entre o capital inicial e o número de prestações a serem pagas. O cálculo é feito da seguinte maneira: 
 
**A = P / n**  
Onde:  
- A = Amortização;  
- P = Principal;  
- n = Número de prestações.  

### **Dicionário**

- Amortização: É o pagamento feito de forma parcelada e em um prazo pré-estabelecido;  
- Principal: Valor total da dívida, ou seja, o montante real que foi emprestado ou financiado;  
- Saldo atual: Na execução do programa, o saldo atual se trata do valor que ainda deverá ser pago;
- Prestação: É o valor da parcela que foi pago no período informado.   

# **Status do Projeto**  
✅Finalizado


# **Tecnologias utilizadas**
- Java;  
- Eclipse IDE;  
- Visual Studio Code.

# **Como utilizar**
**Pré-requisitos: Java 18 (ou superior) instalado.**  

```bash
# clonar repositorio:
git clone https://github.com/GabrielSSGF/SistemaDeAmortizacao.git

# entrar na pasta do projeto com o Prompt de Comando 
# (Obs.: O comando a seguir é feito a partir de onde a pasta foi salva)
cd SistemaDeAmortizacao/src/principal

# Compilar a main através do seguinte comando:
javac -cp .. Main.java

# Após compilar, basta executar o programa:
java -cp .. Main.java

```
# Autores

**Gabriel Soares**  
LinkedIn: https://www.linkedin.com/in/gabriel-soares-588832199/

**Guilherme Vaiano Nogueira Mendonça**  
LinkedIn: https://www.linkedin.com/in/guilherme-mendon%C3%A7a-12a83720b/  
GitHub: https://github.com/GuilhermeVaiano