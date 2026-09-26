#include "kasamodo_app.h"
#include <vector>
#include <string>

int main() {
    kasamodo_app();

    std::vector<std::string> vec;
    vec.push_back("test_package");

    kasamodo_app_print_vector(vec);
}
