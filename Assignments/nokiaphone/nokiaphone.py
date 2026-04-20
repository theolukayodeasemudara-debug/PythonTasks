# // menu options from one 1 - 13
main_menu = """
    Main menu
    1.Phone book
    2.Messages
    3.Chat
    4.Call register
    5.Tones
    6.Settings
    7.Call divert
    8.Games
    9.Calculator
    10.Reminders
    11.Clock
    12.profiles
    13.SIM services
    0.Exit
    """

# START OF PHONEBOOK MENU OPTIONS
phone_menu = """
    Phone Book
    1.Search
    2.Service Nos
    3.Add name
    4.Erase
    5.Edit
    6.Assign tone
    7.Send b'card
    8.Options
    9.Speed dials
    10.Voice tags
    0.Go back
    """
phone_submenu = """
    Options
    1.Type of view
    2.Memory status
    0.Go back
        """
# END OF PHONEBOOK MENU OPTIONS
        
        
# START OF MESSAGES MENU OPTIONS        
messages_menu = """
    Messages
    1.Write message
    2.Inbox
    3.Outbox
    4.Picture messages
    5.Templates
    6.Smileys
    7.Message settings
    8.Info service
    9.Voice mailbox
    10.Service command editor
    """;
    
messages_submenu = """
    Message settings
    1.Set 1
    3.Common
    press 0 to return
    """
messages_innersubmenu_one = """
    Set 1
    1.Message center number
    2.Message sent as
    3.Message validity
    """

messages_innersubmenu_two = """
    Common
    1.Delivery reports
    2.Reply via same centre
    3.Character support
    """
    
# END OF MESSAGES MENU OPTIONS


# START OF CHAT MENU OPTIONS
chat_menu = """
    Chat
    0 to return
    """
# END OF CHAT MENU OPTIONS


# START OF CALL REGISTER MENU OPTIONS
call_registermenu = """
    Call register
    1.Missed calls
    2.Received calls
    3.Dialed numbers
    4.Erase recent call lists
    5.Show call duration
    6.Show call costs
    7.Call cost settings
    8.Prepaid credit
    0 to return
    """

call_registersubmenu_one = """
    Show call duration
    1.Last call duration
    2.All call's duration
    3.Received call's duration
    4.Dialled call's duration
    5.Clear timers
    """
    
call_registersubmenu_two = """
    Show call costs
    1.Last call cost
    2.All call's cost
    3.Clear counters
    """
    
call_registersubmenu_three = """
    Call cost settings
    1.Call cost limit
    2.Show costs in
    """
    
call_registersubmenu_four = """
    Prepaid credit
    """
# END OF CALL REGISTER MENU OPTIONS


# START OF TONES MENU OPTIONS
tones_menu = """
    Tones
    1.Ringing tone
    2.Ringing volume
    3.Incoming call alert
    4.Composer
    5.Message alert tone
    6.Keypad tones
    7.Warning and game tones
    8.Vibrating alert
    9.Screen saver
    0 to return
    """
# END OF TONES MENU OPTIONS


# START OF SETTINGS MENU
settings_menu = """
    Settings
    1.Call settings
    2.Phone settings
    3.Security settings
    4.Restore factory settings
    """
    
settings_submenu_one = """
    Call settings
    1.Automatic redial
    2.Speed dialling
    3.Call waiting options
    4.Own number sending
    5.Phone line in use
    6.Automatic answer
    """
    
settings_submenu_two = """
    Phone settings
    1.Language
    2.Cell info display
    3.Welcome note
    4.Network selection
    5.Lights
    6.Confirm SIM service actions
    """
    
settings_submenu_three = """
    Security settings
    1.PIN code request
    2.Call barring service
    3.Fixed dialling
    4.Closed user group
    5.Phone security
    6.Change access codes
    """
    
settings_submenu_four = """
    Restore factory settings
    """
# END OF SETTINGS MENU OPTIONS


# START OF CALL DIVERT MENU OPTIONS
calldivert_menu = """
    Call divert
    0 to return
    """
# End OF CALL DIVERT MENU OPTIONS


