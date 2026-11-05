// Optional interface help only. No JavaScript stack or click handlers.
if (window.jQuery) {
    jQuery(function ($) {
        $('#st_data').trigger('focus');
        
        $('.stack-item.peek').fadeOut(150).fadeIn(150).fadeOut(150).fadeIn(150);
    });
}
