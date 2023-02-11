import os

os.system("cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=1 .")
os.system("c2rust transpile -v -b sim.rs --translate-const-macros -r --reduce-type-annotations -o c2rust_output --overwrite-existing compile_commands.json")