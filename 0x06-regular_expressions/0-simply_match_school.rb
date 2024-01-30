#!/usr/bin/env ruby
# Task 0: Simply matching School

in_put = ARGV[0]

rgx = /School/

match = in_put.match(rgx)

if match
  puts "School$"
else
  puts ""
end
