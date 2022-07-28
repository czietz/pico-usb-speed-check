cmake_minimum_required(VERSION 3.12)

# Pull in PICO SDK (must be before project)
include(pico_sdk_import.cmake)

project(pico_examples C CXX ASM)

# Initialize the SDK
pico_sdk_init()
include_directories("..")
include_directories(".")

add_executable(usb_speed_check usb_speed_check.c usb_descriptors.c)

# pull in common dependencies
target_link_libraries(usb_speed_check pico_stdlib tinyusb_device tinyusb_board)

# create map/bin/hex/uf2 file etc.
pico_add_extra_outputs(usb_speed_check)

