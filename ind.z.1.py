#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Написать программу, которая считывает текст из файла и определяет, сколько в нем слов,
# состоящих из не менее чем семи букв.

if __name__ == '__main__':
    with open('text.txt', 'r') as f:
        text = f.read()
    a = []
    for i in text.split('\n'):
        for f in i:
            if len(f) >= 7:
                a += i.split()
    print(len(set(a)))
