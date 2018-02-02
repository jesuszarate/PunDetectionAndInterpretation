import sys
import logging
from pathlib import Path
import xml.etree.ElementTree as ET
from extraction_system import pos_tag


class Text:
    def __init__(self, sent, words, tagged_words):
        self.sent = sent
        self.words = words
        self.tagged_words = tagged_words

def readXMLFile(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    pun_dict = dict()
    for text in root.findall('text'):
        sent = []
        word_dict = {}
        for word in text.findall('word'):
            sent.append(word.text)
            word_dict[word.get('id')] = word.text
        tagged = pos_tag.get_tags(sent)
        pun_dict[(text.attrib.get('id'))] = Text(sent, word_dict, tagged)
    return pun_dict

def is_file(filename):
    return Path(filename).is_file()


def main(argv):
    # io.FILEPATH = ''
    if len(argv) != 1:
        print('python pun_extractor.py <XMLfile>')
        sys.exit(2)

    if not (Path(argv[0]).is_file()):
        print('In argument 1 file does not exist: {0}'.format(argv[0]))
        sys.exit(2)

    logging.basicConfig(level=logging.INFO)
    logging.info('If the text file is big this can take a while.')
    logging.info('Processing text...\n')

    text = readXMLFile(argv[0])

    print('This is the first pun tagged with NER, and POS\n')
    first_story = text['hom_1']

    print(first_story.sent)
    print()
    print(first_story.tagged_words)
    print()
    print(first_story.words)


if __name__ == '__main__':
    main(sys.argv[1:])
