let num_1 = '',
    num_2 = '',
    answer = '';
    push_num = [],
    cal = '',
    calculation = false,
    memo_num = 0,
    sign = false,
    key_1 = false,
    key_2 = false,
    dot_key = false,
    dot_key_1 = false;

let numbers = document.getElementsByClassName('number'),
    display = document.getElementById('display'),
    minus = document.getElementById('minus'),
    dot = document.getElementById('dot'),
    operators = document.getElementsByClassName('operator'),
    equal = document.getElementById('equal'),
    clear = document.getElementById('clear'),
    memory = document.getElementById('memory'),
    memory_clear = document.getElementById('memory_clear'),
    memory_recall = document.getElementById('memory_recall');

minus.textContent = "-";

minus.addEventListener('click',() => {
    if (sign == true) {
        sign = false;
    } else {
        sign = true;
    }
})

for (let i = 0; i < 12; i++) {
    numbers[i].addEventListener('click',() => {

        let number = numbers[i].textContent;
        push_num.push(number);

        let last = push_num[push_num.length-1];

        if (last == '-') {
            if (push_num[0] == '-') {
                push_num[0] = '0';
            } else {
                let result_minus = push_num.indexOf('-');
                delete push_num[result_minus];
            }
        }

        if (key_1 == false) {
            if (last == '0') {
                delete push_num[push_num.length-1];
                if (key_2 == false) {
                    push_num[0] = '0';
                    key_2 = true;
                }
            } else if (last == '-') {
                key_1 = false;
            } else {
                key_1 = true;
            }
        }

        if (key_1 == true) {
            if (push_num.length >= 2) {
                if (last == '.') {
                    dot_key_1 = true;
                }
                if (dot_key_1 == false) {
                    dot_key_1 = true;
                    if (push_num[0] == '0') {
                        push_num.shift();
                    }
                }
            }
        }

        if (dot_key == true) {
            if (push_num[push_num.length-1] == '.') {
                delete push_num[push_num.length-1];
            }
        }

        if (calculation == true) {
            if (sign == true) {
                if (push_num[0] == '.') {
                    let dot_num = push_num.join('');
                    num_2 = '-0' + dot_num;
                    display.textContent = num_2;
                } else {
                    num_2 = '-' + push_num.join('');
                    display.textContent = num_2;
                }
            } else {
                if (push_num[0] == '.') {
                    let dot_num = push_num.join('');
                    num_2 = '0' + dot_num;
                    display.textContent = num_2;
                } else {
                    num_2 = push_num.join('');
                    display.textContent = num_2;
                }
            }
        } else {
            if (sign == true) {
                if (push_num[0] == '.') {
                    let dot_num = push_num.join('');
                    num_1 = '-0' + dot_num;
                    display.textContent = num_1;
                } else {
                    num_1 = '-' + push_num.join('');
                    display.textContent = num_1;
                }
            } else {
                if (push_num[0] == '.') {
                    let dot_num = push_num.join('');
                    num_1 = '0' + dot_num;
                    display.textContent = num_1;
                } else {
                    num_1 = push_num.join('');
                    display.textContent = num_1;
                }
            }
        }
    })
}

dot.addEventListener('click',() => {
    dot_key = true;
})

for (let n = 0; n < 4; n++) {
    operators[n].addEventListener('click',() => {
        cal = operators[n].id;
        calculation = true;
        push_num = [];
        sign = false;
        key_1 = false;
        key_2 = false;
        dot_key = false;
        dot_key_1 = false;
    })
}

equal.addEventListener('click',() => {
    if (num_1 == '') {
        num_1 = 0;
    }

    if (num_2 == '') {
        num_2 = num_1;
    }

    let int_1 = parseFloat(num_1);
    let int_2 = parseFloat(num_2);

    switch (cal) {

        case 'add':
            answer = int_1 + int_2;
            break;

        case 'subtract':
            answer = int_1 - int_2;
            break;

        case 'multiply':
            answer = int_1 * int_2;
            break;

        case 'divide':
            answer = int_1 / int_2;
            break;

        default:
            answer = num_1;
    }
    display.textContent = answer;
    num_1 = answer;
    calculation = false;
    push_num = [];
    if (num_1 < 0) {
        sign = true;
        let code_1 = parseFloat(num_1);
        let code_2 = code_1 * -1;
        push_num.push(code_2);
    } else {
        sign = false;
        push_num.push(num_1);
    }
    key_1 = false;
    key_2 = false;
    dot_key = false;
    dot_key_1 = false;
})

clear.addEventListener('click',() => {
    num_1 = '';
    num_2 = '';
    cal = '';
    answer = '';
    calculation = false;
    push_num = [];
    sign = false;
    key_1 = false;
    key_2 = false;
    dot_key = false;
    dot_key_1 = false;
    display.textContent = 0;
})

memory.addEventListener('click',() => {
    let dis_num_1 = display.textContent;
        let dis_num_2 = parseFloat(dis_num_1);
        memo_num += dis_num_2;
})

memory_clear.addEventListener('click',() => {
    memo_num = 0;
})

memory_recall.addEventListener('click',() => {
    display.textContent = memo_num;
    num_1 = memo_num;
    push_num = [];
    if (memo_num < 0) {
        sign = true;
        let code_3 = parseFloat(memo_num);
        let code_4 = code_3 * -1;
        push_num.push(code_4);
    } else {
        sign = false;
        push_num.push(memo_num);
    }
    key_1 = false;
    key_2 = false;
    dot_key = false;
    dot_key_1 = false;
})