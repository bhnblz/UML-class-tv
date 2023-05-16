# Create a class named class TV
class TV:
    # The Attributes
    channel = ""
    volume_level = ""
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
        if 1 <= channel <= 120 and self.tv_is_on:
            self.channel = channel
    # Return the volume
    def get_volume(self):
        return self.volume_level
    # Set new volume
    def set_volume(self, volume_level):
        if 1 <= volume_level <= 7 and self.tv_is_on:
            self.volume_level = volume_level
    # Increase the channel by 1
    def channel_up(self):
        if self.tv_is_on:
            self.channel += 1
    # Decrease the channel by 1
    def channel_down(self):
        if self.tv_is_on:
            self.channel -= 1
    # Increase volume by 1
    def volume_up(self):
        if self.tv_is_on:
            self.volume_level += 1
    # Decrease volume by 1
    def volume_down(self):
        if self.tv_is_on:
            self.volume_level -= 1
