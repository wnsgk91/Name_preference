var express = require('express');
var path = require('path');
var bodyParser = require('body-parser');
var app = express();

// ejs 사용
app.set('view engine', 'ejs');
app.engine('html', require('ejs').renderFile);

var staticResource = path.join(__dirname, '/public');
app.use(express.static(staticResource));
app.use(bodyParser.urlencoded({ extended: false }));


app.listen(5000, function() {
  console.log('Connected');
});

app.get('/', function(req,res){
  res.render('header');
});

app.get('/home', function(req,res){
  res.render('home/home');
});

app.get('/result', function(req,res){
  res.render('result/result');
});
