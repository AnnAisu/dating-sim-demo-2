

init -9 python:

    class Napstablook(Monster):
        def __init__(self):
            Monster.__init__(self)
            self.default_event = Event("Napstablook_manager_default",True,self)
            self.name = "Napstablook"
            self.default_sprite = "napstablook normal"
            self.FP = 20

        def give_gift(self,item):
            renpy.say(self.name,"Oh? What do you have there?")

            if isinstance(item,Spider_Cider):
                renpy.say(self.name,"Thank you! I love this!")
                self.FP += 20
                return True

            if isinstance(item,Spider_Donut):
                renpy.say(self.name,"I don't like donuts.")
                self.FP -= 20
                return False
            return

        def handle_schedule(self):
            #night
            # self.update_schedule("Sunday","Night","Toriel's Room",self.default_event)
            # self.update_schedule("Monday","Night","Toriel's Room",self.default_event)
            # self.update_schedule("Tuesday","Night","Toriel's Room",self.default_event)
            # self.update_schedule("Wednesday","Night","Toriel's Room",self.default_event)
            # self.update_schedule("Thursday","Night","Toriel's Room",self.default_event)
            # self.update_schedule("Friday","Night","Toriel's Room",self.default_event)
            # self.update_schedule("Saturday","Night","Toriel's Room",self.default_event)
            #morning
            self.update_schedule("Sunday","Morning","Snail Hunting Room",self.default_event)
            self.update_schedule("Monday","Morning","Snail Hunting Room",self.default_event)
            self.update_schedule("Tuesday","Morning","Snail Hunting Room",self.default_event)
            self.update_schedule("Wednesday","Morning","Snail Hunting Room",self.default_event)
            self.update_schedule("Thursday","Morning","Snail Hunting Room",self.default_event)
            self.update_schedule("Friday","Morning","Snail Hunting Room",self.default_event)
            self.update_schedule("Saturday","Morning","Snail Hunting Room",self.default_event)
            #day
            self.update_schedule("Sunday","Day","Snail Hunting Room",self.default_event)
            self.update_schedule("Monday","Day","Snail Hunting Room",self.default_event)
            self.update_schedule("Tuesday","Day","Snail Hunting Room",self.default_event)
            self.update_schedule("Wednesday","Day","Snail Hunting Room",self.default_event)
            self.update_schedule("Thursday","Day","Snail Hunting Room",self.default_event)
            self.update_schedule("Friday","Day","Snail Hunting Room",self.default_event)
            self.update_schedule("Saturday","Day","Snail Hunting Room",self.default_event)
            #afternoon
            self.update_schedule("Sunday","Afternoon","Snail Hunting Room",self.default_event)
            self.update_schedule("Monday","Afternoon","Snail Hunting Room",self.default_event)
            self.update_schedule("Tuesday","Afternoon","Snail Hunting Room",self.default_event)
            self.update_schedule("Wednesday","Afternoon","Snail Hunting Room",self.default_event)
            self.update_schedule("Thursday","Afternoon","Snail Hunting Room",self.default_event)
            self.update_schedule("Friday","Afternoon","Snail Hunting Room",self.default_event)
            self.update_schedule("Saturday","Afternoon","Snail Hunting Room",self.default_event)
            #evening
            # self.update_schedule("Sunday","Evening","Toriel's Room",self.default_event)
            # self.update_schedule("Monday","Evening","Living Room",self.default_event)
            # self.update_schedule("Tuesday","Evening","Living Room",self.default_event)
            # self.update_schedule("Wednesday","Evening","Toriel's Room",self.default_event)
            # self.update_schedule("Thursday","Evening","Living Room",self.default_event)
            # self.update_schedule("Friday","Evening","Toriel's Room",self.default_event)
            # self.update_schedule("Saturday","Evening","Living Room",self.default_event)

            


label initialize_napstablook:
        
    image napstablook placeholder = "characters/Toriel/toriel_ph.png"
    image napstablook angry = "characters/Toriel/Toriel_Angry_colored.png"
    image napstablook annoyed = "characters/Toriel/Toriel_Annoyed_colors.png"
    image napstablook awkward = "characters/Toriel/Toriel_Awkward_colors.png"
    image napstablook blushing = "characters/Toriel/Toriel_Blushing_colors.png"
    image napstablook laughing = "characters/Toriel/Toriel_Laughing_colors.png"
    image napstablook normal = "characters/Toriel/Toriel_Neutral_colors.png"
    image napstablook reallysad = "characters/Toriel/Toriel_ReallySad_colors.png"

    define napstablook = ('Napstablook')
    define napstablookChar = Character('Napstablook', color="#FFFFFF")
    python:
        def napstablook(text, *args, **kwargs):
               napstablookChar(text, *args, **kwargs)
    return

label Napstablook_manager_default(owner = False, pause = True):


    call show_buttons from _call_show_buttons_7
    show napstablook normal
    if pause:
        $ renpy.pause()

    $ x = x / 0
    
    menu:
        "Napstablook"
        "Raise FP 10":
            $ owner.FP += 10
        "Lower FP 10":
            $ owner.FP -= 10
        "Give Gift" if len(inventory.items) > 0:
            show screen gift_item_menu(owner)
            "What should you give them?"
        "Exit":
            "okay."

    
    return
