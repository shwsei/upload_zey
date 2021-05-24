import express from 'express'
import decoder from './decoder.js'
const app = express()
const PORT = process.env.PORT || 8080

app.use(express.json())
app.get('/', (_, res) => {
	res.json({
		message: 'Finja que isso é importantekkkkk'
	})
})

app.post('/decoder', (req, res) => {
	const { str } = req.body
	
	if(!str)
		return res.status(400).json({ error: "Value str is empty"})
	
	try{
		res.json({
			json: decoder(str) 
		})
	
	} catch { 
		res.status(500).json({ error: 'Decoded error'})
	}

})


app
	.listen(PORT, () => console.log('Express listening ON', PORT))

