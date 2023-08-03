import { useState, ChangeEvent, FormEvent } from 'react';
import styles from './form.module.css'

type LoanState = {
  loan_amount: number;
  period_type: 'monthly' | 'annual';
  period_quantity: number;
  interest_rate: string;
  amortization_type: 'SAF' | 'SAC' | 'SAM' | 'SAA' | 'SAALM';
};

export default function Form() {

  const getPeriodTypeLabel = () => {
    return loanState.period_type === 'monthly' ? 'Number of months' : 'Number of years';
  }

  const [loanState, setLoanState] = useState<LoanState>({
    loan_amount: 0,
    period_type: 'monthly',
    period_quantity: 0,
    interest_rate: '0',
    amortization_type: 'SAF'
  })

  const handleOnChangeForm = (event: ChangeEvent<HTMLInputElement | HTMLSelectElement>, key: keyof LoanState) => {
    setLoanState({ ...loanState, [key]: event.target.value });
  }

  const handleLoanForm = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    console.log(loanState);
  }

  return (
    <main className={styles.main}>
      <div className={styles.description}>

        <form className={styles.form} onSubmit={handleLoanForm}>
          <div className={styles.inputContainer}>
            <label htmlFor="loan_amount">Loan Amount</label>
            <input
              className={styles.input}
              type="number"
              required
              value={loanState.loan_amount}
              onChange={(event) => handleOnChangeForm(event, 'loan_amount')}            
            />
          </div>

          <div className={styles.selectContainer}>
            <label htmlFor="period_type">Payment type</label>
            <select
              id="period_type"
              value={loanState.period_type}
              onChange={(event) => handleOnChangeForm(event, 'period_type')}
            >
              <option value="monthly">Monthly</option>
              <option value="annual">Annual</option>
            </select>
            </div>

          <div className={styles.inputContainer}>
            <label htmlFor="period_quantity">{getPeriodTypeLabel()}</label>
            <input
              type="number"
              required
              value={loanState.period_quantity}
              onChange={(event) => handleOnChangeForm(event, 'period_quantity')}
            />
          </div>

          <div className={styles.inputContainer}>
            <label htmlFor="interest_rate">Interest rate</label>
            <input
              type="number"
              required
              value={loanState.interest_rate}
              onChange={(event) => handleOnChangeForm(event, 'interest_rate')}
            />
          </div>

          <div className={styles.selectContainer}>
            <label htmlFor="amortization_type">Choose the amortization system</label>
            <select
              id="amortization_type"
              value={loanState.amortization_type}
              onChange={(event) => handleOnChangeForm(event, 'amortization_type')}
            >
              <option value="SAF">French (Price Table)</option>
              <option value="SAC">Constant (SAC)</option>
              <option value="SAM">Mixed</option>
              <option value="SAA">American</option>
              <option value="SAALM">German</option>
            </select>
          </div>

          <button type="submit">Calculate</button>

        </form>

      </div>
    </main>
  )
}