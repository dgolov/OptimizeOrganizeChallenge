import { objects } from './mockData'
import { useNavigate } from 'react-router-dom'
import styles from './objectList.module.scss'
import { GrDocumentUpload } from 'react-icons/gr'
import { CustomButton } from '../../components/CustomButton'

export const ObjectList = () => {
	const navigate = useNavigate()
	return (
		<div className={styles['objectListContainer']}>
			<div className={styles['controlButtons']}>
				<CustomButton isIcon>
					<GrDocumentUpload size={20} />
				</CustomButton>
				<CustomButton>Новый объект</CustomButton>
			</div>

			{objects.map((object) => (
				<div
					onClick={() => navigate(`/object/${object.id}`)}
					className={styles['objectListItem']}>
					<div className={styles['objectListItemName']}>
						<p>{object.address}</p>
						<span>{object.object_type}</span>
					</div>
					<p className={styles['objectListItemDate']}>
						{object.created_at.toLocaleString('en-GB', {
							timeZone: 'UTC',
						})}
					</p>
				</div>
			))}
		</div>
	)
}
