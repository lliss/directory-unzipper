'''
Unzip all files within a directory. Optionally deleting the original zips.
'''

import os
import glob
import zipfile
import re
import argparse


def main():
    '''
    Main program.
    '''
    parser = argparse.ArgumentParser(description='Unzip all the zip files in a directory.')
    parser.add_argument('directory', nargs='?', default=os.getcwd(),
                        help='The directory of zip files to work within.')
    parser.add_argument('-r', '--remove', action='store_true',
                        help='Remove zip files after unzipping.')

    args = parser.parse_args()

    for the_file in glob.glob(args.directory + '/' + '*.zip'):
        if os.path.isfile(the_file):
            unzip_dir = re.sub('[^0-9a-zA-Z]+', '', os.path.basename(the_file))
            try:
                zip_ref = zipfile.ZipFile(the_file, 'r')
                zip_ref.extractall(os.path.join(args.directory, unzip_dir))
                zip_ref.close()
                print('Unzipped:', os.path.basename(the_file))
                if args.remove:
                    print('Removing:', os.path.basename(the_file))
                    os.remove(the_file)
            except zipfile.BadZipfile as ex:
                print('ERROR -- INVALID ZIP FILE: ', ex, '--', os.path.basename(the_file))


if __name__ == '__main__':
    main()
