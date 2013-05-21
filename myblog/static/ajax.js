
var ajax = {  
	send : function(dest, json) {  
		xmlhttp=new XMLHttpRequest();
		xmlhttp.open("POST", dest);
		xmlhttp.setRequestHeader("Content-type","application/json; charset=utf-8");
		xmlhttp.send(JSON.stringify(json));
	},  
}

var aForm = {
	sendValues : function() {
		jsonObj = {
			'firstname' : document.getElementById('firstname').value,
			'lastname' : document.getElementById('lastname').value,
			'dob' : document.getElementById('dob').value 
		};
		ajax.send('/blog/authors/new', jsonObj);
	}
}

var pForm = {
	sendNewPost : function() {
		jsonObj = {
			'title' : document.getElementById('title').value,
			'content' : document.getElementById('content').value,
			'author' : document.getElementById('author').value
		};
		ajax.send('/blog/posts/new', jsonObj);
	},
	sendModifiedPost : function() {
		jsonObj = {
			'title' : document.getElementById('title').value,
			'content' : document.getElementById('content').value,
			'author' : document.getElementById('author').value,
			'id' : document.getElementById('post-form-id').value
		};
		ajax.send('/blog/posts/modify', jsonObj);
	},
	sendDeletePost : function() {
		jsonObj = {
			'id' : document.getElementById('post-form-id').value
		};
		ajax.send('/blog/posts/delete', jsonObj);
	}
}

var idForm = {
	sendValues : function() {
		type = document.getElementById('change-type').selectedOptions[0].value;
		jsonObj = {
			'id' : document.getElementById('id-form-id').value,				
		};
		ajax.send(type, jsonObj);
	}
}
