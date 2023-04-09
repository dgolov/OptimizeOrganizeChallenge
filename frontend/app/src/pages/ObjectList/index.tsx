import { useEffect } from 'react'
import { objects } from './mockData'
import { useNavigate } from 'react-router-dom'
import styles from './objectList.module.scss'
import { GrDocumentUpload } from 'react-icons/gr'
import { CustomButton } from '../../components/CustomButton'
import { useStore } from 'effector-react'
import { $objectsList, fetchObjectsListFx } from './model'
import { currentObjectChanged } from '../ObjectEdit/model'

export const ObjectList = () => {
	const navigate = useNavigate()
	const objectsList = useStore($objectsList)
	useEffect(() => {
		fetchObjectsListFx()
	}, [])
	if (!objectsList.length) return <>loading</>
	return (
		<div className={styles['objectListContainer']}>
			<div className={styles['controlButtons']}>
				<CustomButton isIcon>
					<GrDocumentUpload size={20} />
				</CustomButton>
				<CustomButton>Новый объект</CustomButton>
			</div>

			{objectsList.map((obj) => (
				<div
					key={obj.id}
					onClick={() => navigate(`/object/${obj.id}`)}
					className={styles['objectListItem']}>
					<div className={styles['objectListItemName']}>
						<p>{obj.address}</p>
						<span>{obj.object_type}</span>
					</div>
					<p className={styles['objectListItemDate']}>
						{obj.created_at.toLocaleString('en-GB', {
							timeZone: 'UTC',
						})}
					</p>
				</div>
			))}
		</div>
	)
}
