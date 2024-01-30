#!/usr/bin/env ruby
# Task 5 : Not quite HBTN yet

input = ARGV[0]

matches = input.scan(/h.n/)

puts matches.join
