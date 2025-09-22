# PolyJuice Makes It Real: Black-Box, Universal Red Teaming for Synthetic Image Detectors

**Korean Title:** 폴리주스가 현실로 만든다: 합성 이미지 탐지기를 위한 블랙박스, 범용 레드 팀 전략

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Universal Red Teaming

## 🔗 유사한 논문
- [[2025-09-19/TIDE_ Achieving Balanced Subject-Driven Image Generation via Target-Instructed Diffusion Enhancement_20250919|TIDE Achieving Balanced Subject-Driven Image Generation via Target-Instructed Diffusion Enhancement]] (82.0% similar)
- [[2025-09-22/CIDER_ A Causal Cure for Brand-Obsessed Text-to-Image Models_20250922|CIDER A Causal Cure for Brand-Obsessed Text-to-Image Models]] (81.7% similar)
- [[2025-09-18/Iterative Prompt Refinement for Safer Text-to-Image Generation_20250918|Iterative Prompt Refinement for Safer Text-to-Image Generation]] (80.0% similar)
- [[2025-09-19/End4_ End-to-end Denoising Diffusion for Diffusion-Based Inpainting Detection_20250919|End4 End-to-end Denoising Diffusion for Diffusion-Based Inpainting Detection]] (79.6% similar)
- [[2025-09-18/BiasMap_ Leveraging Cross-Attentions to Discover and Mitigate Hidden Social Biases in Text-to-Image Generation_20250918|BiasMap Leveraging Cross-Attentions to Discover and Mitigate Hidden Social Biases in Text-to-Image Generation]] (79.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15551v1 Announce Type: new 
Abstract: Synthetic image detectors (SIDs) are a key defense against the risks posed by the growing realism of images from text-to-image (T2I) models. Red teaming improves SID's effectiveness by identifying and exploiting their failure modes via misclassified synthetic images. However, existing red-teaming solutions (i) require white-box access to SIDs, which is infeasible for proprietary state-of-the-art detectors, and (ii) generate image-specific attacks through expensive online optimization. To address these limitations, we propose PolyJuice, the first black-box, image-agnostic red-teaming method for SIDs, based on an observed distribution shift in the T2I latent space between samples correctly and incorrectly classified by the SID. PolyJuice generates attacks by (i) identifying the direction of this shift through a lightweight offline process that only requires black-box access to the SID, and (ii) exploiting this direction by universally steering all generated images towards the SID's failure modes. PolyJuice-steered T2I models are significantly more effective at deceiving SIDs (up to 84%) compared to their unsteered counterparts. We also show that the steering directions can be estimated efficiently at lower resolutions and transferred to higher resolutions using simple interpolation, reducing computational overhead. Finally, tuning SID models on PolyJuice-augmented datasets notably enhances the performance of the detectors (up to 30%).

## 🔍 Abstract (한글 번역)

arXiv:2509.15551v1 발표 유형: 신규  
초록: 합성 이미지 탐지기(SID)는 텍스트-이미지(T2I) 모델에서 생성되는 이미지의 사실감 증가로 인한 위험에 대한 주요 방어 수단입니다. 레드 팀은 잘못 분류된 합성 이미지를 통해 SID의 실패 모드를 식별하고 활용하여 SID의 효과를 향상시킵니다. 그러나 기존의 레드 팀 솔루션은 (i) 최신 탐지기에 대해 불가능한 화이트 박스 접근을 요구하며, (ii) 비용이 많이 드는 온라인 최적화를 통해 이미지별 공격을 생성합니다. 이러한 제한점을 해결하기 위해, 우리는 PolyJuice를 제안합니다. 이는 SID에 대한 첫 번째 블랙 박스, 이미지 비특이적 레드 팀 방법으로, SID에 의해 올바르게 분류된 샘플과 잘못 분류된 샘플 간의 T2I 잠재 공간에서 관찰된 분포 변화를 기반으로 합니다. PolyJuice는 (i) SID에 대한 블랙 박스 접근만을 필요로 하는 경량 오프라인 프로세스를 통해 이 변환의 방향을 식별하고, (ii) 이 방향을 활용하여 생성된 모든 이미지를 SID의 실패 모드로 보편적으로 유도함으로써 공격을 생성합니다. PolyJuice로 유도된 T2I 모델은 유도되지 않은 모델에 비해 SID를 속이는 데 있어 훨씬 더 효과적입니다(최대 84%). 우리는 또한 유도 방향이 낮은 해상도에서 효율적으로 추정될 수 있으며, 간단한 보간을 통해 높은 해상도로 전이될 수 있음을 보여주어 계산 오버헤드를 줄입니다. 마지막으로, PolyJuice로 증강된 데이터셋으로 SID 모델을 조정하면 탐지기의 성능이 눈에 띄게 향상됩니다(최대 30%).

## 📝 요약

이 논문은 텍스트-이미지(T2I) 모델에서 생성된 이미지의 사실성이 증가함에 따라 발생하는 위험을 방어하기 위한 합성 이미지 탐지기(SID)의 개선을 다루고 있습니다. 기존의 레드팀 기법은 탐지기의 취약점을 찾기 위해 백박스 접근이 필요하고, 비용이 많이 드는 최적화 과정을 요구합니다. 이를 해결하기 위해, 저자들은 PolyJuice라는 최초의 블랙박스, 이미지 비특정 레드팀 방법을 제안합니다. PolyJuice는 T2I 잠재 공간에서 SID가 올바르게 분류한 샘플과 잘못 분류한 샘플 간의 분포 변화를 이용하여 공격을 생성합니다. 이 방법은 가벼운 오프라인 프로세스를 통해 이 변화를 식별하고, 모든 생성 이미지를 SID의 취약점 방향으로 유도하여 탐지기를 속이는 데 효과적입니다. PolyJuice는 낮은 해상도에서 방향을 추정하고 이를 높은 해상도로 전환할 수 있어 계산 비용을 줄입니다. 또한, PolyJuice로 보강된 데이터셋으로 SID 모델을 조정하면 탐지 성능이 크게 향상됩니다.

## 🎯 주요 포인트

- 1. PolyJuice는 텍스트-이미지(T2I) 모델의 잠재 공간에서 관찰된 분포 변화를 활용하여 이미지 무관한 블랙박스 레드팀 방법을 제안합니다.

- 2. PolyJuice는 가벼운 오프라인 프로세스를 통해 SID의 실패 모드 방향을 식별하고, 모든 생성된 이미지를 이 방향으로 유도하여 공격을 생성합니다.

- 3. PolyJuice로 조정된 T2I 모델은 기존 모델보다 SID를 속이는 데 최대 84% 더 효과적입니다.

- 4. 낮은 해상도에서 추정된 방향을 높은 해상도로 전이할 수 있어 계산 비용을 줄일 수 있습니다.

- 5. PolyJuice로 보강된 데이터셋으로 SID 모델을 튜닝하면 탐지기의 성능이 최대 30% 향상됩니다.

---

*Generated on 2025-09-22 15:19:16*