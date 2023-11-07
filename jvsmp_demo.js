/* 我们假设赋值指令为 66, 加和指令为 88,声明指令为 110(爱取什么名字取什么名字)
            如果按照从上到下的顺序，我们就可以将他们的操作变成指令性的[用|分割左侧和右侧]*/
!function (_stack) {
    // 寄存器
    var register;
    // 存放全局变量 variable->windows
    var variable = {};
    for (let i = 0; i < _stack.length; i++) {
        instruct = _stack[i][0];
        left = _stack[i][1];
        right = _stack[i][2];
        if (instruct === 110) {
            variable[right] = ''
        }
        if (instruct === 66) {
            if (right === '?') {
                variable[left] = register
            } else {
                variable[left] = right
            }
        }
        if (instruct === 88) {
            register = variable[left] + variable[right]
        }
    }
    ;console.log(variable)
    ;console.log(register)
}([[110, 'var', 'a'], [66, 'a', 1000], [110, 'var', 'b'], [66, 'b', 1000], [110, 'var', 'c'], [66, 'c', 1000], [110, 'var', 'd'], [88, 'a', 'b'], [66, 'd', '?'], [110, 'var', 'e'], [88, 'd', 'c'], [66, 'e', '?']])

'a'['charCodeAt']()