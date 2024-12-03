const startBtn = document.getElementById("start-btn");
const userText = document.getElementById("user-text");
const aiResponse = document.getElementById("ai-response");

let recognition;
if ("webkitSpeechRecognition" in window) {
    recognition = new webkitSpeechRecognition(); // Use Web Speech API
    recognition.lang = "en-US";
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;

    recognition.onresult = (event) => {
        const speech = event.results[0][0].transcript;
        userText.textContent = speech;

        // Simulate AI response (placeholder for backend integration)
        aiResponse.textContent = "Processing...";

        fetchAIResponse(speech);
    };

    recognition.onerror = (event) => {
        alert("Speech recognition error: " + event.error);
    };
} else {
    alert("Speech Recognition not supported in this browser.");
}

startBtn.addEventListener("click", () => {
    recognition.start();
});

// Placeholder for AI processing (replace with actual API calls)
function fetchAIResponse(speech) {
    setTimeout(() => {
        aiResponse.textContent = "I heard: " + speech; // Simulated response
    }, 1000);
}
