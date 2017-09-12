// 20_使用Call方法自定义接受者来调用方法1

function testOut(x) {
	console.log('test -->' + x);
}

var Obj = {
	testOut: testOut,
	test2: function (x) {
		console.log("------test2 -----" + x);
	}
}

Obj.testOut('12334')

Obj.testOut.call(Obj,'12334')

Obj.test2.call(Obj,'adasdf')

console.log(Obj.test2);



var table = {
	entries: [],
	addEntry: function(key, value){
		this.entries.push({key: key, value: value})
	},
	forEach: function(f,thisArg){
		var entries = this.entries;
		for (var i = 0 , n = entries.length; i < n; i++) {
			var entry = entries[i]
			f.call(thisArg, entry.key, entry.value, i)
		}
	}
}
