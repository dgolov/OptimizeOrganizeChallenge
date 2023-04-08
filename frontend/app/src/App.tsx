import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import { Routes, Route } from 'react-router-dom'
import { Layout } from './layouts/Layout'
import { ObjectList } from './pages/ObjectList'
import { NotFound } from './pages/NotFound'
import { ObjectEdit } from './pages/ObjectEdit'

function App() {
	const [count, setCount] = useState(0)

	return (
		<div className='App'>
			<Routes>
				<Route path='/' element={<Layout />}>
					<Route index element={<ObjectList />} />
					<Route path='/object/:objectId' element={<ObjectEdit />} />

					<Route path='*' element={<NotFound />} />
				</Route>
			</Routes>
		</div>
	)
}

export default App
