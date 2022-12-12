// 获取 Iframe 元素
var iframeElement = document.getElementById("frame_content-tl");

// Get a reference to the button
var button = iframeElement.contentDocument.querySelector("#getMoreTopic");

// Set a counter variable to track how many times the button has been clicked
var counter = 0;

// Use setInterval to execute a function that clicks the button every 5 seconds
var intervalId = setInterval(function() {
    // Click the button
    button.click();

    // Increment the counter
    counter++;

    // If the button has been clicked 15 times, stop the setInterval timer
    if (counter === 15) {
        clearInterval(intervalId);
    }
}, 3000);
