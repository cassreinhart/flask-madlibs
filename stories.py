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

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text
    
    def getStory(self, storyList):
        storiez = []
        for story in storyList:
            storiez.append(story.text)
        return storiez


# Here's a story to get you started
story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a far-away {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
    )

# fantasy = Story(
#     ["place", "noun", "verb", "adjective", "plural_noun"],
#     """Once upon a time in a far-away {place}, there lived a
#        large {adjective} {noun}. It loved to {verb} {plural_noun}."""
#     ),
# camp = Story(
#     ["name_of_camp", "family_member", "activity", "adjective", "plural_noun"],
#     """Dear {family_member}, I am at {name_of_camp}, and I am having a {adjective} time. 
#     So far, I have {activity}. My favorite thing about camp is {plural_noun}."""
#     ),
# weird_news = Story(
#     ["noun", 'wacky_state', "verb", "noun", "verb", "noun", 'verb', 'noun', 'body_part'],
#     """A {noun} in {wacky_state} was arrested this morning after he {verb} in front of {noun}.
#     He had a history of {verb}, but no one - not even his {noun} - ever imagined he'd {verb} 
#     with a {noun} stuck in his {body_part}."""
#     )
# storyList = [fantasy, camp, weird_news]
