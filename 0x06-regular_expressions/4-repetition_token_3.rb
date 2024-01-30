#!/usr/bin/env ruby
# Task 4 : Repetition Token #3

input = ARGV[0]

matches = input.scan(/hbt*n/)

puts matches.join
