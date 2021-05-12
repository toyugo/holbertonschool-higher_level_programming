const $ = window.$;
$(document).ready(() => {
    const classChar = $('#character');
    const url = 'https://swapi-api.hbtn.io/api/films/?format=json'
    const json = $.getJSON(url, function(data){
    const urlData = data;
    for (idx in urlData['results']) {
        let title = urlData['results'][idx]['title']
        $("UL#list_movies").append("<li>" + title + '</li>')
    }
    });
});
