def get_num_words(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    words = file_contents.split()
    return len(words)


def characters(path_to_file):
    with open(path_to_file, encoding="utf-8-sig") as f:
        file_contents = f.read()
    lowercase_text = file_contents.lower()

    character_count = {}

    for character in lowercase_text:
        if character not in character_count:
            character_count[character] = 1
        else:
            character_count[character] += 1

    return character_count


def sort_characters(path_to_file):
    with open(path_to_file, encoding="utf-8-sig") as f:
        file_contents = f.read()
    lowercase_text = file_contents.lower()

    character_count = {}

    for character in lowercase_text:
        if character not in character_count:
            character_count[character] = 1
        else:
            character_count[character] += 1

    # gjør om {c:n, c:n, c:n} til 
    # [{c:c, n:n},{c:c, n:n},{c:c, n:n}]
    # for så å sortere
    def sort_on(items):
        return items["num"]

    sorted_list = []

    for ch, count in character_count.items():
        sorted_list.append({"char": ch, "num": count})

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list

