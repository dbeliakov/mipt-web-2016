$(document).ready(function() {
    function loadMessages() {
        $.get('/load_messages', {
            'thread_id': $('#thread_id').val(),
            'page_num': $('#page_num').val()
        }).done(function(data) {
            data.messages.forEach(function (message) {
                var row = $('<li class="list-group-item">');
                row.append($('<div class="author">').text(message.author));
                row.append($('<div class="message">').text(message.text));

                $('#messages_list').append(row);
            });
        });
    }

    loadMessages();

    setInterval(loadMessages, 5000);
});
