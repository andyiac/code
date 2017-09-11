// 要引入高阶函数抽象的信号是出现重复或相似的代码


// 正常情况下的代码
var aIndex = 'a'.charCodeAt(0);

var alphabet = ''

for (var i = 0; i < 26; i++) {
	alphabet += String.fromCharCode(aIndex + i)
}

console.log(alphabet);

var digits = ""
for (var i = 0; i < 10; i++) {
	digits +=i
}


console.log(digits)

var random = ''

for (var i = 0; i < 8; i++) {
	random += String.fromCharCode(Math.floor(Math.random() * 26) + aIndex)
}

console.log(random);


// user call back function

function bindString(n, callback) {
	var result = "";
	for (var i = 0; i < n; i++) {
		result += callback(i)
	}
	return result
}


var newAlphabet = bindString(26, function(i){
	return String.fromCharCode(aIndex + i)
})

console.log(newAlphabet);

var newDigits = bindString(10, function (i) {
	return i
})
console.log(newDigits);

var newRandom = bindString(8, function (i){
	return String.fromCharCode(Math.floor(Math.random() * 26) + aIndex)
})

console.log(newRandom);
