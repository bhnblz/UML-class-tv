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
        if 1 <= channel <= 120:
            self.channel = channel
    # Return the volume
    def get_volume(self):
        return self.volume_level
    # Set new volume
    def set_volume(self, volume_level):
        if 1 <= volume_level <= 7:
            self.volume_level = volume_level
    # Increase the channel by 1
    def channel_up(self):
        self.channel += 1
    # Decrease the channel by 1
    def channel_down(self):
        self.channel -= 1
    # Increase volume by 1
    def volume_up(self):
        self.volume_level += 1
    # Decrease volume by 1
    def volume_down(self):
        self.volume_level -= 1

# Create a Test driver program named test_tv
def test_tv():
    # first object from class TV
    test_tv_1 = TV(channel = 30, volume_level = 3)
    print(f"tv1's channel is " + str(test_tv_1.channel), "and volume level is " + str(test_tv_1.get_volume()))
    # second object from class TV
# Call the function
test_tv()