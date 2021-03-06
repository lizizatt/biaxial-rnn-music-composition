import pickle
import gzip
import numpy
from midi_to_statematrix import *

import multi_training
import model

def gen_adaptive(m,pcs,times,keep_thoughts=False,name="final"):
	xIpt, xOpt = map(lambda x: numpy.array(x, dtype='int8'), multi_training.getPieceSegment(pcs))
	all_outputs = [xOpt[0]]
	if keep_thoughts:
		all_thoughts = []
	m.start_slow_walk(xIpt[0])
	cons = 1
	for time in range(multi_training.batch_len*times):
		resdata = m.slow_walk_fun( cons )
		nnotes = numpy.sum(resdata[-1][:,0])
		if nnotes < 2:
			if cons > 1:
				cons = 1
			cons -= 0.02
		else:
			cons += (1 - cons)*0.3
		all_outputs.append(resdata[-1])
		if keep_thoughts:
			all_thoughts.append(resdata)
	noteStateMatrixToMidi(numpy.array(all_outputs),'output/'+name)
	if keep_thoughts:
		pickle.dump(all_thoughts, open('output/'+name+'.p','wb'))

if __name__ == '__main__':

	m = model.Model([300,300],[100,50], dropout=0.5)
	m.learned_config = pickle.load(open("output/final_learned_config.p", 'rb'))
	pcs = multi_training.loadPieces("music")
	gen_adaptive(m, pcs, 10, name="composition")

	quit()
