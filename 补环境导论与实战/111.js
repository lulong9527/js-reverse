// HTMLAnchorElement = function () {
//     if (this instanceof HTMLAnchorElement) {
//         throw TypeError('Illegal constructor')
//     } else if (val) {
//         if (val === "anlan_cE") {
//         }
//     } else {
//         throw TypeError(`Failed to construct 'HTMLAnchorElement': Please use the 'new' operator, this DOM object constructor cannot be called as a function`)
//     }
// };
HTMLAnchorElement = function () {

}
// HTMLAnchorElement.prototype.host = ''
// HTMLAnchorElement.prototype.href = ''

document = {
    createElement: function (val) {
        if (val === 'a') {
            return new HTMLAnchorElement()
        }
    }
}

// 非尖头函数 和 new 过程中  谁调用this 只向谁
Object.defineProperty(HTMLAnchorElement.prototype, 'href', {
    set: function () {
        this.host = arguments[0].split('/').at(-1);
        this._HTMLAnchorElement_href = arguments[0];
        // return arguments[0]   // 这里不用return  等号表达式在解析的时候会自动向前赋值的，这里不需要return
    },
    get: function () {
        // 这里设置中间变量 防止递归栈溢出。所以不能直接写 this.href
        return this._HTMLAnchorElement_href;
    },
})
a = document.createElement('a')
a.href = 'https://www.yuanrenxue.com'
console.log(a.host)
console.log(a.href)