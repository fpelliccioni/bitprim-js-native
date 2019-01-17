from conans import ConanFile, CMake
# import os

class BitprimJs(ConanFile):
    name = "bitprim-js"
    version = "0.1"
    license = "http://www.boost.org/users/license.html"
    url = "https://github.com/bitprim/bitprim-js"
    description = "Javascript API for the Bitcoin Full Node"
    settings = "os", "compiler", "build_type", "arch"
    
    # options = {"shared": [True, False]}
    # default_options = "shared=False"

    generators = "cmake"

    # TODO(fernando): queda pendiente seleccionar el default Shared=False
    

    # TODO(fernando): Set macros for the several DB modes
    requires = (("bitprim-node-cint/0.18.0@bitprim/stable"))
    default_options = {"bitprim-node-cint:db": "full"}

    def imports(self):
        self.copy("*.h", "./deps/include/bitprim", "include/bitprim")
        self.copy("*.hpp", dst="./deps/include/bitprim", src="include/bitprim")
        self.copy("*.lib", dst="./deps/lib", src="lib")
        self.copy("*.a", dst="./deps/lib", src="lib")
        self.copy("*.dylib", dst="./deps/lib", src="lib")
        self.copy("*.so", dst="./deps/lib", src="lib")
        self.copy("*.dll", dst="./deps/lib", src="lib")

