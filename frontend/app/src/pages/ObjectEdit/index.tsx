import { useParams } from 'react-router-dom'
import styles from './objectEdit.module.scss'
import { GeneralForm } from './Forms/General/GeneralForm'
import { currentObjectChanged, fetchCurrentObjectFx } from './model'
import { useEffect, useState } from 'react'
import { ExtraFields } from './Forms/ExtraFields'

export const ObjectEdit = () => {
	const { objectId } = useParams()

	const [currentTab, setCurrentTab] = useState('general')

	useEffect(() => {
		fetchCurrentObjectFx(objectId)
		return () => {
			currentObjectChanged(null)
		}
	}, [objectId])
	return (
		<div>
			<div className={styles['objectEditTabs']}>
				<p
					style={{
						color: currentTab === 'general' ? 'red' : 'black',
					}}
					onClick={() => setCurrentTab('general')}>
					Основное
				</p>
				<p
					style={{
						color: currentTab === 'extraFields' ? 'red' : 'black',
					}}
					onClick={() => setCurrentTab('extraFields')}>
					Дополнительные поля
				</p>
			</div>
			<div className={styles['formContainer']}>
				{currentTab === 'general' && <GeneralForm />}
				{currentTab === 'extraFields' && <ExtraFields />}
			</div>
		</div>
	)
}
