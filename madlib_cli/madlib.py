def welcome_message ():
    print('''

    Welcome to the Madlib game!

    ''')
    
welcome_message()

videogame_path = 'assets/make_me_a_video_game_template.txt'
stormy_path = 'assets/dark_and_stormy_night_template.txt'

def read_template(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
          raise FileNotFoundError


def parse_template(template):
    parts_of_speech = []
    print(parts_of_speech)
    split_template = template.split('{')
    print("split_template:", split_template)

    for i in range(1, len(split_template)):
        singular_speech, remaining_char = split_template[i].split('}', 1)
        print("part:", singular_speech)
        print("rest:", remaining_char)
        parts_of_speech.append(singular_speech)
        print(parts_of_speech)
        split_template[i] = remaining_char
        print(split_template)

    stripped_template = '{}'.join(split_template)
    print("stripped_template:", stripped_template)


    return stripped_template, tuple(parts_of_speech)


template_example = "It was a {Adjective} and {Adjective} {Noun}."
parse_template(template_example)







# def test_merge():


# Create and test a merge function that takes in a “bare” template and a list of user entered language parts, and returns a string with the language parts inserted into the template.
