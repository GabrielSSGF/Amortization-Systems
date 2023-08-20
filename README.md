<h1 align="center">
  <br>
  <a><img src="https://www.dinkytown.net/images/loans.png" alt="Jira" width="200"></a>
  <br>
  Amortization Systems
  <br>
</h1>

<h4 align="center">A desktop app to plan your <a href="https://www.investopedia.com/terms/a/amortized_loan.asp#:~:text=An%20amortized%20loan%20is%20a%20type%20of%20loan%20that%20requires,towards%20reducing%20the%20principal%20amount." target="_blank">financing</a>.</h4>

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

```
P = (PV * r * (1 + r)^n) / ((1 + r)^n - 1)
```

Where:
- P: Installment amount (monthly payment);
- PV: Loan amount (or present value);
- r: Monthly interest rate, calculated as the annual rate divided by 12 and expressed in decimal (e.g., if the annual rate is 6%, r will be 0.06/12 = 0.005);
- n: Total number of periods (or installments) to repay the loan;

This formula calculates the value of the fixed monthly installment that will be paid over the loan term. 

*Note:* that the composition of interest and principal changes in each installment, but the total value of the installment remains constant throughout the entire period. Interest is calculated on the remaining outstanding balance, which gradually decreases with each payment, while the principal amount paid increases, resulting in a gradual reduction of the loan balance until it is fully repaid at the end of the term.


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
- Python 3.10 (or higher) installed.

```bash
# Clone this repository
git clone https://github.com/GabrielSSGF/SistemaDeAmortizacao.git

# Go into the repository
cd Amortization-Systems/

# Run the app
python (or python3) Amortizacao.py

```
## 🖋️ Authors

**Gabriel Soares**  
LinkedIn: https://www.linkedin.com/in/gabriel-soares-588832199/

**Guilherme Vaiano Nogueira Mendonça**  
LinkedIn: https://www.linkedin.com/in/guilherme-vaiano/  
GitHub: https://github.com/GuilhermeVaiano
