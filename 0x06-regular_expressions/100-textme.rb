#!/usr/bin/env ruby
# Task 8 : Textme

log_line = ARGV[0]

sender = log_line.scan(/\[from:([^]]*)\]/).flatten.first
receiver = log_line.scan(/\[to:([^]]*)\]/).flatten.first
flags = log_line.scan(/\[flags:([^]]*)\]/).flatten.first

puts "#{sender},#{receiver},#{flags}"
