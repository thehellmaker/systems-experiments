const express = require('express')
const app = express()
const port = 8080

app.use(express.json());

app.post('/test', (req, res) => {
  console.log(req.body.graphName)
  res.send(req.body)
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
