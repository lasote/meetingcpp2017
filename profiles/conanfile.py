from conans import ConanFile, CMake

class MyprojectConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "bzip2/1.0.6@conan/stable"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

