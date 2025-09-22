# Robust Vision-Language Models via Tensor Decomposition: A Defense Against Adversarial Attacks

**Korean Title:** 텐서 분해를 통한 견고한 비전-언어 모델: 적대적 공격에 대한 방어

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Vision-Language Robustness

## 🔗 유사한 논문
- [[2025-09-22/ORCA_ Agentic Reasoning For Hallucination and Adversarial Robustness in Vision-Language Models_20250922|ORCA Agentic Reasoning For Hallucination and Adversarial Robustness in Vision-Language Models]] (84.6% similar)
- [[2025-09-18/Singular Value Few-shot Adaptation of Vision-Language Models_20250918|Singular Value Few-shot Adaptation of Vision-Language Models]] (83.9% similar)
- [[2025-09-19/Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (82.3% similar)
- [[2025-09-19/V-SEAM_ Visual Semantic Editing and Attention Modulating for Causal Interpretability of Vision-Language Models_20250919|V-SEAM Visual Semantic Editing and Attention Modulating for Causal Interpretability of Vision-Language Models]] (82.1% similar)
- [[2025-09-19/UnifiedVisual_ A Framework for Constructing Unified Vision-Language Datasets_20250919|UnifiedVisual A Framework for Constructing Unified Vision-Language Datasets]] (82.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16163v1 Announce Type: cross 
Abstract: Vision language models (VLMs) excel in multimodal understanding but are prone to adversarial attacks. Existing defenses often demand costly retraining or significant architecture changes. We introduce a lightweight defense using tensor decomposition suitable for any pre-trained VLM, requiring no retraining. By decomposing and reconstructing vision encoder representations, it filters adversarial noise while preserving meaning. Experiments with CLIP on COCO and Flickr30K show improved robustness. On Flickr30K, it restores 12.3\% performance lost to attacks, raising Recall@1 accuracy from 7.5\% to 19.8\%. On COCO, it recovers 8.1\% performance, improving accuracy from 3.8\% to 11.9\%. Analysis shows Tensor Train decomposition with low rank (8-32) and low residual strength ($\alpha=0.1-0.2$) is optimal. This method is a practical, plug-and-play solution with minimal overhead for existing VLMs.

## 🔍 Abstract (한글 번역)

arXiv:2509.16163v1 발표 유형: 교차  
초록: 비전 언어 모델(VLMs)은 다중 모달 이해에서 뛰어나지만, 적대적 공격에 취약합니다. 기존의 방어 방법은 종종 비용이 많이 드는 재훈련이나 상당한 구조 변경을 요구합니다. 우리는 사전 훈련된 VLM에 적합하고 재훈련이 필요 없는 텐서 분해를 사용한 경량 방어 방법을 소개합니다. 비전 인코더 표현을 분해하고 재구성함으로써, 의미를 보존하면서 적대적 노이즈를 필터링합니다. COCO와 Flickr30K에서 CLIP을 사용한 실험은 향상된 견고성을 보여줍니다. Flickr30K에서는 공격으로 인해 손실된 성능의 12.3%를 복구하여 Recall@1 정확도를 7.5%에서 19.8%로 향상시켰습니다. COCO에서는 8.1%의 성능을 회복하여 정확도를 3.8%에서 11.9%로 개선했습니다. 분석 결과, 낮은 랭크(8-32)와 낮은 잔여 강도($\alpha=0.1-0.2$)를 가진 텐서 트레인 분해가 최적임을 보여줍니다. 이 방법은 기존 VLM에 최소한의 오버헤드로 적용 가능한 실용적이고 플러그 앤 플레이 솔루션입니다.

## 📝 요약

이 논문은 비전 언어 모델(VLM)의 적대적 공격에 대한 경량 방어 방법을 제안합니다. 기존 방어법은 재훈련이나 아키텍처 변경이 필요하지만, 이 방법은 텐서 분해를 활용하여 사전 훈련된 VLM에 적용 가능하며 재훈련이 필요 없습니다. 비전 인코더 표현을 분해하고 재구성하여 적대적 노이즈를 걸러내면서 의미를 보존합니다. CLIP 모델을 COCO와 Flickr30K 데이터셋에서 실험한 결과, Flickr30K에서 공격으로 인한 성능 손실을 12.3% 회복하여 Recall@1 정확도를 7.5%에서 19.8%로, COCO에서는 8.1% 회복하여 정확도를 3.8%에서 11.9%로 향상시켰습니다. 최적의 성능은 낮은 랭크(8-32)와 낮은 잔여 강도($\alpha=0.1-0.2$)의 텐서 트레인 분해로 달성되었습니다. 이 방법은 기존 VLM에 최소한의 오버헤드로 적용 가능한 실용적인 솔루션입니다.

## 🎯 주요 포인트

- 1. 비전 언어 모델(VLM)은 멀티모달 이해에서 뛰어나지만 적대적 공격에 취약하다.

- 2. 기존 방어 기법은 비용이 많이 드는 재훈련이나 아키텍처 변경을 요구한다.

- 3. 텐서 분해를 활용한 경량 방어 기법을 제안하며, 이는 사전 훈련된 VLM에 적용 가능하고 재훈련이 필요 없다.

- 4. CLIP을 사용한 실험에서 COCO와 Flickr30K 데이터셋에서의 강인성이 향상되었다.

- 5. 제안된 방법은 기존 VLM에 최소한의 오버헤드로 적용 가능한 실용적인 플러그 앤 플레이 솔루션이다.

---

*Generated on 2025-09-22 14:25:47*