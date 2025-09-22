
# On the Role of Individual Differences in Current Approaches to Computational Image Aesthetics

**Korean Title:** 현재 컴퓨테이셔널 이미지 미학 접근법에서 개인 차이의 역할에 관하여

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Unified Model for Aesthetic Assessment

## 🔗 유사한 논문
- [[Leveraging Perceptual Scores for Dataset Pruning in Computer Vision Tasks]] (76.8% similar)
- [[LLM-I LLMs are Naturally Interleaved Multimodal Creators]] (76.4% similar)
- [[Designing AI-Agents with Personalities A Psychometric Approach]] (76.3% similar)
- [[QuizRank Picking Images by Quizzing VLMs]] (76.2% similar)
- [[BiasMap Leveraging Cross-Attentions to Discover and Mitigate Hidden Social Biases in Text-to-Image Generation]] (76.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.20518v2 Announce Type: replace 
Abstract: Image aesthetic assessment (IAA) evaluates image aesthetics, a task complicated by image diversity and user subjectivity. Current approaches address this in two stages: Generic IAA (GIAA) models estimate mean aesthetic scores, while Personal IAA (PIAA) models adapt GIAA using transfer learning to incorporate user subjectivity. However, a theoretical understanding of transfer learning between GIAA and PIAA, particularly concerning the impact of group composition, group size, aesthetic differences between groups and individuals, and demographic correlations, is lacking. This work establishes a theoretical foundation for IAA, proposing a unified model that encodes individual characteristics in a distributional format for both individual and group assessments. We show that transferring from GIAA to PIAA involves extrapolation, while the reverse involves interpolation, which is generally more effective for machine learning. Extensive experiments with varying group compositions, including sub-sampling by group size and disjoint demographics, reveal substantial performance variation even for GIAA, challenging the assumption that averaging scores eliminates individual subjectivity. Score-distribution analysis using Earth Mover's Distance (EMD) and the Gini index identifies education, photography experience, and art experience as key factors in aesthetic differences, with greater subjectivity in artworks than in photographs. Code is available at https://github.com/lwchen6309/aesthetics_transfer_learning.

## 🔍 Abstract (한글 번역)

arXiv:2502.20518v2 발표 유형: 교체  
초록: 이미지 미적 평가(IAA)는 이미지의 미적 가치를 평가하는 작업으로, 이미지의 다양성과 사용자 주관성으로 인해 복잡합니다. 현재 접근 방식은 두 단계로 이루어져 있습니다: 일반 이미지 미적 평가(GIAA) 모델은 평균 미적 점수를 추정하고, 개인 이미지 미적 평가(PIAA) 모델은 전이 학습을 사용하여 사용자 주관성을 통합하여 GIAA를 적응시킵니다. 그러나 GIAA와 PIAA 간의 전이 학습에 대한 이론적 이해, 특히 그룹 구성, 그룹 크기, 그룹과 개인 간의 미적 차이, 인구 통계학적 상관관계의 영향에 관한 이해는 부족합니다. 본 연구는 IAA에 대한 이론적 기반을 확립하고, 개인 및 그룹 평가 모두에 대해 개인 특성을 분포 형식으로 인코딩하는 통합 모델을 제안합니다. 우리는 GIAA에서 PIAA로의 전이는 외삽을 포함하고, 반대로는 내삽을 포함하며, 이는 일반적으로 기계 학습에 더 효과적임을 보여줍니다. 그룹 크기 및 분리된 인구 통계학적 특성에 따른 하위 샘플링을 포함한 다양한 그룹 구성에 대한 광범위한 실험은, 점수를 평균화하면 개인의 주관성이 제거된다는 가정을 도전하며, GIAA에서도 상당한 성능 변화를 드러냅니다. Earth Mover's Distance(EMD)와 Gini 지수를 사용한 점수 분포 분석은 교육, 사진 경험, 예술 경험이 미적 차이의 주요 요인임을 확인하며, 예술 작품에서 사진보다 더 큰 주관성을 나타냅니다. 코드는 https://github.com/lwchen6309/aesthetics_transfer_learning에서 사용할 수 있습니다.

## 📝 요약

이 논문은 이미지 미학 평가(IAA)의 이론적 기반을 제시하며, 개인 및 그룹 평가를 위한 통합 모델을 제안합니다. 기존의 일반 IAA(GIAA)와 개인 IAA(PIAA) 모델 간의 전이 학습을 이론적으로 분석하여, 그룹 구성, 크기, 미학적 차이 및 인구 통계와의 상관관계를 탐구합니다. GIAA에서 PIAA로의 전이는 외삽, 반대는 내삽으로, 후자가 기계 학습에 더 효과적임을 보입니다. 다양한 그룹 구성 실험을 통해, 평균 점수로 개인 주관성을 제거할 수 없음을 확인했습니다. 교육, 사진 및 예술 경험이 미학적 차이에 중요한 영향을 미치며, 예술 작품이 사진보다 주관성이 크다는 것을 발견했습니다. 코드와 추가 자료는 GitHub에서 제공됩니다.

## 🎯 주요 포인트

- 1. 이미지 미학 평가(IAA)는 이미지의 다양성과 사용자 주관성 때문에 복잡한 과제입니다.

- 2. 현재 접근 방식은 일반 IAA(GIAA) 모델과 개인 IAA(PIAA) 모델로 나뉘며, PIAA는 GIAA를 사용자 주관성을 반영하도록 전이 학습을 통해 적응시킵니다.

- 3. GIAA에서 PIAA로의 전이는 외삽을 포함하며, 반대 방향은 내삽을 포함하여 일반적으로 기계 학습에 더 효과적입니다.

- 4. 그룹 구성, 그룹 크기, 그룹과 개인 간의 미학적 차이, 인구통계학적 상관관계가 성능에 미치는 영향을 이론적으로 분석합니다.

- 5. 교육, 사진 경험, 예술 경험이 미학적 차이에 중요한 요소이며, 예술 작품에서 사진보다 주관성이 더 큽니다.

---

*Generated on 2025-09-19 16:16:38*