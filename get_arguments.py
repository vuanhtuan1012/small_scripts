# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2018-10-12 13:12:58
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2018-10-12 13:24:07


import sys


conf = {
	'help': 'get_arguments.py [start] [end]',
	'start': 0,
	'end': 50
}


def get_arguments(argv):
	try:
		start = int(argv[0]) if len(argv) == 2 else conf['start']
		end = int(argv[1]) if len(argv) == 2 else conf['end']
	except Exception as e:
		print(conf['help'])
		return None, None
	return start, end


def main(argv):
	start, end = get_arguments(argv)

	if start is not None:
		print('start = %d' % start)
		print('end = %d' % end)


if __name__ == '__main__':
	main(sys.argv[1:])