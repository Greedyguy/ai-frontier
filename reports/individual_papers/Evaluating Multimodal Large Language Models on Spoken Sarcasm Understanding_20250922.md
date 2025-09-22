# Evaluating Multimodal Large Language Models on Spoken Sarcasm Understanding

**Korean Title:** 구어적 반어법 이해에 대한 다중모달 대형 언어 모델 평가

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Cross-lingual Sarcasm Understanding|Cross-lingual Sarcasm Understanding]] [[keywords/specific/Few-shot Learning|Few-shot Learning]] [[keywords/specific/Collaborative Gating Fusion|Collaborative Gating Fusion]] [[keywords/broad/Multimodal Large Language Models|Multimodal Large Language Models]] [[keywords/broad/Natural Language Understanding|Natural Language Understanding]] [[categories/cs.CL|cs.CL]] [[2025-09-22/Predicting Language Models' Success at Zero-Shot Probabilistic Prediction_20250922|Predicting Language Models' Success at Zero-Shot Probabilistic Prediction]] (84.7% similar) [[2025-09-19/Large Multi-modal Models Can Interpret Features in Large Multi-modal Models_20250919|Large Multi-modal Models Can Interpret Features in Large Multi-modal Models]] (84.3% similar) [[2025-09-22/Exploring Fine-Tuning of Large Audio Language Models for Spoken Language Understanding under Limited Speech data_20250922|Exploring Fine-Tuning of Large Audio Language Models for Spoken Language Understanding under Limited Speech data]] (84.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Zero-shot Learning, Few-shot Learning
**🔬 Broad Technical**: Multimodal Large Language Models, Natural Language Understanding
**⭐ Unique Technical**: Collaborative Gating Fusion Module
## 🔗 유사한 논문
- [[2025-09-22/Predicting Language Models' Success at Zero-Shot Probabilistic Prediction_20250922|Predicting Language Models' Success at Zero-Shot Probabilistic Prediction]] (84.7% similar)
- [[2025-09-19/Large Multi-modal Models Can Interpret Features in Large Multi-modal Models_20250919|Large Multi-modal Models Can Interpret Features in Large Multi-modal Models]] (84.3% similar)
- [[2025-09-22/Exploring Fine-Tuning of Large Audio Language Models for Spoken Language Understanding under Limited Speech data_20250922|Exploring Fine-Tuning of Large Audio Language Models for Spoken Language Understanding under Limited Speech data]] (84.2% similar)
- [[2025-09-19/Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (84.1% similar)
- [[2025-09-22/Beyond Spurious Signals_ Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing_20250922|Beyond Spurious Signals Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing]] (83.8% similar)


**ArXiv ID**: [2509.15476](https://arxiv.org/abs/2509.15476)
**Published**: 2025-09-22
**Category**: cs.CL
**PDF**: [Download](https://arxiv.org/pdf/2509.15476.pdf)


**ArXiv ID**: [2509.15476](https://arxiv.org/abs/2509.15476)
**Published**: 2025-09-22
**Category**: cs.CL
**PDF**: [Download](https://arxiv.org/pdf/2509.15476.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Cross-lingual Sarcasm Understanding
**🔗 Specific Connectable**: Few-shot Learning, Collaborative Gating Fusion
**🔬 Broad Technical**: Multimodal Large Language Models, Natural Language Understanding

## 🏷️ 추출된 키워드



`Multimodal Large Language Models` • 

`Natural Language Understanding` • 

`Zero-shot Learning` • 

`Few-shot Learning` • 

`Collaborative Gating Fusion Module`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15476v1 Announce Type: new 
Abstract: Sarcasm detection remains a challenge in natural language understanding, as sarcastic intent often relies on subtle cross-modal cues spanning text, speech, and vision. While prior work has primarily focused on textual or visual-textual sarcasm, comprehensive audio-visual-textual sarcasm understanding remains underexplored. In this paper, we systematically evaluate large language models (LLMs) and multimodal LLMs for sarcasm detection on English (MUStARD++) and Chinese (MCSD 1.0) in zero-shot, few-shot, and LoRA fine-tuning settings. In addition to direct classification, we explore models as feature encoders, integrating their representations through a collaborative gating fusion module. Experimental results show that audio-based models achieve the strongest unimodal performance, while text-audio and audio-vision combinations outperform unimodal and trimodal models. Furthermore, MLLMs such as Qwen-Omni show competitive zero-shot and fine-tuned performance. Our findings highlight the potential of MLLMs for cross-lingual, audio-visual-textual sarcasm understanding.

## 🔍 Abstract (한글 번역)

arXiv:2509.15476v1 발표 유형: 신규  
초록: 풍자 감지(sarcasm detection)는 자연어 이해에서 여전히 도전 과제로 남아 있으며, 풍자적 의도는 종종 텍스트, 음성 및 시각을 아우르는 미묘한 교차 모달 단서에 의존합니다. 이전 연구는 주로 텍스트 또는 시각-텍스트 풍자에 초점을 맞춰왔으나, 포괄적인 오디오-비주얼-텍스트 풍자 이해는 여전히 충분히 탐구되지 않았습니다. 본 논문에서는 영어(MUStARD++)와 중국어(MCSD 1.0)에 대해 제로샷, 몇샷, LoRA 미세 조정 설정에서 풍자 감지를 위한 대형 언어 모델(LLM)과 다중 모달 LLM을 체계적으로 평가합니다. 직접 분류 외에도, 우리는 모델을 특징 인코더로 활용하여 협력적 게이팅 융합 모듈을 통해 그들의 표현을 통합하는 방법을 탐구합니다. 실험 결과에 따르면, 오디오 기반 모델이 가장 강력한 단일 모달 성능을 달성하며, 텍스트-오디오 및 오디오-비전 조합이 단일 모달 및 삼중 모달 모델을 능가합니다. 또한, Qwen-Omni와 같은 MLLM은 경쟁력 있는 제로샷 및 미세 조정 성능을 보여줍니다. 우리의 연구 결과는 MLLM이 교차 언어, 오디오-비주얼-텍스트 풍자 이해에 잠재력이 있음을 강조합니다.

## 📝 요약

이 논문은 자연어 이해에서의 풍자 감지 문제를 다룹니다. 기존 연구는 주로 텍스트나 시각-텍스트 풍자에 집중했지만, 이 논문은 오디오-비주얼-텍스트 풍자 이해를 포괄적으로 탐구합니다. 영어(MUStARD++)와 중국어(MCSD 1.0) 데이터셋에서 대형 언어 모델(LLM)과 멀티모달 LLM을 사용하여 제로샷, 퓨샷, LoRA 미세 조정 설정에서 풍자 감지를 평가했습니다. 실험 결과, 오디오 기반 모델이 가장 강력한 단일 모달 성능을 보였고, 텍스트-오디오 및 오디오-비전 조합이 단일 및 삼중 모달 모델보다 우수한 성능을 나타냈습니다. 또한, Qwen-Omni와 같은 MLLM은 경쟁력 있는 제로샷 및 미세 조정 성능을 보였습니다. 이 연구는 MLLM의 다국어 오디오-비주얼-텍스트 풍자 이해 가능성을 강조합니다.

## 🎯 주요 포인트


- 1. 풍자 감지에서 음성 기반 모델이 가장 강력한 단일 모달 성능을 보인다.

- 2. 텍스트-오디오 및 오디오-비전 조합이 단일 모달 및 삼중 모달 모델보다 뛰어난 성능을 발휘한다.

- 3. Qwen-Omni와 같은 다중 모달 대형 언어 모델(MLLMs)이 제로샷 및 미세 조정 성능에서 경쟁력을 보인다.

- 4. MLLMs는 교차 언어, 오디오-비주얼-텍스트 풍자 이해에 잠재력을 가지고 있다.

- 5. 협력 게이팅 융합 모듈을 통해 모델의 표현을 통합하여 풍자 감지 성능을 향상시킨다.


---

*Generated on 2025-09-22 16:21:32*