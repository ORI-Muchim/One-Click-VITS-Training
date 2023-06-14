import os
import subprocess
import sys

os.chdir('./datasets')  # 변경하고자 하는 디렉토리로 이동
subprocess.run(["python", "integral.py", sys.argv[1], sys.argv[2], sys.argv[3]])

config_path = f"../datasets/{sys.argv[2]}.json"
model_name = sys.argv[2]

os.chdir('../vits')  # 다음 작업을 위한 디렉토리로 이동
command = ["python", "train_ms.py", "-c", config_path, "-m", model_name]

subprocess.run(command)
