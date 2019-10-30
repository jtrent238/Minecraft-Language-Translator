import sys
import os

def main():
    filepath = sys.argv[1]
    langcode = sys.argv[1]
    
    if not os.path.isfile(filepath):
        print('File path {} does not exist. Exiting...'.format(filepath))
        sys.exit()
    
    language_file = {}
    with open(filepath) as fp:
        linecount = 0
        for line in fp:
            #print('line {} contents {}'.format(linecount, line))
            strip_local(line)
            linecount += 1

def translate(line):
    

if __name__ == '__main__':
    main()