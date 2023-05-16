import pyfiglet
from colorama import Fore
greetings = "Kon'nichiwa!"
print(pyfiglet.figlet_format (greetings, font = "standard"))
introduction = "Welcome to this file! This is a separate file from class_tv file. This program will display the required output."
print(Fore.LIGHTRED_EX + "=" * 113)
print(Fore.LIGHTRED_EX + introduction.center(113))
print("=" * 113)

# Import class tv from TV
from class_tv import TV 

def test_tv():
    # first object from class TV
    test_tv_1 = TV(channel = 30, volume_level = 3, tv_is_on = True)
    print(Fore.LIGHTMAGENTA_EX + "\ntv1's channel is ", (test_tv_1.channel), "and volume level is ", (test_tv_1.get_volume()))
    # second object from class TV
    test_tv_2 = TV(channel = 3, volume_level = 2, tv_is_on = True)
    print(Fore.LIGHTMAGENTA_EX + "\ntv2's channel is ", (test_tv_2.channel), "and volume level is ", (test_tv_2.get_volume()))
# Call the function 
test_tv()