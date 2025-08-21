cmake_minimum_required(VERSION 3.20)
project (MitchMath LANGUAGES CXX)

set(PYBIND11_FINDPYTHON ON)
find_package(pybind11 CONFIG REQUIRED)

pybind11_add_module(mitchmath 
    src/mitchmath_pybind.cpp
    src/add.cpp
    src/sub.cpp
    src/mul.cpp
    src/divi.cpp

    
)

set_target_properties(mitchmath PROPERTIES CXX_STANDARD 17 CXX_STANDARD_REQUIRED YES)

install(TARGETS mitchmath DESTINATION .)