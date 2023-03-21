require_relative 'greeter'

puts "What's your name"
my_name = gets.strip

greeter = Greeter.new(name)
puts greeter.greet
