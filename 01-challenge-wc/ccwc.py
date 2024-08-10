#!/usr/bin/env python3

import sys
import os
import argparse
import locale

def count_number_of_bytes(content):
    """Count the number of bytes in the content"""
    return len(content.encode('utf-8'))

def count_number_of_lines(content):
    """Count the number of lines in the content"""
    lines = content.splitlines()
    return len(lines)

def count_number_of_words(content):
    """Count the number of words in the content"""
    words = content.split()
    return len(words)

def count_number_of_chars(content):
    """Count the number of chars in the content"""
    return len(content)

def main():
    parser = argparse.ArgumentParser(description="ccws tools for txt files")
    parser.add_argument("-c", type=str, nargs='?', const=sys.stdin, help="Count the number of bytes in a file")
    parser.add_argument("-l", type=str, nargs='?', const=sys.stdin, help="Count the number of lines in a file")
    parser.add_argument("-w", type=str, nargs='?', const=sys.stdin, help="Count the number of words in a file")
    parser.add_argument("-m", type=str, nargs='?', const=sys.stdin, help="Count the number of characters in a file")
    parser.add_argument("filename", nargs='?', help="The text file to count lines, words, and characters.")
    args = parser.parse_args()

    def read_content(source):
        if source == sys.stdin:
            return sys.stdin.read()
        else:
            with open(source, "r", encoding="utf-8", errors='ignore') as file:
                return file.read()

    if args.c is not None:
        content = read_content(args.c)
        print(count_number_of_bytes(content))

    elif args.l is not None:
        content = read_content(args.l)
        print(count_number_of_lines(content))

    elif args.w is not None:
        content = read_content(args.w)
        print(count_number_of_words(content))

    elif args.m is not None:
        content = read_content(args.m)
        current_locale = locale.getpreferredencoding()
        if current_locale.lower() in ["utf-8", "utf8"]:
            print(count_number_of_chars(content))
        else:
            print("Warning: Current locale does not support multibyte characters. Counting bytes instead.")
            print(count_number_of_bytes(content))

    elif args.filename:
        content = read_content(args.filename)
        print(f"{count_number_of_lines(content)} {count_number_of_words(content)} {count_number_of_bytes(content)} {args.filename}")
    
    else:
        if not sys.stdin.isatty():
            content = sys.stdin.read()
            print(f"{count_number_of_lines(content)} {count_number_of_words(content)} {count_number_of_bytes(content)}")
        else:
            parser.print_help()

if __name__ == "__main__":
    main()
