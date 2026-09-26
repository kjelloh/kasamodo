#pragma once

#include <vector>
#include <string>


#ifdef _WIN32
  #define KASAMODO_APP_EXPORT __declspec(dllexport)
#else
  #define KASAMODO_APP_EXPORT
#endif

KASAMODO_APP_EXPORT void kasamodo_app();
KASAMODO_APP_EXPORT void kasamodo_app_print_vector(const std::vector<std::string> &strings);
