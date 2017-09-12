function callMethod(obj, method){
	console.log(arguments);
	var shift = [].shift

	shift.call(arguments)
	shift.call(arguments)

	// 为何不直接 arguments.shift 因为 arguments 并不是标准的 Array 数组
	console.log(typeof(arguments))

	console.log(arguments);
	console.log("obj---->" + obj);
	console.log("--method name-->" + method);
	return obj[method].apply(obj,arguments);
}

var obj = {
	add: function (x, y) {
		return x + y
	}
}

callMethod(obj, "add", 17 ,25)
