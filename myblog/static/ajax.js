var json = {
	'firstname' : 'jill',
	'lastname' : 'jones',
	'dob' : '1990-05-01'
}

var ajax = {  
	send : function() {  
		xmlhttp=new XMLHttpRequest();
		xmlhttp.open("POST","http://djangblog.herokuapp.com/blog/authors/new",true);
		xmlhttp.setRequestHeader("Content-type","application/json");
		xmlhttp.send(json);
	},  
}
