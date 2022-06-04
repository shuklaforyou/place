import argparse
parser = argparse.ArgumentParser ( ) 
parser.add_argument('--words' , '-w' , action = 'store_true') 
parser.add_argument('--lines' , '-l' , action = 'store_true' ) 
parser.add_argument('filename' ) 
args = parser.parse_args( ) 
if args.words :
	print(" words{ }".format(print_words( args.filename )))
elif args.lines :
	print("lines{ }".format(print_lines( args.filename)))
else : 
	print("words{ }".format(print_words( args.filename )))
	print( "lines{ }".format(print_lines( args.filename )))