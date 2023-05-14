# Create a class named class TV
class TV:
    # The Attributes
    channel = 1
    volume_level = 1
    tv_is_on = True
    # Constructors
    def __init__(self, channel, volume_level):
        self.channel = channel
        self.volume_level = volume_level
    # Methods
    # Turn on the TV
    def turn_on(self):
        self.tv_is_on = True
    # Turn off the TV
    def turn_off(self):
        self.tv_is_on = False
    # Return the channel
    def get_channel(self):
        return self.channel
    # Set new channel
    def set_channel(self, channel):
        self.channel = channel
    # Return the volume
    def get_volume(self):
        return self.volume
    # Set new volume
    def set_volume(self, volume):
        self.volume = volume
    # Increase the channel by 1
    def channel_up(self):
        self.channel += 1
    # Decrease the channel by 1
    def channel_down(self):
        self.channel -= 1
    # Increase volume by 1
    def volume_up(self):
        self.volume += 1
    # Decrease volume by 1
    def volume_down(self):
        self.volume -= 1

# Create a Test driver program named test_tv
test_tv_1 = TV(channel = 30, volume = 3)
test_tv_2 = TV(channel = 3, volume = 2)

# Object 1
test_tv_1.turn_on()
test_tv_1.set_channel(30)
print(test_tv_1.get_channel())
test_tv_1.set_volume(3)
print(test_tv_1.get_volume())
test_tv_1.channel_up()
print(test_tv_1.get_channel())
test_tv_1.channel_down()
print(test_tv_1.get_channel())
test_tv_1.volume_up()
print(test_tv_1.get_volume())
test_tv_1.volume_down()
print(test_tv_1.get_volume())

# Object 2
test_tv_2.turn_on()
test_tv_2.set_channel(3)
test_tv_2.set_volume(2)
print(test_tv_2.get_channel())
print(test_tv_2.get_volume())
test_tv_2.channel_up()
print(test_tv_2.get_channel())
test_tv_2.channel_down()
print(test_tv_2.get_channel())
test_tv_2.volume_up()
print(test_tv_2.get_volume())
test_tv_2.volume_down()
print(test_tv_2.get_volume())

# Create a Test driver program named test_tv
    # first object from class TV
    # second object from class TV
# Call the function