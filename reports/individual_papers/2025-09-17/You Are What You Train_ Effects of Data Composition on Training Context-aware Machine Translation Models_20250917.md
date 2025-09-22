# You Are What You Train: Effects of Data Composition on Training Context-aware Machine Translation Models

**Korean Title:** 당신은 당신이 훈련한 것: 문맥 인식 기계 번역 모델 훈련에 대한 데이터 구성의 효과

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Paweł Mąka|Paweł Mąka]] [[authors/Yusuf Can Semerci|Yusuf Can Semerci]] [[authors/Jan Scholtes|Jan Scholtes]] [[authors/Gerasimos Spanakis|Gerasimos Spanakis]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Context-aware Training Strategies

## 🔗 유사한 논문
- [[Translate, then Detect_ Leveraging Machine Translation for Cross-Lingual Toxicity Classification_20250919|Translate, then Detect Leveraging Machine Translation for Cross-Lingual Toxicity Classification]] (80.1% similar)
- [[Internalizing Self-Consistency in Language Models_ Multi-Agent Consensus Alignment_20250919|Internalizing Self-Consistency in Language Models Multi-Agent Consensus Alignment]] (79.5% similar)
- [[Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (79.3% similar)
- [[Opening the Black Box_ Interpretable LLMs via Semantic Resonance Architecture_20250919|Opening the Black Box Interpretable LLMs via Semantic Resonance Architecture]] (79.2% similar)
- [[TICL_ Text-Embedding KNN For Speech In-Context Learning Unlocks Speech Recognition Abilities of Large Multimodal Models_20250918|TICL Text-Embedding KNN For Speech In-Context Learning Unlocks Speech Recognition Abilities of Large Multimodal Models]] (79.0% similar)

## 📋 저자 정보

**Authors:** Paweł Mąka, Yusuf Can Semerci, Jan Scholtes, Gerasimos Spanakis

## 📄 Abstract (원문)

Achieving human-level translations requires leveraging context to ensure
coherence and handle complex phenomena like pronoun disambiguation. Sparsity of
contextually rich examples in the standard training data has been hypothesized
as the reason for the difficulty of context utilization. In this work, we
systematically validate this claim in both single- and multilingual settings by
constructing training datasets with a controlled proportions of contextually
relevant examples. We demonstrate a strong association between training data
sparsity and model performance confirming sparsity as a key bottleneck.
Importantly, we reveal that improvements in one contextual phenomenon do no
generalize to others. While we observe some cross-lingual transfer, it is not
significantly higher between languages within the same sub-family. Finally, we
propose and empirically evaluate two training strategies designed to leverage
the available data. These strategies improve context utilization, resulting in
accuracy gains of up to 6 and 8 percentage points on the ctxPro evaluation in
single- and multilingual settings respectively.

## 🔍 Abstract (한글 번역)

인간 수준의 번역을 달성하기 위해서는 맥락을 활용하여 일관성을 보장하고 대명사 해소와 같은 복잡한 현상을 처리해야 합니다. 표준 훈련 데이터에서 맥락적으로 풍부한 예시의 희소성은 맥락 활용의 어려움의 원인으로 가설이 제기되었습니다. 본 연구에서는 단일 및 다국어 환경 모두에서 맥락적으로 관련 있는 예시의 비율을 조절하여 훈련 데이터셋을 구성함으로써 이 주장을 체계적으로 검증합니다. 우리는 훈련 데이터의 희소성과 모델 성능 간의 강한 연관성을 입증하여 희소성이 주요 병목임을 확인합니다. 중요한 것은, 하나의 맥락적 현상에서의 개선이 다른 현상으로 일반화되지 않는다는 점을 밝혀냈습니다. 일부 언어 간 전이가 관찰되었으나, 동일한 하위 계열 내 언어 간에서는 그다지 높지 않았습니다. 마지막으로, 우리는 사용 가능한 데이터를 활용하기 위해 설계된 두 가지 훈련 전략을 제안하고 실증적으로 평가합니다. 이러한 전략은 맥락 활용을 개선하여 단일 및 다국어 환경에서 각각 ctxPro 평가에서 최대 6% 및 8% 포인트의 정확도 향상을 가져옵니다.

## 📝 요약

이 논문은 인간 수준의 번역을 위해 문맥 활용의 중요성을 강조하며, 문맥적으로 풍부한 예시의 부족이 번역 모델의 성능 저하 원인임을 실험적으로 검증합니다. 연구는 단일 및 다국어 환경에서 문맥 관련 예시의 비율을 조절한 훈련 데이터셋을 구축하여, 데이터 희소성과 모델 성능 간의 강한 연관성을 확인했습니다. 또한, 한 문맥 현상의 개선이 다른 현상으로 일반화되지 않음을 밝혔으며, 동일 언어 계열 내에서의 언어 간 전이는 미미했습니다. 마지막으로, 문맥 활용을 개선하기 위한 두 가지 훈련 전략을 제안하고 평가하여, 단일 및 다국어 환경에서 각각 최대 6%와 8%의 정확도 향상을 달성했습니다.

## 🎯 주요 포인트

- 1. 맥락적으로 풍부한 예시의 부족이 번역 모델의 성능 저하의 주요 원인으로 확인되었습니다.

- 2. 단일 언어 및 다국어 설정에서 맥락 활용을 개선하기 위한 두 가지 훈련 전략이 제안되었습니다.

- 3. 제안된 훈련 전략은 단일 언어 및 다국어 설정에서 각각 최대 6%와 8%의 정확도 향상을 가져왔습니다.

- 4. 한 맥락적 현상의 개선이 다른 현상으로 일반화되지 않는다는 점이 밝혀졌습니다.

- 5. 같은 언어 계열 내에서의 교차 언어 전이는 크게 증가하지 않았습니다.

---

*Generated on 2025-09-20 09:16:16*