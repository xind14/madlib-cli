









- Print a welcome message to the user, explaining the Madlib process and command line interactions
- Read a template Madlib file (Example), and parse that file into usable parts.
- Prompt the user to submit a series of words to fit each of the required components of the Madlib template.
- With the collected user inputs, populate the template such that each provided input is placed into the correct position within the template.
- After the resulting Madlib has been completed, provide the completed response back to the user in the command line.
- Write the completed text (Example)to a new file on your file system (in the repo).
Note: A smaller example file is included as well which can be handy when developing/testing.
















def read_template():

Create and test a read_template function that takes in a path to text file and returns a stripped string of the file’s contents.
read_template should raise a FileNotFoundError if path is invalid.


@pytest.mark.skip("pending")
def test_read_template_raises_exception_with_bad_path():

    with pytest.raises(FileNotFoundError):
        path = "missing.txt"
        read_template(path)

def test_parse_template():
    actual_stripped, actual_parts = parse_template(
        "It was a {Adjective} and {Adjective} {Noun}."
    )
    expected_stripped = "It was a {} and {} {}."
    expected_parts = ("Adjective", "Adjective", "Noun")

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts

    Create and test a parse_template function that takes in a template string and returns a string with language parts removed and a separate tuple of those language parts.



@pytest.mark.skip("pending")
def test_merge():
    actual = merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
    expected = "It was a dark and stormy night."
    assert actual == expected

Create and test a merge function that takes in a “bare” template and a list of user entered language parts, and returns a string with the language parts inserted into the template.
