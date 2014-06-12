#!/usr/local/bin/python2.7

# This script is tested on OpenBSD 5.4 i386
# -----------------------------------------
# Simple Command Switch Management
#
# User enters:
#   - <executable> -h           # print: help
#   - <executable> -s <string>  # print: <string>

# Application start
def main():
  import sys
  from Naked.commandline import Command
  c = Command(sys.argv[0], sys.argv[1:])
  if c.option_with_arg('-s'):
    print(c.arg('-s'))
  elif c.option('-h'):
    print('help')

if __name__ == '__main__':
    main()
