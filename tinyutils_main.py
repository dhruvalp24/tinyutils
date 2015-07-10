import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", help="Network Info.", action="store_true")
parser.add_argument("-m", help="Memory Info.", action="store_true")
parser.add_argument("-c", help="CPU Info.", action="store_true")
parser.add_argument("-s", help="Storage Info.", action="store_true")
parser.add_argument("-a", help="All Info.", action="store_true")
args = parser.parse_args()
# if the input key is n then network info will be displayed
if args.n is True:
    output, err = \
        subprocess.Popen(
            ['python3', 'networkutils.py'], stdout=subprocess.PIPE).communicate()

# if the input key is m then memory info will be displayed
if args.m is True:
    output, err = \
        subprocess.Popen(
            ['python3', 'memoryutils.py'], stdout=subprocess.PIPE).communicate()

# if the input key is c then CPU info will be displayed
if args.c is True:
    output, err = \
        subprocess.Popen(
            ['python3', 'cpuutils.py'], stdout=subprocess.PIPE).communicate()

# if the input key is s then storage info will be displayed
if args.s is True:
    output, err = \
        subprocess.Popen(
            ['python3', 'storageutils.py'], stdout=subprocess.PIPE).communicate()

# if the input key is a then information about all is displayed
if args.a is True:
    output, err = \
        subprocess.Popen(['python3', 'networkutils.py', 'memoryutils.py',
                          'cpuutils.py', 'storageutils.py'], stdout=subprocess.PIPE).communicate()


def main():
    # Calls all available modules
    # network()
    # cpu()
    print("Network Info")

    if __name__ == "__main__":
    # Do not forget this! Otherwise, nothing will seem to be working. :)

        main()
