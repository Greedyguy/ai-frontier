# Sparse-Autoencoder-Guided Internal Representation Unlearning for Large Language Models

**Korean Title:** 희소 오토인코더 기반 내부 표현 학습 제거 기법을 활용한 대형 언어 모델 연구

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.LG|cs.LG]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Activation Alignment

## 🔗 유사한 논문
- [[2025-09-18/Reveal and Release_ Iterative LLM Unlearning with Self-generated Data_20250918|Reveal and Release Iterative LLM Unlearning with Self-generated Data]] (90.1% similar)
- [[2025-09-22/Concept Unlearning in Large Language Models via Self-Constructed Knowledge Triplets_20250922|Concept Unlearning in Large Language Models via Self-Constructed Knowledge Triplets]] (88.1% similar)
- [[2025-09-17/Scrub It Out! Erasing Sensitive Memorization in Code Language Models via Machine Unlearning_20250917|Scrub It Out! Erasing Sensitive Memorization in Code Language Models via Machine Unlearning]] (84.9% similar)
- [[2025-09-19/Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (84.1% similar)
- [[2025-09-22/Do Retrieval Augmented Language Models Know When They Don't Know_20250922|Do Retrieval Augmented Language Models Know When They Don't Know]] (83.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15631v1 Announce Type: cross 
Abstract: As large language models (LLMs) are increasingly deployed across various applications, privacy and copyright concerns have heightened the need for more effective LLM unlearning techniques. Many existing unlearning methods aim to suppress undesirable outputs through additional training (e.g., gradient ascent), which reduces the probability of generating such outputs. While such suppression-based approaches can control model outputs, they may not eliminate the underlying knowledge embedded in the model's internal activations; muting a response is not the same as forgetting it. Moreover, such suppression-based methods often suffer from model collapse. To address these issues, we propose a novel unlearning method that directly intervenes in the model's internal activations. In our formulation, forgetting is defined as a state in which the activation of a forgotten target is indistinguishable from that of ``unknown'' entities. Our method introduces an unlearning objective that modifies the activation of the target entity away from those of known entities and toward those of unknown entities in a sparse autoencoder latent space. By aligning the target's internal activation with those of unknown entities, we shift the model's recognition of the target entity from ``known'' to ``unknown'', achieving genuine forgetting while avoiding over-suppression and model collapse. Empirically, we show that our method effectively aligns the internal activations of the forgotten target, a result that the suppression-based approaches do not reliably achieve. Additionally, our method effectively reduces the model's recall of target knowledge in question-answering tasks without significant damage to the non-target knowledge.

## 🔍 Abstract (한글 번역)

arXiv:2509.15631v1 발표 유형: 교차  
초록: 대형 언어 모델(LLM)이 다양한 애플리케이션에 점점 더 많이 배포됨에 따라, 프라이버시와 저작권 문제로 인해 보다 효과적인 LLM 잊기 기법의 필요성이 높아지고 있습니다. 기존의 많은 잊기 방법은 추가적인 훈련(예: 기울기 상승)을 통해 바람직하지 않은 출력을 억제하는 것을 목표로 하며, 이는 그러한 출력을 생성할 확률을 줄입니다. 이러한 억제 기반 접근 방식은 모델 출력을 제어할 수 있지만, 모델의 내부 활성화에 내재된 기본 지식을 제거하지는 못할 수 있습니다. 응답을 무음 처리하는 것은 그것을 잊는 것과 동일하지 않습니다. 게다가, 이러한 억제 기반 방법은 종종 모델 붕괴를 겪습니다. 이러한 문제를 해결하기 위해, 우리는 모델의 내부 활성화에 직접 개입하는 새로운 잊기 방법을 제안합니다. 우리의 공식화에서, 잊기는 잊혀진 대상의 활성화가 "알려지지 않은" 엔티티와 구별할 수 없는 상태로 정의됩니다. 우리의 방법은 희소 오토인코더 잠재 공간에서 알려진 엔티티의 활성화와 알려지지 않은 엔티티의 활성화 사이로 대상 엔티티의 활성화를 수정하는 잊기 목표를 도입합니다. 대상의 내부 활성화를 알려지지 않은 엔티티의 활성화와 일치시킴으로써, 우리는 모델이 대상 엔티티를 "알려진" 상태에서 "알려지지 않은" 상태로 인식하도록 전환하여 과도한 억제와 모델 붕괴를 피하면서 진정한 잊기를 달성합니다. 실증적으로, 우리는 우리의 방법이 잊혀진 대상의 내부 활성화를 효과적으로 정렬한다는 것을 보여주며, 이는 억제 기반 접근 방식이 신뢰성 있게 달성하지 못하는 결과입니다. 또한, 우리의 방법은 비대상 지식에 큰 손상을 주지 않고 질문-응답 작업에서 대상 지식의 회상을 효과적으로 줄입니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)에서의 효과적인 '잊기' 기술을 제안합니다. 기존의 억제 기반 방법들은 모델 출력만을 통제할 수 있어 근본적인 지식을 제거하지 못하고 모델 붕괴의 위험이 있습니다. 이를 해결하기 위해, 본 연구는 모델의 내부 활성화에 직접 개입하는 새로운 방법론을 제안합니다. 이 방법은 잊고자 하는 대상의 활성화를 '알려진' 엔티티에서 '알 수 없는' 엔티티로 이동시켜 진정한 잊기를 달성합니다. 실험 결과, 제안된 방법은 억제 기반 접근법보다 효과적으로 대상 지식을 잊게 하며, 비대상 지식에 큰 손상을 주지 않고도 질문-응답 작업에서 모델의 기억을 감소시킵니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)의 프라이버시 및 저작권 문제로 인해 효과적인 LLM 망각 기술의 필요성이 증가하고 있습니다.

- 2. 기존의 억제 기반 방법은 모델 출력 제어에는 효과적이지만, 모델의 내부 활성화에 내재된 지식을 제거하지 못하며 모델 붕괴 문제를 겪습니다.

- 3. 제안된 새로운 망각 방법은 모델의 내부 활성화에 직접 개입하여, 잊혀질 대상의 활성화를 알려지지 않은 엔티티와 구별할 수 없도록 조정합니다.

- 4. 이 방법은 억제 기반 접근법이 신뢰성 있게 달성하지 못하는 잊혀질 대상의 내부 활성화를 효과적으로 정렬합니다.

- 5. 제안된 방법은 비대상 지식에 큰 손상을 주지 않으면서 질문-응답 작업에서 대상 지식의 회상을 효과적으로 줄입니다.

---

*Generated on 2025-09-22 15:41:00*