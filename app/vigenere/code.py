# Vinegere

def vinegere_table():
    table = []
    for i in range(90):
        table.append([])
    for row in range(90):
        set_elem = 0
        for column in range(90):
            table[row].append(chr(row + 33 + set_elem))
            set_elem += 1
            if set_elem > 89 - row:
                set_elem = set_elem - 90
    return table


def keyrep(message, keyword):
    msg_lenght = len(message)
    keyword_lenght = len(keyword)
    keyword_tab = ""
    keyword_index = 0

    for i in range(msg_lenght):
        if ord(message[i]) == 32:
            keyword_tab += " "
        else:
            if keyword_index < keyword_lenght:
                keyword_tab += keyword[keyword_index]
                keyword_index += 1
            else:
                keyword_index = 0
                keyword_tab += keyword[keyword_index]
                keyword_index += 1
    return keyword_tab


def cipher_encryption(message, mapped_key):
    table = vinegere_table()
    encrypted_text = ""
    for i in range(len(message)):
        if message[i] == chr(32):
            encrypted_text += " "
        else:
            row = ord(message[i]) - 33
            column = ord(mapped_key[i]) - 33
            encrypted_text += table[row][column]
    return encrypted_text


def itr_count(message, mapped_key):
    counter = 0
    result = ""

    for i in range(90):
        if mapped_key + i > 90:
            result += chr(mapped_key+(i-90))
        else:
            result += chr(mapped_key+i)

    for i in range(len(result)):
        if result[i] == chr(message):
            break
        else:
            counter += 1

    return counter


def cipher_decryption(message, mapped_key):
    table = vinegere_table()
    decrypted_text = ""

    for i in range(len(message)):
        if message[i] == chr(32):
            decrypted_text += " "
        else:
            decrypted_text += chr(33 + itr_count(ord(message[i]), ord(mapped_key[i])))

    return decrypted_text
