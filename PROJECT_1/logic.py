def tekan_logic(current_text, new_char):
    return current_text + new_char

def hitung_logic(text):
    try:
        return str(eval(text))
    except:
        return "Error"

def clear_logic():
    return ""
