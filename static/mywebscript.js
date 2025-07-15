let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    if (!textToAnalyze.trim()) {
        document.getElementById("system_response").innerHTML = "Please enter some text first.";
        return;
    }

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState === 4) {
            if (this.status === 200) {
                document.getElementById("system_response").innerHTML = this.responseText;
            } else {
                document.getElementById("system_response").innerHTML = "Error: Could not analyze text.";
            }
        }
    };

    xhttp.open("GET", "EmotionDetection?textToAnalyze=" + encodeURIComponent(textToAnalyze), true);
    xhttp.send();
};
