---
keywords:
  - Divergent-Convergent Reasoning
  - Large Language Models
  - Zero-shot Event Detection
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2506.05128
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:48:32.710580",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Divergent-Convergent Reasoning",
    "Large Language Models",
    "Zero-shot Event Detection"
  ],
  "rejected_keywords": [
    "Transfer Learning"
  ],
  "similarity_scores": {
    "Divergent-Convergent Reasoning": 0.85,
    "Large Language Models": 0.82,
    "Zero-shot Event Detection": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# DiCoRe: Enhancing Zero-shot Event Detection via Divergent-Convergent LLM Reasoning

**Korean Title:** DiCoRe: 발산-수렴 대형 언어 모델 추론을 통한 제로샷 이벤트 감지 향상

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Large Language Models|Large Language Models]]
**⚡ Unique Technical**: [[keywords/Divergent-Convergent Reasoning|Divergent-Convergent Reasoning]], [[keywords/Zero-shot Event Detection|Zero-shot Event Detection]]

## 🔗 유사한 논문
- [[SNaRe Domain-aware Data Generation for Low-Resource Event Detection]] (81.7% similar)
- [[MAgICoRe Multi-Agent, Iterative, Coarse-to-Fine Refinement for Reasoning]] (80.6% similar)
- [[DetectAnyLLM Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (80.2% similar)
- [[AD-DINOv3 Enhancing DINOv3 for Zero-Shot Anomaly Detection with Anomaly-Aware Calibration]] (79.1% similar)
- [[Explicit Reasoning Makes Better Judges A Systematic Study on Accuracy, Efficiency, and Robustness]] (77.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.05128v2 Announce Type: replace-cross 
Abstract: Zero-shot Event Detection (ED), the task of identifying event mentions in natural language text without any training data, is critical for document understanding in specialized domains. Understanding the complex event ontology, extracting domain-specific triggers from the passage, and structuring them appropriately overloads and limits the utility of Large Language Models (LLMs) for zero-shot ED. To this end, we propose DiCoRe, a divergent-convergent reasoning framework that decouples the task of ED using Dreamer and Grounder. Dreamer encourages divergent reasoning through open-ended event discovery, which helps to boost event coverage. Conversely, Grounder introduces convergent reasoning to align the free-form predictions with the task-specific instructions using finite-state machine guided constrained decoding. Additionally, an LLM-Judge verifies the final outputs to ensure high precision. Through extensive experiments on six datasets across five domains and nine LLMs, we demonstrate how DiCoRe consistently outperforms prior zero-shot, transfer-learning, and reasoning baselines, achieving 4-7% average F1 gains over the best baseline -- establishing DiCoRe as a strong zero-shot ED framework.

## 🔍 Abstract (한글 번역)

arXiv:2506.05128v2 발표 유형: 교차 교체  
초록: 제로샷 이벤트 탐지(ED)는 훈련 데이터 없이 자연어 텍스트에서 이벤트 언급을 식별하는 작업으로, 전문 분야에서 문서 이해에 매우 중요합니다. 복잡한 이벤트 온톨로지를 이해하고, 본문에서 도메인 특화 트리거를 추출하며, 이를 적절히 구조화하는 것은 제로샷 ED에 대한 대형 언어 모델(LLM)의 유용성을 과부하시키고 제한합니다. 이를 해결하기 위해, 우리는 Dreamer와 Grounder를 사용하여 ED 작업을 분리하는 발산-수렴 추론 프레임워크인 DiCoRe를 제안합니다. Dreamer는 개방형 이벤트 발견을 통해 발산적 추론을 장려하여 이벤트 커버리지를 향상시킵니다. 반면에, Grounder는 유한 상태 기계가 안내하는 제한된 디코딩을 사용하여 자유 형식 예측을 작업별 지침과 정렬하는 수렴적 추론을 도입합니다. 추가적으로, LLM-Judge는 최종 출력을 검증하여 높은 정밀도를 보장합니다. 다섯 개의 도메인과 아홉 개의 LLM에 걸친 여섯 개의 데이터셋에 대한 광범위한 실험을 통해, DiCoRe가 이전의 제로샷, 전이 학습 및 추론 기준선을 일관되게 능가하여, 최고의 기준선보다 평균 F1 점수에서 4-7% 향상을 달성하는 방법을 보여주며, DiCoRe를 강력한 제로샷 ED 프레임워크로 확립합니다.

## 📝 요약

Zero-shot 이벤트 탐지(ED)는 훈련 데이터 없이 자연어 텍스트에서 이벤트를 식별하는 작업으로, 전문 분야의 문서 이해에 중요합니다. DiCoRe는 Dreamer와 Grounder를 활용한 발산-수렴 추론 프레임워크로, ED 작업을 분리하여 수행합니다. Dreamer는 개방형 이벤트 발견을 통해 이벤트 범위를 확장하고, Grounder는 유한 상태 기계 기반의 제한된 디코딩을 통해 예측을 작업 지침에 맞춥니다. LLM-Judge는 최종 결과의 정확성을 검증합니다. 다섯 개의 도메인과 아홉 개의 LLM을 사용한 여섯 개의 데이터셋 실험에서 DiCoRe는 기존 방법보다 평균 F1 점수가 4-7% 향상되어 강력한 zero-shot ED 프레임워크로 입증되었습니다.

## 🎯 주요 포인트

- 1. Zero-shot 이벤트 탐지는 훈련 데이터 없이 자연어 텍스트에서 이벤트를 식별하는 중요한 작업이다.

- 2. DiCoRe는 Dreamer와 Grounder를 사용하여 이벤트 탐지 작업을 분리하는 발산-수렴 추론 프레임워크를 제안한다.

- 3. Dreamer는 개방형 이벤트 발견을 통해 발산적 추론을 장려하여 이벤트 커버리지를 향상시킨다.

- 4. Grounder는 유한 상태 기계로 안내된 제한적 디코딩을 통해 자유 형식 예측을 작업별 지침과 정렬하는 수렴적 추론을 도입한다.

- 5. DiCoRe는 여섯 개의 데이터셋과 아홉 개의 대형 언어 모델을 대상으로 한 실험에서 이전의 제로샷, 전이 학습, 추론 기준선을 능가하며 평균 F1 점수 4-7% 향상을 달성했다.

---

*Generated on 2025-09-19 15:16:56*