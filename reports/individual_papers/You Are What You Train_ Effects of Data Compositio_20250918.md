
# You Are What You Train: Effects of Data Composition on Training Context-aware Machine Translation Models

**Korean Title:** 당신은 당신이 훈련하는 대로 됩니다: 데이터 구성이 훈련에 미치는 영향 - 문맥 인식 기계 번역 모델에 대한 연구

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Cross-lingual Transfer|Cross-lingual Transfer]] [[keywords/broad/Context-aware Machine Translation|Context-aware Machine Translation]] [[keywords/broad/Training Data Sparsity|Training Data Sparsity]] [[keywords/specific/Pronoun Disambiguation|Pronoun Disambiguation]] [[keywords/unique/ctxPro|ctxPro]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Cross-lingual Transfer
**🔬 Broad Technical**: Context-aware Machine Translation Models, Training Datasets
**🔗 Specific Connectable**: Pronoun Disambiguation
**⭐ Unique Technical**: ctxPro

**ArXiv ID**: [2509.14031](https://arxiv.org/abs/2509.14031)
**Published**: 2025-09-18
**Category**: cs.AI
**PDF**: [Download](https://arxiv.org/pdf/2509.14031.pdf)


## 🏷️ 추출된 키워드



`Context-aware Machine Translation` • 

`Training Data Sparsity` • 

`Pronoun Disambiguation` • 

`ctxPro` • 

`Cross-lingual Transfer`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14031v1 Announce Type: cross 
Abstract: Achieving human-level translations requires leveraging context to ensure coherence and handle complex phenomena like pronoun disambiguation. Sparsity of contextually rich examples in the standard training data has been hypothesized as the reason for the difficulty of context utilization. In this work, we systematically validate this claim in both single- and multilingual settings by constructing training datasets with a controlled proportions of contextually relevant examples. We demonstrate a strong association between training data sparsity and model performance confirming sparsity as a key bottleneck. Importantly, we reveal that improvements in one contextual phenomenon do no generalize to others. While we observe some cross-lingual transfer, it is not significantly higher between languages within the same sub-family. Finally, we propose and empirically evaluate two training strategies designed to leverage the available data. These strategies improve context utilization, resulting in accuracy gains of up to 6 and 8 percentage points on the ctxPro evaluation in single- and multilingual settings respectively.

## 🔍 Abstract (한글 번역)

arXiv:2509.14031v1 발표 유형: 교차
요약: 인간 수준의 번역을 달성하기 위해서는 맥락을 활용하여 일관성을 보장하고 대명사 모호성과 같은 복잡한 현상을 처리해야 합니다. 표준 교육 데이터에서 맥락이 풍부한 예제의 희소성이 맥락 활용의 어려움의 이유로 추측되었습니다. 본 연구에서는 맥락적으로 관련된 예제의 비율을 제어하여 교육 데이터 세트를 구축함으로써 이 주장을 단일 및 다국어 환경에서 체계적으로 검증합니다. 교육 데이터의 희소성과 모델 성능 사이에 강한 연관성을 보여 희소성을 주요 병목 현상으로 확인합니다. 중요한 점은 한 가지 맥락적 현상의 개선이 다른 현상으로 일반화되지 않는다는 것을 밝혀냅니다. 우리는 일부 교차 언어 전이를 관찰하지만, 동일한 하위 패밀리 내의 언어 간에는 유의미하게 높지 않습니다. 마지막으로, 사용 가능한 데이터를 활용하기 위해 설계된 두 가지 교육 전략을 제안하고 경험적으로 평가합니다. 이러한 전략은 맥락 활용을 개선하여 단일 및 다국어 환경에서 각각 ctxPro 평가에서 6 및 8 퍼센트 포인트의 정확도 향상을 가져옵니다.

## 📝 요약

이 연구는 인간 수준의 번역을 달성하기 위해 맥락을 활용하여 일관성을 유지하고 대명사 모호성과 같은 복잡한 현상을 처리해야 한다는 점을 강조한다. 표준 훈련 데이터에서 맥락이 풍부한 예제의 희소성이 맥락 활용의 어려움의 이유로 제기되었다. 이 연구에서는 훈련 데이터셋을 구성하여 맥락적으로 관련 있는 예제의 비율을 조절하여 이 주장을 단일 및 다국어 설정에서 체계적으로 검증한다. 훈련 데이터의 희소성과 모델 성능 사이에 강한 관련성을 입증하여 희소성을 주요 병목 현상으로 확인한다. 또한, 한 가지 맥락적 현상의 개선이 다른 현상으로 일반화되지 않음을 밝힌다. 동일 부문 내 언어 간의 교차언어 전이는 일부 관찰되지만 유의미하게 높지 않다. 마지막으로, 사용 가능한 데이터를 활용하기 위해 설계된 두 가지 훈련 전략을 제안하고 경험적으로 평가한다. 이러한 전략은 맥락 활용을 개선하여 단일 및 다국어 설정에서 ctxPro 평가에서 최대 6~8%의 정확도 향상을 이끌어냈다.

## 🎯 주요 포인트


- 인간 수준의 번역을 달성하기 위해서는 맥락을 활용하여 일관성을 유지하고 대명사 모호성과 같은 복잡한 현상을 처리해야 함

- 훈련 데이터의 맥락이 부족한 것이 맥락 활용의 어려움의 이유로 제시됨

- 훈련 데이터의 희소성과 모델 성능 사이에 강한 연관성이 있음을 확인하며, 희소성이 주요 병목 현상임을 확인함

- 맥락적 현상 중 하나의 개선이 다른 현상으로 일반화되지 않음을 밝히며, 일부 언어 간의 교차 언어 전이를 관찰함

- 사용 가능한 데이터를 활용하기 위해 두 가지 훈련 전략을 제안하고 실험적으로 평가함, 이로 인해 단일 및 다중 언어 설정에서 ctxPro 평가에서 정확도 향상이 발생함 (최대 6~8%포인트)


---

*Generated on 2025-09-18 16:24:48*