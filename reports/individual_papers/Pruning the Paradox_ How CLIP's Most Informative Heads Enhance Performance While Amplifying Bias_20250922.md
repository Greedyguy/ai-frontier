# Pruning the Paradox: How CLIP's Most Informative Heads Enhance Performance While Amplifying Bias

**Korean Title:** 패러독스 가지치기: CLIP의 가장 정보가 풍부한 헤드가 성능을 향상시키면서 편향을 증폭시키는 방법

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Vision-Language Understanding

## 🔗 유사한 논문
- [[2025-09-18/Singular Value Few-shot Adaptation of Vision-Language Models_20250918|Singular Value Few-shot Adaptation of Vision-Language Models]] (81.3% similar)
- [[2025-09-18/Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients_20250918|Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients]] (80.3% similar)
- [[2025-09-19/Seeing 3D Through 2D Lenses_ 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification_20250919|Seeing 3D Through 2D Lenses 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification]] (80.0% similar)
- [[2025-09-22/Advances in Multimodal Adaptation and Generalization_ From Traditional Approaches to Foundation Models_20250922|Advances in Multimodal Adaptation and Generalization From Traditional Approaches to Foundation Models]] (79.1% similar)
- [[2025-09-19/V-SEAM_ Visual Semantic Editing and Attention Modulating for Causal Interpretability of Vision-Language Models_20250919|V-SEAM Visual Semantic Editing and Attention Modulating for Causal Interpretability of Vision-Language Models]] (78.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.11103v3 Announce Type: replace-cross 
Abstract: CLIP is one of the most popular foundation models and is heavily used for many vision-language tasks, yet little is known about its inner workings. As CLIP is increasingly deployed in real-world applications, it is becoming even more critical to understand its limitations and embedded social biases to mitigate potentially harmful downstream consequences. However, the question of what internal mechanisms drive both the impressive capabilities as well as problematic shortcomings of CLIP has largely remained unanswered. To bridge this gap, we study the conceptual consistency of text descriptions for attention heads in CLIP-like models. Specifically, we propose Concept Consistency Score (CCS), a novel interpretability metric that measures how consistently individual attention heads in CLIP models align with specific concepts. Our soft-pruning experiments reveal that high CCS heads are critical for preserving model performance, as pruning them leads to a significantly larger performance drop than pruning random or low CCS heads. Notably, we find that high CCS heads capture essential concepts and play a key role in out-of-domain detection, concept-specific reasoning, and video-language understanding. Moreover, we prove that high CCS heads learn spurious correlations which amplify social biases. These results position CCS as a powerful interpretability metric exposing the paradox of performance and social biases in CLIP models.

## 🔍 Abstract (한글 번역)

arXiv:2503.11103v3 발표 유형: 교차 대체  
초록: CLIP은 가장 인기 있는 기초 모델 중 하나로, 많은 시각-언어 작업에 널리 사용되고 있지만, 그 내부 작동 방식에 대해서는 거의 알려져 있지 않습니다. CLIP이 실제 응용 프로그램에 점점 더 많이 배포됨에 따라, 잠재적으로 해로운 하위 결과를 완화하기 위해 그 한계와 내재된 사회적 편견을 이해하는 것이 더욱 중요해지고 있습니다. 그러나 CLIP의 인상적인 능력과 문제 있는 단점 모두를 이끄는 내부 메커니즘에 대한 질문은 대체로 답변되지 않은 상태로 남아 있습니다. 이 격차를 해소하기 위해, 우리는 CLIP 유사 모델에서 주의 헤드에 대한 텍스트 설명의 개념적 일관성을 연구합니다. 구체적으로, 우리는 CLIP 모델의 개별 주의 헤드가 특정 개념과 얼마나 일관되게 정렬되는지를 측정하는 새로운 해석 가능성 지표인 개념 일관성 점수(Concept Consistency Score, CCS)를 제안합니다. 우리의 소프트-프루닝 실험은 높은 CCS 헤드가 모델 성능을 유지하는 데 중요하다는 것을 보여줍니다. 왜냐하면 이를 제거하면 무작위 또는 낮은 CCS 헤드를 제거하는 것보다 성능 저하가 훨씬 크기 때문입니다. 특히, 우리는 높은 CCS 헤드가 필수 개념을 포착하고, 도메인 외 탐지, 개념별 추론, 비디오-언어 이해에서 중요한 역할을 한다는 것을 발견했습니다. 더욱이, 우리는 높은 CCS 헤드가 사회적 편견을 증폭시키는 가짜 상관관계를 학습한다는 것을 증명합니다. 이러한 결과는 CCS를 CLIP 모델에서 성능과 사회적 편견의 역설을 드러내는 강력한 해석 가능성 지표로 위치시킵니다.

## 📝 요약

이 논문은 CLIP 모델의 내부 작동 방식을 이해하기 위해 새로운 해석 가능성 지표인 개념 일관성 점수(CCS)를 제안합니다. CCS는 CLIP 모델의 주의 헤드가 특정 개념과 얼마나 일관되게 정렬되는지를 측정합니다. 연구 결과, 높은 CCS를 가진 헤드는 모델 성능 유지에 중요하며, 이들을 제거하면 성능이 크게 저하됩니다. 또한, 이러한 헤드는 도메인 외 탐지, 개념별 추론, 비디오-언어 이해에 중요한 역할을 하지만, 사회적 편향을 증폭시키는 잘못된 상관관계를 학습하기도 합니다. CCS는 CLIP 모델의 성능과 사회적 편향 간의 모순을 드러내는 강력한 해석 가능성 지표로 자리매김합니다.

## 🎯 주요 포인트

- 1. CLIP 모델의 내부 작동 원리에 대한 이해가 부족하며, 이를 보완하기 위해 Concept Consistency Score(CCS)라는 새로운 해석 가능성 지표를 제안합니다.

- 2. CCS는 CLIP 모델의 개별 어텐션 헤드가 특정 개념과 얼마나 일관되게 정렬되는지를 측정하는 지표입니다.

- 3. 높은 CCS를 가진 어텐션 헤드는 모델 성능 유지에 중요하며, 이들을 제거하면 성능이 크게 감소합니다.

- 4. 높은 CCS 헤드는 필수 개념을 포착하고, 도메인 외 탐지, 개념별 추론, 비디오-언어 이해에 중요한 역할을 합니다.

- 5. 높은 CCS 헤드는 사회적 편향을 증폭시키는 잘못된 상관관계를 학습하며, 이는 CLIP 모델의 성능과 사회적 편향의 역설을 드러냅니다.

---

*Generated on 2025-09-22 14:44:12*