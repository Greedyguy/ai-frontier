# Improving Anomalous Sound Detection with Attribute-aware Representation from Domain-adaptive Pre-training

**Korean Title:** 도메인 적응 사전 학습으로부터 속성 인식 표현을 활용한 이상 음향 탐지 개선

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Domain-adaptive Pre-training, Hierarchical Clustering

## 🔗 유사한 논문
- [[2025-09-22/Contrastive Learning with Spectrum Information Augmentation in Abnormal Sound Detection_20250922|Contrastive Learning with Spectrum Information Augmentation in Abnormal Sound Detection]] (83.6% similar)
- [[2025-09-19/Multi-label Scene Classification for Autonomous Vehicles_ Acquiring and Accumulating Knowledge from Diverse Datasets_20250919|Multi-label Scene Classification for Autonomous Vehicles Acquiring and Accumulating Knowledge from Diverse Datasets]] (80.3% similar)
- [[2025-09-22/Hybrid Temporal Differential Consistency Autoencoder for Efficient and Sustainable Anomaly Detection in Cyber-Physical Systems_20250922|Hybrid Temporal Differential Consistency Autoencoder for Efficient and Sustainable Anomaly Detection in Cyber-Physical Systems]] (80.2% similar)
- [[2025-09-19/Domain Adaptation for Ulcerative Colitis Severity Estimation Using Patient-Level Diagnoses_20250919|Domain Adaptation for Ulcerative Colitis Severity Estimation Using Patient-Level Diagnoses]] (79.1% similar)
- [[2025-09-18/Omni-CLST_ Error-aware Curriculum Learning with guided Selective chain-of-Thought for audio question answering_20250918|Omni-CLST Error-aware Curriculum Learning with guided Selective chain-of-Thought for audio question answering]] (79.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.12845v2 Announce Type: replace-cross 
Abstract: Anomalous Sound Detection (ASD) is often formulated as a machine attribute classification task, a strategy necessitated by the common scenario where only normal data is available for training. However, the exhaustive collection of machine attribute labels is laborious and impractical. To address the challenge of missing attribute labels, this paper proposes an agglomerative hierarchical clustering method for the assignment of pseudo-attribute labels using representations derived from a domain-adaptive pre-trained model, which are expected to capture machine attribute characteristics. We then apply model adaptation to this pre-trained model through supervised fine-tuning for machine attribute classification, resulting in a new state-of-the-art performance. Evaluation on the Detection and Classification of Acoustic Scenes and Events (DCASE) 2025 Challenge dataset demonstrates that our proposed approach yields significant performance gains, ultimately outperforming our previous top-ranking system in the challenge.

## 🔍 Abstract (한글 번역)

arXiv:2509.12845v2 발표 유형: 교차 교체  
초록: 비정상 소리 탐지(Anomalous Sound Detection, ASD)는 종종 기계 속성 분류 과제로 공식화되며, 이는 일반적으로 정상 데이터만 훈련에 사용 가능한 상황에서 필요로 하는 전략입니다. 그러나 기계 속성 레이블을 완전히 수집하는 것은 번거롭고 비현실적입니다. 이러한 속성 레이블의 부재 문제를 해결하기 위해, 본 논문에서는 도메인 적응 사전 훈련 모델에서 파생된 표현을 사용하여 기계 속성 특성을 포착할 것으로 기대되는 의사 속성 레이블을 할당하기 위한 집합적 계층적 군집화 방법을 제안합니다. 이후, 기계 속성 분류를 위한 감독된 미세 조정을 통해 이 사전 훈련 모델에 모델 적응을 적용하여 새로운 최첨단 성능을 달성합니다. 2025년 음향 장면 및 이벤트 탐지 및 분류(DCASE) 챌린지 데이터셋에 대한 평가 결과, 제안된 접근 방식이 상당한 성능 향상을 가져오며, 궁극적으로 챌린지에서 이전의 최고 순위 시스템을 능가하는 성과를 보였습니다.

## 📝 요약

이 논문은 비정상 소리 탐지(ASD)를 위한 새로운 접근법을 제안합니다. 일반적으로 ASD는 기계 속성 분류 작업으로 정의되지만, 속성 레이블을 수집하는 것은 어렵습니다. 이를 해결하기 위해, 이 논문에서는 도메인 적응 사전 학습 모델에서 파생된 표현을 사용하여 의사 속성 레이블을 할당하는 응집적 계층적 클러스터링 방법을 제안합니다. 이후, 이 사전 학습 모델에 대해 감독 학습을 통한 미세 조정을 적용하여 기계 속성 분류에서 최첨단 성능을 달성했습니다. DCASE 2025 챌린지 데이터셋 평가 결과, 제안된 방법이 기존 최고 성능 시스템을 능가하는 성과를 보였습니다.

## 🎯 주요 포인트

- 1. 비정상 소리 감지(ASD)는 주로 기계 속성 분류 작업으로 형성되며, 이는 정상 데이터만 훈련에 사용 가능한 일반적인 상황에 기인합니다.

- 2. 기계 속성 레이블의 수집은 번거롭고 비현실적이므로, 본 논문에서는 도메인 적응 사전 훈련 모델에서 파생된 표현을 사용하여 의사 속성 레이블을 할당하는 집합적 계층적 클러스터링 방법을 제안합니다.

- 3. 제안된 방법은 사전 훈련된 모델에 대한 감독된 미세 조정을 통해 기계 속성 분류를 위한 모델 적응을 수행하여 새로운 최첨단 성능을 달성합니다.

- 4. DCASE 2025 챌린지 데이터셋 평가에서 제안된 접근 방식은 상당한 성능 향상을 보여주며, 이전 챌린지에서 최고 순위 시스템을 능가합니다.

---

*Generated on 2025-09-22 15:04:40*