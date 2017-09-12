// 标题： 使用立即调用函数表达式创建局部作用域
// 问题 看下列函数的输出

function wrapElements(a) {
	var result = [], i, n;
	for ( i = 0; i < a.length; i++) {
		result[i] = function () {
			return a[i]
		}
	}
	console.log(result[0]())
	return result;
}

var wrapped = wrapElements([10, 20,30,40,50])

var f = wrapped[0]

console.log(f())
