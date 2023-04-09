import { useState, useEffect, FC } from 'react'
import { useForm } from 'react-hook-form'
import { CustomInput } from '../../../../components/CustomInput'
import { inputs } from './const'
import Select from 'react-select'
import AsyncSelect from 'react-select/async'
import useDebounce from '../../../../shared/hooks/useDebounce'
import { API_URL } from '../../../../shared/const'
import { $currentObject } from '../../model'
import { useStore } from 'effector-react'
import { CustomButton } from '../../../../components/CustomButton'

type Option = { label: string; value: number }

export const GeneralForm: FC = () => {
	const currentObject = useStore($currentObject)
	const [ownerInputValue, setOwnerInputValue] = useState<string>('')
	const [conditionInputValue, setConditionInputValue] = useState<string>('')
	const [options, setOptions] = useState<Option[]>([])
	const [defaultConditions, setDefaultConditions] = useState<Option[]>([])

	const debouncedValue = useDebounce(ownerInputValue, 500)
	const loadConditions = async (id?: number) => {
		if (id) {
			return fetch(API_URL + 'conditions/' + id).then((res) => res.json())
		} else {
			return fetch(API_URL + 'conditions').then((res) => res.json())
		}
	}

	useEffect(() => {
		loadConditions()
	}, [])

	useEffect(() => {
		// console.log('deb')
	}, [debouncedValue])

	const handleOwnerInputChange = (value: string) => {
		setOwnerInputValue(value)
	}
	const handleConditionInputChange = (value: string) => {
		setConditionInputValue(value)
	}

	const {
		register,
		handleSubmit,
		formState: { touchedFields, errors },
	} = useForm()
	const onSubmit = (data: any) => {
		console.log(data)
	}

	const [selectedValue, setSelectedValue] = useState(null)

	// handle selection
	const handleChange = (value: any) => {
		setSelectedValue(value)
	}

	// load options using API call
	const loadOptions = (inputValue: string) => {
		return fetch(API_URL + 'conditions').then((res) => res.json())
	}

	if (!currentObject) return <>loading</>

	return (
		<form onSubmit={handleSubmit(onSubmit)}>
			{inputs.map((input) => (
				<CustomInput
					id={input.name}
					type={input.type}
					inputSize='lg'
					register={register}
					errors={errors}
					touchedFields={touchedFields}
					text={input.label}
					defaultValue={currentObject[input.name]}
				/>
			))}
			<Select
				options={options}
				onInputChange={handleOwnerInputChange}
				inputValue={ownerInputValue}
				isClearable
				isSearchable
				value={null}
			/>
			<AsyncSelect
				noOptionsMessage={() => {
					return (
						<div>
							Начните вводить. Если уже что-то введено и вы видите
							это, значит ничего не найдено.
						</div>
					)
				}}
				cacheOptions
				defaultOptions
				value={selectedValue}
				loadOptions={loadOptions}
				onInputChange={handleConditionInputChange}
				onChange={handleChange}
			/>
			<CustomButton type='submit'>Добавить</CustomButton>
		</form>
	)
}
