import { useStore } from 'effector-react'
import { useState } from 'react'
import { $extraFields, extraFieldsChanged } from './model'
import { Modal } from 'antd'
import styles from './extraFields.module.scss'
import { CustomButton } from '../../../../components/CustomButton'
import { $currentObject, currentObjEditFx } from '../../model'

interface ExtraFieldI {
	[key: string]: string
}

export const ExtraFields = () => {
	const extraFields = useStore($extraFields)
	const currentObject = useStore($currentObject)
	const [isModalOpen, setIsModalOpen] = useState(false)

	const [nameInput, setNameInput] = useState('')
	const [valueInput, setValueInput] = useState('')

	const showModal = () => {
		setIsModalOpen(true)
	}

	const handleOk = () => {
		setIsModalOpen(false)

		extraFieldsChanged({ name: nameInput, value: valueInput })
		currentObjEditFx({
			...currentObject,
			extra_fields: extraFields.reduce(
				(obj, item) => ((obj[item.name] = item.value), obj),
				{}
			),
		})
	}

	const handleCancel = () => {
		setIsModalOpen(false)
	}
	return (
		<div className={styles['extraFieldsPage']}>
			<CustomButton
				customClassName={styles['addButton']}
				onClick={() => {
					showModal()
				}}>
				Добавить
			</CustomButton>
			<Modal
				title='Basic Modal'
				open={isModalOpen}
				onOk={handleOk}
				onCancel={handleCancel}>
				<input
					value={nameInput}
					onChange={(e: any) => setNameInput(e.target.value)}
				/>
				<input
					value={valueInput}
					onChange={(e: any) => setValueInput(e.target.value)}
				/>
			</Modal>
			<div>
				{extraFields.map((field: ExtraFieldI) => {
					if (field) {
						return (
							<div className={styles['extraFieldContainer']}>
								<div>{Object.entries(field)[0][0]}:</div>
								<div>{Object.entries(field)[0][1]}</div>
							</div>
						)
					}
					return <></>
				})}
			</div>
		</div>
	)
}
