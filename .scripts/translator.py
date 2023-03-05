from googletrans import Translator
from googletrans.models import Translated
import sys
import os
from optparse import OptionParser



LANGS = {'en', 'it', 'ar', 'es', 'fr'}

excluded_args = 0
for i, arg in enumerate(sys.argv):
    if 'translator.py' in arg:
        excluded_args = i
        break
else:
    exit()


usage = f"usage: %prog -i FILE [-l LANG]"
parser = OptionParser(usage=usage)

parser.add_option(
    '-i', '--input',
    dest='inputfile',
    metavar='FILE',
    help='input file',
)
parser.add_option(
    '-l', '--lang',
    dest='lang',
    help=f'language of the input file: {LANGS} [default = %default]',
    default='en',
)

(options, args) = parser.parse_args()

if len(args) != 0:
    parser.error('incorrect number of arguments')
if options.inputfile is None:
    parser.error('file not specified')

input_path = options.inputfile

if options.lang not in LANGS:
    parser.error(f'language not found!\nsupported langs: {LANGS}')

lang = options.lang


# opts, args = getopt.getopt(
#     sys.argv[excluded_args+1:],
#     'i:l:', 
#     ['input', 'lang'])

# lang: str = ""
# input_path: str = ""
# for opt, arg in opts:
#     if opt == '-i' or opt == '-input':
#         if arg == '': exit()
#         input_path = arg
#     elif opt == '-l' or opt == '-lang':
#         if arg not in LANGS:
#             exit()
#         lang = arg

# if lang == "": exit()



t = Translator()

# take as input a xml file
with open(input_path, 'r', encoding='utf-8') as in_file:
    for out_lang in LANGS.difference([lang]):
        (head, tail) = os.path.split(input_path)
        head = '' if head == '' else head+'/'
        with open(f'{head}{out_lang}_{tail}', 'a', encoding='utf-8') as out_file:
            in_file.seek(0)
            for line in in_file.readlines():
                beg_value = line.find('>')
                end_value = line.find('<', beg_value)
                if beg_value == -1 or end_value == -1 or beg_value+1 == end_value:
                    out_file.write(line)
                    continue

                beg_str = line[:beg_value+1]
                end_str = line[end_value:]

                trans = t.translate(line[beg_value+1:end_value], src=lang, dest=out_lang)
                if not isinstance(trans, Translated):
                    out_file.write(line)
                    continue

                new_line = beg_str + trans.text + end_str

                out_file.write(new_line)
