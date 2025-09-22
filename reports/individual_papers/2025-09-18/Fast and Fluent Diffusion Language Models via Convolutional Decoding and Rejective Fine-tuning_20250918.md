# Fast and Fluent Diffusion Language Models via Convolutional Decoding and Rejective Fine-tuning

**Korean Title:** 빠르고 유창한 확산 언어 모델: 합성곱 디코딩 및 거부적 미세 조정을 통한 접근

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[authors/Yeongbin Seo|Yeongbin Seo]] [[authors/Dongha Lee|Dongha Lee]] [[authors/Jaehyung Kim|Jaehyung Kim]] [[authors/Jinyoung Yeo|Jinyoung Yeo]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Diffusion Language Models

## 🔗 유사한 논문
- [[Hybrid Autoregressive-Diffusion Model for Real-Time Sign Language Production_20250919|Hybrid Autoregressive-Diffusion Model for Real-Time Sign Language Production]] (81.8% similar)
- [[LNE-Blocking_ An Efficient Framework for Contamination Mitigation Evaluation on Large Language Models_20250918|LNE-Blocking An Efficient Framework for Contamination Mitigation Evaluation on Large Language Models]] (81.3% similar)
- [[Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (81.3% similar)
- [[Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (81.1% similar)
- [[Evolving Language Models without Labels_ Majority Drives Selection, Novelty Promotes Variation_20250918|Evolving Language Models without Labels Majority Drives Selection, Novelty Promotes Variation]] (81.1% similar)

## 📋 저자 정보

**Authors:** Yeongbin Seo, Dongha Lee, Jaehyung Kim, Jinyoung Yeo

## 📄 Abstract (원문)

Autoregressive (AR) language models generate text one token at a time, which
limits their inference speed. Diffusion-based language models offer a promising
alternative, as they can decode multiple tokens in parallel. However, we
identify a key bottleneck in current diffusion LMs: the long decoding-window
problem, where tokens generated far from the input context often become
irrelevant or repetitive. Previous solutions like semi-autoregressive address
this issue by splitting windows into blocks, but this sacrifices speed and
bidirectionality, eliminating the main advantage of diffusion models. To
overcome this, we propose Convolutional decoding (Conv), a normalization-based
method that narrows the decoding window without hard segmentation, leading to
better fluency and flexibility. Additionally, we introduce Rejecting Rule-based
Fine-Tuning (R2FT), a post-hoc training scheme that better aligns tokens at
positions far from context. Our methods achieve state-of-the-art results on
open-ended generation benchmarks (e.g., AlpacaEval) among diffusion LM
baselines, with significantly lower step size than previous works,
demonstrating both speed and quality improvements.

## 🔍 Abstract (한글 번역)

자기회귀(AR) 언어 모델은 한 번에 하나의 토큰을 생성하여 추론 속도가 제한됩니다. 반면, 확산 기반 언어 모델은 여러 토큰을 병렬로 디코딩할 수 있어 유망한 대안이 됩니다. 그러나 현재의 확산 언어 모델에서 중요한 병목 현상을 발견했습니다: 긴 디코딩 윈도우 문제로, 입력 컨텍스트에서 멀리 떨어진 위치에서 생성된 토큰이 종종 관련성이 없거나 반복적이게 됩니다. 이전의 해결책인 반자기회귀 방식은 윈도우를 블록으로 나누어 이 문제를 해결하지만, 이는 속도와 양방향성을 희생시켜 확산 모델의 주요 장점을 없애버립니다. 이를 극복하기 위해, 우리는 하드 세분화 없이 디코딩 윈도우를 좁히는 정규화 기반 방법인 컨볼루션 디코딩(Conv)을 제안하여 더 나은 유창성과 유연성을 제공합니다. 추가로, 우리는 컨텍스트에서 멀리 떨어진 위치의 토큰을 더 잘 정렬하는 사후 훈련 방식인 규칙 기반 거부 미세 조정(R2FT)을 도입합니다. 우리의 방법은 확산 언어 모델 기준에서 개방형 생성 벤치마크(예: AlpacaEval)에서 최첨단 결과를 달성하며, 이전 작업보다 훨씬 작은 단계 크기로 속도와 품질 모두에서 개선을 보여줍니다.

## 📝 요약

이 논문은 확산 기반 언어 모델의 디코딩 속도를 개선하기 위한 새로운 방법론을 제안합니다. 기존 확산 모델은 긴 디코딩 윈도우 문제로 인해 입력 문맥에서 멀리 떨어진 토큰이 비관련적이거나 반복되는 문제가 있었습니다. 이를 해결하기 위해 제안된 방법은 컨볼루션 디코딩(Conv)으로, 하드 세분화 없이 디코딩 윈도우를 좁혀 유창성과 유연성을 향상시킵니다. 또한, R2FT라는 후처리 학습 기법을 도입하여 문맥에서 먼 위치의 토큰 정렬을 개선합니다. 이 방법들은 기존 확산 모델 대비 속도와 품질을 향상시키며, AlpacaEval 등 오픈엔드 생성 벤치마크에서 최첨단 성능을 달성했습니다.

## 🎯 주요 포인트

- 1. 확산 기반 언어 모델은 병렬로 여러 토큰을 디코딩할 수 있어 추론 속도에서 유리하다.

- 2. 기존 확산 언어 모델의 주요 병목 현상은 디코딩 윈도우가 길어질 때 발생하는 비관련성 및 반복성 문제이다.

- 3. 제안된 컨볼루션 디코딩(Conv)은 하드 세분화 없이 디코딩 윈도우를 좁혀 유창성과 유연성을 개선한다.

- 4. R2FT는 문맥에서 먼 위치의 토큰 정렬을 개선하는 후처리 학습 방식이다.

- 5. 제안된 방법은 확산 언어 모델 기준으로 최신 성능을 달성하며, 이전 연구보다 적은 스텝 크기로 속도와 품질을 모두 개선한다.

---

*Generated on 2025-09-20 00:53:32*