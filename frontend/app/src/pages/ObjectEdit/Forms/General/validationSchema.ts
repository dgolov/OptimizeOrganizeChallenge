import * as yup from 'yup'

const GeneralFormSchema = yup.object().shape({
	county: yup.string().trim().required('Обязательное поле'),
	region: yup.string().trim().required('Обязательное поле'),
	address: yup.string().trim().required('Обязательное поле'),
	object_type: yup.string().trim().required('Обязательное поле'),
})

export default GeneralFormSchema
