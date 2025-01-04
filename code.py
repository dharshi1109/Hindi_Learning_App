import streamlit as st
import os
import openai
import os

openai.api_key = "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"

initial_prompt = """
You are an intelligent assistant. Whenever I provide a text para or sentence in hindi , respond in the following format.First if its a para display the sentence one by one.After displaying the sentence give its phonetic version in english followed by the english meaning of the sentence
and if its a sentence display it followed phonetic version then its english meaning. After that extract the keywords for the given para or sentence display its phonetic version ,english meaning in table format then display 5 example sentences for each and every keyword with the english meaning of the sentence
For example:
"prompt:छोटे बड़े सब को महत्व दो क्योंकि जहां सुई का काम है वहां तलवार काम नहीं करती
response:
Hindi Text: छोटे बड़े सब को महत्व दो क्योंकि जहां सुई का काम है वहां तलवार काम नहीं करती
Phonetic Transcription: Chhoṭe baṛe sab ko mahatva do kyunki jahān suī kā kām hai vahān talvār kām nahīṅ kartī
English Translation: Value everyone, big and small, because where a needle works, a sword does not.

Detailed Word Analysis

| Hindi Word | Phonetic Transcription | English Meaning |
|------------|------------------------|----------------|
| छोटे       | Chhoṭe                 | Small, younger |
| बड़े       | Baṛe                   | Big, elder     |
| सब         | Sab                    | Everyone, all  |
| को         | Ko                     | To             |
| महत्व      | Mahatva                | Importance     |
| दो         | Do                     | Give           |
| क्योंकि    | Kyunki                 | Because        |
| जहां       | Jahān                  | Where          |
| सुई        | Suī                    | Needle         |
| का         | Kā                     | Of             |
| काम        | Kām                    | Work           |
| है         | Hai                    | Is             |
| वहां       | Vahān                  | There          |
| तलवार      | Talvār                 | Sword          |
| नहीं       | Nahīṅ                  | Not            |
| करती       | Kartī                  | Does           |

Example Usage of Words

छोटे (Chhoṭe - Small, younger)
1. मेरा छोटा भाई स्कूल जा रहा है। (Mera chhoṭā bhāī skūl jā rahā hai.) - My younger brother is going to school.
2. उस गांव में छोटे छोटे घर हैं। (Us gāv meṅ chhoṭe chhoṭe ghar haiṅ.) - That village has small houses.
3. छोटे बच्चे खेल रहे हैं। (Chhoṭe bacche khel rahe haiṅ.) - Small children are playing.
4. इस बॉक्स में केवल छोटे सामान रखो। (Is bāks meṅ keval chhoṭe sāmān rakho.) - Only keep small items in this box.
5. छोटे पौधे जल्दी बढ़ते हैं। (Chhoṭe paudhe jaldī baḍhte haiṅ.) - Small plants grow quickly.

बड़े (Baṛe - Big, elder)
1. उसके बड़े भाई वकील हैं। (Uske baṛe bhāī vakīl haiṅ.) - His elder brother is a lawyer.
2. बड़े शहरों में अधिक अवसर होते हैं। (Baṛe shahroṅ meṅ adhik avsar hote haiṅ.) - Big cities have more opportunities.
3. बड़े होते ही समझदारी आती है। (Baṛe hote hī samajhdārī ātī hai.) - Wisdom comes with getting older.
4. वह बड़े ध्यान से सुन रहा था। (Vah baṛe dhyān se sun rahā thā.) - He was listening very attentively.
5. बड़े फैसले सोच समझकर लेने चाहिए। (Baṛe faisale soch samajhkar lene chāhie.) - Big decisions should be made thoughtfully.

सब (Sab - Everyone, all)
1. सब लोग खुश हैं। (Sab log khush haiṅ.) - Everyone is happy.
2. सब कुछ ठीक हो जाएगा। (Sab kuch ṭhīk ho jāegā.) - Everything will be alright.
3. मैंने सब को बुलाया है। (Maine sab ko bulāyā hai.) - I have invited everyone.
4. सब छात्र परीक्षा में बैठे। (Sab chhātr parīkṣā meṅ baithe.) - All students sat in the exam.
5. सब जगह शांति हो। (Sab jagah shānti ho.) - Let there be peace everywhere.

को (Ko - To)
1. मैं उसे एक किताब दी। (Maiṅ use ek kitāb dī.) - I gave him a book.
2. उसको जल्दी है। (Usko jaldī hai.) - He is in a hurry.
3. उसको कौन जानता है? (Usko kaun jāntā hai?) - Who knows him?
4. उसे कोई फर्क नहीं पड़ता। (Use koī fark nahīṅ paṛtā.) - It doesn't matter to him.
5. इसे यहाँ रख दो। (Ise yahāṅ rakh do.) - Put this here.

महत्व (Mahatva - Importance)
1. शिक्षा का बहुत महत्व है। (Shikṣā kā bahut mahatva hai.) - Education is very important.
2. समय का महत्व समझो। (Samay kā mahatva samjho.) - Understand the importance of time.
3. स्वास्थ्य को महत्व देना चाहिए। (Svāsthya ko mahatva denā chāhie.) - Health should be given importance.
4. महत्व की बातें पहले करो। (Mahatva kī bāteṅ pahle karo.) - Do important things first.
5. उसके काम का महत्व था। (Uske kām kā mahatva thā.) - His work was important.

दो (Do - Give)
1. कृपया मुझे पानी दो। (Kṛpayā mujhe pānī do.) - Please give me some water.
2. उसे एक मौका दो। (Use ek maukā do.) - Give him a chance.
3. उसे संदेश दो कि मैं आ रहा हूँ। (Use sandeś do ki maiṅ ā rahā hūṅ.) - Give him the message that I am coming.
4. इसे वापस दो। (Ise vāpas do.) - Give it back.
5. खुद को समय दो। (Khud ko samay do.) - Give yourself some time.

क्योंकि (Kyunki - Because)
1. मैं लेट हूँ क्योंकि ट्रैफिक था। (Maiṅ leṭ hūṅ kyunki ṭraifik thā.) - I am late because there was traffic.
2. उसने मना किया क्योंकि उसे समय नहीं था। (Usne manā kiyā kyunki use samay nahīṅ thā.) - He refused because he did not have time.
3. क्योंकि मौसम अच्छा है, हम पिकनिक पर जाएंगे। (Kyunki mausam acchā hai, ham piknik par jāeṅge.) - Because the weather is good, we will go for a picnic.
4. उसे चोट लगी क्योंकि वह गिर गया। (Use choṭ lagī kyunki vah gir gayā.) - He got hurt because he fell.
5. मैं खुश हूँ क्योंकि आप यहाँ हैं। (Maiṅ khuś hūṅ kyunki āp yahāṅ haiṅ.) - I am happy because you are here.
 "

"""

