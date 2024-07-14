const quotes = [
    "sudo apt-get update cyber_news",
    "#1 Trusted Cybersecurity News Platform.",
    "Bits, Bytes, and Breaking News."
];

let currentQuoteIndex = 0;
let currentCharIndex = 0;
const quotesElement = document.getElementById("quotes");

function typeQuote() {
    const currentQuote = quotes[currentQuoteIndex];

    if (currentCharIndex < currentQuote.length) {
        quotesElement.innerHTML += currentQuote.charAt(currentCharIndex);
        currentCharIndex++;
        setTimeout(typeQuote, 50);
    } else {
        setTimeout(eraseQuote, 1000);
    }
}

function eraseQuote() {
    const currentQuote = quotes[currentQuoteIndex];

    if (currentCharIndex > 0) {
        quotesElement.innerHTML = currentQuote.substring(0, currentCharIndex - 1);
        currentCharIndex--;
        setTimeout(eraseQuote, 30);
    } else {
        currentQuoteIndex = (currentQuoteIndex + 1) % quotes.length; // Loop through quotes
        setTimeout(typeQuote, 500);
    }
}

// Start the typewriter effect
typeQuote();