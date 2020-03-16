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

    args = parser.parse_args()

    if args.syllabus:
        compile_latex_document(ROOT + '/syllabus')
