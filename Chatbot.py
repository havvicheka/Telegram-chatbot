from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from difflib import SequenceMatcher  # <-- Smart matching

# --- Bot Info ---
TOKEN = "8150838073:AAGUbykVJUs2qwl5QIrjOWU5KftG90lZ7Y8"
BOT_USERNAME: Final = '@VVVTT_2222_bot'

# --- Command Handlers ---
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello! I'm the Telegram VIP bot. Ask me anything about PNC (Passerelles Numériques Cambodia)!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💬 You can ask about: PNC programs, scholarships, requirements, internship, location, and more!")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✨ This is a custom command! Try asking me: 'What is PNC?' or 'Does PNC give scholarships?'")

# --- PNC Q&A Data ---
RESPONSES = {
    # --- General Info ---
    "what is pnc": "💻 Passerelles Numériques Cambodia (PNC) is an NGO providing IT education and life skills to underprivileged youth.",
    "tell me about pnc": "🌍 PNC trains underprivileged young Cambodians in IT, English, and soft skills for better job opportunities.",
    "who founded pnc": "🇫🇷 Passerelles Numériques was founded in France in 2005 to support IT education in Southeast Asia.",
    "when was pnc established": "📅 PNC Cambodia was established in 2005 under Passerelles Numériques’ global mission.",
    "who can study at pnc": "🙋‍♀️ PNC accepts students from underprivileged backgrounds who show strong motivation and discipline.",
    "what does pnc stand for": "🔠 PNC stands for Passerelles Numériques Cambodia.",
    "where is pnc": "📍 PNC is located in Phnom Penh, Cambodia, near Pochentong area.",
    "who manages pnc": "👩‍🏫 PNC is managed by Cambodian and international staff with support from NGOs and private partners.",

    # --- Mission / Vision / Values ---
    "pnc mission": "🌍 PNC’s mission is to help underprivileged youth access education, professional training, and life skills.",
    "pnc vision": "🌟 PNC’s vision is to build a world where education and technology empower youth to break poverty cycles.",
    "pnc values": "💡 PNC values include Responsibility, Respect, Solidarity, and Trust.",

    # --- Programs & Training ---
    "pnc programs": "📚 PNC offers a 2-year IT training program with English, soft skills, and internship.",
    "what courses does pnc offer": "🖥️ PNC offers courses in software development, networking, database, and QA.",
    "pnc duration": "🎓 The PNC program lasts 2 years, including a professional internship.",
    "does pnc teach english": "🗣️ Yes! English is part of the training to prepare students for international jobs.",
    "does pnc teach soft skills": "🤝 Yes! Students learn teamwork, communication, and time management.",
    "does pnc teach programming": "💻 Definitely! PNC teaches web development, databases, and software engineering.",
    "pnc internship": "💼 In the final year, all students complete a 5–6 month internship at a partner company.",
    "pnc schedule": "🕒 Students usually have full-day classes Monday to Friday, with activities on weekends.",
    "pnc subjects": "📖 Subjects include Programming, Database, Networking, QA, English, Soft Skills, and Life Skills.",

    # --- Scholarship & Admission ---
    "pnc scholarship": "🎓 PNC provides a full scholarship covering tuition, dorm, food, materials, and healthcare.",
    "how to apply to pnc": "📝 Apply through school visits, online registration, or entrance exams during recruitment season.",
    "pnc eligibility": "🙌 Applicants must be from poor families, show motivation, and have completed high school.",
    "pnc requirement": "✅ Must be 17–22 years old, from low-income families, and passionate about IT.",
    "pnc recruitment process": "📋 Includes written tests (math, logic, English), interview, and home visit.",
    "pnc scholarship benefits": "🎁 Full support: tuition, dorm, food, materials, uniform, and healthcare.",
    "pnc scholarship exam": "✏️ Entrance exams include math, logic, and English tests.",
    "pnc scholarship interview": "🎤 Yes. After the written test, there’s an interview to check your motivation.",
    "when is pnc admission open": "📆 Recruitment usually starts around February–April every year.",
    "is pnc free": "💸 Yes! PNC is a full scholarship program — students don’t pay any fees.",
    "how many students are accepted": "👩‍🎓 About 100–150 new students are accepted each year.",

    # --- Student Life ---
    "pnc dorm": "🏠 Yes, dormitory accommodation is provided for students with meals and basic needs.",
    "pnc food": "🍲 PNC provides daily meals for all students.",
    "pnc activities": "🎉 Students join clubs, community service, sports, and cultural events.",
    "pnc clubs": "🤝 PNC has English, IT, Volunteer, Robotics, Sports, Film, and Design clubs.",
    "pnc student life": "😊 Life at PNC is fun and supportive — students live, study, and grow together.",
    "can girls study at pnc": "👩 Yes! PNC strongly encourages female applicants and promotes gender equality.",

    # --- After Graduation ---
    "pnc jobs": "💻 Graduates work as developers, QA testers, network admins, or IT support officers.",
    "pnc alumni success": "🌟 Most graduates find jobs soon after graduation with good salaries and career growth.",
    "pnc partner companies": "🏢 PNC works with many IT companies in Cambodia and abroad for internships and jobs.",
    "pnc salary": "💰 Most PNC graduates earn a stable income higher than Cambodia’s average salary.",
    "pnc graduate rate": "🎓 Nearly all students graduate and secure jobs within months.",

    # --- Contact / Support ---
    "contact pnc": "📧 Contact: info@pn-cambodia.org 🌐 https://www.passerellesnumeriques.org/what-we-do/cambodia/",
    "pnc website": "🌐 https://www.passerellesnumeriques.org/what-we-do/cambodia/",
    "pnc facebook": "📱 Facebook: https://www.facebook.com/PasserellesNumeriquesCambodia",
    "pnc address": "📍 PNC is located in Phnom Penh, Cambodia, near Pochentong area.",
    "pnc phone": "📞 You can reach PNC via +855 (0)23 99 55 00.",

    # --- Polite / Extra ---
    "thank you": "😊 You’re welcome! Would you like to learn more about scholarships or programs?",
    "goodbye": "👋 Goodbye! Keep learning and dreaming with PNC!",
    "hello": "👋 Hi there! Welcome to PNC info bot — how can I help you today?",
    "hi": "Hey there! 😊 Want to learn about PNC programs or scholarships?",
    "who are you": "🤖 I’m your friendly PNC info bot, here to help you learn everything about Passerelles Numériques Cambodia!"
}

DEFAULT_REPLY = (
    "🤔 Sorry, I’m not sure about that. You can contact PNC for help:\n"
    "📧 info@pn-cambodia.org\n🌐 https://www.passerellesnumeriques.org/what-we-do/cambodia/"
)

# --- Smart Text Matching Function ---
def get_best_response(user_text: str) -> str:
    processed = user_text.lower()
    best_match = None
    best_score = 0.0

    for question, answer in RESPONSES.items():
        score = SequenceMatcher(None, processed, question).ratio()
        if score > best_score:
            best_score = score
            best_match = answer

    if best_score > 0.45:  # threshold for flexible matching
        return best_match
    return DEFAULT_REPLY


# --- Message Handler ---
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    message_type = update.message.chat.type
    print(f'User({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group' and BOT_USERNAME in text:
        text = text.replace(BOT_USERNAME, '').strip()

    response = get_best_response(text)
    print('Bot:', response)
    await update.message.reply_text(response)

# --- Error Handler ---
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")

# --- Run Bot ---
if __name__ == '__main__':
    print("🤖 Starting smart PNC bot...")
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    print("🚀 Bot is polling...")
    app.run_polling(poll_interval=1)

