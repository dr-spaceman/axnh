function flash(message) {
    $("#flash").append('<div class="alert alert-warning"><button type="button" class="close" data-dismiss="alert">&times;</button>' + message + '</div>');
}