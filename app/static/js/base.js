$(document).ready(function(){
    //select the first posts page on page load
    GetPosts(1);

    //select posts by pages
    $('.page-num').on("click", function(){
        GetPosts($(this).text())
    });

    //hide archive tab
    $('.archive').css({'height':'0px','box-shadow':'0px','border':'none','padding':'0px'})
    $('#archive-button-element').css({'border-radius':'5px', 'border':'1px solid rgb(128, 128, 128)'})
    $('.archive-year').hide();
    $('.archive-link').hide();

    //on button archive button click open archive tab
    $('#archive-button').on("click", function(){
        if (!$(this).hasClass('archive-open')){
            $('#archive-button-element').css({'border-radius':'5px 5px 0px 0px', 'border-bottom':'none'})
            $('.archive').css({'height':'auto','box-shadow':'5px 5px #888888','border':'1px solid rgb(128, 128, 128)','padding':'1em'})
            $('.archive-year').show();
            $('.archive-link').show();
            $(this).addClass('archive-open');
        }else{
            $('#archive-button-element').css({'border-radius':'5px', 'border':'1px solid rgb(128, 128, 128)'})
            $('.archive').css({'height':'0px','box-shadow':'0px','border':'none','padding':'0px'})
            $('.archive-year').hide();
            $('.archive-link').hide();
            $(this).removeClass('archive-open');
        }

    });
})

//query post md data
function GetPost(post, div){
    $.get('/posts/'+post+'.md', function(data){
        //clear the post div
        div.empty()
        //fill the post div with content
        div.append(data)
        //add a fluid class to all images in the post div. so they scale
        div.find('img').addClass('img-fluid');
    });
}

//query posts by page number
function GetPosts(page_num){
    $('.page-num').css({'color':'#007bff','background-color':'rgb(241, 241, 241)'})
    $(`#page-num-${page_num}`).css({'color':'white', 'background-color':'#2d65ff' });
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