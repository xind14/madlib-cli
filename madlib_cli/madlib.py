# import os

# print("Current working directory:", os.getcwd())

def welcome_message ():
    print('''

    Welcome to the Madlib game!

    ''')
    
welcome_message()

stormy_path = './assets/dark_and_stormy_night_template.txt'
videogame_path = './assets/make_me_a_video_game_template.txt'

def read_template(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
          raise FileNotFoundError


def parse_template(template):
    parts_of_speech = []
    # print(parts_of_speech)
    split_template = template.split('{')
    # print("split_template:", split_template)

    for i in range(1, len(split_template)):
        singular_speech, remaining_char = split_template[i].split('}', 1)
        # print("part:", singular_speech)
        # print("rest:", remaining_char)
        parts_of_speech.append(singular_speech)
        # print(parts_of_speech)
        split_template[i] = remaining_char
        # print(split_template)

    stripped_template = '{}'.join(split_template)
    # print("stripped_template:", stripped_template)


    return stripped_template, tuple(parts_of_speech)


# template_example = "It was a {Adjective} and {Adjective} {Noun}."
# parse_template(template_example)

def merge(stripped_template, parts_of_speech):
    result = stripped_template.format(*parts_of_speech)
    return result




def madlib_generator():

    template = read_template(videogame_path)
    stripped_template, parts_of_speech = parse_template(template)
    user_input = []
    for word in parts_of_speech:
        word_input = input(f"\nEnter {word} > ")
        user_input.append(word_input)
    final_madlib = merge(stripped_template, user_input)
    print(f"\n\n\nHere is you completed Madlib: \n\n{final_madlib}\n")

    with open ('assets/final_madlib.txt', 'w') as file:
        file.write(final_madlib)

madlib_generator()