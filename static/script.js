document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");
    const button = document.querySelector("button");

    
    form.addEventListener("submit", function () {
        button.innerText = "Analyzing...";
        button.disabled = true;
    });

    const progressBar = document.querySelector(".progress-bar");

    if (progressBar) {
        let target = parseInt(progressBar.innerText);
        let width = 0;

        const interval = setInterval(() => {
            if (width >= target) {
                clearInterval(interval);
            } else {
                width++;
                progressBar.style.width = width + "%";
                progressBar.innerText = width + "%";
            }
        }, 10);
    }

});