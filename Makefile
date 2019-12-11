# This Makefile provides some convenience recipes that mitgate the need to change directories
# or track which helper scripts do what.

default:
	$(MAKE) -C sphinx clean
	$(MAKE) -C sphinx html

run_site:
	/usr/bin/env python3 qls.py