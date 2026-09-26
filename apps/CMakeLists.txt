cmake_minimum_required(VERSION 3.15)
project(kasamodo_app CXX)



add_executable(kasamodo_app src/kasamodo_app.cpp src/main.cpp)

# Apply cmake mapping of C++ language features to compiler specific arguments
# kasamodo_app: Most warnings + warnings as errors
# Also see: https://github.com/cpp-best-practices/cppbestpractices/blob/master/02-Use_the_Tools_Available.md
target_compile_features(kasamodo_app PRIVATE cxx_std_23)

# Adapt compiler otpions to concrete compiler
if(MSVC)
	target_compile_options(kasamodo_app PRIVATE
    /W4
    /w14640
    /permissive-
  )
else()
	target_compile_options(kasamodo_app PRIVATE
    -Wall 
    -Wextra 
    -Wshadow 
    -Wnon-virtual-dtor 
    -pedantic
  )
endif()

# Use the cmake support for cross platform install folders structure and location
# Note: 'Gnu' Naming is a bit confusing?
include(GNUInstallDirs)

# Define what cmake install should do
install(TARGETS kasamodo_app
	RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)
