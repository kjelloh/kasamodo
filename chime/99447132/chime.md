# Consider a git clone/pull external source dependancies mechanism as a python script?

## 20260907

I am now working on making [init_toolchain.py](../apps/init_toolchain.py) to clone the Eigen C++ library for consumption by the kasamodo_app.

* [Eigen home](https://libeigen.gitlab.io)
  * ``` git clone https://gitlab.com/libeigen/eigen.git ```

I created init_toolchain.py with chatGPT vibe-coding and edits (seems to work ok)

## 20260906

So I want to do a test-shot at making the kasamodo app solve for a stiffness matrix using the C++ Eigen library.

* I want to try a python script that git clones Eigen and populate build environment with headert files and paths
  * It seems I should provide a -I directive to the compiler?
  * And include with ""?
  * The C++ preprocessor seems to search for #include "some_file" in local folder structure and listed include paths? 
  * [GCC search paths](https://gcc.gnu.org/onlinedocs/cpp/Search-Path.html)
  * Eigen seem to propose ```#include <>``` [Eigen - Getting Started](https://libeigen.gitlab.io/eigen/docs-5.0/GettingStarted.html)


