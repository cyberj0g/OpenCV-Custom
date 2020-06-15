import os
import argparse
import hashlib
import base64
import pathlib


def main(args):
	for f in pathlib.Path(args.i).glob('**/*'):
		f = str(f)
		if os.path.isdir(f):
			continue
		filename = f.replace(args.i, '')
		with open(f, 'rb') as df:
			data = df.read()
			hash = base64.urlsafe_b64encode(hashlib.sha256(data).digest()).decode('latin1').rstrip('=')
			size = os.path.getsize(f)
		if not f.endswith('RECORD'):
			print(f'{filename},sha256={hash},{size}')
		else:
			print(f'{filename},,')


if __name__ == '__main__':
	ap = argparse.ArgumentParser()
	ap.add_argument('-i', help='Input directory', required=True)
	args = ap.parse_args()
	main(args)
