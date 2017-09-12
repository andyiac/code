username = ' i am global!'

function hello() {
	return 'hello' + this.username
}

var obj1 = {
	hello: hello,
	username: ' i am obj1'
}

console.log(obj1.hello())


var obj2 = {
	hello: hello,
	username: ' i am obj2'
}

console.log(obj2.hello())

console.log(hello())

console.log(username);

console.log(this)

console.log(obj1)

// { hello: [Function: hello], username: ' i am obj1' }
