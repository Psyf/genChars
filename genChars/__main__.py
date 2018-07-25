#!/usr/bin/env python3

import sys
import random
import click

random.seed()

def genRandInt():
    return chr(random.randint(48, 57))

def genRandLowerCase():
    return chr(random.randint(97, 122))

def genRandUpperCase():
    return chr(random.randint(65, 90))

@click.command()
@click.option('--length', '-l', default=12, help='Define length of generated string (default=12)')
def main(length):
    '''
    CLI tool to help you generate a random string. 
    '''
    randString = ""

    func_list = [genRandInt, genRandLowerCase, genRandUpperCase]
    for i in range(length):
        randString += random.choice(func_list)()

    print(randString)


if __name__ == '__main__': 
    main()
