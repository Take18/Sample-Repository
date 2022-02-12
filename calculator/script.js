$(function() {
    let num_1 = '',
        num_2 = '',
        answer = '';
        push_num = [],
        cal = '',
        calculation = false,
        memo_num = 0;

    $('.number').on('click', function () {

        $('#minus').text('-');

        push_num.push($(this).text());
        if (calculation == true) {
            num_2 = push_num.join('');
            $('#display').text(num_2);
            console.log(num_2);
        } else {
            num_1 = push_num.join('');
            $('#display').text(num_1);
            console.log(num_1);
        }
    });

    $('.operator').on('click', function () {
        cal = $(this).attr('id');
        calculation = true;
        push_num = [];
    });

    $('#equal').on('click', function () {

        let int_1 = parseFloat(num_1);
        console.log(int_1);
        let int_2 = parseFloat(num_2);
        console.log(int_2);

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
        $('#display').text(answer);
        num_1 = answer;
    });

    $('.clear').on('click', function () {
        num_1 = '';
        num_2 = '';
        cal = '';
        answer = '';
        calculation = false;
        push_num = [];
        $('#display').text(0);
    });

    $('#memory').on('click', function () {
        let dis_num_1 = $('#display').text();
        let dis_num_2 = parseFloat(dis_num_1);
        memo_num += dis_num_2;
    });

    $('#memory_clear').on('click', function () {
        memo_num = 0;
    });

    $('#memory_recall').on('click', function () {
        $('#display').text(memo_num);
        num_1 = memo_num;
    });
});