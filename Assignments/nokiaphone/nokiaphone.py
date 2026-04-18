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
    12.Profiles
    13.SIM services
    0.Exit
    """

# START OF PHONEBOOK MENU OPTIONS
phoneMenu = """
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
phoneSubMenu = """
    Options
    1.Type of view
    2.Memory status
    0.Go back
        """
# END OF PHONEBOOK MENU OPTIONS
        
        
# START OF MESSAGES MENU OPTIONS        
messagesMenu = """
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
    
messagesSubMenu = """
    Message settings
    1.Set 1
    3.Common
    """
messagesInnerSubMenuOne = """
    Set 1
    1.Message center number
    2.Message sent as
    3.Message validity
    """

messagesInnerSubMenuTwo = """
    Common
    1.Delivery reports
    2.Reply via same centre
    3.Character support
    """
    
# END OF MESSAGES MENU OPTIONS


# START OF CHAT MENU OPTIONS
chatMenu = """
    Chat
    """
# END OF CHAT MENU OPTIONS


# START OF CALL REGISTER MENU OPTIONS
callRegisterMenu = """
    Call register
    1.Missed calls
    2.Received calls
    3.Dialed numbers
    4.Erase recent call lists
    5.Show call duration
    6.Show call costs
    7.Call cost settings
    8.Prepaid credit
    """

callRegSubMenuOne = """
    Call register
    1.Last call duration
    2.All call's duration
    3.Received call's duration
    4.Dialled call's duration
    5.Clear timers
    """
    
callRegSubMenuTwo = """
    Show call costs
    1.Last call cost
    2.All call's cost
    3.Clear counters
    """
    
callRegSubMenuThree = """
    Call cost settings
    1.Call cost limit
    2.Show costs in
    """
    
callRegSubMenuFour = """
    Prepaid credit
    """
# END OF CALL REGISTER MENU OPTIONS


# START OF TONES MENU OPTIONS
tonesMenu = """
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
    """
# END OF TONES MENU OPTIONS


# START OF SETTINGS MENU
settingsMenu = """
    Settings
    1.Call settings
    2.Phone settings
    3.Security settings
    4.Restore factory settings
    """
    
settingsSubMenuOne = """
    Call settings
    1.Automatic redial
    2.Speed dialling
    3.Call waiting options
    4.Own number sending
    5.Phone line in use
    6.Automatic answer
    """
    
settingsSubMenuTwo = """
    Phone settings
    1.Language
    2.Cell info display
    3.Welcome note
    4.Network selection
    5.Lights
    6.Confirm SIM service actions
    """
    
settingsSubMenuThree = """
    Security settings
    1.PIN code request
    2.Call barring service
    3.Fixed dialling
    4.Closed user group
    5.Phone security
    6.Change access codes
    """
    
settingsSubMenuFour = """
    Restore factory settings
    """
# END OF SETTINGS MENU OPTIONS


# START OF CALL DIVERT MENU OPTIONS
callDivertMenu = """
    Call divert
    """
# End OF CALL DIVERT MENU OPTIONS


# START OF GAMES MENU OPTIONS
gamesMenu = """
    Games
    """
# End OF GAMES MENU OPTIONS


# START OF CALCULATOR MENU OPTIONS
calculatorMenu = """
    Calculator
    """
# End OF CALCULATOR MENU OPTIONS


# START OF REMINDERS MENU OPTIONS
remindersMenu = """
    Reminders
    """
# End OF REMINDERS MENU OPTIONS


# START OF CLOCK MENU OPTIONS
clockMenu = """
    Clock
    1.Alarm clock
    2.Clock settings
    3.Date settings
    4.Stopwatch
    5.Countdown timer
    6.Auto update of time and date
    """
# End OF CLOCK MENU OPTIONS


# START OF PROFILES MENU OPTIONS
profilesMenu = """
    Profiles
    """
# End OF PROFILES MENU OPTIONS


# START OF SIM SERVICES MENU OPTIONS
simServicesMenu = """
    SIM services
    """
# End OF SIM SERVICES MENU OPTIONS

print(main_menu)
user_option = int(input("Enter menu option: "))        

# while():
match user_option:
    case 1:
        print(phoneMenu)
        option = int(input("Enter menu option: "))
        if option == 8:
            print(phoneSubMenu)
        
    case 2:
        print(messagesMenu)
        option = int(input("Enter menu option: "))
        if option == 7: 
            print(messagesSubMenu)
            option = int(input("Enter menu option: "))
            if option == 1:
                print(messagesInnerSubMenuOne)
            elif option == 2:
                print(messagesInnerSubMenuTwo)

    case 3:
        print(chatMenu)
        
    case 4:
        print(callRegisterMenu)
        option = int(input("Enter menu option: "))
        if(option == 5):
            print(callRegSubMenuOne)
        elif(option == 6):
            print(callRegSubMenuTwo)
        elif(option == 7):
            print(callRegSubMenuThree)
        elif(option == 8):
            print(callRegSubMenuFour)
            
    case 5:
        print(tonesMenu)
        
    case 6:
        print(settingsMenu)
        option = int(input("Enter menu option: "))
        if(option == 1):
            print(settingsSubMenuOne)
        elif(option == 2):
            print(settingsSubMenuOne)
        elif(option == 3):
            print(settingsSubMenuThree)
        elif(option == 4):
            print(settingsSubMenuFour)

    case 7:
        print(callDivertMenu) 

    case 8:
        print(gamesMenu)
        
    case 9:
        print(calculatorMenu)
        
    case 10:
        print(remindersMenu)
        
    case 11:
        print(clockMenu)
        
    case 12:
        print(Profiles)
        
    case 13:
        print(simServicesMenu)
    case _:   
        print("You entered a wrong input")
