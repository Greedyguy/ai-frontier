
# EnCoBo: Energy-Guided Concept Bottlenecks for Interpretable Generation

**Korean Title:** 에너지 유도 개념 병목을 통한 해석 가능한 생성: EnCoBo

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Concept Bottleneck Models

## 🔗 유사한 논문
- [[Early_Stopping_Chain-of-thoughts_in_Large_Language_Models_20250918|Early Stopping Chain-of-thoughts in Large Language Models]] (78.7% similar)
- [[Uni-cot Towards Unified Chain-of-Thought Reasoning Across Text and Vision]] (78.5% similar)
- [[Imagined Autocurricula]] (77.4% similar)
- [[MAgICoRe Multi-Agent, Iterative, Coarse-to-Fine Refinement for Reasoning]] (77.1% similar)
- [[From Correction to Mastery Reinforced Distillation of Large Language Model Agents]] (77.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.08334v2 Announce Type: replace-cross 
Abstract: Concept Bottleneck Models (CBMs) provide interpretable decision-making through explicit, human-understandable concepts. However, existing generative CBMs often rely on auxiliary visual cues at the bottleneck, which undermines interpretability and intervention capabilities. We propose EnCoBo, a post-hoc concept bottleneck for generative models that eliminates auxiliary cues by constraining all representations to flow solely through explicit concepts. Unlike autoencoder-based approaches that inherently rely on black-box decoders, EnCoBo leverages a decoder-free, energy-based framework that directly guides generation in the latent space. Guided by diffusion-scheduled energy functions, EnCoBo supports robust post-hoc interventions-such as concept composition and negation-across arbitrary concepts. Experiments on CelebA-HQ and CUB datasets showed that EnCoBo improved concept-level human intervention and interpretability while maintaining competitive visual quality.

## 🔍 Abstract (한글 번역)

arXiv:2507.08334v2 발표 유형: 교체-크로스  
초록: 개념 병목 모델(Concept Bottleneck Models, CBMs)은 명시적이고 인간이 이해할 수 있는 개념을 통해 해석 가능한 의사 결정을 제공합니다. 그러나 기존의 생성적 CBMs는 병목 지점에서 보조적인 시각적 단서에 의존하는 경우가 많아 해석 가능성과 개입 능력을 저해합니다. 우리는 생성 모델을 위한 사후 개념 병목인 EnCoBo를 제안하며, 이는 모든 표현이 명시적인 개념을 통해서만 흐르도록 제한하여 보조 단서를 제거합니다. 블랙박스 디코더에 본질적으로 의존하는 오토인코더 기반 접근 방식과 달리, EnCoBo는 디코더가 없는 에너지 기반 프레임워크를 활용하여 잠재 공간에서 직접 생성을 안내합니다. 확산-스케줄된 에너지 함수에 의해 안내되는 EnCoBo는 임의의 개념에 걸쳐 개념 조합 및 부정과 같은 강력한 사후 개입을 지원합니다. CelebA-HQ 및 CUB 데이터셋에 대한 실험 결과, EnCoBo는 개념 수준의 인간 개입과 해석 가능성을 개선하면서도 경쟁력 있는 시각적 품질을 유지했습니다.

## 📝 요약

이 논문은 해석 가능한 의사결정을 제공하는 개념 병목 모델(CBM)의 한계를 극복하기 위해 EnCoBo라는 새로운 모델을 제안합니다. 기존의 생성적 CBM은 보조 시각적 단서를 사용하여 해석 가능성과 개입 능력을 저해하는 반면, EnCoBo는 모든 표현을 명시적인 개념을 통해 흐르도록 제한하여 이러한 단서를 제거합니다. EnCoBo는 블랙박스 디코더를 사용하는 자동 인코더 기반 접근법과 달리, 디코더가 없는 에너지 기반 프레임워크를 활용하여 잠재 공간에서 직접 생성 과정을 안내합니다. 이 모델은 확산 스케줄링된 에너지 함수를 통해 개념 조합 및 부정과 같은 강력한 사후 개입을 지원합니다. CelebA-HQ와 CUB 데이터셋 실험 결과, EnCoBo는 개념 수준의 인간 개입과 해석 가능성을 향상시키면서도 경쟁력 있는 시각적 품질을 유지했습니다.

## 🎯 주요 포인트

- 1. EnCoBo는 명시적 개념을 통해 모든 표현을 흐르게 하여 보조 시각적 단서를 제거하는 개념 병목 모델입니다.

- 2. EnCoBo는 블랙박스 디코더에 의존하지 않고, 디코더 없는 에너지 기반 프레임워크를 활용하여 잠재 공간에서 직접 생성 과정을 안내합니다.

- 3. EnCoBo는 확산 스케줄 에너지 함수를 통해 개념 조합 및 부정과 같은 강력한 사후 개입을 지원합니다.

- 4. CelebA-HQ와 CUB 데이터셋 실험에서 EnCoBo는 개념 수준의 인간 개입 및 해석 가능성을 개선하면서도 경쟁력 있는 시각적 품질을 유지했습니다.

---

*Generated on 2025-09-19 15:18:39*