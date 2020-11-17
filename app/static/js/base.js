$(document).ready(function(){

    //query post md data
    $('.post').each(function() {
        post_name = $(this).attr('id');
        div = $(this);
        GetPost(post_name, div)
    });

})

function GetPost(post, div){
    $.get('/posts/'+post+'.md', function(data, data2){
        div.append(data)
        //add a fluid class to all images. so they scale
        div.find('img').addClass('img-fluid');
    });
}