#!/usr/local/bin/python2.7

# This script is tested on OpenBSD 5.4 i386
# -----------------------------------------
# Simple Command Argument Management
#
# User enters: <executable> -l Python --framework Naked

# Application start
def main():
  import sys
  from Naked.commandline import Command
  c = Command(sys.argv[0], sys.argv[1:])
  if c.option_with_arg('-l') and c.option_with_arg('--framework'):
    language = c.arg('-l')
    framework = c.arg('--framework')
    print(framework+' - '+language)
    # Output: Naked - Python

if __name__ == '__main__':
    main()
