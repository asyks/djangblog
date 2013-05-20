var json = {
	'firstname' : 'jill',
	'lastname' : 'jones',
	'dob' : '1990-05-01'
}

var ajax = {  
	send : function() {  
		xmlhttp=new XMLHttpRequest();
		xmlhttp.open("POST","/blog/authors/new");
		xmlhttp.setRequestHeader("Content-type","application/json; charset=utf-8");
		xmlhttp.send(JSON.stringify(json));
	},  
}

var form = {
	getValues : function() {

	}
}

authorForm = document.getElementById('author-form');
authorForm.addEventListener('submit', form.getValues());

