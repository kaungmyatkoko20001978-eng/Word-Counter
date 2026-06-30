words=''
while words != "quit":
    words=(input("Paste your text here(Type in 'quit' to exit program): "))
    character_count=(len(words.replace(" ","")))
    print(f"Total Characters(Not Including Spaces): {character_count} ")
    word_count = words.split()
    print(f"Total Words: {len(word_count)}")