import os
import sys
from termcolor import colored


def computeTrueCase(filename, output_file='output_files'):
    log = ''
    try:
        print ('Converting to PDF...')

        if not os.path.exists(output_file):
            os.makedirs(output_file)

        log = os.popen('pdflatex --output-directory={0} {1}'.format(output_file, filename)).read()

        # Uncomment to open pdf after build completes
        # os.popen('open {0}'.format('{0}/{1}pdf'.format(output_file, filename[:-3]))).read()

        print(log)
        print ('Done!')
    except:
        print(log)
        print('Ooops! Something went wrong. Does the folder name you provided exist?')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print colored('Please provide filename and output directory', 'red')
        print colored('i.e. python toPDF.py HW0.tex', 'red')
        exit()
    if len(sys.argv) > 2:
        print colored('Too many arguments provided', 'red')
        exit()
    if not os.path.exists(sys.argv[1]):
        print colored('Tex file you provided does not exist.', 'red')
        exit()

    computeTrueCase(sys.argv[1])
