
# V-SEAM: Visual Semantic Editing and Attention Modulating for Causal Interpretability of Vision-Language Models

**Korean Title:** V-SEAM: 시각-언어 모델의 인과적 해석 가능성을 위한 시각적 의미 편집 및 주의 조절

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Visual Semantic Editing

## 🔗 유사한 논문
- [[VLM-E2E Enhancing End-to-End Autonomous Driving with Multimodal Driver Attention Fusion]] (85.1% similar)
- [[UnifiedVisual A Framework for Constructing Unified Vision-Language Datasets]] (83.6% similar)
- [[Visible Yet Unreadable A Systematic Blind Spot of Vision Language Models Across Writing Systems]] (83.1% similar)
- [[VSE-MOT Multi-Object Tracking in Low-Quality Video Scenes Guided by Visual Semantic Enhancement]] (82.5% similar)
- [[GeoAware-VLA Implicit Geometry Aware Vision-Language-Action Model]] (82.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14837v1 Announce Type: new 
Abstract: Recent advances in causal interpretability have extended from language models to vision-language models (VLMs), seeking to reveal their internal mechanisms through input interventions. While textual interventions often target semantics, visual interventions typically rely on coarse pixel-level perturbations, limiting semantic insights on multimodal integration. In this study, we introduce V-SEAM, a novel framework that combines Visual Semantic Editing and Attention Modulating for causal interpretation of VLMs. V-SEAM enables concept-level visual manipulations and identifies attention heads with positive or negative contributions to predictions across three semantic levels: objects, attributes, and relationships. We observe that positive heads are often shared within the same semantic level but vary across levels, while negative heads tend to generalize broadly. Finally, we introduce an automatic method to modulate key head embeddings, demonstrating enhanced performance for both LLaVA and InstructBLIP across three diverse VQA benchmarks. Our data and code are released at: https://github.com/petergit1/V-SEAM.

## 🔍 Abstract (한글 번역)

arXiv:2509.14837v1 발표 유형: 신규  
초록: 최근 인과 해석 가능성의 발전은 언어 모델에서 비전-언어 모델(VLMs)로 확장되어 입력 개입을 통해 내부 메커니즘을 밝히려 하고 있습니다. 텍스트 개입은 종종 의미론을 목표로 하지만, 시각적 개입은 일반적으로 거친 픽셀 수준의 변형에 의존하여 다중 모달 통합에 대한 의미론적 통찰을 제한합니다. 본 연구에서는 V-SEAM이라는 새로운 프레임워크를 소개하여 VLMs의 인과 해석을 위한 시각적 의미 편집과 주의 조절을 결합합니다. V-SEAM은 개념 수준의 시각적 조작을 가능하게 하고, 객체, 속성, 관계라는 세 가지 의미 수준에서 예측에 긍정적 또는 부정적 기여를 하는 주의 헤드를 식별합니다. 우리는 긍정적 헤드가 동일한 의미 수준 내에서 종종 공유되지만, 수준 간에는 다르며, 부정적 헤드는 일반적으로 널리 일반화된다는 것을 관찰했습니다. 마지막으로, 주요 헤드 임베딩을 조절하는 자동 방법을 도입하여 LLaVA와 InstructBLIP 모두에 대해 세 가지 다양한 VQA 벤치마크에서 향상된 성능을 입증합니다. 우리의 데이터와 코드는 다음에서 공개됩니다: https://github.com/petergit1/V-SEAM.

## 📝 요약

이 논문은 비전-언어 모델(VLM)의 인과적 해석을 위한 새로운 프레임워크인 V-SEAM을 소개합니다. V-SEAM은 시각적 의미 편집과 주의 조절을 결합하여 VLM의 내부 메커니즘을 분석합니다. 이를 통해 객체, 속성, 관계라는 세 가지 의미 수준에서 개념 수준의 시각적 조작이 가능하며, 예측에 긍정적 또는 부정적 영향을 미치는 주의 헤드를 식별합니다. 연구 결과, 긍정적 주의 헤드는 동일한 의미 수준 내에서 공유되지만, 부정적 주의 헤드는 일반화되는 경향이 있음을 발견했습니다. 또한, 주요 헤드 임베딩을 자동으로 조절하는 방법을 제안하여 LLaVA와 InstructBLIP의 성능을 세 가지 VQA 벤치마크에서 향상시켰습니다. 데이터와 코드는 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 본 연구는 V-SEAM이라는 새로운 프레임워크를 도입하여 VLMs의 인과적 해석을 위한 시각적 의미 편집과 주의 조절을 결합합니다.

- 2. V-SEAM은 개념 수준의 시각적 조작을 가능하게 하고, 예측에 긍정적 또는 부정적 기여를 하는 주의 헤드를 객체, 속성, 관계의 세 가지 의미 수준에서 식별합니다.

- 3. 긍정적 주의 헤드는 동일한 의미 수준 내에서 자주 공유되지만, 수준 간에는 다르게 나타나는 반면, 부정적 주의 헤드는 일반적으로 널리 일반화되는 경향이 있습니다.

- 4. 주요 헤드 임베딩을 조절하는 자동 방법을 도입하여 LLaVA와 InstructBLIP의 세 가지 다양한 VQA 벤치마크에서 성능 향상을 입증했습니다.

- 5. 연구 데이터와 코드는 https://github.com/petergit1/V-SEAM에서 공개됩니다.

---

*Generated on 2025-09-19 15:52:57*