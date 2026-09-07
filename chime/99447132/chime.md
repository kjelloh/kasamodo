# Consider a git clone/pull external source dependancies mechanism as a python script?

## 20260907

I am now working on making [init_toolchain.py](../apps/init_toolchain.py) to clone the Eigen C++ library for consumption by the kasamodo_app.

* [Eigen home](https://libeigen.gitlab.io)
  * ``` git clone https://gitlab.com/libeigen/eigen.git ```

I created init_toolchain.py with chatGPT vibe-coding and edits (seems to work ok)

I now have a simple initial git clone and subsequente git fecth.

But the next step to cherry pick the source code to consume turned out to hide some complexity?

* I now have a simple 'copy this source folder' to a designated folder for consumption
* For now I have the folder to conume from in 'srrc' folder as 'src/foreign'
  * So the eigen git repo copies the repo 'Eigen' folder to 'src/foreign/Eigen'
* What is now missing is a way to configure the tool chain to allow C++ code to do

```cpp
#include <Eigen/Dense>
```

* That is, know about the include path to 'src/foreign'

But here it seems I have the option to try to configure cmake to do this for me?

* We can imagine we generate a 'src/foreign/CMakeLists.txt'?
* Then the root CMakeLists.txt can include it as a 'sub module'?
* I tried some variants of this but the cmake semantics got in the way!
* I tried vibe coding but failed to get any clear grips on how to interact with cmake?

  * At one session I got random bits like:

```sh
add_library(foreign_foo STATIC ...?
target_include_directories(...?
target_link_libraries(my_application ...



```

  * At another session I got stuff like:

```text
Your generated:
src/foreign/CMakeLists.txt
could be:
```

```sh
# GENERATED FILE -- DO NOT EDIT

add_library(Eigen3 INTERFACE)

target_include_directories(Eigen3
    INTERFACE
        ${CMAKE_CURRENT_LIST_DIR}
)
```

```text
Your project's root CMakeLists.txt then only needs:
```

```sh
cmake_minimum_required(VERSION 3.20)

project(MyProject LANGUAGES CXX)

add_subdirectory(src/foreign)

add_executable(my_app
    src/main.cpp
)

target_link_libraries(my_app
    PRIVATE
        Eigen3
)
```

But nothing of this made me satisfied. It just seemed too complicarted and opaque.

* I mean, it's not rocket science?
* For Eigen I now I have headers only.
* And ALL the source code (headers) are in a tree under the repo 'Eigen' folder.
* It should not be that complicated to tell cmake this?

It seems clean to me to have the root CMakeLists.txt do add_subdirectory(src/foreign)!

* But I do NOT want the extra step to also do 'target_link_libraries' in the root cmake file?
* Is there not a way to put everything about the dependancy on foreign in 'foreign/CMakeLists.txt'?

At this stage I started to wonder if maybe I can assume all git repos I use this way have a CMakeLists.txt that KNOWS how to provide for 'cmake --install'?

* Then I could in theory get 'conan functionality' by just engage the aölready-trhere 'cmake --install' capability provided by the library developers?
* I could then even be tempted to also support 'building any library from scratch'?

Hm, I have to think about this...


## 20260906

So I want to do a test-shot at making the kasamodo app solve for a stiffness matrix using the C++ Eigen library.

* I want to try a python script that git clones Eigen and populate build environment with headert files and paths
  * It seems I should provide a -I directive to the compiler?
  * And include with ""?
  * The C++ preprocessor seems to search for #include "some_file" in local folder structure and listed include paths? 
  * [GCC search paths](https://gcc.gnu.org/onlinedocs/cpp/Search-Path.html)
  * Eigen seem to propose ```#include <>``` [Eigen - Getting Started](https://libeigen.gitlab.io/eigen/docs-5.0/GettingStarted.html)


