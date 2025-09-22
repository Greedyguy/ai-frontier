# ViSpec: Accelerating Vision-Language Models with Vision-Aware Speculative Decoding

**Korean Title:** ViSpec: 비전 인식 추측 디코딩을 통한 비전-언어 모델 가속화

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Multimodal Coherence|Multimodal Coherence]] [[keywords/specific/Attention Mechanism|Attention Mechanism]] [[keywords/broad/Vision Language Models|Vision Language Models]] [[keywords/broad/Speculative Decoding|Speculative Decoding]] [[keywords/unique/Vision Aware Speculative Decoding|Vision Aware Speculative Decoding]] [[categories/cs.CL|cs.CL]] [[2025-09-22/LLMs Can Compensate for Deficiencies in Visual Representations_20250922|LLMs Can Compensate for Deficiencies in Visual Representations]] (84.9% similar) [[2025-09-22/Distribution-Aligned Decoding for Efficient LLM Task Adaptation_20250922|Distribution-Aligned Decoding for Efficient LLM Task Adaptation]] (84.0% similar) [[2025-09-22/Robust Vision-Language Models via Tensor Decomposition_ A Defense Against Adversarial Attacks_20250922|Robust Vision-Language Models via Tensor Decomposition: A Defense Against Adversarial Attacks]] (83.9% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Multimodal Coherence
**🔗 Specific Connectable**: Attention Mechanism
**🔬 Broad Technical**: Vision Language Models, Speculative Decoding
**⭐ Unique Technical**: Vision Aware Speculative Decoding
## 🔗 유사한 논문
- [[2025-09-22/LLMs Can Compensate for Deficiencies in Visual Representations_20250922|LLMs Can Compensate for Deficiencies in Visual Representations]] (84.9% similar)
- [[2025-09-22/Distribution-Aligned Decoding for Efficient LLM Task Adaptation_20250922|Distribution-Aligned Decoding for Efficient LLM Task Adaptation]] (84.0% similar)
- [[2025-09-22/Robust Vision-Language Models via Tensor Decomposition_ A Defense Against Adversarial Attacks_20250922|Robust Vision-Language Models via Tensor Decomposition A Defense Against Adversarial Attacks]] (83.9% similar)
- [[2025-09-22/CARD_ A Cache-Assisted Parallel Speculative Decoding Framework via Query-and-Correct Paradigm for Accelerating LLM Inference_20250922|CARD A Cache-Assisted Parallel Speculative Decoding Framework via Query-and-Correct Paradigm for Accelerating LLM Inference]] (83.7% similar)
- [[2025-09-19/V-SEAM_ Visual Semantic Editing and Attention Modulating for Causal Interpretability of Vision-Language Models_20250919|V-SEAM Visual Semantic Editing and Attention Modulating for Causal Interpretability of Vision-Language Models]] (83.6% similar)


**ArXiv ID**: [2509.15235](https://arxiv.org/abs/2509.15235)
**Published**: 2025-09-22
**Category**: cs.CL
**PDF**: [Download](https://arxiv.org/pdf/2509.15235.pdf)


**ArXiv ID**: [2509.15235](https://arxiv.org/abs/2509.15235)
**Published**: 2025-09-22
**Category**: cs.CL
**PDF**: [Download](https://arxiv.org/pdf/2509.15235.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Multimodal Coherence
**🔗 Specific Connectable**: Attention Mechanism
**⭐ Unique Technical**: Vision Aware Speculative Decoding
**🔬 Broad Technical**: Vision Language Models, Speculative Decoding

## 🏷️ 추출된 키워드



`Vision Language Models` • 

`Speculative Decoding` • 

`Attention Mechanism` • 

`Vision Aware Speculative Decoding` • 

`Multimodal Coherence`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15235v1 Announce Type: cross 
Abstract: Speculative decoding is a widely adopted technique for accelerating inference in large language models (LLMs), yet its application to vision-language models (VLMs) remains underexplored, with existing methods achieving only modest speedups (<1.5x). This gap is increasingly significant as multimodal capabilities become central to large-scale models. We hypothesize that large VLMs can effectively filter redundant image information layer by layer without compromising textual comprehension, whereas smaller draft models struggle to do so. To address this, we introduce Vision-Aware Speculative Decoding (ViSpec), a novel framework tailored for VLMs. ViSpec employs a lightweight vision adaptor module to compress image tokens into a compact representation, which is seamlessly integrated into the draft model's attention mechanism while preserving original image positional information. Additionally, we extract a global feature vector for each input image and augment all subsequent text tokens with this feature to enhance multimodal coherence. To overcome the scarcity of multimodal datasets with long assistant responses, we curate a specialized training dataset by repurposing existing datasets and generating extended outputs using the target VLM with modified prompts. Our training strategy mitigates the risk of the draft model exploiting direct access to the target model's hidden states, which could otherwise lead to shortcut learning when training solely on target model outputs. Extensive experiments validate ViSpec, achieving, to our knowledge, the first substantial speedup in VLM speculative decoding.

## 🔍 Abstract (한글 번역)

arXiv:2509.15235v1 발표 유형: 교차  
초록: 추론 속도를 높이기 위한 추측 디코딩은 대형 언어 모델(LLM)에서 널리 채택된 기법이지만, 시각-언어 모델(VLM)에 대한 적용은 아직 충분히 탐구되지 않았으며, 기존 방법들은 겨우 1.5배 미만의 속도 향상만을 달성하고 있습니다. 다중 모달 기능이 대규모 모델의 중심이 되면서 이 격차는 점점 더 중요해지고 있습니다. 우리는 대형 VLM이 텍스트 이해를 손상시키지 않으면서 계층별로 중복된 이미지 정보를 효과적으로 필터링할 수 있는 반면, 작은 초안 모델은 그러한 능력이 부족하다고 가정합니다. 이를 해결하기 위해, 우리는 VLM에 특화된 새로운 프레임워크인 Vision-Aware Speculative Decoding (ViSpec)을 소개합니다. ViSpec은 경량의 비전 어댑터 모듈을 사용하여 이미지 토큰을 압축된 표현으로 변환하고, 이를 초안 모델의 주의 메커니즘에 원래의 이미지 위치 정보를 유지하면서 매끄럽게 통합합니다. 또한, 각 입력 이미지에 대한 전역 특징 벡터를 추출하고, 이를 모든 후속 텍스트 토큰에 추가하여 다중 모달 일관성을 향상시킵니다. 긴 보조 응답을 가진 다중 모달 데이터셋의 부족 문제를 해결하기 위해, 기존 데이터셋을 재활용하고 수정된 프롬프트를 사용하여 대상 VLM으로 확장된 출력을 생성함으로써 특화된 훈련 데이터셋을 구성합니다. 우리의 훈련 전략은 초안 모델이 대상 모델의 숨겨진 상태에 직접 접근하여 지름길 학습을 할 위험을 완화하며, 이는 대상 모델 출력만으로 훈련할 경우 발생할 수 있습니다. 광범위한 실험을 통해 ViSpec은 VLM 추측 디코딩에서 최초로 실질적인 속도 향상을 달성했음을 검증합니다.

## 📝 요약

이 논문은 대형 비전-언어 모델(VLM)의 추론 속도를 높이기 위한 새로운 방법론인 Vision-Aware Speculative Decoding(ViSpec)을 제안합니다. 기존의 방법들이 1.5배 미만의 속도 향상에 그친 반면, ViSpec은 이미지 정보를 압축하여 텍스트 이해를 유지하면서도 불필요한 정보를 효과적으로 제거합니다. 이를 위해 경량의 비전 어댑터 모듈을 사용하여 이미지 토큰을 압축하고, 이 정보를 초안 모델의 주의 메커니즘에 통합합니다. 또한, 각 이미지에 대한 전역 특징 벡터를 추출하여 텍스트 토큰에 추가함으로써 다중 모달 일관성을 높입니다. ViSpec은 특별히 구성된 학습 데이터셋을 활용하여 대형 VLM의 숨겨진 상태에 대한 직접 접근을 피하고, 실험을 통해 VLM 추론 속도에서 최초로 유의미한 개선을 달성했습니다.

## 🎯 주요 포인트


- 1. ViSpec는 VLMs에 특화된 새로운 프레임워크로, 경량의 비전 어댑터 모듈을 사용하여 이미지 토큰을 압축된 표현으로 변환합니다.

- 2. ViSpec는 입력 이미지의 글로벌 피처 벡터를 추출하여 모든 텍스트 토큰에 추가함으로써 멀티모달 일관성을 강화합니다.

- 3. ViSpec는 기존 데이터셋을 재활용하고 수정된 프롬프트를 사용하여 확장된 출력을 생성함으로써 멀티모달 데이터셋의 부족 문제를 해결합니다.

- 4. ViSpec는 대규모 VLM의 추론 속도를 실질적으로 향상시켜, VLM 추론에서 최초로 의미 있는 속도 향상을 달성했습니다.

- 5. ViSpec의 훈련 전략은 초안 모델이 목표 모델의 숨겨진 상태에 직접 접근하여 발생할 수 있는 지름길 학습을 방지합니다.


---

*Generated on 2025-09-22 16:30:55*