# One-Click-VITS-Training

This is your one-stop solution to train the complete process of VITS, from pre-processing of audio data files, transcript creation using OpenAI's Whisper, text cleaning, config.json file creation, to the final step of model training.

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Inference](#inference)
- [Reference](#Reference)

---

## Prerequisites

* You have a Windows/Linux/Mac machine with a minimum of 8GB RAM.
* GPU must have at least 16 GB of VRAM.
* Python >= 3.8
* Install PyTorch.
```sh
pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu117
```

---

## Installation

Clone this repository to your local machine and install the necessary requirements:

```sh
git clone https://github.com/ORI-Muchim/One-Click-VITS-Training.git
```

```sh
cd One-Click-VITS-Training
```

```sh
pip install -r requirements.txt
```

---

## Usage

1. Work In Progress!

---

## Inference

```sh
python ./vits/inferencems.py {model_name} {model_step}
```

---

## Reference

- https://github.com/jaywalnut310/vits.git
- https://github.com/CjangCjengh/vits.git

---