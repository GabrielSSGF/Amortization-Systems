<h1 align="center">
  <br>
  <a><img src="https://www.dinkytown.net/images/loans.png" alt="Jira" width="200"></a>
  <br>
  Amortization Systems
  <br>
</h1>

<h4 align="center">A desktop app to plan your <a href="https://www.investopedia.com/terms/a/amortized_loan.asp#:~:text=An%20amortized%20loan%20is%20a%20type%20of%20loan%20that%20requires,towards%20reducing%20the%20principal%20amount." target="_blank">financing</a>.</h4>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#systems-explanation">Systems Explanation</a> •
  <a href="#planned-features">Planned Features</a> •
  <a href="#technologies-used">Technologies used</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#credits">Credits</a>
</p>

## ▶️ Project Status: Ongoing. . .

## ⚙️ Key Features
The project was developed with the objective of automating the calculations that are necessary when adopting an amortization system to pay a debt and/or loan by installments.

## 🧾 Systems Explanation
<details>
  <summary>📚 Content</summary>
  <p>

### Terminology
---
- Amortization: It is the payment made in installments and within a pre-established period;
- Principal: Total amount of the debt, that is, the actual amount that was borrowed or financed;
- Current balance: When executing the program, the current balance is the amount still to be paid;
- Installment: It is the value of the installment that was paid in the informed period

### French Amortization System
---
Also known as the *Price* Table, the French Amortization System is one of the most well-known and currently adopted models. Through it, payment is made through a set of successive and constant installments, usually with installments paid monthly in equal amounts, already with built-in interest. The calculation is done as follows:

![](https://www.maxieduca.com.br/blog/wp-content/uploads/2018/03/resposta-da-quest%C3%A3o-02.jpg "Formula used in the French Amortization System")

### Constant Amortization System
---
It consists of the constant payment of the debt based on periodic decreasing payments. That is, the more time passes, the smaller the installments of the outstanding balance are, while the amount is amortized in a constant manner in all periods.
In general, interest and capital are calculated only once and divided for payment in several installments during the settlement period. The amortization amount is calculated by dividing the initial capital by the number of installments to be paid. The calculation is done as follows:
 
**A = P / n**

Where:
- A = Amortization;
- P = Main;
- n = Number of installments. 

### Mixed Amortization System
---
The Mixed System is an amortization system that presents intermediate characteristics between the other two main amortization systems, the Constant Amortization System (SAC) and the French Amortization System (SAF).
Therefore, in the mixed amortization system, the borrower will pay a portion that is the average between the SAC and the Price System. To perform this calculation, it is necessary to add the portion of the SAC and the Price System and divide it by two. Therefore, it can be said that the SAM plots have an intermediate logic between the two systems.

### American Amortization System
---
In this system, the return of principal is made in one lump sum at the end of the amortization period. Interim amortizations are not foreseen during the term of the payments, and interest is paid periodically. Due to the financial impact that the system itself conceives, aiming at the one-time payment of the debt, it is necessary to set up a amortization fund, which will finance this amount. The fund is set up concurrently with interest payments on the principal through the use of the multi-operation capital accumulation factor.

### German Amortization System
---
The German System consists of settling a debt where interest is paid in advance in equal installments, except for the first payment which corresponds to the interest charged at the time of the financial transaction.
In this system, the last amortization must coincide with the payment, since all interest is charged in advance on previous installments, as well as all payments, with the exception of the first, must be equal.

  </p>
</details>

For those curious behind the logic used for the implementation of these systems.


## 🎯 Planned Features

- Complete interface for the desktop app;
- Storing multiple simulations by date;
- Option to export the grouped simulations in a Excel file.

## 🧰 Technologies used
- Python;
- Rust;
- Tauri;
- TypeScript;
- Visual Studio Code.

## 📑 How To Use
**Prerequisites:**
- Rust;
- Tauri;
- Python 3.10 (ou superior) instalado.

```bash
# Clone this repository
git clone https://github.com/GabrielSSGF/SistemaDeAmortizacao.git

# Go into the repository
cd SistemaDeAmortizacao/

# Run the app
python (or python3) Amortizacao.py

```
## 🖋️ Authors

**Gabriel Soares**  
LinkedIn: https://www.linkedin.com/in/gabriel-soares-588832199/

**Guilherme Vaiano Nogueira Mendonça**  
LinkedIn: https://www.linkedin.com/in/guilherme-mendon%C3%A7a-12a83720b/  
GitHub: https://github.com/GuilhermeVaiano
