from conans import ConanFile, CMake
from conan.tools.files import save

class FooConan(ConanFile):
    name = "foo"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    scm = {"type": "git", "revision": "auto"}


    def build(self):
        save(self, "foo.txt", "contents")

    def package(self):
        self.copy("*")

