import { FC } from 'react'
import styles from './customButton.module.scss'

export const CustomButton: FC<{
	children: React.ReactNode
	isIcon?: boolean
	onClick?: () => void
	customClassName?: string
	type?: 'button' | 'submit' | 'reset' | undefined
}> = ({ children, isIcon, onClick, customClassName = '', type }) => {
	return (
		<button
			type={type}
			onClick={() => {
				onClick && onClick()
			}}
			className={`${styles['button']} ${
				isIcon ? styles['icon'] : ''
			} ${customClassName}`}>
			{children}
		</button>
	)
}