# START OF GAMES MENU OPTIONS
games_menu = """
    Games
    o to return
    """
# End OF GAMES MENU OPTIONS


# START OF CALCULATOR MENU OPTIONS
calculator_menu = """
    Calculator
    """
# End OF CALCULATOR MENU OPTIONS


# START OF REMINDERS MENU OPTIONS
reminders_menu = """
    Reminders
    o to return
    """
# End OF REMINDERS MENU OPTIONS


# START OF CLOCK MENU OPTIONS
clock_menu = """
    Clock
    1.Alarm clock
    2.Clock settings
    3.Date settings
    4.Stopwatch
    5.Countdown timer
    6.Auto update of time and date
    0 to return
    """
# End OF CLOCK MENU OPTIONS


# START OF PROFILES MENU OPTIONS
profiles_menu = """
    profiles
    0 to return
    """
# End OF PROFILES MENU OPTIONS


# START OF SIM SERVICES MENU OPTIONS
sim_services_menu = """
    SIM services
    0 to return
    """
# End OF SIM SERVICES MENU OPTIONS


print(main_menu)
options = int(input("Enter menu option: "))


if options == 1:
    print(phone_menu)
    while True:
        options = int(input("Enter menu option: "))
        if options == 8:
            print(phone_submenu)
        elif options != 8:
            print(phone_menu)
        elif options == 0:
            print(phone_menu)

    
if options == 2:
    print(messages_menu)
    while True:
        options = int(input("Enter menu option: "))
        if options == 7:
            print(messages_submenu)
        elif options != 7:
            print(messages_menu)
            if options == 1:
                print(messages_innersubmenu_one)
            elif options == 2:
                print(messages_innersubmenu_one)
            elif options != 1 or options != 2:
                print(messages_menu)
            elif options == 0:
                print(messages_menu)
                
                
if options == 3:
    print(chat_menu)
    while True:
        options = int(input("Enter menu option: "))
        if options == 0:
            print(main_menu)
                        
    
if options == 4:
    print(call_registermenu)
    while True:
        options = int(input("Enter menu option: "))
        if options == 5:
            print(call_registersubmenu_one)
        elif options == 6:
            print(call_registersubmenu_two)
        elif options == 7:
            print(call_registersubmenu_three)
        elif options == 8:
            print(call_registersubmenu_four)
        elif options != 5 or options != 6 or options != 7 or options !=8:
            print(call_registermenu)
            

if options == 5:
    print(tones_menu)
    while True:
        options = int(input("Enter menu option: "))
        if options != 5:
            print(tones_menu)
            if options == 0:
                print(main_menu)
  
            
if options == 6:
    print(settings_menu)
    while True:
        options = int(input("Enter menu option: "))
        if options == 1:
            print(settings_submenu_one) 
        elif options == 2:
            print(settings_submenu_two)
        elif options == 3:
            print(settings_submenu_three)
        elif options == 4:
            print(settings_submenu_four) 
            
            
if options == 7:
    print(calldivert_menu)
    while True:
        options = int(input("Enter menu option: "))
        if options == 0:
            print(main_menu)


if options == 8:
    print(games_menu)
    while True:
        options = int(input("Enter menu option: "))
        if options == 0:
            print(main_menu)
    
    
if options == 9:
    print(calcultor_menu)
    while True:
        options = int(input("Enter menu option: "))
        if options == 0:
            print(main_menu)
    
    
if options == 10:
    print(reminders_menu)
    while True:
        options = int(input("Enter menu option: "))
        if options == 0:
            print(main_menu)
    
    
if options == 11:
    print(clock_menu)
    while True:
        options = int(input("Enter menu option: "))
        if options == 0:
            print(main_menu)
    
    
if options == 12:
    print(profiles_menu)
    while True:
        options = int(input("Enter menu option: "))
        if options == 0:
            print(main_menu)
    

if options == 13:
    print(sim_services_menu)
    while True:
        options = int(input("Enter menu option: "))
        if options == 0:
            print(main_menu)
    

# shut down phone
if options == 0:
    while True:
        break    
