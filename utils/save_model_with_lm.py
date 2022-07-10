import sys
from pathlib import Path

from transformers import Wav2Vec2ProcessorWithLM, Wav2Vec2Processor
from pyctcdecode import build_ctcdecoder


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage:')
        print('python save_model_with_lm.py /path/to/model /where/to/save /path/to/lm.file')
        exit(1)

    MODEL_ID = Path(sys.argv[1])
    SAVE_TO = Path(sys.argv[2])
    LM_PATH = str(Path(sys.argv[3]).absolute())

    processor = Wav2Vec2Processor.from_pretrained(MODEL_ID)

    vocab_dict = processor.tokenizer.get_vocab()
    sorted_vocab_dict = {k.lower(): v for k, v in sorted(vocab_dict.items(), key=lambda item: item[1])}

    print(vocab_dict)
    print(sorted_vocab_dict)

    print('Tokenizer size', len(processor.tokenizer))
    print('Pad token ID', processor.tokenizer.pad_token_id)

    decoder = build_ctcdecoder(
        labels=list(sorted_vocab_dict.keys()),
        kenlm_model_path=LM_PATH,
    )

    processor_with_lm = Wav2Vec2ProcessorWithLM(
        feature_extractor=processor.feature_extractor,
        tokenizer=processor.tokenizer,
        decoder=decoder
    )

    processor_with_lm.save_pretrained(SAVE_TO)

    print('Done.')
