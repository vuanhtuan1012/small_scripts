# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2018-10-11 23:06:10
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2018-10-12 10:48:46
# @Reference: https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console

from time import sleep

def print_progress_bar(iteration, total, prefix = 'Progress:', suffix = 'Completed', decimals = 2, length = 50, fill = '█'):
    percent = ("{0:." + str(decimals) + "f}").format(100*iteration/total)
    filled_length = int(length*iteration//total)
    bar = fill*filled_length + '-'*(length-filled_length)
    print('\r%s |%s| %s%% (%d/%d)' % (prefix, bar, percent, iteration, total), end = '\r')
    if iteration == total:
        print('\r%s |%s| %s%% (%d/%d) %s' % (prefix, bar, percent, iteration, total, suffix), end = '\r')
        print()


def main():
    items = list(range(0, 150))
    l = len(items)

    print_progress_bar(0, l) # initialize
    for i, item in enumerate(items):
        sleep(0.1) # do stuff
        print_progress_bar(i + 1, l) # update progress

if __name__ == '__main__':
    main()