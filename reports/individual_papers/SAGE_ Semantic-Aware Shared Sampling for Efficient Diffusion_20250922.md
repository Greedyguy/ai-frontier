# SAGE: Semantic-Aware Shared Sampling for Efficient Diffusion

**Korean Title:** SAGE: 효율적인 확산을 위한 의미 인식 공유 샘플링

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Shared Sampling Scheme

## 🔗 유사한 논문
- [[2025-09-17/SpecDiff_ Accelerating Diffusion Model Inference with Self-Speculation_20250917|SpecDiff Accelerating Diffusion Model Inference with Self-Speculation]] (81.9% similar)
- [[2025-09-18/Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model_20250918|Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model]] (80.5% similar)
- [[2025-09-22/Autoguided Online Data Curation for Diffusion Model Training_20250922|Autoguided Online Data Curation for Diffusion Model Training]] (80.4% similar)
- [[2025-09-22/Space Group Equivariant Crystal Diffusion_20250922|Space Group Equivariant Crystal Diffusion]] (80.2% similar)
- [[2025-09-22/G2D2_ Gradient-Guided Discrete Diffusion for Inverse Problem Solving_20250922|G2D2 Gradient-Guided Discrete Diffusion for Inverse Problem Solving]] (79.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15865v1 Announce Type: new 
Abstract: Diffusion models manifest evident benefits across diverse domains, yet their high sampling cost, requiring dozens of sequential model evaluations, remains a major limitation. Prior efforts mainly accelerate sampling via optimized solvers or distillation, which treat each query independently. In contrast, we reduce total number of steps by sharing early-stage sampling across semantically similar queries. To enable such efficiency gains without sacrificing quality, we propose SAGE, a semantic-aware shared sampling framework that integrates a shared sampling scheme for efficiency and a tailored training strategy for quality preservation. Extensive experiments show that SAGE reduces sampling cost by 25.5%, while improving generation quality with 5.0% lower FID, 5.4% higher CLIP, and 160% higher diversity over baselines.

## 🔍 Abstract (한글 번역)

arXiv:2509.15865v1 발표 유형: 신규  
초록: 확산 모델은 다양한 분야에서 명백한 이점을 보여주지만, 수십 번의 순차적인 모델 평가를 요구하는 높은 샘플링 비용은 여전히 주요한 제한 사항으로 남아 있습니다. 이전의 노력들은 주로 최적화된 해법이나 증류를 통해 샘플링을 가속화했으며, 이는 각 쿼리를 독립적으로 처리합니다. 반면에, 우리는 의미적으로 유사한 쿼리 간에 초기 단계의 샘플링을 공유함으로써 전체 단계 수를 줄입니다. 이러한 효율성 향상을 품질을 희생하지 않고 달성하기 위해, 우리는 효율성을 위한 공유 샘플링 체계와 품질 보존을 위한 맞춤형 훈련 전략을 통합한 의미 인식 공유 샘플링 프레임워크인 SAGE를 제안합니다. 광범위한 실험 결과, SAGE는 샘플링 비용을 25.5% 절감하면서, 기준치 대비 5.0% 낮은 FID, 5.4% 높은 CLIP, 160% 높은 다양성으로 생성 품질을 향상시킵니다.

## 📝 요약

이 논문은 확산 모델의 샘플링 비용을 줄이기 위한 SAGE라는 새로운 프레임워크를 제안합니다. 기존 방법들이 각 쿼리를 독립적으로 처리하는 데 반해, SAGE는 의미적으로 유사한 쿼리 간의 초기 샘플링을 공유하여 전체 단계 수를 줄입니다. 이를 통해 효율성을 높이면서도 품질을 유지할 수 있도록 맞춤형 학습 전략을 통합합니다. 실험 결과, SAGE는 샘플링 비용을 25.5% 절감하고, 생성 품질을 개선하여 FID 5.0% 감소, CLIP 5.4% 증가, 다양성 160% 증가를 달성했습니다.

## 🎯 주요 포인트

- 1. 확산 모델의 높은 샘플링 비용 문제를 해결하기 위해 SAGE라는 새로운 프레임워크를 제안합니다.

- 2. SAGE는 의미적으로 유사한 쿼리 간의 초기 단계 샘플링을 공유하여 총 샘플링 단계를 줄입니다.

- 3. SAGE는 효율성을 위한 공유 샘플링 스킴과 품질 유지를 위한 맞춤형 훈련 전략을 통합합니다.

- 4. 실험 결과, SAGE는 샘플링 비용을 25.5% 절감하면서 생성 품질을 향상시킵니다.

- 5. SAGE는 기존 기준 대비 FID 5.0% 감소, CLIP 5.4% 증가, 다양성 160% 증가를 달성합니다.

---

*Generated on 2025-09-22 15:27:04*