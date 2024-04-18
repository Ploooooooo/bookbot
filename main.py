def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    switched_to_lower = to_lowercase(text)
    letterd_dict = characted_count(switched_to_lower)
    sorted_dict = sort_dict(letterd_dict)
    after_sort_dict_of_dict = sort_on(sorted_dict)
    print (f"--- Begin report of {book_path} ---")
    print (f"{word_count} words found in the document")
    for index in range(len(after_sort_dict_of_dict)):
        for key, value in after_sort_dict_of_dict[index].items():
            print(f"The '{key}' character was found '{value}' times")
    print ("--- End report ---")


def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents
    
def count_words(text):
    words = text.split()
    return len(words)
    
def to_lowercase(text):
    lowercase = text.lower()
    return (lowercase)

def characted_count(switched_to_lower):
    string = switched_to_lower
    lst = []
    for letter in string:
        lst.append(letter)
    letters_counter = {}
    for l in lst:
        if l in letters_counter:
            letters_counter[l] +=1
        else:
            letters_counter[l] = 1
    return (letters_counter)

def sort_dict (letterd_dict):
    final_dict={}
    for key in letterd_dict:
        if key.isalpha()==True:
            final_dict[key]=letterd_dict[key]
    return (final_dict)

def sort_on(sorted_dict):
    sorted_dict_by_v = sorted(sorted_dict.items(), key=lambda x:x[1], reverse=True)
    back_to_dict = dict(sorted_dict_by_v)
    dict_of_dict = [{key: value} for key, value in back_to_dict.items()]
    return (dict_of_dict)
            

main()
