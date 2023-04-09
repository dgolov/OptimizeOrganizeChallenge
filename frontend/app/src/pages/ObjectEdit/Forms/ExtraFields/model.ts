import { createEvent, createStore } from 'effector'

export const $extraFields = createStore<any[]>([])
export const extraFieldsChanged = createEvent<{}>()

$extraFields.on(extraFieldsChanged, (state, change) => [...state, change])
$extraFields.watch((s) => console.log(s))
