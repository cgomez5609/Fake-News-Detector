import spacy
from multiprocessing import Pool
from spacy.lang.en.stop_words import STOP_WORDS
import string
import re

nlp = spacy.load("en_core_web_sm")

def is_empty_string(post: str):
    """
    

    Parameters
    ----------
    post : str
        Any string.

    Returns
    -------
    bool
        Returns true is string is made up of empty white spaces or ("").

    """
    if post.isspace() or post == "":
        return True
    else:
        return False
    
def make_lower_case(post: str) -> str:
    """
    

    Parameters
    ----------
    post : str
        Any non-empty string.

    Returns
    -------
    str
        return a string in lower case format.

    """
    return post.lower()

def remove_stopwords(post: str) -> str:
    """
    Best if used right after make_lowercase()

    Parameters
    ----------
    post : str
        Any non-empty string.

    Returns
    -------
    str
        Removes all stop words found in text.

    """
    if is_empty_string(post):
        return ""
    
    doc = nlp(post)
    new_string = list()

    for word in doc:
        if word.text in STOP_WORDS:
            pass
        else:
            new_string.append(word.text)
    
    return " ".join(new_string)

def remove_missed_punctuation(post: str) -> str:
    """
    Some punctuation isn't caugh't by the other function named remove_punctuation
    so this takes of anything that may remain.

    Parameters
    ----------
    post : str
        Any post.

    Returns
    -------
    str
        Returns the same post, but without punctuation.

    """
    if is_empty_string(post):
        return ""
    
    temp_string:str = re.sub(r"[^A-Za-z ]", "", post)
    return " ".join(temp_string.split())
    
def remove_punctuation(post: str) -> str:
    """
    

    Parameters
    ----------
    post : str
        Any post.

    Returns
    -------
    str
        Returns the post without punctuation. Some punctuation may be missed thus 
        this function is followed by another function that is similar.

    """
    if is_empty_string(post):
        return ""
    
    temp_string: str = "".join([element for element in post if element not in string.punctuation])
    
    return " ".join(temp_string.split())

def lemmatization(post: str) -> str:
    """
    Lemmatization is get the root form of the word. 
    Example: 
        working -> work
        loving -> love

    Parameters
    ----------
    post : str
        Any post.

    Returns
    -------
    str
        Returns a string that has its words lemmatized.

    """
    if is_empty_string(post):
        return ""
    
    new_string = list()
    for token in nlp(post):
        new_string.append(token.lemma_)
    return " ".join(new_string)

def tokenize(post: str):
    tokens = list()
    for token in nlp(post):
        tokens.append(token.text)
    return tokens