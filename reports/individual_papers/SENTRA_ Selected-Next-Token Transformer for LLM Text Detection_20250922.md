# SENTRA: Selected-Next-Token Transformer for LLM Text Detection

**Korean Title:** SENTRA: LLM 텍스트 탐지를 위한 선택된 다음 토큰 변환기

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/specific/Contrastive Pre-training|Contrastive Pre-training]] [[keywords/broad/Transformer|Transformer]] [[keywords/broad/NLP|NLP]] [[keywords/unique/Selected-Next-Token Transformer|Selected-Next-Token Transformer]] [[categories/cs.LG|cs.LG]] [[2025-09-19/DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM: Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (86.1% similar) [[2025-09-22/DynamicNER_ A Dynamic, Multilingual, and Fine-Grained Dataset for LLM-based Named Entity Recognition_20250922|DynamicNER: A Dynamic, Multilingual, and Fine-Grained Dataset for LLM-based Named Entity Recognition]] (83.1% similar) [[2025-09-18/LLM-I_ LLMs are Naturally Interleaved Multimodal Creators_20250918|LLM-I: LLMs are Naturally Interleaved Multimodal Creators]] (82.7% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Contrastive Pre-training
**🔬 Broad Technical**: Transformer, Natural Language Processing
**⭐ Unique Technical**: Selected-Next-Token Transformer
## 🔗 유사한 논문
- [[2025-09-19/DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (86.1% similar)
- [[2025-09-22/DynamicNER_ A Dynamic, Multilingual, and Fine-Grained Dataset for LLM-based Named Entity Recognition_20250922|DynamicNER A Dynamic, Multilingual, and Fine-Grained Dataset for LLM-based Named Entity Recognition]] (83.1% similar)
- [[2025-09-18/LLM-I_ LLMs are Naturally Interleaved Multimodal Creators_20250918|LLM-I LLMs are Naturally Interleaved Multimodal Creators]] (82.7% similar)
- [[2025-09-22/Subjective Behaviors and Preferences in LLM_ Language of Browsing_20250922|Subjective Behaviors and Preferences in LLM Language of Browsing]] (82.5% similar)
- [[2025-09-22/Can Large Language Models Infer Causal Relationships from Real-World Text_20250922|Can Large Language Models Infer Causal Relationships from Real-World Text]] (82.2% similar)


**ArXiv ID**: [2509.12385](https://arxiv.org/abs/2509.12385)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.12385.pdf)


**ArXiv ID**: [2509.12385](https://arxiv.org/abs/2509.12385)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.12385.pdf)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Contrastive Pre-training
**⭐ Unique Technical**: Selected-Next-Token Transformer
**🔬 Broad Technical**: Transformer, Natural Language Processing

## 🏷️ 추출된 키워드



`Transformer` • 

`Natural Language Processing` • 

`Contrastive Pre-training` • 

`Selected-Next-Token Transformer`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.12385v2 Announce Type: replace-cross 
Abstract: LLMs are becoming increasingly capable and widespread. Consequently, the potential and reality of their misuse is also growing. In this work, we address the problem of detecting LLM-generated text that is not explicitly declared as such. We present a novel, general-purpose, and supervised LLM text detector, SElected-Next-Token tRAnsformer (SENTRA). SENTRA is a Transformer-based encoder leveraging selected-next-token-probability sequences and utilizing contrastive pre-training on large amounts of unlabeled data. Our experiments on three popular public datasets across 24 domains of text demonstrate SENTRA is a general-purpose classifier that significantly outperforms popular baselines in the out-of-domain setting.

## 🔍 Abstract (한글 번역)

arXiv:2509.12385v2 발표 유형: 교차 대체  
초록: 대형 언어 모델(LLM)은 점점 더 강력해지고 널리 사용되고 있습니다. 그에 따라, 이들의 오용 가능성과 현실도 증가하고 있습니다. 본 연구에서는 명시적으로 LLM 생성 텍스트로 선언되지 않은 텍스트를 탐지하는 문제를 다룹니다. 우리는 새로운 범용 감독 학습 LLM 텍스트 탐지기인 SElected-Next-Token tRAnsformer (SENTRA)를 제시합니다. SENTRA는 선택된 다음 토큰 확률 시퀀스를 활용하고, 대량의 라벨이 없는 데이터에 대한 대조적 사전 학습을 활용하는 트랜스포머 기반 인코더입니다. 24개의 텍스트 도메인에 걸친 세 가지 인기 있는 공개 데이터셋에 대한 실험에서 SENTRA는 범용 분류기로서 도메인 외 설정에서 인기 있는 기준선을 크게 능가함을 보여줍니다.

## 📝 요약

이 논문은 LLM(대형 언어 모델) 생성 텍스트를 탐지하는 문제를 다룹니다. 저자들은 새로운 범용 감독 학습 기반 LLM 텍스트 탐지기인 SENTRA를 제안합니다. SENTRA는 선택된 다음 토큰 확률 시퀀스를 활용하는 Transformer 기반 인코더로, 대량의 비라벨 데이터에 대한 대조적 사전 학습을 사용합니다. 24개 도메인에 걸친 세 가지 공용 데이터셋 실험에서 SENTRA는 범용 분류기로서, 도메인 외 설정에서 기존의 인기 있는 기준 모델들을 능가하는 성능을 보였습니다. 주요 기여는 LLM 탐지의 정확성을 높이는 새로운 방법론을 제시한 것입니다.

## 🎯 주요 포인트


- 1. LLM의 오용 가능성과 현실이 증가하고 있으며, 이를 탐지하는 문제를 다루고 있다.

- 2. LLM이 생성한 텍스트를 탐지하기 위한 새로운 범용 감독 학습 모델인 SENTRA를 제안한다.

- 3. SENTRA는 선택된 다음 토큰 확률 시퀀스를 활용하는 Transformer 기반 인코더이다.

- 4. 대량의 비라벨 데이터에 대한 대조적 사전 학습을 통해 성능을 향상시킨다.

- 5. 24개 도메인의 텍스트를 포함한 세 가지 대중적인 공개 데이터셋 실험에서 SENTRA는 범용 분류기로서 타 인기 기준 모델들을 크게 능가한다.


---

*Generated on 2025-09-22 16:16:45*