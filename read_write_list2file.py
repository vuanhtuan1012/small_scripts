# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2018-10-15 17:31:55
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2018-10-15 18:18:22


def list_to_file(filename, list):
	with open(filename, 'w', encoding='utf-8') as f:
		for ele in list:
			f.write('%s\n' % str(ele))


def file_to_list(filename):
	with open(filename, 'r', encoding='utf-8') as f:
		list = [line.strip() for line in f]
	return list


def main():
	conf = {
		'list': ['kid', 'many', 'love', 'play'],
		'filename': 'list2file.txt'
	}
	
	print('list to write:')
	print(conf['list'])
	list_to_file(conf['filename'], conf['list'])
	list = file_to_list(conf['filename'])
	print('read list:')
	print(list)


if __name__ == '__main__':
	main()