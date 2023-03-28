import requests
import telebot

API_KEY = ''
COD_EX_API_URL = 'https://api.codex.jaagrav.in'

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the mobile compiler.")

@bot.message_handler(func=lambda message: True)
def prompt_for_language(message):
    bot.reply_to(message, "Enter the language of the code to be compiled:")
    bot.register_next_step_handler(message, prompt_for_input)

def prompt_for_input(message):
    language = message.text.strip()
    bot.reply_to(message, "Enter the code to be compiled:")
    bot.register_next_step_handler(message, compile_code, language)

def compile_code(message, language):
    code = message.text.strip()
    input_str = ""
    if language.lower() == 'python':
        language= 'py'
        bot.reply_to(message, "Enter the input for the code (if any else send anything):")
        bot.register_next_step_handler(message, run_code, code, language, input_str)
    elif language.lower()== "c++" or language.lower()=="cpp":
        language= 'cpp'
        bot.reply_to(message, "Enter the input for the code (if any else send anything):")
        bot.register_next_step_handler(message, run_code, code, language, input_str)
    elif language.lower()== "java":
        language= 'java'
        bot.reply_to(message, "Enter the input for the code (if any else send anything):")
        bot.register_next_step_handler(message, run_code, code, language, input_str)
    elif language.lower()== "c":
        language= 'c'
        bot.reply_to(message, "Enter the input for the code (if any else send anything):")
        bot.register_next_step_handler(message, run_code, code, language, input_str)
    elif language.lower()== "go" or language.lower()=="golang":
        language= 'go'
        bot.reply_to(message, "Enter the input for the code (if any else send anything):")
        bot.register_next_step_handler(message, run_code, code, language, input_str)
    elif language.lower()== "c#" or language.lower()=="cs":
        language= 'cs'
        bot.reply_to(message, "Enter the input for the code (if any else send anything):")
        bot.register_next_step_handler(message, run_code, code, language, input_str)
    elif language.lower()== 'javascript' or language.lower()=="js":
        language= 'js'
        bot.reply_to(message, "Enter the input for the code (if any else send anything):")
        bot.register_next_step_handler(message, run_code, code, language, input_str)
    else:
        
        bot.reply_to(message, "Oops, We only support Java, Python, C++, C , GoLang, C# and JavaScript")
            

def run_code(message, code, language, input_str):
    input_str = message.text.strip()
    payload = {
        'code': code,
        'language': language,
        'input': input_str
    }
    try:
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(COD_EX_API_URL, data=payload, headers=headers) # compile the code
        output = response.json().get('output') # extract the output from the response
        if output:
            bot.reply_to(message, output) # send the output back to the user
        else:
            bot.reply_to(message, "Sorry, an error occurred while compiling the code.")
            
        # unregister the message handlers
        bot.remove_message_handler(run_code)
        bot.remove_message_handler(compile_code)
        bot.remove_message_handler(prompt_for_input)
        bot.remove_message_handler(prompt_for_language)
    except:
        print("Error Occured")

bot.polling()
