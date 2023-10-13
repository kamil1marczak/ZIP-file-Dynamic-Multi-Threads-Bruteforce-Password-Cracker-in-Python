import string
import itertools
import sys
from colorama import init, Fore
import argparse
from concurrent.futures import ThreadPoolExecutor
import zipfile

init()

GREEN = Fore.GREEN
RED = Fore.RED
RESET = Fore.RESET

class PasswordGenerator:
    def __init__(self, n, *args):

        self.alphanumeric = []
        self.alphanumeric += string.ascii_uppercase if '-u' in args else []
        self.alphanumeric += string.ascii_lowercase if '-l' in args else []
        self.alphanumeric += string.digits if '-d' in args else []
        self.alphanumeric += string.punctuation if '-p' in args else []

        self.password_list = itertools.product(self.alphanumeric, repeat=n)

    def password_yield(self):
        for password in self.password_list:
            yield "".join(password)

class HackingTool:

    def __init__(self, file, max_len, *args):
        self.file_name = file
        self.max_len = max_len + 1
        self.password = ""
        self.arg_list = args
        self.zip_file = zipfile.ZipFile(self.file_name, 'r')

    def password_cracker(self):
        with ThreadPoolExecutor(max_workers=n_threads) as pool:
            for n in range(1, self.max_len):
                password_generator = PasswordGenerator(n, *self.arg_list).password_yield()
                list(pool.map(self.is_zip_open, password_generator))

    def is_zip_open(self, password):

        password_byte = password.encode()

        try:
            self.zip_file.extractall(pwd=password_byte)
        except:
            if self.password == "":
                print(f"{RED}[!] Wrong password:\n\tFILE: {self.file_name}\n\tPASSWORD: {password}{RESET}\n")

        else:
            self.password = password
            print(f"{GREEN}[+] Found combo:\n\tFILE: {self.file_name}\n\tPASSWORD: {password}{RESET}\n")
            open("password.txt", "w").write(f"file:{self.file_name} password:{self.password}")
            sys.exit(2)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="ZIP File Dynamic Bruteforce Password Cracker in Python")
    parser.add_argument("file", help="name of file to bruteforce.")
    parser.add_argument("--max", type=int, help="Maximal len of password default = 14")
    parser.add_argument("-t", "--threads", type=int, help="Number of threads, default = 1")
    parser.add_argument("-l", "--lowercase", help="Password generator will include lowercase", action="store_true")
    parser.add_argument("-u", "--uppercase", help="Password generator will include uppercase", action="store_true")
    parser.add_argument("-d", "--digits", help="Password generator will include digits", action="store_true")
    parser.add_argument("-p", "--punctuation", help="Password generator will include punctuation", action="store_true")

    args = parser.parse_args()
    file = args.file

    max_len = args.max if args.max else 14
    n_threads = args.threads if args.threads else 1

    argument_list = []
    argument_list += ["-l"] if args.lowercase else []
    argument_list += ["-u"] if args.uppercase else []
    argument_list += ["-d"] if args.digits else []
    argument_list += ["-p"] if args.punctuation else []

    #to get traceback, deactivate line below
    # sys.tracebacklimit = 0

    hack = HackingTool(file, max_len, *argument_list)

    hack.password_cracker()
