#!/usr/bin/env ruby
# Task 7 : OMG WHY ARE YOU SHOUTING?

input = ARGV[0]

matches = input.scan(/[A-Z]*/)

puts matches.join
