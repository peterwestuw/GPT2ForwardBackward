# GPT2ForwardBackward
Code for running forward and backward versions of GPT2

## Setup

Simply download this code
then download and extract forward and backward openGPT2 models

NOTE: this requires the latest (as of January 19 2020) version
of Huggingface transformers code, installed from source from:

https://github.com/huggingface/transformers

Once above setup is done, models can be loaded as:
```
from modeling_opengpt2 import OpenGPT2LMHeadModel
from padded_encoder import Encoder
model_forward = OpenGPT2LMHeadModel.from_pretrained(path_to_forward)
model_backward = OpenGPT2LMHeadModel.from_pretrained(path_to_backward)
encoder = Encoder()
```
