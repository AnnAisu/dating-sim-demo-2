init:
    $ screen_width = config.screen_width # 800
    $ screen_height = config.screen_height # 600
    $ shop_dialog_width = int(screen_width*.70)
    $ shop_dialog_height = int(screen_height*.215)



define payneShop = Character('PayneGray',
    window_left_margin = int(screen_width*.02),
    window_right_margin = int(screen_width*.265),
    window_top_margin = int(screen_height*(-.05)),#-30,
    window_bottom_margin = 16,
    window_top_padding = 10,
    window_bottom_padding = 10,
    window_left_padding = 15,
    window_right_padding = 15)

screen shop_box(shop):
    ### Main Shop Menu Box###
    frame pos(int(screen_width*.73),.688):
        vbox:
            anchor(-.25,0)
            maximum(int(screen_width*.24),int(screen_height*.267))
            minimum(int(screen_width*.24),int(screen_height*.267))
            textbutton "BUY" background "#000000" action [Play ("sound", "audio/sfx/click.wav"),Show("buy_box")]
            textbutton "SELL" background "#000000" action [Play ("sound", "audio/sfx/click.wav"),ui.callsinnewcontext(shop.shop_sell)]
            textbutton "TALK" background "#000000" action [Play ("sound", "audio/sfx/click.wav"),ui.callsinnewcontext(shop.shop_dialogue)] 
            textbutton "EXIT" background "#000000" action [Play ("sound", "audio/sfx/click.wav"),Hide("buy_box"),Hide("shop_box"),Show("show_nav_button"),Show("show_menu_button")]
            hbox:
                #anchor(0,0)
                vbox:
                    anchor(42,0)
                    text "[player.gold]G" xalign 0.5

                vbox:
                    #anchor(-40,0)
                    $ t = len(inventory.items)
                    text "[t]/[inventory.max_items]" text_align 1.0

screen buy_box():
    ###  ###
    #frame pos(int(screen_width*.02),.10):
    frame pos(int(screen_width*.02),.688):
        window xmargin -21 ymargin -21:
            maximum(shop_dialog_width,shop_dialog_height)
            minimum(shop_dialog_width,shop_dialog_height)
            vbox:
                textbutton "Spider Donut - 1G" background "#000000" action [Play ("sound", "audio/sfx/click.wav"),ui.callsinnewcontext("buy_item",Spider_Donut())]
                textbutton "Spider Cider - 5G" background "#000000" action [Play ("sound", "audio/sfx/click.wav"),ui.callsinnewcontext("buy_item",Spider_Cider())]
                textbutton "Test - 5G" background "#000000" 
                textbutton "Test - 5G" background "#000000" 
                textbutton "Exit" background "#000000" action [Play ("sound", "audio/sfx/click.wav"),Hide("buy_box")]

screen buy_dialogue(shop):
    frame pos(int(screen_width*.73),.688):
        vbox:
            anchor(-.25,0)
            maximum(int(screen_width*.24),int(screen_height*.267))
            minimum(int(screen_width*.24),int(screen_height*.267))
            hbox:
                vbox:
                    anchor(42,0)
                    text "[player.gold]G" xalign 0.5

                vbox:
                    text "[len(inventory.items)]/[inventory.max_items]" text_align 1.0

init -1 python:
    class Shop():
        def __init__(self):
            self.name = "PayneGray"
            self.template = payneShop.copy(self.name,window_top_margin = int(screen_height*(-.064)))
            self.welcome = {}
            self.welcome['sprite'] = 'flowey normal'
            self.welcome['text'] = ()
            self.welcome['text'] = "There doesn't seem to be anybody here.","There are some items sitting on the ground.","Spiders look down at you from the ceiling."
    
            #adding this so the label can be dynamic
            self.shop_dialogue = "Shop_Dialogue"
            self.shop_sell = "Shop_Sell"
            self.shop_exit = "Shop_Exit"



        ###Shop Access Functions###

        def enter(self):
            renpy.jump("Shop_Intro")


        def buy(self,item):
            if player.gold >= item.sale_cost:
                player.gold = player.gold - item.sale_cost
            if inventory.has_space():
                inventory.add(item)

label buy_item(item):
    if not inventory.has_space():
        "You can't carry anymore"
    elif player.gold < item.sale_cost:
        "You do not have enough Gold."
    else:
        $ muffetShop.buy(item)
        "You bought a [item.name]."
    return

label Shop_Intro:
    $ count = 0

    while count < len(muffetShop.welcome['text']):
        $ line = muffetShop.welcome['text'][count]
        "[line]"
        $ count += 1

    show screen shop_box(muffetShop)
    while True:
        pause

    return

label Shop_Dialogue:
    
    "I don't think there is anybody here..."

    return


label Shop_Sell:
    
    "The spiders look at you condescendingly."
    "They are here to make money, not buy your trash."

    return
    


label Muffet_Shop:
    python:
        muffetShop = Shop()
        muffetShop.enter()
    return

label Shop_Exit:
    hide screen shop_box
    hide screen buy_box
    