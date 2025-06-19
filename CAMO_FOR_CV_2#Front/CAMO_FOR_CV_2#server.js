const express = require('express');
const app = express();
const path = require('path');

app.use(express.static('public'));

app.listen(3000, () => {
    console.log("Web sunucusu http://localhost:3000 adresinde çalışıyor.");
});
