import express from 'express';
import routes from './routes/index.js';

const app = express();

app.use('/', routes);

const port = 1245;
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});

export default app;