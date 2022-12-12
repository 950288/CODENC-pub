// 获取 Iframe 元素
var iframeElement = document.getElementById("frame_content-tl");

// 获取所有包含 onclick="replyshow()" 的 a 标签
var replyElements = iframeElement.contentDocument.querySelectorAll('a[onclick^="replyshow"]');

// 遍历所有 a 标签，触发它们的 click 事件
for (var i = 0; i < replyElements.length; i++) {
    replyElements[i].click();
}

// 获取所有 class 以 "content"开头并后面跟着一串数字的 div 元素
var divElements = iframeElement.contentDocument.querySelectorAll('div[class^="content"]');
// divElements = divElements.reverse()
console.log(divElements)
// 遍历所有 div 元素
// for (var i = 0; i < divElements.length; i++) {
for (var i = divElements.length - 1; i > divElements.length - 200; i--) {
    // 获取当前遍历的 div 元素
    var divElement = divElements[i];

    // 判断是否含有 class 为 "ReplyList" 的 div 元素
    if (divElement.querySelector('div.ReplyList') !== null) {
        // 获取第一个 class 为 "ReplyList" 的 div 元素
        var replyListElement = divElement.querySelector('div.ReplyList');

        // 获取包含回复内容的 p 元素
        var replyElement = replyListElement.querySelector('p.hf_pct');
        console.log(replyElement)
        if(replyElement === null){
            continue;
        }

        // 获取回复内容文本
        var replyText = replyElement.textContent;
        console.log(replyText);

        // 获取输入框元素
        var inputElement = divElement.querySelectorAll("textarea")
        console.log(inputElement)

        if (inputElement.length) {

            // 将回复内容文本粘贴到输入框中
            inputElement[0].value = replyText;

        }

        // 点击回复按钮
        // console.log(divElement.querySelector(".grenBtn"))
        // divElement.querySelector(".grenBtn").click();

    }

}
