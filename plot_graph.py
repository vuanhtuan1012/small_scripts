# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2018-10-12 10:52:17
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2018-10-12 11:40:49


import matplotlib.pyplot as plt
import numpy as np

conf = {
	'xticks_distance': 5,
	'xticks_start': 50,
	'xticks_end': 100,
	'marker_size': 5,
	'legend_fontsize': 5, # make legend smaller/bigger
	'legend_numpoints': 1, # number of marker points in legend
	'heigh_width_ratio': 0.5,
	'markers': ['.', 'x', '*', '+', '_'],

	'filename': 'res.png',
}


"""
- plot graph to file
- manually set heigh_width_ratio
- manually set marker_size
- manually set xticks range
- manually set legend size
"""
def plot_graph(filename, scores):
    n = len(list(scores.values())[0])
    i = 0
    for l, s in scores.items():
        plt.plot(range(n), s, conf['markers'][i], markersize=conf['marker_size'], label=l)
        i+=1

    plt.axis([0, n+1, -1, 1]) # xaxis limit [0, n+1], yaxis limit [-1, 1]
    plt.xticks(range(0, n+1, conf['xticks_distance']), range(conf['xticks_start'], conf['xticks_end']+1, conf['xticks_distance'])) # set xaxis ticks

    aspect = conf['heigh_width_ratio']*(conf['xticks_end']-conf['xticks_start']+1)/2
    plt.gca().set_aspect(aspect)

    plt.legend(loc = 0, numpoints = conf['legend_numpoints'], prop = {'size': conf['legend_fontsize']})

    plt.xlabel('comment')
    plt.ylabel('score')
    
    plt.savefig(filename, bbox_inches='tight', dpi=600)


def main():
	low = -1; heigh = 1;
	n = conf['xticks_end'] - conf['xticks_start']
	scores = {
		'google': np.random.uniform(low, heigh, n),
		'vader_blob': np.random.uniform(low, heigh, n),
		'textblob': np.random.uniform(low, heigh, n),
		'text_processing': np.random.uniform(low, heigh, n),
		'vader_translated': np.random.uniform(low, heigh, n),
	}
	plot_graph(conf['filename'], scores)


if __name__ == '__main__':
	main()