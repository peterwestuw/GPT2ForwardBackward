# GPT2ForwardBackward
Code for running forward and backward versions of GPT-2 XL. These were trained for the paper:

West, Peter et al. “Reflective Decoding: Beyond Unidirectional Generation with Off-the-Shelf Language Models.” ACL (2021)

If you use our model weights for academic research, we request that you cite the original paper:

```
@misc{west2021reflective,
      title={Reflective Decoding: Beyond Unidirectional Generation with Off-the-Shelf Language Models}, 
      author={Peter West and Ximing Lu and Ari Holtzman and Chandra Bhagavatula and Jena Hwang and Yejin Choi},
      year={2021},
      eprint={2010.08566},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

## Setup

Simply download this code
then download and extract forward and backward openGPT2 models

The model parameters are available at:

https://drive.google.com/drive/folders/10l0eF934JzkG83cOekLxnjAkO2rya45a?usp=sharing


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
