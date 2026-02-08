/* =========================
   GLOBAL ELEMENTS
========================= */
const homeScreen = document.getElementById("home");
const chatScreen = document.getElementById("chat");

const chatBox = document.getElementById("chat-box");
const input = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");
const voiceToggle = document.getElementById("voiceToggle");

const jinwoo = document.getElementById("jinwoo");

/* =========================
   ENTER DOMAIN (HOME → CHAT)
========================= */
function enterDomain() {
  homeScreen.classList.add("hidden");
  chatScreen.classList.remove("hidden");

  // Lock Jin-Woo animation when chat starts
  if (jinwoo) {
    jinwoo.style.animation = "none";
    jinwoo.style.transform = "none";
  }
}

/* =========================
   CHAT UI HELPERS
========================= */
function addMessage(text, sender) {
  const div = document.createElement("div");
  div.className = sender;

  const span = document.createElement("span");
  span.innerText = text;

  div.appendChild(span);
  chatBox.appendChild(div);
  chatBox.scrollTop = chatBox.scrollHeight;
}

/* =========================
   VOICE MODE (TEXT TO SPEECH)
========================= */
function speak(text) {
  if (!voiceToggle || !voiceToggle.checked) return;
  if (!window.speechSynthesis) return;

  const utter = new SpeechSynthesisUtterance(text);

  utter.rate = 0.9;   // calm
  utter.pitch = 0.9;  // deeper tone
  utter.volume = 1.0;

  speechSynthesis.cancel(); // avoid overlap
  speechSynthesis.speak(utter);
}

/* =========================
   SEND MESSAGE TO BACKEND
========================= */
function sendMessage() {
  const message = input.value.trim();
  if (!message) return;

  // Show user message
  addMessage(message, "user");
  input.value = "";

  // Temporary interpreting message
  addMessage("Shadow analysis in progress…", "bot");

  fetch("http://127.0.0.1:5000/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ message: message })
  })
    .then(res => res.json())
    .then(data => {
      // Remove "interpr​eting" line
      chatBox.removeChild(chatBox.lastChild);

      // Show AI response
      addMessage(data.reply, "bot");
      speak(data.reply);
    })
    .catch(() => {
      chatBox.removeChild(chatBox.lastChild);
      addMessage("Shadow link unstable. Retry command.", "bot");
    });
}

/* =========================
   EVENTS
========================= */
sendBtn.addEventListener("click", sendMessage);

input.addEventListener("keydown", (e) => {
  if (e.key === "Enter") {
    sendMessage();
  }
});

/* =========================
   JIN-WOO ANIME PRESENCE
   (DRAG + HOVER + ROTATE)
========================= */
let dragging = false;
let startX = 0;
let startY = 0;

if (jinwoo) {

  // Drag start
  jinwoo.addEventListener("mousedown", (e) => {
    dragging = true;
    startX = e.clientX;
    startY = e.clientY;
    jinwoo.classList.remove("release");
    jinwoo.style.cursor = "grabbing";
  });

  // Drag rotate
  document.addEventListener("mousemove", (e) => {
    if (!dragging) return;

    const dx = e.clientX - startX;
    const dy = e.clientY - startY;

    jinwoo.style.transform =
      `rotateY(${dx * 0.25}deg) rotateX(${-dy * 0.25}deg) scale(1.05)`;
  });

  // Drag end
  document.addEventListener("mouseup", () => {
    if (!dragging) return;

    dragging = false;
    jinwoo.style.cursor = "grab";
    jinwoo.classList.add("release");

    jinwoo.style.transform =
      "rotateX(0deg) rotateY(0deg) scale(1)";
  });

  // Hover parallax
  jinwoo.addEventListener("mousemove", (e) => {
    if (dragging) return;

    const rect = jinwoo.getBoundingClientRect();
    const cx = rect.left + rect.width / 2;
    const cy = rect.top + rect.height / 2;

    const dx = e.clientX - cx;
    const dy = e.clientY - cy;

    jinwoo.style.transform =
      `rotateY(${dx * 0.05}deg) rotateX(${-dy * 0.05}deg) scale(1.03)`;
  });

  // Reset on leave
  jinwoo.addEventListener("mouseleave", () => {
    if (dragging) return;

    jinwoo.style.transform =
      "rotateX(0deg) rotateY(0deg) scale(1)";
  });
}
