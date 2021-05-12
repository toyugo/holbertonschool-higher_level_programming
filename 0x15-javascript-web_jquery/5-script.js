const $ = window.$;
$(document).ready(() => {
    const header = $('header');
    $('DIV#add_item').click(() => {
        $("UL.my_list").append('<li>Item</li>');
    });
});
