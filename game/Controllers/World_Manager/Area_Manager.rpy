init -10 python:
    class Area():

        def __init__(self,name):
            self.rooms = {}
            self.current_room = False
            self.name = name
            self.random_areas = {}
            self.random_monsters = []
            #self.random_scenes = ['papyrus_random','sans_random','toriel_random','flowey_random']
        
        def add_room(self,room):
            self.rooms[room.name] = room

        def move_to_room(self,name):
            for r in self.rooms:
                if r.name == name:
                    self.current_room = r
                    renpy.jump("load_room")
                    break

        def move_dir(self,direction):
            dirx = self.current_room.x
            diry = self.current_room.y

            if direction == 'north':
                diry += 1
            if direction == 'east':
                dirx += 1
            if direction == 'south':
                diry -= 1
            if direction == 'west':
                dirx -= 1

            for room_name,room in self.rooms.iteritems():
                if not room.locked:
                    if room.x == dirx and room.y == diry:

                        self.current_room = room
                        renpy.jump("load_room")

        def get_random_monster(self,name):
            for x in self.random_monsters:
                if x.name == name:
                    return x

            return False


        def cr_get_neighbors(self):
            dirs = []

            for r_name,r in self.rooms.iteritems():
                if r.x == self.current_room.x and r.y == self.current_room.y+1 and not r.locked and not r.locksouth:
                    dirs.append('north')
                    continue
                if r.x == self.current_room.x and r.y == self.current_room.y-1 and not r.locked and not r.locknorth:
                    dirs.append('south')
                    continue
                if r.x == self.current_room.x+1 and r.y == self.current_room.y and not r.locked and not r.lockwest:
                    dirs.append('east')
                    continue
                if r.x == self.current_room.x-1 and r.y == self.current_room.y and not r.locked and not r.lockeast:
                    dirs.append('west')

            return dirs