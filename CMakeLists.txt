cmake_minimum_required(VERSION 3.0)

project(test C)

add_library(
  lib STATIC
  C/lib.c
)

set_target_properties(lib PROPERTIES LANGUAGE C)

add_executable(sim C/sim.c)
target_link_libraries(sim lib)
set_target_properties(sim PROPERTIES LANGUAGE C)