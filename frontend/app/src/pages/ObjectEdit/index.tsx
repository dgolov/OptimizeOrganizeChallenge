import { useParams } from 'react-router-dom'
import styles from './objectEdit.module.scss'
import { GeneralForm } from './Forms/General/GeneralForm'

export const ObjectEdit = () => {
	const { objectId } = useParams()
	return (
		<div className={styles['formContainer']}>
			<GeneralForm />
		</div>
	)
}
