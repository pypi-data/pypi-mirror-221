import scipy.io.wavfile
import os
import re
from phonemizer import phonemize
import sounddevice as sd
import onnxruntime
import numpy as np
from huggingface_hub import snapshot_download

class TTS:
    def __init__(self, model_name: str, save_path: str = "./model") -> None:
        if not os.path.exists(save_path):
            os.mkdir(save_path)
        
        model_dir = os.path.join(save_path, model_name)
        
        if not os.path.exists(model_dir):
            snapshot_download(repo_id=model_name, allow_patterns=["*.txt", "*.onnx"], 
                              local_dir=model_dir
                              )
        
        sess_options = onnxruntime.SessionOptions()
        self.model = onnxruntime.InferenceSession(os.path.join(model_dir, "exported/model.onnx"), sess_options=sess_options)
        
        with open(os.path.join(model_dir, "exported/vocab.txt"), "r", encoding="utf-8") as vocab_file:
            self.symbols = vocab_file.read().split("\n")
        
        self.symbol_to_id = {s: i for i, s in enumerate(self.symbols)}
    
    def _ru_phonems(self, text: str) -> str:
        '''clean text'''
        text = text.lower()
        phonemes = phonemize(text, language='ru', backend='espeak', strip=True, preserve_punctuation=True, with_stress=True)
        phonemes = re.sub(re.compile(r'\s+'), ' ', phonemes)
        return phonemes
    
    def _text_to_sequence(self, text: str) -> list[int]:
        '''convert text to seq'''
        sequence = []
        clean_text = self._ru_phonems(text)
        for symbol in clean_text:
            symbol_id = self.symbol_to_id[symbol]
            sequence += [symbol_id]
        return sequence
    
    def _intersperse(self, lst, item):
        result = [item] * (len(lst) * 2 + 1)
        result[1::2] = lst
        return result
    
    def _get_text(self, text: str) -> list[int]:
        text_norm = self._text_to_sequence(text)
        text_norm = self._intersperse(text_norm, 0)
        return text_norm
    
    def save_wav(self, audio, path:str):
        '''save audio to wav'''
        scipy.io.wavfile.write(path, 22050, audio)
    
    def play_audio(self, audio):
        '''play audio'''
        sd.play(audio, 22050, blocking=True)
    
    def __call__(self, text: str, play = False):
        phoneme_ids = self._get_text(text)
        text = np.expand_dims(np.array(phoneme_ids, dtype=np.int64), 0)
        text_lengths = np.array([text.shape[1]], dtype=np.int64)
        scales = np.array(
            [0.667, 1, 0.8],
            dtype=np.float32,
        )
        audio = self.model.run(
            None,
            {
                "input": text,
                "input_lengths": text_lengths,
                "scales": scales,
                "sid": None,
            },
        )[0][0,0][0]
        if play:
            self.play_audio(audio)
        return audio