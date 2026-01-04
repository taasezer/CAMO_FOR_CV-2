cmake_minimum_required(VERSION 3.20)
project(CargoCapture)

find_package(OpenCV REQUIRED)
add_executable(capture camo_capture.cpp)
target_link_libraries(capture ${OpenCV_LIBS})
