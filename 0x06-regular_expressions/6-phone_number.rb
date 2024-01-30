#!/usr/bin/env ruby
# Task 6 : Call me maybe

input = ARGV[0]

matches = input.scan(/^\d{1,10}$/)

puts matches.join
