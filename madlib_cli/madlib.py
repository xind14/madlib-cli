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








# def test_merge():


# Create and test a merge function that takes in a “bare” template and a list of user entered language parts, and returns a string with the language parts inserted into the template.
