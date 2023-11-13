window = {}
document = {}
window.addEventListener = '1'
document.addEventListener = function (a, b, c) {
    b()
}
document.attachEvent = function (a, b, c) {
    b()
}
document.createElement = function () {
    return {
        'innerHTML': "<a href=\'/\'>_1H</a>",
        "firstChild": {"href": 'https://www.python-spider.com/'}
    }
}
setTimeout = function () {

}

__jscode

function decode() {
    return document.cookie
}