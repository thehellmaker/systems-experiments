import express, { Express, Request, Response } from 'express';

interface ExecuteApiRequest {
  graphName: string;
  // Add other expected properties from req.body here
}

const app: Express = express();
const port: number = 8080;

app.use(express.json());

app.post('/test', (req: Request<{}, {}, ExecuteApiRequest>, res: Response) => {
  console.log(req.body.graphName);
  res.send(req.body);
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});