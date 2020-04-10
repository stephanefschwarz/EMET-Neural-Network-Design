import sys
sys.path.append('../')
from pycore.tikzeng import *

arch = [
	to_head('..'),
	to_cor(),
	to_begin(),

	to_ConvConvRelu( name='ccr_b1', s_filer=512, n_filer=(5,5,5,5,5), offset="(0,0,0)", to="(0,0,0)", width=(2,2,2,2,2), height=30, depth=30),

	# to_Conv('tweet_conv_1', 510, 5, offset='(0, 0, 0)',
	# 	    to='(0, 0, 0)'),

	to_end()

]

def main():

	file_name = str(sys.argv[0]).split('.')[0]
	to_generate(arch, file_name + '.tex')

if __name__ == '__main__':
	main()