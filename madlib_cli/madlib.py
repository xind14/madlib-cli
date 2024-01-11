def welcome_message ():

    """
    Print a welcome message to the user

    The welcome message includes instructions on the game and how to quit the game.
    """

    print('''
    *******************************************************
    **             Welcome to the Madlib Game            **
    **                                                   **
    **      Input the type of speech when prompted.      **
    **      For example (Adjective, Noun, Verb etc).     **
    **                                                   **
    **          To quit at any time, type "quit"         **
    *******************************************************

    ''')
    
welcome_message()

stormy_path = './assets/dark_and_stormy_night_template.txt'
videogame_path = './assets/make_me_a_video_game_template.txt'

def read_template(file_path):

    """
    Read and return the content of a file

    file_path (str): The path to the file.

    returns: The content of the file.
    
    raises: FileNotFoundError: If the file is not found.
    """

    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
          raise FileNotFoundError


def parse_template(template):

    """
    Parse the template and extract parts of speech.

    split_template: The Madlib template.

    tuple: A tuple containing the stripped template and a tuple of parts of speech.
    """

    parts_of_speech = []
    split_template = template.split('{')

    for i in range(1, len(split_template)):
        singular_speech, remaining_char = split_template[i].split('}', 1)
        parts_of_speech.append(singular_speech)
        split_template[i] = remaining_char

    stripped_template = '{}'.join(split_template)

    return stripped_template, tuple(parts_of_speech)


def merge(stripped_template, parts_of_speech):

    """
    Merge the stripped Madlib template with user input.

    stripped_template (str): The stripped Madlib template.
    parts_of_speech (tuple): Tuple containing parts of speech.

    Returns: The final merged Madlib.
    """

    result = stripped_template.format(*parts_of_speech)
    return result




def madlib_generator():

    """
    Generate a Madlib using a template and user input.

    It reads a template from a file, parses it, prompts the user for input,
    and merges the input with the template to create the final Madlib.

    The user can quit the Madlib game by entering "quit" at any time.
    
    """

    template = read_template(videogame_path)
    stripped_template, parts_of_speech = parse_template(template)
    user_input = []
    for word in parts_of_speech:
        word_input = input(f"\nEnter {word} > ")
        if word_input.lower() == "quit":
            print("\nYou've exited out of the Madlib Game.\n")
            return
        user_input.append(word_input)
    final_madlib = merge(stripped_template, user_input)
    print(f"\n\n\nHere is you completed Madlib: \n\n{final_madlib}\n")

    with open ('assets/final_madlib.txt', 'w') as file:
        file.write(final_madlib)

madlib_generator()