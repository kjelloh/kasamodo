# Kasamodo console app

The kasamodo app is a C++23 console application.

This app is experimental.

## LICENSE

All source code is licenced as defined by [Apps LICENSE](../../apps/LICENCE.txt).

## Prerequisites

- A C++23 compiler
- CMake
- Conan package manager

## Build

* Update dependancies wit helper init_tool_chain.zsh

```sh
./init_tool_chain.zsh
```

  * Does ```conan install . --settings=compiler.cppstd=23 --settings=build_type=$BUILD_TYPE --build=missing````
  * Does ```cmake --preset $PRESET_NAME```
  * By mapping:

```sh
case $BUILD_TYPE in
    "Debug") PRESET_NAME="conan-debug" ;;
    "Release") PRESET_NAME="conan-release" ;;
    "RelWithDebInfo") PRESET_NAME="conan-relwithdebinfo" ;;
    "MinSizeRel") PRESET_NAME="conan-minsizerel" ;;
    *) 
```

* Generate: CMakeLists.txt -> Build (Make) Configuration.

```sh
  cmake -S . -B build
```

* Build: Build (Make) Configuration -> target(s)

```sh
cmake --build build
```

* Run target cpp_habilis

```sh
./build/kasamodo_app --help
```

# History

## The conan package manager scaffolding

The conan package manager scaffolding was generated with the conan 'new' command.

```sh
kjell-olovhogdahl@MacBook-Pro ~/Documents/GitHub/kasamodo/apps % conan new cmake_exe -d name=kasamodo_app -d version=0.0
File saved: CMakeLists.txt
File saved: conanfile.py
File saved: src/kasamodo_app.cpp
File saved: src/kasamodo_app.h
File saved: src/main.cpp
File saved: test_package/conanfile.py
kjell-olovhogdahl@MacBook-Pro ~/Documents/GitHub/kasamodo/apps % 
```