import subprocess
import sys

subprocess.run(["python", f"./datasets/integral.py {sys.argv[1]} {sys.argv[2]} {sys.argv[3]}"])
