# Synthetic-to-Real Object Detection using YOLOv11 and Domain Randomization Strategies

**Korean Title:** YOLOv11과 도메인 랜덤화 전략을 활용한 합성-실제 객체 탐지

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[authors/Luisa Torquato Niño|Luisa Torquato Niño]] [[authors/Hamza A. A. Gardi|Hamza A. A. Gardi]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Synthetic-to-Real Training

## 🔗 유사한 논문
- [[Performance Optimization of YOLO-FEDER FusionNet for Robust Drone Detection in Visually Complex Environments_20250918|Performance Optimization of YOLO-FEDER FusionNet for Robust Drone Detection in Visually Complex Environments]] (83.2% similar)
- [[A Novel Compression Framework for YOLOv8_ Achieving Real-Time Aerial Object Detection on Edge Devices via Structured Pruning and Channel-Wise Distillation_20250918|A Novel Compression Framework for YOLOv8 Achieving Real-Time Aerial Object Detection on Edge Devices via Structured Pruning and Channel-Wise Distillation]] (83.1% similar)
- [[Deep Learning-Driven Multimodal Detection and Movement Analysis of Objects in Culinary_20250919|Deep Learning-Driven Multimodal Detection and Movement Analysis of Objects in Culinary]] (80.9% similar)
- [[Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation_20250919|Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation]] (80.0% similar)
- [[Lost in Translation Vocabulary Alignment for Source-Free Domain Adaptation in Open-Vocabulary Semantic Segmentation_20250918|Lost in Translation Vocabulary Alignment for Source-Free Domain Adaptation in Open-Vocabulary Semantic Segmentation]] (79.4% similar)

## 📋 저자 정보

**Authors:** Luisa Torquato Niño, Hamza A. A. Gardi

## 📄 Abstract (원문)

This paper addresses the synthetic-to-real domain gap in object detection,
focusing on training a YOLOv11 model to detect a specific object (a soup can)
using only synthetic data and domain randomization strategies. The methodology
involves extensive experimentation with data augmentation, dataset composition,
and model scaling. While synthetic validation metrics were consistently high,
they proved to be poor predictors of real-world performance. Consequently,
models were also evaluated qualitatively, through visual inspection of
predictions, and quantitatively, on a manually labeled real-world test set, to
guide development. Final mAP@50 scores were provided by the official Kaggle
competition. Key findings indicate that increasing synthetic dataset diversity,
specifically by including varied perspectives and complex backgrounds, combined
with carefully tuned data augmentation, were crucial in bridging the domain
gap. The best performing configuration, a YOLOv11l model trained on an expanded
and diverse dataset, achieved a final mAP@50 of 0.910 on the competition's
hidden test set. This result demonstrates the potential of a synthetic-only
training approach while also highlighting the remaining challenges in fully
capturing real-world variability.

## 🔍 Abstract (한글 번역)

이 논문은 객체 탐지에서 합성 데이터와 실제 데이터 간의 도메인 격차를 다루며, 합성 데이터와 도메인 랜덤화 전략만을 사용하여 특정 객체(수프 캔)를 탐지하기 위한 YOLOv11 모델 훈련에 중점을 둡니다. 방법론은 데이터 증강, 데이터셋 구성, 모델 확장을 통한 광범위한 실험을 포함합니다. 합성 데이터에 대한 검증 지표는 일관되게 높았지만, 실제 성능을 예측하는 데에는 부적절했습니다. 따라서 모델은 예측의 시각적 검토를 통한 정성적 평가와 수작업으로 라벨링된 실제 테스트 세트에서의 정량적 평가를 통해 개발을 안내했습니다. 최종 mAP@50 점수는 공식 Kaggle 대회에서 제공되었습니다. 주요 발견은 다양한 관점과 복잡한 배경을 포함하여 합성 데이터셋의 다양성을 증가시키고, 신중하게 조정된 데이터 증강을 결합하는 것이 도메인 격차를 줄이는 데 중요하다는 것을 나타냅니다. 가장 성능이 뛰어난 구성은 확장되고 다양한 데이터셋에서 훈련된 YOLOv11l 모델로, 대회의 숨겨진 테스트 세트에서 최종 mAP@50이 0.910을 기록했습니다. 이 결과는 합성 데이터만을 사용한 훈련 접근법의 잠재력을 보여주면서도 실제 세계의 변동성을 완전히 포착하는 데 남아 있는 과제를 강조합니다.

## 📝 요약

이 논문은 객체 탐지에서 합성 데이터와 실제 데이터 간의 도메인 차이를 해결하기 위해 YOLOv11 모델을 사용하여 특정 객체(수프 캔)를 탐지하는 방법을 연구합니다. 합성 데이터와 도메인 랜덤화 전략을 활용하여 데이터 증강, 데이터셋 구성, 모델 스케일링을 실험했습니다. 합성 데이터에서의 검증 지표는 높았으나 실제 성능 예측에는 한계가 있어, 수동으로 라벨링된 실제 데이터셋을 통해 정량적 및 정성적으로 평가했습니다. 주요 발견 사항으로는 다양한 시점과 복잡한 배경을 포함한 합성 데이터셋의 다양성 증가와 데이터 증강의 정밀한 조정이 도메인 차이를 줄이는 데 중요하다는 점이 있습니다. 최종적으로 확장된 데이터셋으로 훈련된 YOLOv11l 모델이 Kaggle 대회에서 mAP@50 점수 0.910을 기록하며 합성 데이터만으로도 효과적인 훈련이 가능함을 보여주었습니다. 그러나 실제 세계의 변동성을 완전히 포착하는 데는 여전히 도전 과제가 남아 있습니다.

## 🎯 주요 포인트

- 1. 본 논문은 YOLOv11 모델을 사용하여 합성 데이터와 도메인 랜덤화를 통해 특정 객체(수프 캔)를 탐지하는 방법을 연구합니다.

- 2. 합성 데이터셋의 다양성을 증가시키고 복잡한 배경과 다양한 관점을 포함하는 것이 도메인 격차를 줄이는 데 중요했습니다.

- 3. 최종적으로 확장된 다양한 데이터셋으로 훈련된 YOLOv11l 모델이 Kaggle 대회에서 mAP@50 점수 0.910을 기록했습니다.

- 4. 합성 데이터만을 사용한 훈련 접근법의 잠재력을 보여주었지만, 실제 세계의 변동성을 완전히 포착하는 데 남아있는 과제를 강조합니다.

---

*Generated on 2025-09-20 01:06:59*