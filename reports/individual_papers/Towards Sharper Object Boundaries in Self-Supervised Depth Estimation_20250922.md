# Towards Sharper Object Boundaries in Self-Supervised Depth Estimation

**Korean Title:** 자기 지도 심도 추정에서 더 선명한 객체 경계를 향하여

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Mixture Distribution Depth Estimation

## 🔗 유사한 논문
- [[2025-09-19/Depth AnyEvent_ A Cross-Modal Distillation Paradigm for Event-Based Monocular Depth Estimation_20250919|Depth AnyEvent A Cross-Modal Distillation Paradigm for Event-Based Monocular Depth Estimation]] (82.9% similar)
- [[2025-09-22/Self-Supervised Cross-Modal Learning for Image-to-Point Cloud Registration_20250922|Self-Supervised Cross-Modal Learning for Image-to-Point Cloud Registration]] (81.4% similar)
- [[2025-09-18/Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning_20250918|Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning]] (81.0% similar)
- [[2025-09-19/UCorr_ Wire Detection and Depth Estimation for Autonomous Drones_20250919|UCorr Wire Detection and Depth Estimation for Autonomous Drones]] (80.7% similar)
- [[2025-09-22/Shedding Light on Depth_ Explainability Assessment in Monocular Depth Estimation_20250922|Shedding Light on Depth Explainability Assessment in Monocular Depth Estimation]] (80.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15987v1 Announce Type: cross 
Abstract: Accurate monocular depth estimation is crucial for 3D scene understanding, but existing methods often blur depth at object boundaries, introducing spurious intermediate 3D points. While achieving sharp edges usually requires very fine-grained supervision, our method produces crisp depth discontinuities using only self-supervision. Specifically, we model per-pixel depth as a mixture distribution, capturing multiple plausible depths and shifting uncertainty from direct regression to the mixture weights. This formulation integrates seamlessly into existing pipelines via variance-aware loss functions and uncertainty propagation. Extensive evaluations on KITTI and VKITTIv2 show that our method achieves up to 35% higher boundary sharpness and improves point cloud quality compared to state-of-the-art baselines.

## 🔍 Abstract (한글 번역)

arXiv:2509.15987v1 발표 유형: 교차  
초록: 정확한 단안 깊이 추정은 3D 장면 이해에 필수적이지만, 기존 방법들은 종종 객체 경계에서 깊이를 흐리게 하여 잘못된 중간 3D 점을 도입합니다. 선명한 경계를 달성하려면 매우 세밀한 감독이 필요하지만, 우리의 방법은 자기 감독만으로도 선명한 깊이 불연속성을 생성합니다. 구체적으로, 우리는 픽셀 단위 깊이를 혼합 분포로 모델링하여 여러 가능한 깊이를 포착하고 불확실성을 직접 회귀에서 혼합 가중치로 전환합니다. 이 공식은 분산 인식 손실 함수와 불확실성 전파를 통해 기존 파이프라인에 매끄럽게 통합됩니다. KITTI 및 VKITTIv2에 대한 광범위한 평가 결과, 우리의 방법이 최첨단 기준선과 비교하여 경계 선명도를 최대 35% 향상시키고 포인트 클라우드 품질을 개선함을 보여줍니다.

## 📝 요약

이 논문은 단안 깊이 추정의 정확성을 개선하기 위한 새로운 방법을 제안합니다. 기존 방법들은 객체 경계에서 깊이의 흐릿함을 초래하는 반면, 제안된 방법은 자기 지도 학습만으로 선명한 깊이 경계를 생성합니다. 각 픽셀의 깊이를 혼합 분포로 모델링하여 여러 가능한 깊이를 포착하고, 불확실성을 직접 회귀에서 혼합 가중치로 전환합니다. 이 접근법은 분산 인식 손실 함수와 불확실성 전파를 통해 기존 파이프라인에 통합됩니다. KITTI 및 VKITTIv2 데이터셋에서의 광범위한 평가 결과, 경계 선명도가 최대 35% 향상되고, 포인트 클라우드 품질이 최첨단 기준보다 개선되었습니다.

## 🎯 주요 포인트

- 1. 본 연구는 단안 깊이 추정에서 객체 경계의 깊이 흐림 문제를 해결하기 위해 자가 감독만으로 선명한 깊이 불연속성을 생성하는 방법을 제안합니다.

- 2. 제안된 방법은 픽셀별 깊이를 혼합 분포로 모델링하여 여러 가능한 깊이를 포착하고 불확실성을 직접 회귀에서 혼합 가중치로 전환합니다.

- 3. 이 방법은 분산 인식 손실 함수와 불확실성 전파를 통해 기존 파이프라인에 원활하게 통합됩니다.

- 4. KITTI 및 VKITTIv2 데이터셋에서의 광범위한 평가 결과, 제안된 방법이 최첨단 기준선 대비 최대 35% 높은 경계 선명도를 달성하고 포인트 클라우드 품질을 향상시킵니다.

---

*Generated on 2025-09-22 14:21:39*