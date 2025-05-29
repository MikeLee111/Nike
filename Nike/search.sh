#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <filename> <search_string>"
    exit 1
fi

filename="$1"
search_str="$2"
output_file="search_result.txt"

if [ ! -f "$filename" ]; then
    echo "File '$filename' does not exist."
    exit 2
fi

grep -n "$search_str" "$filename" | tee "$output_file"