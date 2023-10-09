def ensure_book(book: str, text: str):
    miss = []
    for c in text:
        if c not in book:
            miss.append(c)

    return book + "".join(miss)


gen_code_keys = lambda book, plain_text: ({c: str(book.find(c)) for c in plain_text})

encoder = lambda code_keys, plain_text: "".join(
    ["*" + code_keys[c] for c in plain_text]
)[1:]

encrypt = lambda book, plain_text: encoder(gen_code_keys(book, plain_text), plain_text)

gen_decode_keys = lambda book, cipher_text: {
    s: book[int(s)] for s in cipher_text.split("*")
}

book = "unuhoangdzqjuwhwuhfh"
text = "ho1angdzp12"

book = ensure_book(book, text)
code = encrypt(book, text)

print(code)
print("".join(gen_decode_keys(book, code).values()))
