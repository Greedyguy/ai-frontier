---
keywords:
  - SPICE
  - SWE-bench
  - Effort Estimation
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2507.09108
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:25:59.303881",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "SPICE",
    "SWE-bench",
    "Effort Estimation"
  ],
  "rejected_keywords": [
    "Foundation Models",
    "Test Coverage"
  ],
  "similarity_scores": {
    "SPICE": 0.8,
    "SWE-bench": 0.75,
    "Effort Estimation": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# SPICE: An Automated SWE-Bench Labeling Pipeline for Issue Clarity, Test Coverage, and Effort Estimation

**Korean Title:** SPICE: 문제 명확성, 테스트 커버리지 및 노력 추정을 위한 자동화된 SWE-Bench 라벨링 파이프라인

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Effort Estimation|Effort Estimation]]
**⚡ Unique Technical**: [[keywords/SPICE|SPICE]], [[keywords/SWE-bench|SWE-bench]]

## 🔗 유사한 논문
- [[An Empirical Study on Failures in Automated Issue Solving]] (79.2% similar)
- [[Post-Hoc_Split-Point_Self-Consistency_Verification_for_Efficient,_Unified_Quantification_of_Aleatoric_and_Epistemic_Uncertainty_in_Deep_Learning_20250918|Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning]] (76.2% similar)
- [[Self-Guided_Function_Calling_in_Large_Language_Models_via_Stepwise_Experience_Recall_20250918|Self-Guided Function Calling in Large Language Models via Stepwise Experience Recall]] (76.0% similar)
- [[Towards_Robust_Agentic_CUDA_Kernel_Benchmarking,_Verification,_and_Optimization_20250919|Towards Robust Agentic CUDA Kernel Benchmarking, Verification, and Optimization]] (75.8% similar)
- [[Trace Sampling 2.0 Code Knowledge Enhanced Span-level Sampling for Distributed Tracing]] (75.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.09108v5 Announce Type: replace-cross 
Abstract: High-quality labeled datasets are crucial for training and evaluating foundation models in software engineering, but creating them is often prohibitively expensive and labor-intensive. We introduce SPICE, a scalable, automated pipeline for labeling SWE-bench-style datasets with annotations for issue clarity, test coverage, and effort estimation. SPICE combines context-aware code navigation, rationale-driven prompting, and multi-pass consensus to produce labels that closely approximate expert annotations. SPICE's design was informed by our own experience and frustration in labeling more than 800 instances from SWE-Gym. SPICE achieves strong agreement with human-labeled SWE-bench Verified data while reducing the cost of labeling 1,000 instances from around \$100,000 (manual annotation) to just \$5.10. These results demonstrate SPICE's potential to enable cost-effective, large-scale dataset creation for SE-focused FMs. To support the community, we release both SPICE tool and SPICE Bench, a new dataset of 6,802 SPICE-labeled instances curated from 291 open-source projects in SWE-Gym (over 13x larger than SWE-bench Verified).

## 🔍 Abstract (한글 번역)

arXiv:2507.09108v5 발표 유형: 교차 교체  
초록: 소프트웨어 공학에서 기초 모델을 훈련하고 평가하기 위해 고품질의 라벨링된 데이터셋이 필수적이지만, 이를 생성하는 것은 종종 지나치게 비싸고 노동 집약적입니다. 우리는 이슈 명확성, 테스트 커버리지, 노력 추정을 위한 주석을 포함한 SWE-bench 스타일 데이터셋에 라벨을 붙이는 확장 가능하고 자동화된 파이프라인인 SPICE를 소개합니다. SPICE는 맥락 인식 코드 탐색, 근거 기반 프롬프트, 다중 패스 합의를 결합하여 전문가 주석에 가깝게 라벨을 생성합니다. SPICE의 설계는 SWE-Gym에서 800개 이상의 인스턴스를 라벨링하는 과정에서의 경험과 좌절감을 바탕으로 했습니다. SPICE는 인간이 라벨링한 SWE-bench 검증 데이터와 강한 일치를 이루면서도 1,000개의 인스턴스를 라벨링하는 비용을 약 \$100,000(수동 주석)에서 단 \$5.10으로 줄였습니다. 이러한 결과는 SE에 중점을 둔 기초 모델을 위한 비용 효율적이고 대규모의 데이터셋 생성을 가능하게 하는 SPICE의 잠재력을 보여줍니다. 커뮤니티를 지원하기 위해, 우리는 SPICE 도구와 SWE-Gym의 291개 오픈 소스 프로젝트에서 선별된 6,802개의 SPICE 라벨 인스턴스로 구성된 새로운 데이터셋인 SPICE Bench를 공개합니다 (SWE-bench Verified보다 13배 이상 큼).

## 📝 요약

이 논문은 소프트웨어 공학 분야의 기초 모델을 위한 고품질 라벨링 데이터셋의 중요성을 강조하며, 이를 위한 자동화된 파이프라인인 SPICE를 소개합니다. SPICE는 이슈 명확성, 테스트 커버리지, 노력 추정에 대한 주석을 달아주는 자동화된 라벨링 시스템으로, 전문가 수준의 주석과 유사한 결과를 제공합니다. SPICE는 코드 탐색, 이유 기반 프롬프트, 다중 패스 합의를 결합하여 라벨링 비용을 크게 절감합니다. 실제로 1,000개의 인스턴스 라벨링 비용을 약 10만 달러에서 5.10달러로 줄였습니다. 또한, SPICE Bench라는 새로운 데이터셋을 공개하여 커뮤니티의 발전을 지원합니다.

## 🎯 주요 포인트

- 1. SPICE는 소프트웨어 엔지니어링 분야에서 데이터셋의 라벨링을 자동화하여 비용과 노동력을 크게 절감하는 파이프라인입니다.

- 2. SPICE는 코드 탐색, 이유 기반의 프롬프트, 다중 합의 과정을 통해 전문가 수준의 라벨을 생성합니다.

- 3. SPICE는 1,000개의 인스턴스를 라벨링하는 비용을 약 \$100,000에서 \$5.10으로 줄였습니다.

- 4. SPICE Bench는 291개의 오픈 소스 프로젝트에서 수집된 6,802개의 인스턴스를 포함하는 새로운 데이터셋으로, 기존 SWE-bench Verified보다 13배 이상 큽니다.

- 5. SPICE 도구와 SPICE Bench 데이터셋은 커뮤니티 지원을 위해 공개되었습니다.

---

*Generated on 2025-09-19 15:19:00*