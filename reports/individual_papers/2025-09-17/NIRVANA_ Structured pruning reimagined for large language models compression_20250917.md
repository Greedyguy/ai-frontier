---
keywords:
  - Large Language Models
  - Attention Mechanism
  - Structured Pruning
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:49:59.100943",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Models",
    "Attention Mechanism",
    "Structured Pruning"
  ],
  "rejected_keywords": [
    "Neural Tangent Kernel",
    "Optimization"
  ],
  "similarity_scores": {
    "Large Language Models": 0.9,
    "Attention Mechanism": 0.78,
    "Structured Pruning": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# NIRVANA: Structured pruning reimagined for large language models compression

**Korean Title:** NIRVANA: 대규모 언어 모델 압축을 위한 구조적 프루닝의 재구성

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]       [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Structured Pruning|Structured Pruning]]
**🚀 Evolved Concepts**: [[keywords/Large Language Models|Large Language Models]]

## 🔗 유사한 논문
- [[Value-Guided KV Compression for LLMs via Approximated CUR Decomposition_20250919|Value-Guided KV Compression for LLMs via Approximated CUR Decomposition]] (81.0% similar)
- [[LNE-Blocking_ An Efficient Framework for Contamination Mitigation Evaluation on Large Language Models_20250918|LNE-Blocking An Efficient Framework for Contamination Mitigation Evaluation on Large Language Models]] (79.9% similar)
- [[LLM-I_ LLMs are Naturally Interleaved Multimodal Creators_20250918|LLM-I LLMs are Naturally Interleaved Multimodal Creators]] (79.8% similar)
- [[A Novel Compression Framework for YOLOv8_ Achieving Real-Time Aerial Object Detection on Edge Devices via Structured Pruning and Channel-Wise Distillation_20250918|A Novel Compression Framework for YOLOv8 Achieving Real-Time Aerial Object Detection on Edge Devices via Structured Pruning and Channel-Wise Distillation]] (79.8% similar)
- [[TDRM_ Smooth Reward Models with Temporal Difference for LLM RL and Inference_20250918|TDRM Smooth Reward Models with Temporal Difference for LLM RL and Inference]] (79.6% similar)

## 📋 저자 정보

**Authors:** Mengting Ai, Tianxin Wei, Sirui Chen, Jingrui He

## 📄 Abstract (원문)

Structured pruning of large language models (LLMs) offers substantial
efficiency improvements by removing entire hidden units, yet current approaches
often suffer from significant performance degradation, particularly in
zero-shot settings, and necessitate costly recovery techniques such as
supervised fine-tuning (SFT) or adapter insertion. To address these critical
shortcomings, we introduce NIRVANA, a novel pruning method explicitly designed
to balance immediate zero-shot accuracy preservation with robust fine-tuning
capability. Leveraging a first-order saliency criterion derived from the Neural
Tangent Kernel under Adam optimization dynamics, NIRVANA provides a
theoretically grounded pruning strategy that respects essential model training
behaviors. To further address the unique challenges posed by structured
pruning, NIRVANA incorporates an adaptive sparsity allocation mechanism across
layers and modules (attention vs. MLP), which adjusts pruning intensity between
modules in a globally balanced manner. Additionally, to mitigate the high
sensitivity of pruning decisions to calibration data quality, we propose a
simple yet effective KL divergence-based calibration data selection strategy,
ensuring more reliable and task-agnostic pruning outcomes. Comprehensive
experiments conducted on Llama3, Qwen, and T5 models demonstrate that NIRVANA
outperforms existing structured pruning methods under equivalent sparsity
constraints, providing a theoretically sound and practical approach to LLM
compression. The code is available at
https://github.com/iDEA-iSAIL-Lab-UIUC/NIRVANA.

## 🔍 Abstract (한글 번역)

대형 언어 모델(LLM)의 구조적 가지치기는 전체 은닉 유닛을 제거함으로써 상당한 효율성 향상을 제공합니다. 그러나 현재의 접근 방식은 특히 제로샷 설정에서 성능 저하를 겪는 경우가 많으며, 감독된 미세 조정(SFT) 또는 어댑터 삽입과 같은 비용이 많이 드는 복구 기술을 필요로 합니다. 이러한 중요한 단점을 해결하기 위해, 우리는 즉각적인 제로샷 정확도 보존과 강력한 미세 조정 능력을 균형 있게 설계한 새로운 가지치기 방법인 NIRVANA를 소개합니다. Adam 최적화 동역학 하에서 신경 접선 커널에서 파생된 일차 중요도 기준을 활용하여, NIRVANA는 필수적인 모델 훈련 행동을 존중하는 이론적으로 근거 있는 가지치기 전략을 제공합니다. 구조적 가지치기가 제기하는 독특한 과제를 추가로 해결하기 위해, NIRVANA는 계층 및 모듈(주의 vs. MLP) 간의 적응형 희소성 할당 메커니즘을 통합하여 모듈 간 가지치기 강도를 전역적으로 균형 있게 조정합니다. 또한, 가지치기 결정이 보정 데이터 품질에 매우 민감한 문제를 완화하기 위해, 우리는 단순하지만 효과적인 KL 발산 기반 보정 데이터 선택 전략을 제안하여 보다 신뢰할 수 있고 작업에 구애받지 않는 가지치기 결과를 보장합니다. Llama3, Qwen, T5 모델에서 수행된 종합적인 실험은 NIRVANA가 동일한 희소성 제약 하에서 기존의 구조적 가지치기 방법을 능가하며, LLM 압축에 대한 이론적으로 타당하고 실용적인 접근 방식을 제공함을 보여줍니다. 코드는 https://github.com/iDEA-iSAIL-Lab-UIUC/NIRVANA에서 확인할 수 있습니다.

## 📝 요약

대형 언어 모델(LLM)의 구조적 프루닝은 효율성을 높이지만, 성능 저하와 복구 비용 문제를 동반합니다. 이를 해결하기 위해, 우리는 NIRVANA라는 새로운 프루닝 방법을 제안합니다. 이 방법은 Neural Tangent Kernel을 활용한 saliency 기준을 통해 이론적으로 타당한 프루닝 전략을 제공합니다. 또한, 계층과 모듈 간의 적응적 희소성 할당 메커니즘을 도입하여 균형 잡힌 프루닝을 구현합니다. KL 발산 기반의 교정 데이터 선택 전략을 통해 프루닝 결정의 민감성을 완화합니다. 실험 결과, NIRVANA는 기존 방법보다 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. NIRVANA는 즉각적인 zero-shot 정확도 유지와 강력한 미세 조정 능력을 균형 있게 제공하는 새로운 가지치기 방법입니다.

- 2. NIRVANA는 Adam 최적화 동력학 하의 Neural Tangent Kernel에서 유도된 1차 중요도 기준을 활용하여 이론적으로 근거 있는 가지치기 전략을 제공합니다.

- 3. 적응형 희소성 할당 메커니즘을 통해 NIRVANA는 레이어와 모듈(예: 주의 메커니즘 vs. MLP) 간의 가지치기 강도를 전역적으로 균형 있게 조정합니다.

- 4. KL 발산 기반의 교정 데이터 선택 전략을 제안하여 가지치기 결정의 민감성을 줄이고, 보다 신뢰할 수 있는 작업 무관한 가지치기 결과를 보장합니다.

- 5. Llama3, Qwen, T5 모델에 대한 실험에서 NIRVANA는 기존의 구조적 가지치기 방법보다 우수한 성능을 보이며, LLM 압축에 대한 이론적이고 실용적인 접근법을 제공합니다.

---

*Generated on 2025-09-20 07:40:33*