from typing import Final
from telegram import Update
import re
from telegram.ext import Application,CommandHandler, MessageHandler,filters,ContextTypes
TOKEN = "8150838073:AAGUbykVJUs2qwl5QIrjOWU5KftG90lZ7Y8"
BOT_USERNAME:Final = '@VVVTT_2222_bot'

#command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Thanks for chatting with me! I am a Telegram VIP!")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I am a Telegram VIP!Please type somthing so I can respond")


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command!")

#Responses

def handle_response(text: str) -> str:
    processed: str = text.lower()
    words = processed.split()

     # General Info
    if any(q in processed for q in ['hello', 'hi', 'hey']):
        return 'Hey there! 😊 Welcome to Telegram VIP bot.'
    
    if 'what is pnc' in processed or 'tell me about pnc' in processed:
        return 'PNC stands for Passerelles Numériques Cambodia. It’s an NGO that provides IT education and life skills to underprivileged youth. 💻📘'

    if 'where is pnc' in processed or 'pnc location' in processed:
        return 'PNC is located in Phnom Penh, Cambodia. 📍'

    if 'tell me about pnc' in processed or 'pnc programs' in processed:
        return "🌏 Passerelles numériques Cambodia (PNC) is a non-profit organization providing IT education and personal development to underprivileged youth, preparing them for professional careers. 💡"

    if 'what is the mission of pnc' in processed or 'pnc mission' in processed:
        return 'The mission of PNC is to help underprivileged youth gain education, professional experience, and life skills to build a better future. 🌍'
    
    if 'what is the vision of pnc' in processed or 'pnc vision' in processed:
        return 'PNC’s vision is to create a world where education and technology empower youth to break the cycle of poverty. 🌟'
    
    if 'who founded pnc' in processed or 'pnc founder' in processed:
        return 'PNC is part of Passerelles Numériques, founded in France in 2005 to support IT education in Southeast Asia. 🇫🇷'
    
    if 'pnc values' in processed or 'how many values' in processed:
        return '🌟 PNC promotes Responsibility, Respect, Solidarity, and Trust.💡'


    # Scholarship

    if 'how can i apply to pnc' in processed or 'pnc application' in processed:
        return 'You can apply to PNC through the official website or by following announcements during recruitment periods. 📝'
    
    if 'who can study at pnc' in processed or 'pnc eligibility' in processed:
        return 'PNC accepts students from poor backgrounds who are motivated, hardworking, and have potential in IT. 🙌'

    if 'how long is the pnc program' in processed or 'pnc study duration' in processed:
        return 'The PNC program lasts for 2 years, including technical training, English, and soft skills. 🎓'

    if 'does pnc provide internship' in processed or 'pnc internship' in processed:
        return 'Yes! In the final year, students do an internship at a partner company to gain real-world experience. 💼'
    
    if 'study for free at pnc' in processed or 'pnc study free or not' in processed:
        return '🎓 PNC provides full scholarships covering tuition, accommodation, meals, study materials, and healthcare. Students must come from low-income families, have completed high school, and show strong motivation to study IT. The scholarship lasts 2years, including a professional internship, with career guidance after graduation. '
    
    if 'how to apply' in processed or 'pnc requirement' in processed :
        return '📝 Admission includes application submission, entrance exams (English & math), interview, and a home visit to verify financial need. Only motivated students from disadvantaged backgrounds are selected. ✅'
    
    if 'what do students learn' in processed or 'pnc subjects' in processed:
        return '💻 PNC’s 2-year program covers programming, databases, networking, QA, English, and soft skills like communication, teamwork, and leadership. The final year includes a professional internship. 🚀'
    
    if 'does pnc provide internship' in processed or 'pnc internship' in processed:
        return 'Yes! In the final year, students do an internship at a partner company to gain real-world experience. 💼'
    
    if'what is the pnc scholarship' in processed or 'tell me about the pnc scholarship'in processed:
        return 'The PNC Scholarship helps underprivileged students study IT for free at Passerelles Numériques Cambodia. 🎓'
    
    if 'does pnc provide internship' in processed or 'pnc internship' in processed:
        return 'Yes! In the final year, students do an internship at a partner company to gain real-world experience. 💼'
    
    if 'why choose pnc' in processed:
        return '🌟 PNC emphasizes Responsibility, Respect, Solidarity, and Trust. These values guide academics, student life, and professional training, developing ethical and skilled IT professionals.'

    if'who can apply for pnc scholarship'in processed or 'pnc scholarship eligibility' in processed:
        return 'Students from poor families with strong motivation and potential in IT can apply for the PNC Scholarship. 💪'
    
    if'how to contact pnc"'in processed or 'how to join' in processed:
        return '📧 You can contact PNC via email at info@pn-cambodia.org or visit their website at www.pn-cambodia.org for more details. 🌐'

    if'how long is the pnc program'in processed or'pnc study duration' in processed:
        return 'The PNC program 2 years of technical and soft skill training, and 4 month for internship. 🎓'

    if'what does the pnc scholarship cover'in processed or 'pnc scholarship benefits'in processed :
        return 'The PNC Scholarship covers tuition fees, accommodation, meals, school materials, and personal development training. 🏫🍲📘'

    if'how to apply for pnc scholarship'in processed or 'pnc scholarship application' in processed :
        return 'You can apply by filling out the application form on the official PNC website or during recruitment in your province. 📝'

    if 'when is the pnc scholarship open'in processed or 'pnc scholarship deadline'in processed:
        return 'The PNC Scholarship usually opens once a year. Follow PNC’s Facebook page for official announcements. 📅'

    if'does pnc scholarship include internship'in processed or'pnc internship'in processed:
        return 'Yes! During the last year, students do an internship at a partner company to gain real experience. 💼'

    if'does pnc provide allowance'in processed or 'pnc scholarship allowance'in processed:
        return 'Yes, PNC provides an allowance for personal needs during your studies. 💰'

    if'is there an exam for pnc scholarship'in processed or'pnc scholarship test'in processed:
        return 'Yes! Applicants take an entrance exam that includes math, logic, and English tests. ✏️'

    if'does pnc provide interview'in processed or 'pnc scholarship interview'in processed:
        return 'Yes. After passing the written test, candidates are invited for an interview to assess motivation and communication skills. 🎤'

    if'does pnc provide english class'in processed or'pnc english training'in processed:
        return 'Yes! English classes are included to help students communicate confidently in professional environments. 🗣️'

    if'what job can i get after graduation'in processed or'pnc graduate jobs'in processed:
        return 'Graduates often work as web developers, software testers, network administrators, or IT support officers in tech companies. 💻'

    if'how successful are pnc graduates'in processed or'pnc alumni success'in processed:
        return 'Most PNC graduates find jobs soon after graduation, with good salaries that help support their families. 🌟'

    if "how to get scholarship"in processed :
        return "📝 Apply during admission, pass entrance exams, attend interview, and have financial needs verified by PNC social workers. ✅"
    
    if "learning method" in processed: 
        return"📖 PNC uses hands-on learning, projects, teamwork, mentoring, and continuous assessment to prepare students for real IT jobs. 🛠️"
    
    if "student clubs" in processed or "do you have club study for student" in processed: 
        return"Clubs include English Club, IT Club, Volunteer Club, Arobit Club, sports club,film club,Design club 🤝"
    
    if 'benifit at pnc' in processed or 'What is benitfit at pnc' in processed:
        return'You get a lot of such as computer one for learn 2 year food 3 time in one day, bike, healthy,dorm for lived.'
 
    if 'thank you' in processed or 'thanks' in processed:
        return 'You’re welcome! 😊 Glad to help. Do you want to know more about PNC?'

    if 'goodbye' in processed or 'bye' in processed:
        return 'Goodbye! 👋 Have a nice day and keep learning with PNC!'

    return'I do not understand what you wrote...'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print('Update{update}caused error{context.error}')

if __name__ == '__main__':
    print('starting bot...')
    app =Application.builder().token(TOKEN).build()

    #commands

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    
    #Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #error
    app.add_error_handler(error)
    # Poll the bot
    print('Polling...')
    app.run_polling(poll_interval=3)