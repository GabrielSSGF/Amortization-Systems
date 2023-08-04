import React, { ChangeEvent } from 'react';
import styles from './input.module.css';

type InputProps = {
    label: string;
    value: string | number;
    onChange: (event: ChangeEvent <HTMLInputElement>) => void;
    type: string;
    required: boolean;
};

export default function Input(props: InputProps) {
    return (
        <div className={styles.inputContainer}>
            <label>{props.label}</label>
            <input
              className={styles.input}
              type={props.type}
              required={props.required}
              value={props.value}
              onChange={props.onChange}
            />
        </div>
    );
}