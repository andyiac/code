// 闭包有三个事实

function makeSandwich () {
	var magicIngredient = "peanut butter"
	function make(filling) {
		return magicIngredient + " and " + filling
	}
	return make("jelly")
}

var result = makeSandwich()

console.log(result);

// 引用在当前函数以外定义的变量
//make() 函数引用 外部函数 makeSandwich() 函数内的 magicIngredient 变量

function sandwichMaker() {
	var magicIngredient = "peanut butter"
	function make(filling) {
		return magicIngredient + " and " + filling
	}
	return make;
}

var f = sandwichMaker()
console.log(f)
var r1 = f("jelly")

console.log(r1)

//第二个事实即时外部函数已经返回，当前函数 make 仍然可以引用 在外部很熟所定义的变量
