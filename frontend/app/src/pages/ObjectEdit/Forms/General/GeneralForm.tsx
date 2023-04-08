import { useForm } from 'react-hook-form'

export const GeneralForm = () => {
	const {
		register,
		formState: { errors },
		handleSubmit,
	} = useForm()
	const onSubmit = (data: any) => {
		console.log(data)
	}
	return (
		<div>
			<input type='text' {...register('county')} />
		</div>
	)
}
