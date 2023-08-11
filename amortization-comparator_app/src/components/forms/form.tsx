import { useState, ChangeEvent, FormEvent } from 'react';
import styles from './form.module.css'

import Input from '../input/Input';
import Select from '../select/Select';
import CalcButton from './calcButton/CalcButton';

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

//------------------------------------SELECTS OPTIONS-------------------------------------------------

  const periodOptions = [
    {value: 'monthly', label:'Monthly'},
    {value: 'annual', label:'Annual'},
  ];

  const amortizationOptions = [
    { value: 'SAF', label: 'French (Price Table)' },
    { value: 'SAC', label: 'Constant (SAC)' },
    { value: 'SAM', label: 'Mixed' },
    { value: 'SAA', label: 'American' },
    { value: 'SAALM', label: 'German' },
  ];


//------------------------------------HANDLES---------------------------------------------------------
  const handleOnChangeForm = (event: ChangeEvent<HTMLInputElement | HTMLSelectElement>, key: keyof LoanState) => {
    setLoanState({ ...loanState, [key]: event.target.value });
  }

  const handleLoanForm = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    console.log(loanState);
  }


  return (
    <main className={styles.main}>


        <form className={styles.form} onSubmit={handleLoanForm}>
          <div className={styles.formRow}>
              <Input
                label="Loan Amount"
                value={loanState.loan_amount}
                onChange={(event) => handleOnChangeForm(event, 'loan_amount')}
                type="number"
                required
              />

              <Select
                label="Payment type"
                value={loanState.period_type}
                options={periodOptions}
                onChange={(event) => handleOnChangeForm(event, 'period_type')}
              />

              <Input
                label={getPeriodTypeLabel()}
                value={loanState.period_quantity}
                onChange={(event) => handleOnChangeForm(event, 'period_quantity')}
                type="number"
                required
              />

          </div>

          <div className={styles.formRow}>
              <Input
                label="Interest rate"
                value={loanState.interest_rate}
                onChange={(event) => handleOnChangeForm(event, 'interest_rate')}
                type="number"
                required
              />

              <Select
                label="Choose the amortization system"
                value={loanState.amortization_type}
                options={amortizationOptions}
                onChange={(event) => handleOnChangeForm(event, 'amortization_type')}
              />

              <CalcButton type="submit">Calculate</CalcButton>
          </div>

        </form>


    </main>
  )
}