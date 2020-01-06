#!/usr/bin/env python3

from pathlib import Path
from pprint import pprint
from glob import glob
from json import load, dump
from shutil import copy
from os import chdir
import random


def read_json(path='names.json'):
    with open(path, 'r') as in_file:
        return load(in_file)

def get_text_files(path=Path.cwd()):
    alias_path = Path.cwd()
    if path != alias_path:
        chdir(path)

    files = [Path(file).resolve() for file in glob('*.txt')]

    if alias_path != path:
        chdir(alias_path)

    return files

def build_dictionary(files):
    dictionary = dict()
    categories = [str(f.name).split('.')[0] for f in files]
    blank_list_per_file = [list() for i in range(len(files))]
    print(blank_list_per_file)
    
    for key, blank in zip(categories, blank_list_per_file):
        dictionary[key] = blank
    print(dictionary)
    
    for path, category in zip(files, categories):
        with open(path) as in_file:
            listed = in_file.readlines()
            listed = [name.capitalize()[:-1] for name in listed if not name == '']
            dictionary[category].extend(listed)
    return dictionary

def dump_json(dictionary, dump_path='names.json'):
    if Path(dump_path).resolve().exists():
        print(f"Truncating {dump_path}")
    with open(dump_path, 'w', encoding='utf-8') as out_file:
        dump(dictionary, out_file, indent=4)
        print("JSON written from Dictionary")

def move_txt_files(files, directory="out_of_the_way"):
    directory = Path(directory).resolve()
    if not directory.is_dir():
        directory.mkdir()
    for file in files:
        src = file.resolve()
        dest = file.joinpath(directory, file.name).resolve()
        if src.exists() and not dest.exists():
            copy(src, dest)
            print(f"{file} moved to {directory} directory...")
        else:
            print(f"{file} remains unmoved...")

def get_random(times=1,
               names=read_json(),
               first=True,                    # False for only Family
               last=True,                     # False for only First
               typical=random.randint(0, 1),  # 0 True, 1 False
               sex=random.randint(0, 1)):     # 0 Male, 1 Female
    for i in range(times):
        if first:
            if sex == 0:
                choices = list(names['male'])
            elif sex == 1:
                choices = list(names['female'])
            else:
                choices = random.randint(0, 1) # wtf
                
            #fix later
            #elif sex == 2:
                #choices = random.shuffle(names['male'] + names['female'])

            if typical == 1:
                choices = list(names['atypical'])

            random.shuffle(choices)
            first_name = random.choice(choices)

        if last:
            choices = list(names['family'])
            random.shuffle(choices)
            
            last_name = random.choice(choices)

        if not first_name:
            first_name = ""
        if not last_name:
            last_name = ""

        print(f"{first_name} {last_name}".title().strip())


# MAIN
if __name__ == '__main__':
    all_names = build_dictionary(get_text_files())
    dump_json(all_names)
    move_txt_files(get_text_files())
    json_names = read_json()
    get_random(20, json_names)
