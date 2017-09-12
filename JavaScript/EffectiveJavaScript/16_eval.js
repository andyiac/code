// 不要直接调用 eval 函数因为开销很大
// 以下是间接调用方法

var src = "console.log('hello world ')"

(0, eval)(src)
