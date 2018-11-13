var express = require('express');
var path = require('path');
var bodyParser = require('body-parser');
var app = express();
var jquery = require('jquery');

// ejs 사용
app.set('view engine', 'ejs');
app.engine('html', require('ejs').renderFile);

// mysql 연결
var mysql = require('mysql');
var con = mysql.createConnection({
 host: 'localhost',
 user: 'root',
 password: 'dlwnsgk94', //변경
 database : 'sad' //변경

 });

con.connect();

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





app.get(['/result',"'/result?name="], function(req, res){

	var sql = "SELECT * FROM name";

	con.query(sql, function(err, names, fields){

		var name = req.query.name;

		if(name){
			var sql = "SELECT * FROM name WHERE name='"+name+"'";
			con.query(sql,[name], function(err, name, fields){
				res.render('result/result', {name:name})
			})
		}else{
			res.render('result/result',{name:names});
		}
	})
})