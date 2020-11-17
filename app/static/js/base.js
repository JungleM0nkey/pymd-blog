$(document).ready(function(){
    /*$('.header').height($( window ).height());*/

    $('.post').each(function() {
        post_name = $(this).attr('id');
        div = $(this);
        GetPost(post_name, div)
    });

})

function GetPost(post, div){
    $.get('/posts/'+post+'.md', function(data, data2){
        div.append(data)
        console.log(data2)
    });
}