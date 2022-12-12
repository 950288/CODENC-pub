function _touch(){
    // console.log("ready!");
    //setTimeout(_95, 5000);
}
// disable alert pop-up
// window.alert = function() {
//     return false;
// }
function getStyle( obj , attr ){
    // console.log(obj)
    try {
        if ( window.getComputedStyle ) {
    
            return getComputedStyle( obj , null )[attr];
    
        } else{
    
            return obj.currentStyle[attr];
    
        }
    } catch (error) {
        console.log(error);
        return null;
    }
}

function NEpages(){
    try {
        document.getElementsByClassName("orientationright")[0].click();
    } catch (error) {
        
    }
    try {
        document.getElementsByClassName("next")[0].click();
    } catch (error) {
        
    }

    try {
        document.getElementsByClassName("next")[1].click();
    } catch (error) {
        
    }

    try {
        document.getElementsByClassName("nextChapter")[1].click();
        document.getElementsByClassName("nextChapter")[0].click();
    } catch (error) {
        
    }
}

function _NEpage(){

    setTimeout(NEpages,5000);
    setTimeout(_95, 15000);
    return;
}

function _taglisener(This , n = 0){
    // console.log("taglisener" + n);
    //console.log(This.nextElementSibling.contentWindow.document.getElementsByTagName("video")[0])
    // console.log(This)
    if(getStyle(This , 'background-position') == "0px -24px"){
        console.log("taglisener" + n + "return");
        This.nextElementSibling.contentWindow.document.getElementsByTagName("video")[0].currentTime = 
        This.nextElementSibling.contentWindow.document.getElementsByTagName("video")[0].duration - 1 ;
        console.log("taglisener" + n + "return");
        return;
    }else{
        setTimeout(_taglisener , 500 , This , ++n);
    }
}
function _getvideo(videolist , element , a , tag = null , tags){
    // console.log(tag , a);
    // console.log(tags , a);
    //console.log("get" + a);

    try{
        element.contentWindow.document.getElementsByTagName("html")[0].scrollTop = 
        element.contentWindow.document.getElementsByTagName("html")[0].scrollHeight;
        setTimeout(function(element){
            element.contentWindow.document.getElementsByTagName("html")[0].scrollTop = 
            element.contentWindow.document.getElementsByTagName("html")[0].scrollHeight;
        } , 500 , element);
    } catch (error) {
        //console.log(error);
    }

    var vid = new Array();
    try {
        vid = element.contentWindow.document.getElementsByTagName("video");
        // console.log(vid);
        // console.log(tag);
    } catch (error) {
        //console.log(error);
    }

    if(vid.length != 0){
        for(var j = 0 ; j < vid.length ; j++){
            tags[videolist.length] = tag;
            videolist[videolist.length] = element.contentWindow.document.getElementsByTagName("video")[j];
            // console.log(videolist);
            // console.log(tags);
        }
        return;
    }
    let ele = [];
    try {
        ele = element.getElementsByTagName("iframe");
        //console.log(ele);
    } catch (error) {
        //console.log(error);
    }
    if( ele.length == 0){
        try {
            ele = element.contentWindow.document.getElementsByTagName("iframe");
            //console.log(ele);
        } catch (error) {
            //console.log(error);
        }
    }
    if( ele != null){
        for(j = 0; j < ele.length; j++) {
            try{
                if(a > 0 & getStyle(ele[j].previousElementSibling , 'background-position') != "0px -24px"){
                    // console.log(ele[j].previousElementSibling)
                    // console.log(tags , a)
                    _getvideo(videolist, ele[j] , a - 1 , ele[j].previousElementSibling , tags);
                }
            }catch (error) {
                console.log(error)
                if(a > 0){
                    try {
                        // console.log(tag , a)
                        _getvideo(videolist ,  ele[j] , a - 1 , tag , tags);
                    } catch (error) {}
                }else{
                    return;
                }
            }
        }
    }
    return videolist;
}

function _95(counter = 0){
    var videolist = new Array();
    var tags = new Array();
    
    _getvideo( videolist , document.getElementsByTagName("html")[0] , 5 , null , tags);

    console.log(videolist);
    console.log(tags);
    if(videolist.length == 0){
        if( counter < 1){
            setTimeout(_95 , 500 , ++counter);
        }else{
            _NEpage();
        }
    }else{
        var li = 0;
        playy(videolist , tags , li , counter);
    }
}

_95();
for (let i = 0; i < document.getElementsByClassName("posCatalog_name").length; i++) {
    document.getElementsByClassName("posCatalog_name")[i].addEventListener("onclick",_touch());
}

function _videotracker(This){//useless
    //console.log("tocked!");
    This.playbackRate = 1;
    //console.log(This);
    if( This.currentTime > This.duration - 2 ){
        return;
    }
    setTimeout(_videotracker, 250 , This);
}

function _Listener(){
    this.play();
    setTimeout(this.play(), 50);
}

function playy(videolist , tags , li ,counter){
    videolist[li].play();
    // console.log(videolist[li])
    // console.log(videolist[li].parentNode.parentNode.parentNode.parentNode.parentNode)
    setTimeout(_taglisener , 0 , tags[li] , 0 + j*1000);
    _videotracker(videolist[li]);
    videolist[li].addEventListener("pause",_Listener);
    videolist[li].playbackRate = 1;
    videolist[li].addEventListener("ended",function() {
        if(getStyle(tags[li] , 'background-position') == "0px -24px"){
            console.log("over" , _Listener)
            if(li == videolist.length - 1 ){
                if( counter < 1){
                    setTimeout(_95 , 0 , ++counter);
                }else{
                    _NEpage();
                }
            }
            videolist[li].removeEventListener("pause",_Listener);
            playy(videolist , tags , li + 1 , counter);
            //console.log(this);
        }
    })
}

