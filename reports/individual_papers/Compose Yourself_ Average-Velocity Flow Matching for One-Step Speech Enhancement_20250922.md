# Compose Yourself: Average-Velocity Flow Matching for One-Step Speech Enhancement

**Korean Title:** "Compose Yourself: One-Step Speech Enhancement을 위한 평균 속도 흐름 매칭"

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Average-Velocity Flow Matching

## 🔗 유사한 논문
- [[2025-09-19/MeanFlowSE_ one-step generative speech enhancement via conditional mean flow_20250919|MeanFlowSE one-step generative speech enhancement via conditional mean flow]] (89.3% similar)
- [[2025-09-18/Real-Time Streaming Mel Vocoding with Generative Flow Matching_20250918|Real-Time Streaming Mel Vocoding with Generative Flow Matching]] (81.9% similar)
- [[2025-09-19/SpeechOp_ Inference-Time Task Composition for Generative Speech Processing_20250919|SpeechOp Inference-Time Task Composition for Generative Speech Processing]] (80.3% similar)
- [[2025-09-19/Diffusion-Based Unsupervised Audio-Visual Speech Separation in Noisy Environments with Noise Prior_20250919|Diffusion-Based Unsupervised Audio-Visual Speech Separation in Noisy Environments with Noise Prior]] (79.3% similar)
- [[2025-09-17/RFM-Editing_ Rectified Flow Matching for Text-guided Audio Editing_20250917|RFM-Editing Rectified Flow Matching for Text-guided Audio Editing]] (78.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15952v1 Announce Type: cross 
Abstract: Diffusion and flow matching (FM) models have achieved remarkable progress in speech enhancement (SE), yet their dependence on multi-step generation is computationally expensive and vulnerable to discretization errors. Recent advances in one-step generative modeling, particularly MeanFlow, provide a promising alternative by reformulating dynamics through average velocity fields. In this work, we present COSE, a one-step FM framework tailored for SE. To address the high training overhead of Jacobian-vector product (JVP) computations in MeanFlow, we introduce a velocity composition identity to compute average velocity efficiently, eliminating expensive computation while preserving theoretical consistency and achieving competitive enhancement quality. Extensive experiments on standard benchmarks show that COSE delivers up to 5x faster sampling and reduces training cost by 40%, all without compromising speech quality. Code is available at https://github.com/ICDM-UESTC/COSE.

## 🔍 Abstract (한글 번역)

arXiv:2509.15952v1 발표 유형: 교차  
초록: 확산 및 흐름 매칭(FM) 모델은 음성 향상(SE) 분야에서 놀라운 진전을 이루었지만, 다단계 생성에 대한 의존성은 계산 비용이 많이 들고 이산화 오류에 취약합니다. 최근의 일단계 생성 모델링, 특히 MeanFlow의 발전은 평균 속도장을 통해 동력을 재구성함으로써 유망한 대안을 제공합니다. 본 연구에서는 SE에 맞춘 일단계 FM 프레임워크인 COSE를 제시합니다. MeanFlow에서의 야코비안-벡터 곱(JVP) 계산의 높은 훈련 부담을 해결하기 위해, 평균 속도를 효율적으로 계산하는 속도 구성 정체성을 도입하여 비싼 계산을 제거하면서 이론적 일관성을 유지하고 경쟁력 있는 향상 품질을 달성합니다. 표준 벤치마크에 대한 광범위한 실험 결과, COSE는 최대 5배 빠른 샘플링을 제공하고 훈련 비용을 40% 절감하면서도 음성 품질을 손상시키지 않습니다. 코드는 https://github.com/ICDM-UESTC/COSE에서 이용할 수 있습니다.

## 📝 요약

이 논문에서는 COSE라는 새로운 일단계 흐름 매칭(FM) 프레임워크를 제안하여 음성 향상을 효율적으로 수행합니다. 기존의 다단계 생성 모델은 계산 비용이 높고 오류에 취약한 반면, COSE는 평균 속도장을 활용하여 이러한 문제를 해결합니다. 특히, MeanFlow의 높은 계산 비용을 줄이기 위해 속도 구성 정체성을 도입하여 평균 속도를 효율적으로 계산합니다. 실험 결과, COSE는 최대 5배 빠른 샘플링 속도를 제공하고, 훈련 비용을 40% 절감하면서도 음성 품질을 유지합니다.

## 🎯 주요 포인트

- 1. COSE는 다단계 생성의 계산 비용 문제를 해결하기 위해 설계된 음성 향상용 일단계 흐름 매칭(FM) 프레임워크입니다.

- 2. MeanFlow의 고비용 Jacobian-벡터 곱(JVP) 계산 문제를 해결하기 위해 평균 속도를 효율적으로 계산하는 속도 구성 정체성을 도입했습니다.

- 3. COSE는 표준 벤치마크 실험에서 최대 5배 빠른 샘플링 속도와 40%의 훈련 비용 절감을 달성하면서도 음성 품질을 유지합니다.

- 4. COSE의 코드와 관련 자료는 https://github.com/ICDM-UESTC/COSE에서 제공됩니다.

---

*Generated on 2025-09-22 14:18:48*