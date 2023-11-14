window = global
document = {
    all:{length: 22}
}

!function (a) {
    // 变量池
    let variable = {'window': window};
    // 寄存器
    let register = "";
    let left;
    let right;
    // 指令
    let instruct;

    function analysis(a) {
        if (a === 'a_a') {
            return register
        }
        if (typeof a !== 'string') {
            return variable[a[0]]
        }
        return a
    }

    for (i of a) {
        instruct = i[0];
        switch (instruct) {
            case 166:
                variable[i[1]] = void 0;
                break;
            case 188:
                left = analysis(i[1]);
                right = analysis(i[2]);
                // 判断处理结果是否进寄存器
                if (i.at(-1) === 1 && i.length === 4) {
                    register = left[right]
                } else {
                    left[right]
                }
                break;
            case 222:
                left = analysis(i[1])
                right = analysis(i[2])
                variable[right] = left;
                break;
            case 355:
                if (i.at(-1) === 1 && i.length === 3) {
                    register = typeof analysis(i[1])
                }
                break;
            case 888:
                window[i[2]] = analysis(i[1])
                break;
        }
    }
}(
    [[166, 'a'],
        [188, ['window'], 'document', 1],
        [188, 'a_a', 'all', 1],
        [222, 'a_a', 'a'],
        [166, 'b'],
        [355, ['a'], 1],
        [222, 'a_a', 'b'],
        [166, 'c'],
        [188, ['a'], 'length', 1],
        [222, 'a_a', 'c'],
        [888, ['b'], 'sign1'],
        [888, ['c'], 'sign2']]
)
console.log(window.sign1)
console.log(window.sign2)