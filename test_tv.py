import tv_class

tv_class.TV

def test_tv():
    # first object from class TV
    test_tv_1 = tv_class(channel = 30, volume = 3)
    print("tv1's channel is " + str(test_tv_1), "and volume level is " + str(test_tv_1))
    # second object from class TV
    test_tv_2 = tv_class(channel = 3, volume = 2)
    print("tv2's channel is " + str(test_tv_2), "and volume level is " + str(test_tv_2))
# Call the function
test_tv()