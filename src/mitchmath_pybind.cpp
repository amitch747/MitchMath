#include <pybind11/pybind11.h>
#include "math.hpp"


PYBIND11_MODULE(mitchmath, m) {
    m.def("add", &add);
    m.def("sub", &sub);
    m.def("mul", &mul);
    m.def("divi", &divi);
}