#include <iostream>
#include <string_view>

namespace {

  constexpr std::string_view version = "0.1.0";

  void print_usage(std::string_view program_name) {
    std::cout << "Usage: " << program_name << " [options]\n"
      << "\nOptions:\n"
      << "  -h, --help       Show this help message\n"
      << "  -v, --version    Show the version\n";
  }

} // namespace

int main(int argc, char* argv[]) {
  const std::string_view program_name = argc > 0 ? argv[0] : "kasamodo app";

  if (argc == 1) {
    print_usage(program_name);
    return 0;
  }

  for (int index = 1; index < argc; ++index) {
    const std::string_view argument = argv[index];

    if (argument == "-h" || argument == "--help") {
      print_usage(program_name);
    }
    else if (argument == "-v" || argument == "--version") {
      std::cout << version << '\n';
    }
    else {
      std::cerr << "Unknown option: " << argument << "\n\n";
      print_usage(program_name);
      return 2;
    }
  }

  return 0;
}
