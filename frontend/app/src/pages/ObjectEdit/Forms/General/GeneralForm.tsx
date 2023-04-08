import { useState } from 'react'
import { useForm } from 'react-hook-form'
import { CustomInput } from '../../../../components/CustomInput'
import { inputs } from './const'
import Select from 'react-select'
import axios from 'axios'
import debounce from 'lodash/debounce'

type Option = { label: string; value: number }

export const GeneralForm = () => {
	const [inputValue, setInputValue] = useState<string>('')
	const [options, setOptions] = useState<Option[]>([])

	const fetchOptions = debounce(async (inputValue: string) => {
		const response = await axios.get<any[]>(
			`https://my-api.com/search?q=${inputValue}`
		)
		const data: Option[] = response.data.map((item: any) => ({
			label: item.name,
			value: item.id,
		}))
		setOptions(data)
	}, 1000)

	const handleInputChange = (value: string) => {
		setInputValue(value)
		if (value) {
			fetchOptions(value)
		} else {
			setOptions([])
		}
	}

	const {
		register,
		handleSubmit,
		formState: { touchedFields, errors },
	} = useForm()
	const onSubmit = (data: any) => {
		console.log(data)
	}

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
				/>
			))}
			<Select
				options={options}
				onInputChange={handleInputChange}
				inputValue={inputValue}
				isClearable
				isSearchable
				value={null}
			/>
		</form>
	)
}
