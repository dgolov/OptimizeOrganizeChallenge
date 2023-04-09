import { createStore, createEffect } from 'effector'
import { API_URL } from '../../shared/const'

export const $objectsList = createStore<any[]>([])

export const fetchObjectsListFx = createEffect(async () => {
	const data = fetch(API_URL + 'objects')
		.then((response) => {
			return response.json()
		})
		.then((data) => {
			return data
		})

	return data
})

$objectsList.on(fetchObjectsListFx.doneData, (state, data) => data)
