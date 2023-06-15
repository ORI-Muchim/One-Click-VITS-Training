#matplotlib inline
import matplotlib.pyplot as plt
import IPython.display as ipd
import os
import json
import math
import torch
import sys
from torch import nn
from torch.nn import functional as F
from torch.utils.data import DataLoader
import commons
import utils
from data_utils import TextAudioLoader, TextAudioCollate, TextAudioSpeakerLoader, TextAudioSpeakerCollate
from models import SynthesizerTrn
from text.symbols import symbols
from text import text_to_sequence
from scipy.io.wavfile import write

def get_text(text, hps):
    text_norm = text_to_sequence(text, hps.data.text_cleaners)
    if hps.data.add_blank:
        text_norm = commons.intersperse(text_norm, 0)
    text_norm = torch.LongTensor(text_norm)
    return text_norm

hps = utils.get_hparams_from_file(f"./models/{sys.argv[1]}/config.json")

net_g = SynthesizerTrn(
    len(symbols),
    hps.data.filter_length // 2 + 1,
    hps.train.segment_size // hps.data.hop_length,
    n_speakers=hps.data.n_speakers,
    **hps.model).cuda()
_ = net_g.eval()

_ = utils.load_checkpoint(f"./models/{sys.argv[1]}/G_{sys.argv[2]}.pth", net_g, None)

output_dir = f'./vitsoutput/{sys.argv[1]}'
os.makedirs(output_dir, exist_ok=True)

n_speakers = hps.data.n_speakers

for idx in range(n_speakers):
    sid = torch.LongTensor([idx]).cuda()
    stn_tst = get_text("가장 밝게 빛나는 순간은 주위의 모든 것이 가장 어두울 때이다.", hps)
    with torch.no_grad():
        x_tst = stn_tst.cuda().unsqueeze(0)
        x_tst_lengths = torch.LongTensor([stn_tst.size(0)]).cuda()
        audio = net_g.infer(x_tst, x_tst_lengths, sid=sid, noise_scale=.667, noise_scale_w=0.8, length_scale=1)[0][0,0].data.cpu().float().numpy()
    write(f'{output_dir}/output{idx}.wav', hps.data.sampling_rate, audio)
