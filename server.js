const fs = require("fs");
const express = require("express");
var app = express();
var path= require('path');



app.use(express.static(path.join(__dirname, 'public')));


const hostname = "127.0.0.1";
const port = 3000;



app.listen(port, hostname, () => {
    console.log("Server running!");
});


app.get("/", function(req, res) {
    res.statusCode = 200;
    res.setHeader("Content-Type", "text/html");
    fs.createReadStream("home.html").pipe(res);
});