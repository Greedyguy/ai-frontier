# Two Is Better Than One: Aligned Representation Pairs for Anomaly Detection

**Korean Title:** 두 개가 하나보다 낫다: 이상 탐지를 위한 정렬된 표현 쌍

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Context Contrasting, Content Alignment

## 🔗 유사한 논문
- [[2025-09-17/Consistent View Alignment Improves Foundation Models for 3D Medical Image Segmentation_20250917|Consistent View Alignment Improves Foundation Models for 3D Medical Image Segmentation]] (82.5% similar)
- [[2025-09-22/Self-Supervised Cross-Modal Learning for Image-to-Point Cloud Registration_20250922|Self-Supervised Cross-Modal Learning for Image-to-Point Cloud Registration]] (80.9% similar)
- [[2025-09-19/Superpose Task-specific Features for Model Merging_20250919|Superpose Task-specific Features for Model Merging]] (80.3% similar)
- [[2025-09-19/Seeing 3D Through 2D Lenses_ 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification_20250919|Seeing 3D Through 2D Lenses 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification]] (80.2% similar)
- [[2025-09-22/Region-Aware Deformable Convolutions_20250922|Region-Aware Deformable Convolutions]] (79.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2405.18848v3 Announce Type: replace-cross 
Abstract: Anomaly detection focuses on identifying samples that deviate from the norm. Discovering informative representations of normal samples is crucial to detecting anomalies effectively. Recent self-supervised methods have successfully learned such representations by employing prior knowledge about anomalies to create synthetic outliers during training. However, we often do not know what to expect from unseen data in specialized real-world applications. In this work, we address this limitation with our new approach Con$_2$, which leverages prior knowledge about symmetries in normal samples to observe the data in different contexts. Con$_2$ consists of two parts: Context Contrasting clusters representations according to their context, while Content Alignment encourages the model to capture semantic information by aligning the positions of normal samples across clusters. The resulting representation space allows us to detect anomalies as outliers of the learned context clusters. We demonstrate the benefit of this approach in extensive experiments on specialized medical datasets, outperforming competitive baselines based on self-supervised learning and pretrained models and presenting competitive performance on natural imaging benchmarks.

## 🔍 Abstract (한글 번역)

arXiv:2405.18848v3 발표 유형: 교차 교체  
초록: 이상 탐지는 표준에서 벗어난 샘플을 식별하는 데 중점을 둡니다. 정상 샘플의 유용한 표현을 발견하는 것은 이상을 효과적으로 감지하는 데 중요합니다. 최근의 자기 지도 학습 방법은 훈련 중에 합성 이상치를 생성하기 위해 이상에 대한 사전 지식을 활용하여 이러한 표현을 성공적으로 학습했습니다. 그러나 특수한 실제 응용 분야에서는 보이지 않는 데이터에서 무엇을 기대해야 할지 모르는 경우가 많습니다. 이 연구에서는 정상 샘플의 대칭성에 대한 사전 지식을 활용하여 데이터를 다양한 맥락에서 관찰하는 새로운 접근 방식 Con$_2$로 이 한계를 해결합니다. Con$_2$는 두 부분으로 구성됩니다: Context Contrasting는 맥락에 따라 표현을 클러스터링하고, Content Alignment는 정상 샘플의 위치를 클러스터 간에 정렬하여 모델이 의미론적 정보를 포착하도록 장려합니다. 결과적으로 생성된 표현 공간은 학습된 맥락 클러스터의 이상치로서 이상을 감지할 수 있게 합니다. 우리는 특수 의료 데이터셋에 대한 광범위한 실험에서 이 접근 방식의 이점을 입증하며, 자기 지도 학습 및 사전 학습된 모델을 기반으로 하는 경쟁적인 기준선을 능가하고 자연 이미지 벤치마크에서 경쟁력 있는 성능을 보여줍니다.

## 📝 요약

이 논문은 이상 탐지 분야에서 새로운 접근법인 Con$_2$를 제안합니다. Con$_2$는 정상 샘플의 대칭성을 활용하여 다양한 문맥에서 데이터를 관찰함으로써 이상 탐지를 개선합니다. 이 방법은 두 가지 구성 요소로 이루어져 있습니다. 첫째, Context Contrasting는 문맥에 따라 표현을 클러스터링하고, 둘째, Content Alignment는 정상 샘플의 위치를 클러스터 간에 정렬하여 의미 정보를 포착하도록 합니다. 이로 인해 학습된 문맥 클러스터의 외부에 위치한 샘플을 이상치로 탐지할 수 있습니다. 제안된 방법은 전문적인 의료 데이터셋에서 기존의 자가 지도 학습 및 사전 학습 모델 기반의 경쟁 방법들을 능가하는 성능을 보였으며, 자연 이미지 벤치마크에서도 경쟁력 있는 성능을 입증했습니다.

## 🎯 주요 포인트

- 1. 이상 탐지는 정상 샘플의 정보 표현을 발견하는 것이 중요하며, Con$_2$는 정상 샘플의 대칭성에 대한 사전 지식을 활용하여 데이터를 다양한 맥락에서 관찰합니다.

- 2. Con$_2$는 맥락 대비(Context Contrasting)와 콘텐츠 정렬(Content Alignment)을 통해 정상 샘플의 위치를 클러스터 간에 정렬하여 의미 있는 정보를 포착하도록 모델을 유도합니다.

- 3. 이 접근법은 학습된 맥락 클러스터의 이상치로서 이상을 감지할 수 있는 표현 공간을 제공합니다.

- 4. Con$_2$는 전문 의료 데이터셋에서의 실험을 통해 경쟁력 있는 성능을 보이며, 자가 지도 학습 및 사전 학습된 모델 기반의 경쟁 베이스라인을 능가합니다.

- 5. 자연 이미지 벤치마크에서도 경쟁력 있는 성능을 나타냅니다.

---

*Generated on 2025-09-22 14:35:58*