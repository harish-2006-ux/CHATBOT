const chat = document.getElementById("chat");
const sendBtn = document.getElementById("send-btn");
const input = document.getElementById("user-input");
const chatBox = document.getElementById("chat-box");
const voiceToggle = document.getElementById("voiceToggle");

function enterDomain() {
  document.body.classList.add("domain-active");
  chat.classList.remove("hidden");
}

function addMessage(text, sender) {
  const div = document.createElement("div");
  div.className = sender;
  div.innerHTML = `<span>${text}</span>`;
  chatBox.appendChild(div);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function speak(text) {
  if (!voiceToggle.checked) return;
  speechSynthesis.speak(new SpeechSynthesisUtterance(text));
}

function sendMessage() {
  const msg = input.value.trim();
  if (!msg) return;

  addMessage(msg, "user");
  input.value = "";
  addMessage("Shadow analysis in progress…", "bot");

 fetch("https://chatbot-21v7.onrender.com/chat", {

    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: msg })
  })
  .then(res => res.json())
  .then(data => {
    chatBox.removeChild(chatBox.lastChild);
    addMessage(data.reply, "bot");
    speak(data.reply);
  });
}

sendBtn.onclick = sendMessage;
input.addEventListener("keydown", e => {
  if (e.key === "Enter") sendMessage();
});
