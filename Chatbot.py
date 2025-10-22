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


    if any(q in processed for q in ['hello', 'hi', 'hey']):
        return 'Hey there! 😊 Welcome to PNC chatbot.'
    
    if 'what is pnc' in processed or 'tell me about pnc' in processed:
        return 'PNC stands for Passerelles Numériques Cambodia. It’s an NGO that provides IT education and life skills to underprivileged youth. 💻📘'

    if 'where is pnc located' in processed or 'pnc location' in processed:
        return 'PNC is located in Phnom Penh, Cambodia. 📍'

    if 'what courses does pnc offer' in processed or 'pnc programs' in processed:
        return 'PNC offers training in IT fields such as Web Development, Networking, and Quality Assurance (QA). 👨‍💻'

    if 'how can i apply to pnc' in processed or 'pnc application' in processed:
        return 'You can apply to PNC through the official website or by following announcements during recruitment periods. 📝'

    if 'what is the mission of pnc' in processed or 'pnc mission' in processed:
        return 'The mission of PNC is to help underprivileged youth gain education, professional experience, and life skills to build a better future. 🌍'

    if 'who can study at pnc' in processed or 'pnc eligibility' in processed:
        return 'PNC accepts students from poor backgrounds who are motivated, hardworking, and have potential in IT. 🙌'

    if 'how long is the pnc program' in processed or 'pnc study duration' in processed:
        return 'The PNC program lasts for 2 years, including technical training, English, and soft skills. 🎓'

    if 'does pnc provide internship' in processed or 'pnc internship' in processed:
        return 'Yes! In the final year, students do an internship at a partner company to gain real-world experience. 💼'

    if 'who founded pnc' in processed or 'pnc founder' in processed:
        return 'PNC is part of Passerelles Numériques, founded in France in 2005 to support IT education in Southeast Asia. 🇫🇷'

    if 'what is the vision of pnc' in processed or 'pnc vision' in processed:
        return 'PNC’s vision is to create a world where education and technology empower youth to break the cycle of poverty. 🌟'

    if 'thank you' in processed or 'thanks' in processed:
        return 'You’re welcome! 😊 Glad to help. Do you want to know more about PNC?'

    if 'goodbye' in processed or 'bye' in processed:
        return 'Goodbye! 👋 Have a nice day and keep learning with PNC!'

    elif any(q in processed for q in ['what is the pnc scholarship', 'tell me about the pnc scholarship']):
        return 'The PNC Scholarship helps underprivileged students study IT for free at Passerelles Numériques Cambodia. 🎓'

    if any(q in processed for q in ['who can apply for pnc scholarship', 'pnc scholarship eligibility']):
        return 'Students from poor families with strong motivation and potential in IT can apply for the PNC Scholarship. 💪'

    if any(q in processed for q in ['what does the pnc scholarship cover', 'pnc scholarship benefits']):
        return 'The PNC Scholarship covers tuition fees, accommodation, meals, school materials, and personal development training. 🏫🍲📘'

    if any(q in processed for q in ['how to apply for pnc scholarship', 'pnc scholarship application']):
        return 'You can apply by filling out the application form on the official PNC website or during recruitment in your province. 📝'

    if any(q in processed for q in ['when is the pnc scholarship open', 'pnc scholarship deadline']):
        return 'The PNC Scholarship usually opens once a year. Follow PNC’s Facebook page for official announcements. 📅'

    if any(q in processed for q in ['does pnc scholarship include internship', 'pnc internship']):
        return 'Yes! During the last year, students do an internship at a partner company to gain real experience. 💼'

    if any(q in processed for q in ['does pnc provide allowance', 'pnc scholarship allowance']):
        return 'Yes, PNC provides an allowance for personal needs during your studies. 💰'

    if any(q in processed for q in ['where is pnc located', 'pnc location']):
        return 'PNC is located in Phnom Penh, Cambodia. 📍'

    if any(q in processed for q in ['is there an exam for pnc scholarship', 'pnc scholarship test']):
        return 'Yes! Applicants take an entrance exam that includes math, logic, and English tests. ✏️'

    if any(q in processed for q in ['does pnc provide interview', 'pnc scholarship interview']):
        return 'Yes. After passing the written test, candidates are invited for an interview to assess motivation and communication skills. 🎤'

    if any(q in processed for q in ['does pnc scholarship include internship', 'pnc internship']):
        return 'Yes! In the final year, students do an internship with a partner company to gain professional experience. 💼'

    if any(q in processed for q in ['does pnc provide allowance', 'pnc scholarship allowance']):
        return 'Yes, PNC provides a small monthly allowance for personal needs during your studies. 💰'

    if any(q in processed for q in ['where is pnc located', 'pnc location']):
        return 'PNC is located in Phnom Penh, Cambodia, near the Institute of Technology of Cambodia (ITC). 📍'

    if any(q in processed for q in ['how long is the pnc program', 'pnc study duration']):
        return 'The PNC program lasts 3 years — 2 years of technical and soft skill training, and 1 year for internship. 🎓'

    if any(q in processed for q in ['does pnc provide english class', 'pnc english training']):
        return 'Yes! English classes are included to help students communicate confidently in professional environments. 🗣️'

    if any(q in processed for q in ['what job can i get after graduation', 'pnc graduate jobs']):
        return 'Graduates often work as web developers, software testers, network administrators, or IT support officers in tech companies. 💻'

    if any(q in processed for q in ['how successful are pnc graduates', 'pnc alumni success']):
        return 'Most PNC graduates find jobs soon after graduation, with good salaries that help support their families. 🌟'

    if any(q in processed for q in ['pnc contact', 'how to contact pnc']):
        return 'You can contact PNC via Facebook Page “Passerelles Numériques Cambodia” or visit the official website: www.passerellesnumeriques.org 🌐'

    if any(q in processed for q in ['thank you', 'thanks']):
        return 'You’re welcome! 😊 Good luck with your PNC Scholarship application!'


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