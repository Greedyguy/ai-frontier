
# Masked Feature Modeling Enhances Adaptive Segmentation

**Korean Title:** 가리고 있는 특징 모델링은 적응 세분화를 향상시킵니다.

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Auxiliary Self-supervised Tasks

## 🔗 유사한 논문
- [[Semi-MoE_Mixture-of-Experts_meets_Semi-Supervised_Histopathology_Segmentation_20250918|Semi-MoE: Mixture-of-Experts meets Semi-Supervised Histopathology Segmentation]] (81.3% similar)
- [[CSMoE_An_Efficient_Remote_Sensing_Foundation_Model_with_Soft_Mixture-of-Experts_20250918|CSMoE: An Efficient Remote Sensing Foundation Model with Soft Mixture-of-Experts]] (81.1% similar)
- [[BEVUDA++_Geometric-aware_Unsupervised_Domain_Adaptation_for_Multi-View_3D_Object_Detection_20250918|BEVUDA++: Geometric-aware Unsupervised Domain Adaptation for Multi-View 3D Object Detection]] (79.6% similar)
- [[MAP: End-to-End Autonomous Driving with Map-Assisted Planning]] (78.8% similar)
- [[Improving_Generalized_Visual_Grounding_with_Instance-aware_Joint_Learning_20250918|Improving Generalized Visual Grounding with Instance-aware Joint Learning]] (78.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13801v1 Announce Type: new 
Abstract: Unsupervised domain adaptation (UDA) for semantic segmentation aims to transfer models from a labeled source domain to an unlabeled target domain. While auxiliary self-supervised tasks-particularly contrastive learning-have improved feature discriminability, masked modeling approaches remain underexplored in this setting, largely due to architectural incompatibility and misaligned optimization objectives. We propose Masked Feature Modeling (MFM), a novel auxiliary task that performs feature masking and reconstruction directly in the feature space. Unlike existing masked modeling methods that reconstruct low-level inputs or perceptual features (e.g., HOG or visual tokens), MFM aligns its learning target with the main segmentation task, ensuring compatibility with standard architectures like DeepLab and DAFormer without modifying the inference pipeline. To facilitate effective reconstruction, we introduce a lightweight auxiliary module, Rebuilder, which is trained jointly but discarded during inference, adding zero computational overhead at test time. Crucially, MFM leverages the segmentation decoder to classify the reconstructed features, tightly coupling the auxiliary objective with the pixel-wise prediction task to avoid interference with the primary task. Extensive experiments across various architectures and UDA benchmarks demonstrate that MFM consistently enhances segmentation performance, offering a simple, efficient, and generalizable strategy for unsupervised domain-adaptive semantic segmentation.

## 🔍 Abstract (한글 번역)

arXiv:2509.13801v1 발표 유형: 새로운
요약: 시맨틱 분할을 위한 비지도 도메인 적응(UDA)은 레이블이 지정된 소스 도메인에서 모델을 레이블이 지정되지 않은 대상 도메인으로 전이하는 것을 목표로 합니다. 보조 자기 지도 학습 작업, 특히 대조 학습은 특징 구별력을 향상시켰지만, 마스크 모델링 접근 방식은 이 설정에서 여전히 탐구되지 않은 상태입니다. 이는 주로 구조적 불일치와 최적화 목표의 불일치로 인합니다. 저희는 특징 마스킹 및 재구성을 특징 공간에서 직접 수행하는 새로운 보조 작업인 Masked Feature Modeling (MFM)을 제안합니다. 기존의 마스크 모델링 방법은 낮은 수준의 입력이나 지각적 특징(예: HOG 또는 시각적 토큰)을 재구성하는 반면, MFM은 주요 분할 작업과 학습 대상을 조정하여 DeepLab 및 DAFormer와 같은 표준 아키텍처와 호환되도록 보장합니다. 유효한 재구성을 용이하게 하기 위해 우리는 경량 보조 모듈인 Rebuilder를 소개합니다. 이 모듈은 학습 중에 함께 훈련되지만 추론 중에는 폐기되어 테스트 시에는 제로 계산 오버헤드를 추가하지 않습니다. 중요한 점은 MFM이 분할 디코더를 활용하여 재구성된 특징을 분류함으로써 보조 목표를 픽셀별 예측 작업과 긴밀하게 결합하여 주요 작업과의 간섭을 피합니다. 다양한 아키텍처 및 UDA 벤치마크를 통해 수행된 포괄적인 실험은 MFM이 일관되게 분할 성능을 향상시키며, 비지도 도메인 적응 시맨틱 분할에 대한 간단하고 효율적이며 일반화 가능한 전략을 제공함을 보여줍니다.

## 📝 요약

본 연구는 자기 감독적 학습 방법 중 하나인 Masked Feature Modeling (MFM)을 제안하고, 이를 통해 비지도 도메인 적응(UDA) 시맨틱 세그멘테이션 성능을 향상시키는 방법을 탐구한다. 기존의 마스킹 모델링 방법과 달리 MFM은 특징 공간에서 직접 특징 마스킹 및 재구성을 수행하여 주요 세그멘테이션 작업과 호환성을 보장한다. 실험 결과, MFM은 다양한 아키텍처와 UDA 벤치마크에서 일관되게 세그멘테이션 성능을 향상시키는 것으로 나타났으며, 비지도 도메인 적응 시맨틱 세그멘테이션에 대한 간단하고 효율적이며 일반화 가능한 전략을 제공한다.

## 🎯 주요 포인트

- 1. 자가 지도 학습 작업을 통해 특징 구별성을 향상시키는 대조 학습에 대한 연구가 있지만, 마스크 모델링 접근법은 아직 이 분야에서 충분히 탐구되지 않았다.

- 2. MFM은 특징 공간에서 특징 마스킹 및 재구성을 수행하는 새로운 보조 작업으로, 기존의 마스크 모델링 방법과는 다르게 주요 세그멘테이션 작업과 학습 대상을 일치시켜 표준 아키텍처와 호환되도록 한다.

- 3. Rebuilder라는 가벼운 보조 모듈을 도입하여 효과적인 재구성을 돕는데, 이는 테스트 시에는 제거되어 추가적인 계산 부담이 없다.

- 4. MFM은 재구성된 특징을 분류하기 위해 세그멘테이션 디코더를 활용하여 보조 목표를 픽셀별 예측 작업과 밀접하게 결합시켜 기본 작업과의 간섭을 피한다.

- 5. 다양한 아키텍처와 UDA 벤치마크를 통한 실험 결과, MFM은 일관되게 세그멘테이션 성능을 향상시키며, 비지도 도메인 적응 세그멘테이션에 대한 간단하고 효율적이며 일반화 가능한 전략을 제공한다.

---

*Generated on 2025-09-18 17:01:43*