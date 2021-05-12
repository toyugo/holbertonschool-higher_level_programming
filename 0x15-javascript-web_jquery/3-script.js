const $ = window.$;
$(document).ready(() => {
  $('DIV#red_header').click(function(){
    const header = $('header');
    header.addClass( "red");
    header.css('color', '#FF0000');
  });
});