#!/usr/bin/env ruby
# Task 3 : Repetition Token #2


input = ARGV[0]

matches = input.scan(/hbt+n/)

puts matches.join
