# Cache-of-Thought: Master-Apprentice Framework for Cost-Effective Vision Language Model Reasoning

**Korean Title:** "생각의 캐시: 비용 효율적인 비전 언어 모델 추론을 위한 마스터-견습생 프레임워크"

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Master Apprentice Framework|Master Apprentice Framework]] [[keywords/specific/Multimodal Retrieval|Multimodal Retrieval]] [[keywords/specific/In-context Learning|In-context Learning]] [[keywords/broad/Vision Language Models|Vision Language Models]] [[keywords/unique/Cache of Thought|Cache of Thought]] [[categories/cs.LG|cs.LG]] [[2025-09-18/Uni-cot_ Towards Unified Chain-of-Thought Reasoning Across Text and Vision_20250918|Uni-cot: Towards Unified Chain-of-Thought Reasoning Across Text and Vision]] (85.6% similar) [[2025-09-19/ThinkAct_ Vision-Language-Action Reasoning via Reinforced Visual Latent Planning_20250919|ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning]] (84.3% similar) [[2025-09-18/Early Stopping Chain-of-thoughts in Large Language Models_20250918|Early Stopping Chain-of-thoughts in Large Language Models]] (84.1% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Master Apprentice Framework
**🔗 Specific Connectable**: Multimodal Retrieval, In-context Learning
**🔬 Broad Technical**: Vision Language Models
**⭐ Unique Technical**: Cache of Thought
## 🔗 유사한 논문
- [[2025-09-18/Uni-cot_ Towards Unified Chain-of-Thought Reasoning Across Text and Vision_20250918|Uni-cot Towards Unified Chain-of-Thought Reasoning Across Text and Vision]] (85.6% similar)
- [[2025-09-19/ThinkAct_ Vision-Language-Action Reasoning via Reinforced Visual Latent Planning_20250919|ThinkAct Vision-Language-Action Reasoning via Reinforced Visual Latent Planning]] (84.3% similar)
- [[2025-09-18/Early Stopping Chain-of-thoughts in Large Language Models_20250918|Early Stopping Chain-of-thoughts in Large Language Models]] (84.1% similar)
- [[2025-09-22/ORCA_ Agentic Reasoning For Hallucination and Adversarial Robustness in Vision-Language Models_20250922|ORCA Agentic Reasoning For Hallucination and Adversarial Robustness in Vision-Language Models]] (84.1% similar)
- [[2025-09-19/ASCoT_ An Adaptive Self-Correction Chain-of-Thought Method for Late-Stage Fragility in LLMs_20250919|ASCoT An Adaptive Self-Correction Chain-of-Thought Method for Late-Stage Fragility in LLMs]] (83.9% similar)


**ArXiv ID**: [2502.20587](https://arxiv.org/abs/2502.20587)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2502.20587.pdf)


**ArXiv ID**: [2502.20587](https://arxiv.org/abs/2502.20587)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2502.20587.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Master Apprentice Framework
**🔗 Specific Connectable**: In-context Learning, Multimodal Retrieval
**⭐ Unique Technical**: Cache of Thought
**🔬 Broad Technical**: Vision Language Models

## 🏷️ 추출된 키워드



`Vision Language Models` • 

`Multimodal Retrieval` • 

`In-context Learning` • 

`Cache of Thought` • 

`Master Apprentice Framework`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.20587v2 Announce Type: replace 
Abstract: Vision Language Models (VLMs) have achieved remarkable success in a wide range of vision applications of increasing complexity and scales, yet choosing the right VLM model size involves a trade-off between response quality and cost. While smaller VLMs are cheaper to run, they typically produce responses only marginally better than random guessing on benchmarks such as MMMU.
  In this paper, we propose Cache of Thought (CoT), a master apprentice framework for collaborative inference between large and small VLMs. CoT manages high quality query results from large VLMs (master) in a cache, which are then selected via a novel multi modal retrieval and in-context learning to aid the performance of small VLMs (apprentice). We extensively evaluate CoT on various widely recognized and challenging general reasoning benchmarks, and show that CoT increases overall reasoning performance by up to 7.7% under the same budget, and specifically boosts the performance of apprentice VLMs by up to 36.6%. Our code is available at https://github.com/UIUC-MONET/Cache-of-Thoughts

## 🔍 Abstract (한글 번역)

arXiv:2502.20587v2 발표 유형: 교체  
초록: 비전 언어 모델(Vision Language Models, VLMs)은 점점 더 복잡하고 규모가 커지는 다양한 비전 응용 분야에서 놀라운 성공을 거두었지만, 적절한 VLM 모델 크기를 선택하는 것은 응답 품질과 비용 간의 균형을 요구합니다. 작은 VLM은 실행 비용이 저렴하지만, 일반적으로 MMMU와 같은 벤치마크에서 무작위 추측보다 약간 더 나은 응답을 생성합니다.  
이 논문에서는 대형 및 소형 VLM 간의 협력적 추론을 위한 마스터 견습생 프레임워크인 Cache of Thought (CoT)를 제안합니다. CoT는 대형 VLM(마스터)에서 높은 품질의 쿼리 결과를 캐시에 관리하고, 이를 새로운 다중 모달 검색 및 컨텍스트 내 학습을 통해 선택하여 소형 VLM(견습생)의 성능을 지원합니다. 우리는 다양한 널리 인정받는 도전적인 일반 추론 벤치마크에서 CoT를 광범위하게 평가하였으며, CoT가 동일한 예산 하에서 전체 추론 성능을 최대 7.7% 향상시키고, 특히 견습생 VLM의 성능을 최대 36.6% 향상시킴을 보여줍니다. 우리의 코드는 https://github.com/UIUC-MONET/Cache-of-Thoughts에서 이용할 수 있습니다.

## 📝 요약

이 논문은 Vision Language Models(VLMs)의 효율적인 활용을 위해 Cache of Thought(CoT)라는 마스터-견습생 프레임워크를 제안합니다. CoT는 대형 VLM(마스터)의 고품질 쿼리 결과를 캐시에 저장하고, 이를 소형 VLM(견습생)의 성능 향상을 위해 활용합니다. 다중 모달 검색 및 맥락 내 학습을 통해 소형 VLM의 성능을 최대 36.6% 향상시키며, 동일한 예산 내에서 전체 추론 성능을 최대 7.7% 개선합니다. 이 연구는 다양한 일반 추론 벤치마크에서 CoT의 효과를 입증했습니다.

## 🎯 주요 포인트


- 1. Vision Language Models(VLMs)는 다양한 비전 응용 분야에서 성공을 거두었지만, 모델 크기 선택 시 응답 품질과 비용 간의 균형이 필요합니다.

- 2. Cache of Thought(CoT)는 대형 VLM(마스터)과 소형 VLM(견습생) 간의 협력 추론을 위한 프레임워크로, 대형 VLM의 고품질 쿼리 결과를 캐시에 저장하여 소형 VLM의 성능을 향상시킵니다.

- 3. CoT는 다양한 일반 추론 벤치마크에서 최대 7.7%의 성능 향상을 보여주며, 특히 견습생 VLM의 성능을 최대 36.6%까지 향상시킵니다.

- 4. CoT는 새로운 멀티 모달 검색 및 컨텍스트 학습을 통해 소형 VLM의 성능을 지원합니다.

- 5. CoT의 코드는 https://github.com/UIUC-MONET/Cache-of-Thoughts 에서 제공됩니다.


---

*Generated on 2025-09-22 15:55:10*