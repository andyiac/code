// 原始方法
function averageOfArray(a){
	for (var i = 0, sum =0, n = a.length; i < n ; i++) {
		sum += a[i]
	}
	return sum / n;
}

result = averageOfArray([2,7,3,4])
console.log(result);

// 使用 apply 方法
function average() {
	for (var i = 0, sum =0, n = arguments.length; i < n ; i++) {
		sum+= arguments[i]
	}
	return sum / n
}
result2 = average.apply(null, [2,7,3,4])
console.log(result2);

// 推荐方法
function average2() {
	return averageOfArray(arguments)
}
result3 = average2.apply(null, [2,7,3,4])
console.log(result3);
