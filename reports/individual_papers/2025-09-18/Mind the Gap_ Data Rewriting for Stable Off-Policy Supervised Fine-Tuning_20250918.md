---
keywords:
  - Large Language Models
  - Off-Policy Learning
  - Dynamic Fine-Tuning
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:19:32.318238",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Models",
    "Off-Policy Learning",
    "Dynamic Fine-Tuning"
  ],
  "rejected_keywords": [
    "Supervised Fine-Tuning",
    "Importance Sampling"
  ],
  "similarity_scores": {
    "Large Language Models": 0.8,
    "Off-Policy Learning": 0.77,
    "Dynamic Fine-Tuning": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Mind the Gap: Data Rewriting for Stable Off-Policy Supervised Fine-Tuning

**Korean Title:** 갭에 주의하라: 안정적인 오프-정책 지도 학습 미세 조정을 위한 데이터 재작성

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Off-Policy Learning|Off-Policy Learning]]
**⚡ Unique Technical**: [[keywords/Dynamic Fine-Tuning|Dynamic Fine-Tuning]]
**🚀 Evolved Concepts**: [[keywords/Large Language Models|Large Language Models]]

## 🔗 유사한 논문
- [[Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (82.9% similar)
- [[From Correction to Mastery_ Reinforced Distillation of Large Language Model Agents_20250919|From Correction to Mastery Reinforced Distillation of Large Language Model Agents]] (82.1% similar)
- [[Delta Knowledge Distillation for Large Language Models_20250919|Delta Knowledge Distillation for Large Language Models]] (81.4% similar)
- [[Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (80.3% similar)
- [[FroM_ Frobenius Norm-Based Data-Free Adaptive Model Merging_20250918|FroM Frobenius Norm-Based Data-Free Adaptive Model Merging]] (79.8% similar)

## 📋 저자 정보

**Authors:** Shiwan Zhao, Xuyang Zhao, Jiaming Zhou, Aobo Kong, Qicheng Li, Yong Qin

## 📄 Abstract (원문)

Supervised fine-tuning (SFT) of large language models can be viewed as an
off-policy learning problem, where expert demonstrations come from a fixed
behavior policy while training aims to optimize a target policy. Importance
sampling is the standard tool for correcting this distribution mismatch, but
large policy gaps lead to high variance and training instability. Existing
approaches mitigate this issue using KL penalties or clipping, which passively
constrain updates rather than actively reducing the gap. We propose a simple
yet effective data rewriting framework that proactively shrinks the policy gap
by keeping correct solutions as on-policy data and rewriting incorrect ones
with guided re-solving, falling back to expert demonstrations only when needed.
This aligns the training distribution with the target policy before
optimization, reducing importance sampling variance and stabilizing off-policy
fine-tuning. Experiments on five mathematical reasoning benchmarks demonstrate
consistent and significant gains over both vanilla SFT and the state-of-the-art
Dynamic Fine-Tuning (DFT) approach. The data and code will be released at
https://github.com/NKU-HLT/Off-Policy-SFT.

## 🔍 Abstract (한글 번역)

대규모 언어 모델의 지도 학습 세부 조정(Supervised Fine-Tuning, SFT)은 고정된 행동 정책에서 전문가 시연이 제공되는 반면, 훈련은 목표 정책을 최적화하는 것을 목표로 하는 오프 정책 학습 문제로 볼 수 있습니다. 중요도 샘플링은 이러한 분포 불일치를 수정하기 위한 표준 도구이지만, 큰 정책 격차는 높은 분산과 훈련 불안정을 초래합니다. 기존 접근법은 KL 페널티나 클리핑을 사용하여 이 문제를 완화하는데, 이는 격차를 적극적으로 줄이기보다는 수동적으로 업데이트를 제한합니다. 우리는 올바른 솔루션을 온 정책 데이터로 유지하고 잘못된 솔루션을 안내된 재해결로 다시 작성하여 필요할 때만 전문가 시연으로 돌아가는 간단하면서도 효과적인 데이터 재작성 프레임워크를 제안합니다. 이는 최적화 전에 훈련 분포를 목표 정책과 일치시켜 중요도 샘플링 분산을 줄이고 오프 정책 세부 조정의 안정성을 높입니다. 다섯 가지 수학적 추론 벤치마크에 대한 실험은 기본 SFT와 최신 동적 세부 조정(Dynamic Fine-Tuning, DFT) 접근법 모두에 비해 일관되고 상당한 성능 향상을 보여줍니다. 데이터와 코드는 https://github.com/NKU-HLT/Off-Policy-SFT에서 공개될 예정입니다.

## 📝 요약

대규모 언어 모델의 지도 학습 미세 조정(SFT)은 고정된 행동 정책에서 전문가 시범을 사용하여 목표 정책을 최적화하는 오프-정책 학습 문제로 볼 수 있습니다. 기존 방법들은 KL 패널티나 클리핑을 사용하여 정책 간 격차를 수동적으로 줄이지만, 본 연구는 데이터를 재작성하여 올바른 솔루션은 온-정책 데이터로 유지하고, 잘못된 솔루션은 가이드 하에 재해결하여 정책 격차를 능동적으로 줄이는 프레임워크를 제안합니다. 이를 통해 중요도 샘플링의 분산을 줄이고 학습의 안정성을 높입니다. 다섯 개의 수학적 추론 벤치마크 실험에서 기존 방법들보다 일관되고 유의미한 성능 향상을 보였습니다. 데이터와 코드는 https://github.com/NKU-HLT/Off-Policy-SFT에서 공개될 예정입니다.

## 🎯 주요 포인트

- 1. 대규모 언어 모델의 지도 학습 미세 조정은 오프 정책 학습 문제로 볼 수 있으며, 중요도 샘플링은 분포 불일치를 수정하는 표준 도구이다.

- 2. 기존 접근 방식은 KL 패널티나 클리핑을 사용하여 정책 간극 문제를 완화하지만, 이는 간극을 적극적으로 줄이지 못한다.

- 3. 제안된 데이터 재작성 프레임워크는 올바른 솔루션을 온 정책 데이터로 유지하고, 잘못된 솔루션은 가이드 재해결로 수정하여 정책 간극을 줄인다.

- 4. 이 방법은 중요도 샘플링의 분산을 줄이고 오프 정책 미세 조정의 안정성을 높인다.

- 5. 다섯 가지 수학적 추론 벤치마크 실험에서 제안된 방법은 기존의 SFT와 최첨단 DFT 접근 방식보다 일관되고 유의미한 성능 향상을 보여준다.

---

*Generated on 2025-09-20 00:55:22*