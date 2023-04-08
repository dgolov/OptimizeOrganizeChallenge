import { NavLink } from 'react-router-dom'
import styles from './sidebar.module.scss'

export const Sidebar = () => {
	return (
		<aside className={styles['sidebarContainer']}>
			<NavLink
				style={({ isActive }) => ({
					fontWeight: isActive ? 'bold' : '',
				})}
				className={styles['sidebarLink']}
				to='/'>
				Поручения
			</NavLink>
			<NavLink
				style={({ isActive }) => {
					return {
						fontWeight: isActive ? 'bold' : '',
					}
				}}
				className={styles['sidebarLink']}
				to='/'>
				События
			</NavLink>
			<NavLink
				style={({ isActive }) => {
					return {
						fontWeight: isActive ? 'bold' : '',
					}
				}}
				className={styles['sidebarLink']}
				to='/'>
				Дэшборд
			</NavLink>
			<NavLink
				style={({ isActive }) => {
					return {
						fontWeight: isActive ? 'bold' : '',
					}
				}}
				className={styles['sidebarLink']}
				to='/'>
				Отчеты
			</NavLink>
		</aside>
	)
}