conversation_history = [{"role": "system", "content": initial_prompt}]

KEYWORDS_FILE = "keywords.txt"
def load_keywords_from_file(file_path):
    try:
        with open(file_path, 'r',encoding='utf-8') as file:
            return file.read().splitlines()  
    except FileNotFoundError:
        return []
def update_conversation_history(existing_keywords, conversation_history, system_prompt=""):
    keywords_text = ", ".join(existing_keywords)  
    conversation_history.append({
        "role": "system",
        "content": f"Please avoid repeating the following keywords in the conversation: {keywords_text}"
    })
    return conversation_history
extracted_keywords = load_keywords_from_file(KEYWORDS_FILE)
conversation_history = update_conversation_history(extracted_keywords, conversation_history)

def load_existing_keywords():
    if os.path.exists(KEYWORDS_FILE):
        with open(KEYWORDS_FILE, 'r', encoding='utf-8') as file:
            existing_keywords = {}
            for line in file:
                parts = line.strip().split(" - ")
                if len(parts) == 2:
                    existing_keywords[parts[0]] = parts[1]
            return existing_keywords
    return {}

def save_keywords(keywords):
    with open(KEYWORDS_FILE, 'a', encoding='utf-8') as file:
        for word, meaning in keywords.items():
            file.write(f"{word} - {meaning}\n")

def save_conversation(conversation):
    with open("conversation_history.txt", "a", encoding="utf-8") as file:
        for message in conversation:
            file.write(f"Role: {message['role']}\n")
            file.write(f"Message: {message['content']}\n")
            file.write("\n" + "="*50 + "\n")

def store_conversation_in_history(user_input, assistant_response):
    conversation = [
        {"role": "user", "content": user_input},
        {"role": "assistant", "content": assistant_response}
    ]
    save_conversation(conversation)


def process_hindi_text(hindi_text):
    conversation_history.append({"role": "user", "content": hindi_text})
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=conversation_history
    )
    
    reply = response['choices'][0]['message']['content'].strip()
    
    conversation_history.append({"role": "assistant", "content": reply})
    store_conversation_in_history(hindi_text, reply)
    return reply

import re

def load_keywords_from_file():
    keywords = {}
    if os.path.exists(KEYWORDS_FILE):
        with open(KEYWORDS_FILE, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(" - ")
                if len(parts) == 2:
                    keywords[parts[0]] = parts[1]
    return keywords


    
import re

def extract_and_store_keywords(response):
    existing_keywords = load_keywords_from_file()
    new_keywords = {}
    table_pattern = r"\| (\S.*?) \| (\S.*?) \| (\S.*?) \|"
    matches = re.findall(table_pattern, response)
    for match in matches:
        hindi_word = match[0].strip()  
        phonetic = match[1].strip()    
        english_meaning = match[2].strip()  
        if hindi_word not in existing_keywords:
            new_keywords[hindi_word] = english_meaning
    if new_keywords:
        save_keywords(new_keywords)
    
    #return new_keywords




def read_keywords_from_file():
    file_path = 'keywords.txt'
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read().splitlines()
    else:
        return []
def process_hindi_text1(hindi_text):
    result = process_hindi_text(hindi_text)  
    extract_and_store_keywords(result)          
    return result


def show_history_page():
    st.title("Conversation History")
    

    if os.path.exists("conversation_history.txt"):
        with open("conversation_history.txt", "r", encoding="utf-8") as file:
            history = file.read()
            if history:
                st.subheader("Past Conversations")
                st.text_area("All Conversations", history, height=300)
            else:
                st.write("No conversations stored.")
    else:
        st.write("No conversation history found.")



def show_prompt_page():
    st.title("Learning Hindi")
    hindi_text = st.text_area("Enter Hindi Text")
    
    if hindi_text:
        response = process_hindi_text1(hindi_text)
        
        st.subheader("Response")
        st.write(response)


def show_word_page():
    st.title("Words")
    
    #option = st.selectbox("Select Option", ["View Words", "Learn Words"])
    
    #if option == "View Words":
    words = read_keywords_from_file()
    if words:
        st.subheader("Words with meaning")
        table = "| Hindi Word | English Meaning |\n"
        table += "|------------|----------------|\n"
        
        for line in words:
                parts = line.split(" - ")  
                if len(parts) == 2: 
                    word, meaning = parts
                    table += f"| {word} | {meaning} |\n"
        
        
        st.markdown(table)
    else:
        st.write("No words found.")
    

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Choose a page", ["Prompt", "Words Page", "Conversation History"])
    
    if page == "Prompt":
        show_prompt_page()
    elif page == "Words Page":
        show_word_page()
    elif page == "Conversation History":
        show_history_page()


main()
