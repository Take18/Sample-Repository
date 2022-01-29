$(function() {
    let num_1 = '', num_2 = '', answer = '';
    push_num = [],
        cal = '',
        calculation = false;

    $('.number').on('click', function () {
        push_num.push($(this).text());
        if (calculation == true) {
            num_2 = push_num.join('');
            $('#display').text(num_2);
        } else {
            num_1 = push_num.join('');
            $('#display').text(num_1);
        }
    });

    $('.operator').on('click', function () {
        cal = $(this).attr('id');
        caluculation = true;
        push_num = [];
    });

    $('#equal').on('click', function () {

        let int_1 = parseInt(num_1);
        let int_2 = parseInt(num_1 );
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
    });

    $('#memory_clear').on('click', function () {
    });

    $('#memory_recall').on('click', function () {
    });
});