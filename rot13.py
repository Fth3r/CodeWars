# 6 kyu kata
def rot13(message):
    bank = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    upper_bank = bank.upper()
    new_message = ""
    
    for l in range(len(message)):
        if message[l] in bank:
            i = bank.find(message[l])
            new_message = new_message + bank[i+13]
        elif message[l] in upper_bank:
            i = upper_bank.find(message[l])
            new_message = new_message + upper_bank[i+13]
        else:
            new_message = new_message + message[l]
    return new_message
