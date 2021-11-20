# GPT2ForwardBackward
Code for running forward and backward versions of GPT-2 XL. These were trained for the paper:

**Reflective Decoding: Beyond Unidirectional Generation with Off-the-Shelf Language Models**; Peter West, Ximing Lu, Ari Holtzman, Chandra Bhagavatula, Jena Hwang, and Yejin Choi; ACL (2021)

This paper introduces [Reflective Decoding](https://github.com/peterwestuw/ReflectiveDecoding)

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
of Huggingface transformers code (v4.5), installed from source from:

https://github.com/huggingface/transformers

Once above setup is done, models can be loaded as:
```
from modeling_opengpt2 import OpenGPT2LMHeadModel
from padded_encoder import Encoder
model_forward = OpenGPT2LMHeadModel.from_pretrained(path_to_forward)
model_backward = OpenGPT2LMHeadModel.from_pretrained(path_to_backward)
encoder = Encoder()
```
Then used identically to huggingface GPT-2 models (e.g. using `.forward()` and `.generate()`)

NOTE: The backward model expects *reverse* direction data, so you must reverse sequences after tokenizing. 
For example, to generate with the backward model you would call:

```
input_text = ' And that was the last I heard from her.'
input_tokens = encoder.encode(input_text)[::-1]

output = model_backward.generate(torch.tensor([input_tokens]).to(device_backward) )
output_tokens = output.tolist()[0][::-1]
print(encoder.decode(output_tokens))
```

Note that token order is reversed *before* generating to feed data into the backward model in the backwards order, then reversed again *after* generation to give a forward output sequence. 
