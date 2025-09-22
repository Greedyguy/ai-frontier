# IEFS-GMB: Gradient Memory Bank-Guided Feature Selection Based on Information Entropy for EEG Classification of Neurological Disorders

**Korean Title:** 정보 엔트로피에 기반한 EEG 신경 장애 분류를 위한 그래디언트 메모리 뱅크 유도 특징 선택: IEFS-GMB

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Feature Selection, Information Entropy

## 🔗 유사한 논문
- [[2025-09-17/Exploring the Relationship between Brain Hemisphere States and Frequency Bands through Deep Learning Optimization Techniques_20250917|Exploring the Relationship between Brain Hemisphere States and Frequency Bands through Deep Learning Optimization Techniques]] (84.0% similar)
- [[2025-09-19/UMind_ A Unified Multitask Network for Zero-Shot MEEG Visual Decoding_20250919|UMind A Unified Multitask Network for Zero-Shot MEEG Visual Decoding]] (82.1% similar)
- [[2025-09-17/Personalization on a Budget_ Minimally-Labeled Continual Learning for Resource-Efficient Seizure Detection_20250917|Personalization on a Budget Minimally-Labeled Continual Learning for Resource-Efficient Seizure Detection]] (81.9% similar)
- [[2025-09-18/Explaining deep learning for ECG using time-localized clusters_20250918|Explaining deep learning for ECG using time-localized clusters]] (80.8% similar)
- [[2025-09-19/Brain-HGCN_ A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis_20250919|Brain-HGCN A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis]] (80.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15259v1 Announce Type: cross 
Abstract: Deep learning-based EEG classification is crucial for the automated detection of neurological disorders, improving diagnostic accuracy and enabling early intervention. However, the low signal-to-noise ratio of EEG signals limits model performance, making feature selection (FS) vital for optimizing representations learned by neural network encoders. Existing FS methods are seldom designed specifically for EEG diagnosis; many are architecture-dependent and lack interpretability, limiting their applicability. Moreover, most rely on single-iteration data, resulting in limited robustness to variability. To address these issues, we propose IEFS-GMB, an Information Entropy-based Feature Selection method guided by a Gradient Memory Bank. This approach constructs a dynamic memory bank storing historical gradients, computes feature importance via information entropy, and applies entropy-based weighting to select informative EEG features. Experiments on four public neurological disease datasets show that encoders enhanced with IEFS-GMB achieve accuracy improvements of 0.64% to 6.45% over baseline models. The method also outperforms four competing FS techniques and improves model interpretability, supporting its practical use in clinical settings.

## 🔍 Abstract (한글 번역)

arXiv:2509.15259v1 발표 유형: 교차  
초록: 딥러닝 기반 EEG 분류는 신경 질환의 자동 검출에 있어 매우 중요하며, 진단 정확도를 향상시키고 조기 개입을 가능하게 합니다. 그러나 EEG 신호의 낮은 신호 대 잡음비는 모델 성능을 제한하며, 이는 신경망 인코더가 학습한 표현을 최적화하기 위해 특징 선택(FS)이 필수적임을 의미합니다. 기존의 FS 방법들은 EEG 진단을 위해 특별히 설계된 경우가 드물며, 많은 경우 아키텍처에 의존하고 해석 가능성이 부족하여 적용 가능성이 제한됩니다. 게다가 대부분의 방법은 단일 반복 데이터에 의존하여 변동성에 대한 견고성이 제한적입니다. 이러한 문제를 해결하기 위해 우리는 Gradient Memory Bank에 의해 안내되는 정보 엔트로피 기반 특징 선택 방법인 IEFS-GMB를 제안합니다. 이 접근법은 역사적 그래디언트를 저장하는 동적 메모리 뱅크를 구축하고, 정보 엔트로피를 통해 특징 중요성을 계산하며, 엔트로피 기반 가중치를 적용하여 유익한 EEG 특징을 선택합니다. 네 가지 공개 신경 질환 데이터셋에 대한 실험 결과, IEFS-GMB로 강화된 인코더는 기본 모델 대비 0.64%에서 6.45%까지 정확도 향상을 달성하였습니다. 이 방법은 또한 네 가지 경쟁 FS 기술을 능가하며 모델 해석 가능성을 개선하여 임상 환경에서의 실용성을 뒷받침합니다.

## 📝 요약

이 논문은 EEG 신호의 낮은 신호 대 잡음비로 인한 모델 성능 한계를 극복하기 위해 정보 엔트로피 기반의 특징 선택 방법인 IEFS-GMB를 제안합니다. 이 방법은 그래디언트 메모리 뱅크를 활용하여 특징의 중요성을 계산하고, 엔트로피 기반 가중치를 적용하여 유용한 EEG 특징을 선택합니다. 네 가지 공공 신경 질환 데이터셋에서 실험한 결과, IEFS-GMB로 강화된 인코더는 기존 모델 대비 0.64%에서 6.45%까지 정확도가 향상되었습니다. 또한, 다른 네 가지 특징 선택 기법을 능가하며 모델 해석 가능성을 개선하여 임상적 활용 가능성을 높였습니다.

## 🎯 주요 포인트

- 1. EEG 신호의 낮은 신호 대 잡음 비율로 인해 딥러닝 기반 EEG 분류에서 특징 선택(FS)이 중요하다.

- 2. 기존의 FS 방법들은 EEG 진단에 특화되어 있지 않으며, 해석 가능성이 부족하여 적용에 한계가 있다.

- 3. 제안된 IEFS-GMB 방법은 정보 엔트로피 기반의 특징 선택 기법으로, 그래디언트 메모리 뱅크를 활용하여 EEG 특징의 중요성을 계산한다.

- 4. IEFS-GMB를 적용한 인코더는 네 가지 공공 신경 질환 데이터셋에서 기존 모델 대비 0.64%에서 6.45%까지 정확도가 향상되었다.

- 5. 제안된 방법은 임상 환경에서의 실용성을 뒷받침하며, 네 가지 경쟁 FS 기법보다 우수한 성능과 모델 해석 가능성을 제공한다.

---

*Generated on 2025-09-22 13:50:57*