# Create a class named class TV
class TV:
    # The Attributes
    channel = ""
    volume_level = ""
    tv_is_on = True
    # Constructors
    def __init__(self, channel, volume_level, tv_is_on):
        self.channel = channel
        self.volume_level = volume_level
        self.tv_is_on = tv_is_on
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
        else:
            print("TV is off. You cannot set the channel")
    # Return the volume
    def get_volume(self):
        return self.volume_level
    # Set new volume
    def set_volume(self, volume_level):
        if 1 <= volume_level <= 7:
            self.volume_level = volume_level
        else:
            print("TV is off. You cannot set the volume")
    # Increase the channel by 1
    def channel_up(self):
        if self.tv_is_on:
            self.channel += 1
        else:
            print("TV is off. You cannot increase the channel")
    # Decrease the channel by 1
    def channel_down(self):
        if self.tv_is_on:
            self.channel -= 1
        else:
            print("TV is off. You cannot decrease the channel")
    # Increase volume by 1
    def volume_up(self):
        if self.tv_is_on:
            self.volume_level += 1
        else:
            print("TV is off. You cannot increase the volume")
    # Decrease volume by 1
    def volume_down(self):
        if self.tv_is_on:
            self.volume_level -= 1
        else:
            print("TV is off. You cannot decrease the volume")