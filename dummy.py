import string

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename", type=str,
                    help="finename")
parser.add_argument("-c", "--connector", type=str,
                    help="connector")
parser.add_argument("-s", "--string", type=str,
                    help="string to tokenize")

args = parser.parse_args()

connector = args.connector
filename = args.filename
s = args.string

tokens = s.split()

with open(filename, "a+") as f:
	f.write(connector.join(tokens)+"\n")

