const express = require('express');
const app = express();
const port = 3000; // Change this to the desired port number

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
