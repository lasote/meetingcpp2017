from conans import ConanFile, CMake


class LibaConan(ConanFile):
    name = "LibA"
    version = "1.0.0"
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "src/*"

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_dir="src")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*.lib", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["a"]

