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
				Объекты
			</NavLink>
			<NavLink
				style={({ isActive }) => ({
					fontWeight: isActive ? 'bold' : '',
				})}
				className={styles['sidebarLink']}
				to='/dashboard'>
				Дэшборд
			</NavLink>
			<NavLink
				style={({ isActive }) => ({
					fontWeight: isActive ? 'bold' : '',
				})}
				className={styles['sidebarLink']}
				to='/tasks'>
				Поручения
			</NavLink>
			<NavLink
				style={({ isActive }) => ({
					fontWeight: isActive ? 'bold' : '',
				})}
				className={styles['sidebarLink']}
				to='/events'>
				События
			</NavLink>

			<NavLink
				style={({ isActive }) => ({
					fontWeight: isActive ? 'bold' : '',
				})}
				className={styles['sidebarLink']}
				to='/reports'>
				Отчеты
			</NavLink>
			<NavLink
				style={({ isActive }) => ({
					fontWeight: isActive ? 'bold' : '',
				})}
				className={styles['sidebarLink']}
				to='http://localhost:8000/admin'>
				Админ
			</NavLink>
		</aside>
	)
}
