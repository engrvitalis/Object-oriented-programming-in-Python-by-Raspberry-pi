from room import Room


kitchen = Room('kitchen')
kitchen.set_description("A dank and dirty room buzzing with flies")

ballroom = Room('ballroom')
ballroom.set_description("A vast room with a shiny wooden floor; huge candlesticks guard the entrance")

dining_hall = Room('dinning hall')
dining_hall.set_description("A large room with ornate golden decorations on each wall")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

dining_hall.get_details()
kitchen.get_details()