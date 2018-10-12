# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2018-10-12 13:57:31
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2018-10-12 14:01:13


import re

def verify_url(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE
    )

    return False if re.match(regex, url) is None else True


def main():
    url = 'https://www.telecom-paristech.fr/'
    print('%s : %s' % (url, str(verify_url(url))))

    url = 'htt://www.telecom-paristech.fr/'
    print('%s : %s' % (url, str(verify_url(url))))


if __name__ == '__main__':
    main()