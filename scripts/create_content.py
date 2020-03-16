#!/usr/bin/env python
"""This script compiles the content of the course."""
import subprocess as sp
import argparse
import os

ROOT = os.environ['COURSE_ROOT']


def compile_latex_document(dirname=None):
    cwd = os.getcwd()
    if dirname:
        os.chdir(dirname)

    for type_ in ['pdflatex', 'bibtex', 'pdflatex', 'pdflatex']:
        os.system(type_ + ' main')

    os.chdir(cwd)


if __name__ == '__main__':

    parser = argparse.ArgumentParser('Create content')

    parser.add_argument('-s', '--syllabus', action='store_true', help='compile syllabus')

    parser.add_argument('-a', '--all', action='store_true', help='compile all')

    args = parser.parse_args()

    if args.syllabus or args.all:
        compile_latex_document(ROOT + '/syllabus')
