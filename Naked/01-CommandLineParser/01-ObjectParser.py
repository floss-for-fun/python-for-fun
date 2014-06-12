#!/usr/local/bin/python2.7

# This script is tested on OpenBSD 5.4 i386
# -----------------------------------------
# Simple Command to Python Object Parser
#
# User enters: <executable> hello world --print

# Application start
def main():
  import sys
  from Naked.commandline import Command
  c = Command(sys.argv[0], sys.argv[1:])
  if c.cmd == 'hello' and c.cmd2 == "world":
    if c.option('--print'):
      print('Hello World!')

if __name__ == '__main__':
    main()
