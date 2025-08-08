# Gemini AI Chatbot

A modern, minimalistic AI-powered chatbot built with **React.js** (frontend) and **Node.js/Express** (backend), integrated with Google's **Gemini API** for intelligent, conversational responses.  
Designed with a sleek **yellow & black** theme, real-time typing animations, Markdown support, and speech capabilities.

---

## 🚀 Features

- **Conversational AI** powered by Gemini API  
- **Minimalistic UI** with a classic yellow & black color scheme  
- **Typing animation** for smooth bot responses  
- **Markdown rendering** with syntax-highlighted code blocks  
- **Auto-scroll** to the latest message  
- **Dark mode toggle**  
- **Speech-to-text & text-to-speech** support  
- **Chat history** saved locally in `localStorage`  
- **Avatars** for user & bot messages

---

## 🛠️ Tech Stack

**Frontend**  
- React.js  
- Tailwind CSS (for styling)  
- React Markdown & Syntax Highlighter  
- Web Speech API (TTS & STT)

**Backend**  
- Node.js & Express.js  
- Gemini API SDK (Google Generative AI)  
- CORS enabled for frontend-backend communication

---

## 📂 Project Structure

ai-chatbot-gemini/
│
├── backend/ # Express server + Gemini API integration
│ ├── index.js
│ └── package.json
│
├── ai-chatbot/ # React frontend
│ ├── public/
│ ├── src/
│ └── package.json
│
└── README.md

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/samuel-maithre/ai-chatbot-gemini.git
cd ai-chatbot-gemini

```
### Backend Setup
cd backend
npm install

### Frontend Setup
cd ../ai-chatbot
npm install
npm start

🤝 Contributing
Pull requests are welcome! Please follow standard Git branching and commit guidelines.

👤 Author
Samuel Maithre
