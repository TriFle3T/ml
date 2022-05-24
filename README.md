# ml

<!-- code_chunk_output -->

- [KoBERT with Huggingface](#kobert-with-huggingface)
- [Requirements](#requirements)
- [How to install](#how-to-install)
- [Data](#data)
- [Result](#result)
- [Reference](#reference)

<!-- /code_chunk_output -->

---

## KoBERT with Huggingface

Huggingface 기반 KoBERT를 사용하여 텍스트 감정 분석을 진행하였습니다.

## Requirements

- python==3.9.2
- mxnet==1.7.0.post2
- gluonnlp==0.10.0
- pandas==1.2.5
- sentencepiece==0.1.96
- transformers==4.2.2
- torch==1.11.0

## How to install

### in colab

```python
!pip install "git+https://github.com/SKTBrain/KoBERT.git#egg=kobert_tokenizer&subdirectory=kobert_hf"
```

### in vscode

```sh
python -m venv .venv
```

Python:Select Interpreter</br>
Python 3.9.2('.venv':venv)

```sh
pip install --upgrade pip
pip install "git+https://github.com/SKTBrain/KoBERT.git#egg=kobert_tokenizer&subdirectory=kobert_hf"
pip install -r requirements.txt
```

## Data

### Source

1. [AIHub 감정분류를 위한 대화 음성](https://aihub.or.kr/opendata/keti-data/recognition-laguage/KETI-02-002)
2. [AIHub 한국어 감정정보 단발성 대화](https://aihub.or.kr/opendata/keti-data/recognition-laguage/KETI-02-009)

### Dataset

| 감정 | 개수(1) | 개수(1+2) |
| ---- | ------- | --------- |
| 행복 | 4548    | 10585     |
| 분노 | 11635   | 17300     |
| 혐오 | 4660    | 10089     |
| 공포 | 4131    | 9599      |
| 중립 | 3262    | 8092      |
| 슬픔 | 14000   | 19267     |
| 놀람 | 1755    | 7653      |

## Result

| model(data) | acc     |
| ----------- | ------- |
| model1(1)   | 0.92422 |
| model2(1+2) | 0.74187 |

---

## Reference

- [KoBERT](https://github.com/SKTBrain/KoBERT)
- [Huggingface Transformers](https://github.com/huggingface/transformers)
