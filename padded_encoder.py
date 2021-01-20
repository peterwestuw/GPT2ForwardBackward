#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 16:03:52 2019

@author: peterawest
"""
from transformers import GPT2Tokenizer


class Encoder():
    def __init__(self):
        self.encoder = GPT2Tokenizer.from_pretrained('gpt2')
        
        assert(len(self.encoder.encode('<|endoftext|>')) ==1 )
        self.endoftext = self.encoder.encode('<|endoftext|>')[0]
        self.padding = 0
        
    def encode(self, text):
        return [t + 1 for t in self.encoder.encode(text)]
    
    def decode(self, tokens):
        tokens_shifted = [t - 1 for t in tokens if t !=0 ]
        if len(tokens_shifted) != len(tokens):
            print('WARNING: padding removed from sequence during decoding')
            
        return self.encoder.decode(tokens_shifted)
        
        