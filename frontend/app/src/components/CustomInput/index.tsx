import React, { FC } from 'react'
import styles from './customInput.module.scss'

interface CustomInputPropsI
	extends React.InputHTMLAttributes<HTMLInputElement> {
	props?: any
	inputSize?: 'sm' | 'md' | 'lg' | 'full'
	classNames?: string
	isTextArea?: boolean
	touchedFields?: any
	errors?: any
	register?: any
	text?: string
}

export const CustomInput: FC<CustomInputPropsI> = ({
	classNames,
	inputSize = 'md',
	touchedFields,
	errors,
	text,
	register,
	isTextArea,
	...props
}) => (
	<div className={styles['inputContainer']}>
		{' '}
		<div className={styles['inputContainerTop']}>
			{isTextArea ? (
				<textarea
					{...register(props.id)}
					{...props}
					className={`${classNames || ''} ${styles.input} ${
						styles['textArea']
					} ${
						props.id && touchedFields[props.id] && errors[props.id]
							? styles['error']
							: ''
					} textArea`}
				/>
			) : (
				<input
					{...register(props.id)}
					{...props}
					className={`${classNames || ''} ${styles[inputSize]} ${
						styles.input
					} ${
						props.id && touchedFields[props.id] && errors[props.id]
							? styles['error']
							: ''
					}`}
				/>
			)}
			<label htmlFor={props.id} className={'form__labels'}>
				{text}
			</label>
		</div>
		{props.id && touchedFields[props.id] && errors[props.id] ? (
			<div className={'error'}>{errors[props.id]?.message}</div>
		) : null}
	</div>
)
