import random


class WordFinder:
    """Word Finder: finds random words from a dictionary.
    
    >>> wf = WordFinder("words_mini.txt")
    3 words read

    >>> wf
    <WordFinder words=3>

    >>> print(len(wf.random()) > 0)
    True

    >>> print(len(wf.random()) > 0)
    True

    >>> print(len(wf.random()) > 0)
    True

    >>> print(len(wf.random()) > 0)
    True

    >>> wf_empty_lines = WordFinder("words_empty_lines.txt")
    4 words read

    >>> wf_empty_lines
    <WordFinder words=4>

    >>> print(len(wf_empty_lines.random()) > 0)
    False

    >>> print(len(wf_empty_lines.random()) == 0)
    True

    >>> wf_comments = WordFinder("words_comments.txt")
    4 words read

    >>> wf_comments
    <WordFinder words=4>

    >>> print(len(wf_comments.random()) > 0)
    True

    >>> print(len(wf_comments.random()) == 0)
    False

    """
    def __init__(self, path_to_file):
        """Initialize a random word finder from the path of a file supplied"""
        self.path_to_file = path_to_file
        self.words = []
        self.parse_file()

    def parse_file(self):
        """Reads words and strips new line endings into a list"""
        with open(self.path_to_file, 'r') as file:
            self.words = [line.rstrip('\n') for line in file.readlines()]
        print(("No" if len(self.words) == 0 else str(len(self.words))) + " words read")

    def random(self):
        """Grabs a random word from the words list, if populated"""
        if len(self.words) == 0:
            return ""
        return random.choice(self.words)
    
    def __repr__(self):
        """Shows the amount of words in the current word list as read from file that was initialized"""
        return f"<WordFinder words={len(self.words)}>"
    

class SpecialWordFinder(WordFinder):
    """Updated changes to process blank and commented out lines in read files and add to omitted list

    >>> wf = SpecialWordFinder("words_mini.txt")
    3 words read
    
    >>> wf
    <SpecialWordFinder words=3 omitted=0>

    >>> print(len(wf.random()) > 0)
    True

    >>> print(len(wf.random()) > 0)
    True

    >>> print(len(wf.random()) > 0)
    True

    >>> print(len(wf.random()) > 0)
    True

    >>> wf_empty_lines = SpecialWordFinder("words_empty_lines.txt")
    4 words read

    >>> wf_empty_lines
    <SpecialWordFinder words=0 omitted=4>

    >>> len(wf_empty_lines.words) == 0
    True

    >>> print(len(wf_empty_lines.random()) > 0)
    False

    >>> print(len(wf_empty_lines.random()) == 0)
    True

    >>> wf_comments = SpecialWordFinder("words_comments.txt")
    4 words read

    >>> wf_comments
    <SpecialWordFinder words=0 omitted=4>

    >>> print(len(wf_comments.random()) > 0)
    False

    >>> print(len(wf_comments.random()) == 0)
    True

    """
    def __init__(self, path):
        """Calls WordFinder class and processes list to refine for list behavior changes"""
        super().__init__(path)
        self.omitted = []
        self.process_list()

    def process_list(self):
        if len(self.words) == 0:
            return
        self.omitted = [line for line in self.words if len(line.rstrip('\n')) == 0 or line[0] == '#']
        self.words = [line.rstrip('\n') for line in self.words if len(line.rstrip('\n')) > 0 and line[0] != '#']

    def __repr__(self):
        """Shows the amount of words in the current word list as read from file that was initialized"""
        return f"<SpecialWordFinder words={len(self.words)} omitted={len(self.omitted)}>"
