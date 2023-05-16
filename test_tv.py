from class_tv import TV

def test_tv():
    # first object from class TV
    test_tv_1 = TV(channel = 30, volume_level = 3, tv_is_on = True)
    print("tv1's channel is ", (test_tv_1.channel), "and volume level is ", (test_tv_1.get_volume()))
    # second object from class TV
    test_tv_2 = TV(channel = 3, volume_level = 2, tv_is_on = True)
    print("tv2's channel is ", (test_tv_2.channel), "and volume level is ", (test_tv_2.get_volume()))
# Call the function
test_tv()