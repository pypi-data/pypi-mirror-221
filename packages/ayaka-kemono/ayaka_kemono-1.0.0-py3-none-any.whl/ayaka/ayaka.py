#!/usr/bin/env python

# Command
# python main.py sauce=[SAUCE] --path=[FILE_PATH]

import argparse
from ayaka.lib import download_from_artist

def main():
    parser = argparse.ArgumentParser(description='Ayaka - pixiv fanbox downloader')
    parser.add_argument('--artist', type=str, help='artist id', required=True)
    parser.add_argument('-p', '--path', type=str, help='file path')

    args = parser.parse_args()
    config = vars(args)
    
    if not config['path']:
        config['path'] = ''

    download_from_artist(artist_id=config['artist'], path=config['path'])
    
if __name__ == '__main__':
    main()