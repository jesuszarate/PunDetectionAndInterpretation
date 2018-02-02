import nltk
from nltk.chunk import conlltags2tree, tree2conlltags


def get_tags(tokens):
    # tokenized = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(tokens)

    namedEnt = nltk.ne_chunk(tagged)
    iob_tagged = tree2conlltags(namedEnt)

    ne_tree = conlltags2tree(iob_tagged)

    return ne_tree


# hetero_pun = 'Dentists dont like a hard day at the orifice.'
# homog_pun = 'Can honeybee abuse lead to a sting operation ?'
# 
# print(get_tags(homog_pun))
