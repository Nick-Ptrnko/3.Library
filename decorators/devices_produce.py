def fabric_of_device(device_name):
    count = 0
    def device():
        nonlocal count
        count += 1
        print (f"Produce {count} {device_name}")
    return device

phone = fabric_of_device("Pixel 8 pro")
laptop = fabric_of_device("ThinkPad")


phone()
phone()
phone()
phone()
phone()


