#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Constants(object):
	"""A class defining a fixed numer for some classes.
	"""
	EXIT_SUCCESS = 0
	EXIT_FAILURE = 1
	pass

	
def main():
	"""Run an example for a Constants class."""
	print Constants.EXIT_SUCCESS
	print Constants.EXIT_FAILURE

	return 0

if __name__ == '__main__':
	sys.exit(main())
