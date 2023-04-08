import { Outlet } from 'react-router-dom'
import styles from './layout.module.scss'
import { Sidebar } from './Sidebar'

export const Layout = () => {
	return (
		<div className={styles['layout']}>
			<Sidebar />
			<main>
				<Outlet />
			</main>
		</div>
	)
}
