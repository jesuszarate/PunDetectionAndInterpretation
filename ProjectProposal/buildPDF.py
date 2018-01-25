import os
import sys


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
        print('Please provide filename and output directory')
        print('i.e. python toPDF.py HW0.tex')
        exit()
    if len(sys.argv) > 2:
        print('Too many arguments provided')
        exit()
    if not os.path.exists(sys.argv[1]):
        print('Tex file you provided does not exist.')
        exit()

    computeTrueCase(sys.argv[1])
