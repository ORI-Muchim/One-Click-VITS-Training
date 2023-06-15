- # One-Click-VITS-Training

This tool allows you to complete the entire process of VITS (Data Preprocessing + Whisper ASR + Text Preprocessing + Modification config.json + Training, Inference) with ONE-CLICK!



## Table of Contents 
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Prepare_Datasets](#Prepare_Datasets)
- [Usage](#usage)
- [Inference](#inference)
- [Changes](#Changes)
- [Reference](#Reference)

## Prerequisites
- A Windows/Linux system with a minimum of 16GB RAM.
- A GPU with at least 12GB of VRAM.
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

## Prepare_Datasets

Place the audio files as follows. 

.mp3 or .wav files are okay.

```
One-Click-VITS-Training
├────datasets
│       ├───speaker0
│       │   ├────1.mp3
│       │   └────1.wav
│       └───speaker1
│       │    ├───1.mp3
│       │    └───1.wav
│       └integral.py
│
├────vits
├────main.py
├────Readme.md
└────requirements.txt
```

This is just an example, and it's okay to add more speakers.

---

## Usage

To start this tool, use the following command, replacing {language}, {model_name}, and {sample_rate} with your respective values:

```sh
python main.py {language} {model_name} {sample_rate}
```

For those with low specifications, please use this code:

```sh
python main_low.py {language} {model_name} {sample_rate}
```

If the data configuration is complete and you want to resume training, enter this code:

```sh
python main_resume.py {model_name}
```

---
## Inference

After the model has been trained, you can generate predictions by using the following command, replacing {model_name} and {model_step} with your respective values:

```sh
python inference.py {model_name} {model_step}
```

Or check ./vits/inference.ipynb.

---

## Changes

In the repository of [CjangCjengh/vits](https://github.com/CjangCjengh/vits.git), I made some modifications to the Korean text cleaning method. The other cleaning process is the same by posting it to the CjangCjengh repository, but the cleaner file was modified using the [g2pk2](https://github.com/tenebo/g2pk2) library as Korean pronounced.

---
## References

For more information, please refer to the following repositories: 
- [jaywalnut310/vits](https://github.com/jaywalnut310/vits.git) 
- [CjangCjengh/vits](https://github.com/CjangCjengh/vits.git)
- [g2pk](https://github.com/Kyubyong/g2pK)
- [g2pk2](https://github.com/tenebo/g2pk2)