#importing randomly
import random
#defining main function of the program
def main():
#these comments are inactivating the string on line 8 and 9 such that the programme is nit tiresome by asking inputs,this would mean that the user enters 
# all the cases of the 6 cases of tense ,from line 10 to line 20,strings have been made to store the parameters as already entered such that the program can
# the values and execute the program automatically.but inputs for line 5
   #quantity=int(input("please enter the number of the noun:"))
   #tense=input("please enter the tense as on of the following:past,present,future.")
   sentence=make_sentence(1,"past")
   print(f"{sentence}")
   sentence=make_sentence(1,"present")
   print(f"{sentence}")
   sentence=make_sentence(1,"future")
   print(f"{sentence}")
   sentence=make_sentence(2,"past")
   print(f"{sentence}")
   sentence=make_sentence(2,"present")
   print(f"{sentence}")
   sentence=make_sentence(2,"future")
   print(f"{sentence}")

def get_determiner(quantity):
    """return a randomly chosen determiner.A determiner is a word like"the","a","one","some","many".
    if quantity is 1,this function will return either "a" or"one"or "the".Otherwise this function will return
    either "some","many",or"the".
    parameter
        quantity:an integer.
            if quantity is 1,this function will return a
            determiner for a single noun .otherwise this  function will return a determiner for plural noun.
            Return:a randomly chosen determiner.
            """
    if quantity ==1:
        words=["a","one","the"]
    else:
        words=["some","many","the"]
    word=random.choice(words)
    return word
def get_noun(quantity):
    """Return a randomly chosen noun.
    if quantity is 1, this function return one of theses ten single nouns:"bird","boy","cat","car","child","dog","girl","man","rabbit","woman".
    Otherwise, this function will return one of these ten plural noun:
    "birds","boys","cars","cats","children","dogs","girls","men","rabbits","women".
    parameter
        quantity: an integer that determines if the returned noun is single  or plural.
        Return: a randomly chosen noun.
        """
    if quantity==1:
        words=["bird","boy","cat","car","child","dog","girl","man","rabbit","woman"]
    else:
        words=["birds","boys","cars","cats","children","dogs","girls","men","rabbits","women"]
    word=random.choice(words)
    return word

def get_verb(quantity,tense):
    """Return a randomly chosen verb.If tense is "past",this function will return one of these ten verbs:
    "drank","ate","grew","laughed","thought","ran","slept","talked","walked","wrote".
    If tense is "present" and quantity is 1,this function will return one of these ten verbs:"drinks","eats","grows",
    "laughs","thinks","runs","sleeps","talks","walks","writes"
    if tense is "present and quantity is not 1, this function will return one of these ten verbs:"drink","eat","grow","laugh",
    "think","run","sleep","talk","walk","write"
    if tense is"future",this function will return one of these ten verbs:"will drink","will eat","will grow",will laugh",
    "will think","will run","will sleep","will sleep",
    "will talk","will walk","will write"
    parameter
        quantity:an integer that determines if the returned verb is singular or plural
        tense:the word that determines if the returned verb is in past,present,or future tense.
    return:a randomly chosen verb.
        """
    if tense=="past":
        words=["drank","ate","grew","laughed","thought","ran","slept","talked","walked","wrote"]
    elif tense=="present" and quantity==1:
        words=["drinks","eats","grows","laughs","thinks","runs","sleeps","talks","walks","writes"]
    elif tense=="present" and quantity>1:
        words=["drink","eat","grow","laugh","think","run","sleep","talk","walk","write"]
    elif tense=="future":
        words=["will drink","will eat","will grow","will laugh","will think","will run","will sleep","will talk","will walk","will write"]
    word=random.choice(words)
    return word

def get_preposition():
    """Return a randomly chosen preposition fro this list of prepositions:
        "about","above","across","along","around","at","before","behind","below","beyond","by","despite","after","before","behind","except","for",
        "from","in","into","near","of","off","on","onto","out","over","past","to","under","with","without"
        return : a randomly chosen preposition.
        """
    words=["about","above","across","along","around","at","before","behind","below","beyond","by","despite","after",
                   "before","behind","except","for",
        "from","in","into","near","of","off","on","onto","out","over","past","to","under","with","without"]
    word=random.choice(words)
    return word

def get_prepositional_phrase(quantity):
    """"Build and return a prepositional phrase composed of three words:a preposition,a  determiner,and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.
    parameter
        quantity:an integer that determines if the determiner and noun in the prepositional phrase returned from this
        function should be single or plural.
        preposition(str)= a preposition word
         determiner(str)= a determiner word
         noun(str)      =a noun word
            returns:
            str=a prepositional phrase with a determiner,preposition,a noun
            """
    preposition=get_preposition()
    determiner=get_determiner(quantity)
    noun=get_noun(quantity)
    prepositional_phrase=f"{preposition} {determiner} {noun}"
    return prepositional_phrase

def make_sentence(quantity,tense,):
    """Build and return a sentence with three words:
    a determiner,a noun,and a verb.
    the grammatical quantity of the determiner and noun will match the
    number in the quantity parameter.
    The grammatical quantity and tense of the the verb will match the number
    and tense in the quantity and tense parameters
        parameter
            quantity(int): an integer that determines that the noun is singular or plural
            tense(str): the state of the verb being present,past,or future.
            determiner(str): a determiner word.
            noun(str): a noun word
            verb(str): a verb word
            Returns:
            str:A sentence with a determiner,noun,and verb
            """
    determiner=get_determiner(quantity)
    noun=get_noun(quantity)
    verb=get_verb(quantity,tense)
    prepositional_phase=get_prepositional_phrase(quantity)
    sentence=f"{determiner} {noun} {verb}"
    return sentence
#calling main function to start running the program
main()
