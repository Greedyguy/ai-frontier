
# Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations

**Korean Title:** 사전 훈련된 표현을 보존함으로써 시각-언어-행동 모델에서 일반화 향상하기

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Spatial Reasoning|Spatial Reasoning]] [[keywords/broad/Vision-Language-Action Models|Vision-Language-Action Models]] [[keywords/broad/Pretrained Representations|Pretrained Representations]] [[keywords/specific/Co-training Strategy|Co-training Strategy]] [[keywords/unique/String-based Action Tokenizer|String-based Action Tokenizer]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Co-training Strategy
**🔬 Broad Technical**: Vision-Language-Action Models, Pretrained Representations
**🔗 Specific Connectable**: Dual-encoder Design
**⭐ Unique Technical**: String-based Action Tokenizer

**ArXiv ID**: [2509.11417](https://arxiv.org/abs/2509.11417)
**Published**: 2025-09-18
**Category**: cs.AI
**PDF**: [Download](https://arxiv.org/pdf/2509.11417.pdf)


## 🏷️ 추출된 키워드



`Vision-Language-Action Models` • 

`Pretrained Representations` • 

`Dual-encoder Design` • 

`String-based Action Tokenizer` • 

`Co-training Strategy`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.11417v2 Announce Type: replace-cross 
Abstract: Vision-language-action (VLA) models finetuned from vision-language models (VLMs) hold the promise of leveraging rich pretrained representations to build generalist robots across diverse tasks and environments. However, direct fine-tuning on robot data often disrupts these representations and limits generalization. We present a framework that better preserves pretrained features while adapting them for robot manipulation. Our approach introduces three components: (i) a dual-encoder design with one frozen vision encoder to retain pretrained features and another trainable for task adaptation, (ii) a string-based action tokenizer that casts continuous actions into character sequences aligned with the model's pretraining domain, and (iii) a co-training strategy that combines robot demonstrations with vision-language datasets emphasizing spatial reasoning and affordances. Evaluations in simulation and on real robots show that our method improves robustness to visual perturbations, generalization to novel instructions and environments, and overall task success compared to baselines.

## 🔍 Abstract (한글 번역)

arXiv:2509.11417v2 발표 유형: replace-cross
요약: 시각-언어-행동 (VLA) 모델은 시각-언어 모델 (VLMs)에서 세밀 조정된 것으로, 다양한 작업과 환경을 가로지르는 일반적인 로봇을 구축하기 위해 풍부한 사전 학습된 표현을 활용하는 가능성을 가지고 있습니다. 그러나 로봇 데이터에 직접 세밀 조정하는 것은 종종 이러한 표현을 방해하고 일반화를 제한합니다. 저희는 사전 학습된 특징을 보다 잘 보존하면서 로봇 조작을 위해 적응시키는 프레임워크를 제시합니다. 저희의 접근 방식은 세 가지 구성 요소를 소개합니다: (i) 사전 학습된 특징을 보존하기 위해 하나는 얼린 시각 인코더와 작업 적응을 위해 다른 하나가 훈련 가능한 이중 인코더 설계, (ii) 연속적인 작업을 모델의 사전 학습 도메인과 일치하는 문자 시퀀스로 변환하는 문자 기반 행동 토크나이저, 그리고 (iii) 로봇 데모와 공간 추론 및 affordances를 강조하는 시각-언어 데이터셋을 결합하는 공동 훈련 전략. 시뮬레이션 및 실제 로봇에서의 평가 결과, 저희 방법은 시각적 격동에 대한 강건성, 새로운 지시사항 및 환경에 대한 일반화, 그리고 기본선에 비해 전반적인 작업 성공을 향상시킵니다.

## 📝 요약

이 연구는 시각-언어-행동(VLA) 모델이 시각-언어 모델(VLMs)로부터 세밀 조정되어 다양한 작업과 환경에 걸쳐 일반적인 로봇을 구축하는 것을 약속한다. 그러나 로봇 데이터에 직접 세밀 조정하는 것은 종종 이러한 표현을 방해하고 일반화를 제한한다. 본 연구는 사전 훈련된 특징을 보다 잘 보존하면서 로봇 조작을 위해 적응시키는 프레임워크를 제시한다. 접근 방식은 세 가지 구성 요소를 도입한다: (i) 사전 훈련된 특징을 보존하기 위해 하나는 고정된 비전 인코더와 다른 하나는 작업 적응을 위해 훈련 가능한 이중 인코더 설계, (ii) 연속적인 행동을 모델의 사전 훈련 도메인에 맞게 문자 시퀀스로 변환하는 문자 기반 행동 토크나이저, (iii) 로봇 데모와 공간 추론 및 affordances를 강조하는 시각-언어 데이터셋을 결합하는 공동 훈련 전략. 시뮬레이션 및 실제 로봇에서의 평가 결과, 본 방법은 시각적 격동에 대한 강건성, 새로운 지시사항 및 환경에 대한 일반화, 전반적인 작업 성공 면에서 기준선과 비교하여 개선됨을 보여준다.

## 🎯 주요 포인트


- VLA 모델은 VLM으로부터 finetuned되며 다양한 작업과 환경에 걸쳐 일반적인 로봇을 구축하는 데 유용하다.

- 로봇 데이터에 대한 직접적인 finetuning은 pretrained 특성을 파괴하고 일반화를 제한할 수 있다.

- 새로운 프레임워크는 pretrained 특성을 보존하면서 로봇 조작을 위해 적응시키는 방법을 제시한다.


---

*Generated on 2025-09-18 16:35:58*