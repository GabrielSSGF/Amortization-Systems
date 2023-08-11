import React, { ButtonHTMLAttributes} from 'react';
import styles from './CalcButton.module.css'

type ButtonProps = ButtonHTMLAttributes<HTMLButtonElement>;

export default function CalcButton(props: ButtonProps) {
    return <button className={styles.button} {...props} />
}