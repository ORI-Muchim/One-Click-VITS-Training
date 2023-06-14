- # One-Click-VITS-Training (Work in Progress)

This toolkit serves as a comprehensive guide for training the VITS model. The process covers everything from preprocessing audio data files, creating transcripts using OpenAI's Whisper, cleaning text, creating a config.json file, and ultimately training the model.

## Table of Contents 
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Inference](#inference)
- [Reference](#Reference)

## Prerequisites
- A Windows/Linux system with a minimum of 8GB RAM.
- A GPU with at least 16GB of VRAM.
- Python >= 3.8
- Anaconda installed.
- PyTorch installed.

```sh
pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu117
```

---

## Installation 
1. **Create an Anaconda environment:**

```sh
conda create -n one-click-vits python=3.8
```

2. **Activate the environment:**

```sh
conda activate one-click-vits
```

3. **Clone this repository to your local machine:**

```sh
git clone https://github.com/ORI-Muchim/One-Click-VITS-Training.git
```

4. **Navigate to the cloned directory:**

```sh
cd One-Click-VITS-Training
```

5. **Install the necessary dependencies:**

```sh
pip install -r requirements.txt
```

---
## Usage

To start training, use the following command, replacing {language}, {model_name}, and {sample_rate} with your respective values:

```sh
python main.py {language} {model_name} {sample_rate}
```

---
## Model Inference

After the model has been trained, you can generate predictions by using the following command, replacing {model_name} and {model_step} with your respective values:

```sh
python ./vits/inferencems.py {model_name} {model_step}
```

---
## References

For more information, please refer to the original repositories: 
- [jaywalnut310/vits](https://github.com/jaywalnut310/vits.git) 
- [CjangCjengh/vits](https://github.com/CjangCjengh/vits.git)