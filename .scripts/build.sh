#!/bin/bash
gcc -Wall -Werror -Wextra -g $1.c -o $1  && ./$1
