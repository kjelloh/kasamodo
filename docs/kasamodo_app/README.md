# Kasamodo console app

The kasamodo app is a C++23 console application.

This app is experimental.

## Prerequisites

- A C++23 compiler
- CMake

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