# Saccadic Vision for Fine-Grained Visual Classification

**Korean Title:** 정밀한 시각 분류를 위한 단속적 시각

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Contextualized Selective Attention

## 🔗 유사한 논문
- [[2025-09-18/Improving Generalized Visual Grounding with Instance-aware Joint Learning_20250918|Improving Generalized Visual Grounding with Instance-aware Joint Learning]] (82.0% similar)
- [[2025-09-19/MARIC_ Multi-Agent Reasoning for Image Classification_20250919|MARIC Multi-Agent Reasoning for Image Classification]] (81.1% similar)
- [[2025-09-22/Diffusion-Based Cross-Modal Feature Extraction for Multi-Label Classification_20250922|Diffusion-Based Cross-Modal Feature Extraction for Multi-Label Classification]] (81.0% similar)
- [[2025-09-22/IEFS-GMB_ Gradient Memory Bank-Guided Feature Selection Based on Information Entropy for EEG Classification of Neurological Disorders_20250922|IEFS-GMB Gradient Memory Bank-Guided Feature Selection Based on Information Entropy for EEG Classification of Neurological Disorders]] (80.7% similar)
- [[2025-09-22/Emulating Human-like Adaptive Vision for Efficient and Flexible Machine Visual Perception_20250922|Emulating Human-like Adaptive Vision for Efficient and Flexible Machine Visual Perception]] (80.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15688v1 Announce Type: cross 
Abstract: Fine-grained visual classification (FGVC) requires distinguishing between visually similar categories through subtle, localized features - a task that remains challenging due to high intra-class variability and limited inter-class differences. Existing part-based methods often rely on complex localization networks that learn mappings from pixel to sample space, requiring a deep understanding of image content while limiting feature utility for downstream tasks. In addition, sampled points frequently suffer from high spatial redundancy, making it difficult to quantify the optimal number of required parts. Inspired by human saccadic vision, we propose a two-stage process that first extracts peripheral features (coarse view) and generates a sample map, from which fixation patches are sampled and encoded in parallel using a weight-shared encoder. We employ contextualized selective attention to weigh the impact of each fixation patch before fusing peripheral and focus representations. To prevent spatial collapse - a common issue in part-based methods - we utilize non-maximum suppression during fixation sampling to eliminate redundancy. Comprehensive evaluation on standard FGVC benchmarks (CUB-200-2011, NABirds, Food-101 and Stanford-Dogs) and challenging insect datasets (EU-Moths, Ecuador-Moths and AMI-Moths) demonstrates that our method achieves comparable performance to state-of-the-art approaches while consistently outperforming our baseline encoder.

## 🔍 Abstract (한글 번역)

arXiv:2509.15688v1 발표 유형: 교차  
초록: 세밀한 시각적 분류(FGVC)는 시각적으로 유사한 범주를 미세하고 국지적인 특징을 통해 구별해야 하며, 이는 높은 클래스 내 변동성과 제한된 클래스 간 차이로 인해 여전히 어려운 과제입니다. 기존의 부분 기반 방법은 종종 픽셀에서 샘플 공간으로의 매핑을 학습하는 복잡한 지역화 네트워크에 의존하며, 이는 이미지 콘텐츠에 대한 깊은 이해를 요구하면서 다운스트림 작업을 위한 특징의 활용성을 제한합니다. 또한, 샘플링된 포인트는 종종 높은 공간적 중복성을 겪어 필요한 부분의 최적 개수를 정량화하는 것이 어렵습니다. 인간의 안구 운동 시각에서 영감을 받아, 우리는 먼저 주변 특징(거친 보기)을 추출하고 샘플 맵을 생성한 다음, 여기에서 고정 패치를 샘플링하고 가중치 공유 인코더를 사용하여 병렬로 인코딩하는 2단계 프로세스를 제안합니다. 우리는 주변 및 집중 표현을 융합하기 전에 각 고정 패치의 영향을 평가하기 위해 맥락화된 선택적 주의를 사용합니다. 부분 기반 방법에서 흔히 발생하는 공간 붕괴를 방지하기 위해, 고정 샘플링 중에 비최대 억제를 활용하여 중복성을 제거합니다. 표준 FGVC 벤치마크(CUB-200-2011, NABirds, Food-101 및 Stanford-Dogs)와 도전적인 곤충 데이터셋(EU-Moths, Ecuador-Moths 및 AMI-Moths)에 대한 종합적인 평가 결과, 우리의 방법이 최첨단 접근법과 비교할 만한 성능을 달성하면서도 일관되게 우리의 기본 인코더를 능가함을 보여줍니다.

## 📝 요약

이 논문은 세밀한 시각적 분류(FGVC)를 위한 새로운 방법론을 제안합니다. 기존의 부분 기반 방법이 복잡한 네트워크에 의존하는 반면, 이 연구는 인간의 시각적 주사 과정을 모방한 두 단계 접근법을 사용합니다. 첫 단계에서는 주변 특징을 추출하고, 두 번째 단계에서는 주의가 필요한 부분을 선택적으로 인코딩합니다. 비최대 억제를 통해 공간적 중복을 제거하여 성능을 향상시킵니다. 제안된 방법은 여러 FGVC 벤치마크와 곤충 데이터셋에서 기존 최첨단 방법과 유사한 성능을 보이며, 기본 인코더보다 우수한 결과를 나타냅니다.

## 🎯 주요 포인트

- 1. 미세한 시각적 분류(FGVC)는 유사한 카테고리를 구별하기 위해 미세하고 국부적인 특징을 필요로 하며, 높은 클래스 내 변동성과 제한된 클래스 간 차이로 인해 여전히 도전적인 과제입니다.

- 2. 기존의 부분 기반 방법은 복잡한 로컬라이제이션 네트워크에 의존하며, 이는 이미지 콘텐츠에 대한 깊은 이해를 요구하고 다운스트림 작업에서의 특징 유용성을 제한합니다.

- 3. 인간의 안구 운동에서 영감을 받아, 주변 특징을 추출하고 샘플 맵을 생성한 후, 주의 패치를 병렬로 인코딩하는 두 단계 프로세스를 제안합니다.

- 4. 주의 패치의 영향을 평가하기 위해 문맥화된 선택적 주의를 사용하고, 주변 및 집중 표현을 융합하기 전에 각 주의 패치의 영향을 평가합니다.

- 5. 표준 FGVC 벤치마크 및 곤충 데이터셋에 대한 종합적인 평가를 통해 제안된 방법이 최첨단 접근 방식과 유사한 성능을 달성하면서도 기본 인코더보다 일관되게 우수한 성능을 보임을 입증합니다.

---

*Generated on 2025-09-22 14:08:32*