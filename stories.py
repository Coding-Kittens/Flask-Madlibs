"""Madlibs Stories."""

class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self,id, words, text):
        """Create story with words and template text."""
        self.id =id
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started

stories = [Story(
    "1",["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a far-off {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
),Story(
    "2",["a_place", "thing", "name"],
    """There once was a {thing},that went to {a_place}. The name of the{thing} was{name}. """
),Story(
    "3",["name", "noun", "word_for_story", "adjective", "two_adjectives"],
    """Way back in days of old there was a {word_for_story} told, about a {noun} known as {name}! {quality} and {quality2} there was no {noun} quite like{name}!"""
),Story(
    "4",[ "noun", "verb", "adjective", "plural_noun"],
    """The {adjective} {plural_noun} liked to {verb} with the {noun}.The {plural_noun} and the {noun} would {verb} all day"""
),Story(
    "5",["place","past_tense_verb", "noun", "thing", "adjective", "plants","action"],
    """ While {past_tense_verb} in the {place} today {noun} was {adjective} enough to come across a {thing} amonst the thicket of {plants}. {noun} watched the {thing} for a while then decided to {action}"""
)]


story_dict = {story.id: story for story in stories}
