import { useParams } from 'react-router-dom'
import styles from './objectEdit.module.scss'

export const ObjectEdit = () => {
	const { objectId } = useParams()
	return <div className={styles['formContainer']}></div>
}
