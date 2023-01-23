#world replacement program

def replace_world():

    str = "Hello, this is a world replacement program"
    world_to_replace = input("Enter the world to replace: ")
    world_replacement = input("Enter the world replacement: ")
    print (str.replace(world_to_replace, world_replacement))

replace_world()
