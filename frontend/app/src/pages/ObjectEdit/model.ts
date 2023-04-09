import { extraFieldsChanged } from './Forms/ExtraFields/model'
import { createEffect, createEvent, createStore } from 'effector'
import { API_URL } from '../../shared/const'

export const $currentObject = createStore<any>({})

export const fetchCurrentObjectFx = createEffect(
	async (id: string | undefined) => {
		const data = fetch(API_URL + 'objects/' + id)
			.then((res) => res.json())
			.then((data) => data)
		return data
	}
)

export const currentObjectChanged = createEvent<any>()

export const currentObjEditFx = createEffect(async (obj: any) => {
	const data = fetch(API_URL + 'objects/' + obj.id, {
		method: 'PUT',
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify(obj),
	})
		.then((res) => res.json())
		.then((data) => data)
	return data
})

$currentObject
	.on(currentObjectChanged, (state, data) => data)
	.on(fetchCurrentObjectFx.doneData, (_, data) => {
		if (data.extraFields && JSON.parse(data.extraFields)) {
			console.log(data.extraFields)
			// extraFieldsChanged(data.extraFields)
		}
		return data
	})

$currentObject.watch((s) => console.log(s))
