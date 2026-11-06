const input = document.getElementById("user-input");

const sendButton = document.getElementById("send-button");

const chatBox = document.getElementById("chat-box");

let isSending = false;


function addMessage(message, type) {

    const messageElement = document.createElement("div");

    messageElement.classList.add("message");

    messageElement.classList.add(type);

    messageElement.textContent = message;

    chatBox.appendChild(messageElement);

    chatBox.scrollTop = chatBox.scrollHeight;
}


async function sendMessage() {

    const question = input.value.trim();


    if (question === "" || isSending) {
        return;
    }

    isSending = true;
    sendButton.disabled = true;


    // Display user's message
    addMessage(question, "user-message");


    // Clear input
    input.value = "";


    try {

        const response = await fetch("/ask", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question: question
            })

        });


        if (!response.ok) {
            throw new Error(`Request failed with status ${response.status}`);
        }

        const data = await response.json();


        // Display bot's response
        addMessage(data.answer, "bot-message");


    } catch (error) {

        addMessage(
            "Sorry, something went wrong.",
            "bot-message"
        );

        console.error(error);

    } finally {

        isSending = false;
        sendButton.disabled = false;
    }
}


sendButton.addEventListener("click", sendMessage);


input.addEventListener("keypress", function(event) {

    if (event.key === "Enter") {

        event.preventDefault();
        sendMessage();

    }

});