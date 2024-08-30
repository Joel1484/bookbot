def main():
    path_to_frankenstein = "books/frankenstein.txt"
    text_to_print = get_book_content(path_to_frankenstein)
    wordcount = get_wordcount(text_to_print)
    amount_of_characters = get_character_amount(text_to_print)
    print(text_to_print)
    print(f"--- Begin report of {path_to_frankenstein} ---")
    print(f"This book contains {wordcount} words.")
    for d in amount_of_characters:
        print(f"The letter {d['name']} appears {d['num']} in the Book.")
    print("--- End of report ---")

def get_book_content(book_path):
        with open (book_path) as f:
            return f.read()

def get_wordcount(text):
        words = text.split()
        num_of_words = len(words)
        return num_of_words

def sort_on(dict):
    return dict["num"]

def get_character_amount(text):
        amount = {}
        list = []
        low_string = text.lower()
        for l in low_string:
            if l in amount:
                amount[l] += 1
            else:
                amount[l] = 1
        for a in amount:
            if a.isalpha():
                list.append({"name" : a , "num" : amount[a]})
        list.sort(reverse=True, key=sort_on)
        
        return list           

main()