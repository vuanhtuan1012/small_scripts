# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2018-10-12 13:37:25
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2018-10-12 13:51:55

import sys, getopt

conf = {
    'help': 'get_options.py -r url'
}

def get_options(argv):
    url = None

    try:
        opts, args = getopt.getopt(argv,"hr:", ["url="])
    except getopt.GetoptError:
        print(conf['help'])
        sys.exit(2)

    if not opts:
        print(conf['help'])
        sys.exit()

    for opt, arg in opts:
        if opt == '-h':
            print(conf['help'])
            sys.exit()
        elif opt in ("-r", "--url"):
            url = arg

    return url


def main(argv):
    url = get_options(argv)
    print('url = %s' % url)

if __name__ == '__main__':
    main(sys.argv[1:])