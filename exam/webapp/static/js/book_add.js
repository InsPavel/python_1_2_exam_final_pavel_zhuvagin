function dataPost(id) {
    let url = $(event.target).data('url');
    let csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

    $.ajax({
        url: url,
        data: {
            book_id: id,
            csrfmiddlewaretoken: csrftoken
        },
        success: function(response) {
                console.log(response)
        },
        type: 'POST',
    });

}

function dataDelete(id) {
    let url = $(event.target).data('delete-url');
    let csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

    $.ajax({
        url: url,
        data: {
             book_id: id,
            csrfmiddlewaretoken: csrftoken
        },
        success: function(response) {
                console.log(response)
        },
        type: 'POST',
    });


}