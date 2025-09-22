# Fast OTSU Thresholding Using Bisection Method

**Korean Title:** 이분법을 이용한 빠른 오츠 임계값 설정

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Optimized Thresholding Algorithm

## 🔗 유사한 논문
- [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (79.6% similar)
- [[2025-09-19/DiffCut_ Catalyzing Zero-Shot Semantic Segmentation with Diffusion Features and Recursive Normalized Cut_20250919|DiffCut Catalyzing Zero-Shot Semantic Segmentation with Diffusion Features and Recursive Normalized Cut]] (78.8% similar)
- [[2025-09-18/Semi-MoE_ Mixture-of-Experts meets Semi-Supervised Histopathology Segmentation_20250918|Semi-MoE Mixture-of-Experts meets Semi-Supervised Histopathology Segmentation]] (78.4% similar)
- [[2025-09-18/A Novel Compression Framework for YOLOv8_ Achieving Real-Time Aerial Object Detection on Edge Devices via Structured Pruning and Channel-Wise Distillation_20250918|A Novel Compression Framework for YOLOv8 Achieving Real-Time Aerial Object Detection on Edge Devices via Structured Pruning and Channel-Wise Distillation]] (78.2% similar)
- [[2025-09-22/Ideal Registration Segmentation is All You Need_20250922|Ideal Registration Segmentation is All You Need]] (78.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16179v1 Announce Type: cross 
Abstract: The Otsu thresholding algorithm represents a fundamental technique in image segmentation, yet its computational efficiency is severely limited by exhaustive search requirements across all possible threshold values. This work presents an optimized implementation that leverages the bisection method to exploit the unimodal characteristics of the between-class variance function. Our approach reduces the computational complexity from O(L) to O(log L) evaluations while preserving segmentation accuracy. Experimental validation on 48 standard test images demonstrates a 91.63% reduction in variance computations and 97.21% reduction in algorithmic iterations compared to conventional exhaustive search. The bisection method achieves exact threshold matches in 66.67% of test cases, with 95.83% exhibiting deviations within 5 gray levels. The algorithm maintains universal convergence within theoretical logarithmic bounds while providing deterministic performance guarantees suitable for real-time applications. This optimization addresses critical computational bottlenecks in large-scale image processing systems without compromising the theoretical foundations or segmentation quality of the original Otsu method.

## 🔍 Abstract (한글 번역)

arXiv:2509.16179v1 발표 유형: 교차  
초록: 오츠(Otsu) 임계값 설정 알고리즘은 이미지 분할에서 기본적인 기법을 나타내지만, 모든 가능한 임계값에 대한 철저한 탐색 요구로 인해 계산 효율성이 심각하게 제한됩니다. 본 연구는 클래스 간 분산 함수의 단봉 특성을 활용하기 위해 이분법을 활용한 최적화 구현을 제시합니다. 우리의 접근 방식은 분할 정확성을 유지하면서 계산 복잡성을 O(L)에서 O(log L) 평가로 줄입니다. 48개의 표준 테스트 이미지에 대한 실험적 검증은 기존의 철저한 탐색과 비교하여 분산 계산이 91.63% 감소하고 알고리즘 반복이 97.21% 감소함을 보여줍니다. 이분법은 테스트 사례의 66.67%에서 정확한 임계값 일치를 달성하며, 95.83%는 5 그레이 레벨 이내의 편차를 보입니다. 알고리즘은 이론적 로그 경계 내에서 보편적인 수렴성을 유지하면서 실시간 응용에 적합한 결정론적 성능 보장을 제공합니다. 이 최적화는 원래 오츠 방법의 이론적 기초나 분할 품질을 손상시키지 않으면서 대규모 이미지 처리 시스템의 중요한 계산 병목 현상을 해결합니다.

## 📝 요약

이 논문은 이미지 분할의 기본 기법인 Otsu 임계값 알고리즘의 계산 효율성을 개선한 연구를 다룹니다. 기존의 모든 가능한 임계값을 탐색하는 방식의 비효율성을 해결하기 위해, 본 연구는 클래스 간 분산 함수의 단봉 특성을 활용한 이분법을 제안합니다. 이를 통해 계산 복잡도를 O(L)에서 O(log L)로 줄이면서도 분할 정확도를 유지합니다. 48개의 표준 테스트 이미지 실험 결과, 분산 계산이 91.63% 감소하고 알고리즘 반복 횟수가 97.21% 감소했습니다. 이분법은 테스트 케이스의 66.67%에서 정확한 임계값을 찾았으며, 95.83%는 5 그레이 레벨 이내의 편차를 보였습니다. 이 알고리즘은 이론적 로그 범위 내에서 보편적 수렴성을 유지하며, 실시간 응용에 적합한 성능을 보장합니다. 이는 대규모 이미지 처리 시스템에서 계산 병목 현상을 해결하면서도 Otsu 방법의 이론적 기초나 분할 품질을 손상시키지 않습니다.

## 🎯 주요 포인트

- 1. Otsu 임계값 알고리즘의 계산 복잡도를 O(L)에서 O(log L)로 줄이는 최적화 구현을 제안합니다.

- 2. 제안된 방법은 클래스 간 분산 함수의 단봉 특성을 활용하여 이분법을 적용합니다.

- 3. 실험 결과, 기존 탐색 대비 분산 계산이 91.63% 감소하고 알고리즘 반복이 97.21% 감소했습니다.

- 4. 이분법은 테스트 이미지의 66.67%에서 정확한 임계값을 찾았으며, 95.83%는 5 그레이 레벨 이내의 편차를 보였습니다.

- 5. 최적화된 알고리즘은 대규모 이미지 처리 시스템에서 이론적 로그 경계 내의 수렴성을 유지하면서 실시간 응용에 적합한 성능을 보장합니다.

---

*Generated on 2025-09-22 14:26:07*