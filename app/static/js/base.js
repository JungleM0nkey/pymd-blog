$(document).ready(function(){
    //$('.post').each(function() {
    //    post_name = $(this).attr('id');
    //    div = $(this);
    //    GetPost(post_name, div);
    //});
    GetPosts(1);
    $('.page-num').on("click", function(){
        GetPosts($(this).text())
    });
})

//query post md data
function GetPost(post, div){
    $.get('/posts/'+post+'.md', function(data){
        div.empty()
        div.append(data)
        //add a fluid class to all images. so they scale
        div.find('img').addClass('img-fluid');
    });
}

//query posts by page number
function GetPosts(page_num){
    $.get('/posts', function(data){
        posts = data['posts']
        if (page_num == 1){
            i=0
            $('.post').each(function() {
                post_name = posts[i]
                div = $(this)
                GetPost(post_name, div);
                i++
            });
        }else{
            i=page_num
            $('.post').each(function() {
                post_name = posts[i]
                div = $(this)
                GetPost(post_name, div);
                i++
            });
        }
    });
}