import React, {ChangeEvent} from 'react';
import styles from './select.module.css';

type Option = {value: string, label: string};

type SelectProps = {
    label: string;
    value: string;
    options: Option[];
    onChange: (event: ChangeEvent<HTMLSelectElement>) => void;
};

export default function Select({ label, value, options, onChange }: SelectProps) {
    return(
      <div className={styles.selectContainer}>
        <label htmlFor={label}> {label} </label>

        <select id={label} value={value} onChange={onChange}>
          
          {options.map((option) => (
            <option key={option.value} value={option.value}>
              {option.label}
            </option>
          ))}
          
        </select>
      </div>
    );
}