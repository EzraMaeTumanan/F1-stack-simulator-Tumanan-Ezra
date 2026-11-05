// Optional interface help only. No JavaScript stack or click handlers.
if (window.jQuery) {
    jQuery(function ($) {
        $('#st_data').trigger('focus');
        // Pulse the item that Jinja marked with the "peek" class after Peek.
        $('.stack-item.peek').fadeOut(150).fadeIn(150).fadeOut(150).fadeIn(150);
    });
}
