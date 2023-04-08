import { FC } from 'react'
import styles from './customButton.module.scss'

export const CustomButton: FC<{
	children: React.ReactNode
	isIcon?: boolean
}> = ({ children, isIcon }) => {
	return (
		<button
			className={`${styles['button']} ${isIcon ? styles['icon'] : ''}`}>
			{children}
		</button>
	)
}
