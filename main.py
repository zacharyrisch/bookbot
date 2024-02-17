def main():
    with open("./books/frankenstein.txt") as f: 
        file_contents = f.read()
        # print(file_contents)


def count_words():
    with open("./books/frankenstein.txt") as f: 
        file_contents = f.read()
        word_list = file_contents.split()
        return len(word_list)
    
def character_count(book_path): 
    with open(book_path) as f: 
        file_contents = f.read()
        string = file_contents
        lower_string = string.lower()
        character_dict = {}
        for letter in lower_string: 
            if letter.isalpha():
                if letter in character_dict:
                    character_dict[letter] += 1
                else: 
                    character_dict[letter] = 1
        return character_dict
    
def sort_on(character_dict):
    return character_dict["num"]

character_dict = character_count("./books/frankenstein.txt")
characters =[]
for character, count in character_dict.items():
        characters.append({"letter": character, "num": count})

characters.sort(reverse=True, key=sort_on)
print(characters)
    
git add .
git commit -m "sorted character list"
git push origin main        




main()



