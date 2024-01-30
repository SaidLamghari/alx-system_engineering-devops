#!/usr/bin/env ruby
#Simply matching School

in_put = ARGV[0]

rgx = /School/

mtch = in_put.mtch(rgx)

if mtch
  puts "School$"
else
  puts ""
end
