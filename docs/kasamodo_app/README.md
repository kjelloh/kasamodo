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