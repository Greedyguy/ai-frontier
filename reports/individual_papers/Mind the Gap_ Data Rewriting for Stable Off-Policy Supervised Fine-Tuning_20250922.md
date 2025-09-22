# Mind the Gap: Data Rewriting for Stable Off-Policy Supervised Fine-Tuning

**Korean Title:** 갭에 주의하라: 안정적인 오프-정책 감독 미세 조정을 위한 데이터 재작성

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Two-Stage Approach|Two-Stage Approach]] [[keywords/specific/Importance Sampling|Importance Sampling]] [[keywords/broad/Supervised Fine-Tuning|Supervised Fine-Tuning]] [[keywords/broad/Off-Policy Learning|Off-Policy Learning]] [[keywords/unique/Data Rewriting Framework|Data Rewriting Framework]] [[categories/cs.LG|cs.LG]] [[2025-09-18/Mind the Gap_ Data Rewriting for Stable Off-Policy Supervised Fine-Tuning_20250918|Mind the Gap: Data Rewriting for Stable Off-Policy Supervised Fine-Tuning]] (97.8% similar) [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo: Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (85.4% similar) [[2025-09-22/Distribution-Aligned Decoding for Efficient LLM Task Adaptation_20250922|Distribution-Aligned Decoding for Efficient LLM Task Adaptation]] (84.0% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Two-Stage Approach
**🔗 Specific Connectable**: Importance Sampling
**🔬 Broad Technical**: Supervised Fine-Tuning, Off-Policy Learning
**⭐ Unique Technical**: Data Rewriting Framework
## 🔗 유사한 논문
- [[2025-09-18/Mind the Gap_ Data Rewriting for Stable Off-Policy Supervised Fine-Tuning_20250918|Mind the Gap Data Rewriting for Stable Off-Policy Supervised Fine-Tuning]] (97.8% similar)
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (85.4% similar)
- [[2025-09-22/Distribution-Aligned Decoding for Efficient LLM Task Adaptation_20250922|Distribution-Aligned Decoding for Efficient LLM Task Adaptation]] (84.0% similar)
- [[2025-09-19/From Correction to Mastery_ Reinforced Distillation of Large Language Model Agents_20250919|From Correction to Mastery Reinforced Distillation of Large Language Model Agents]] (83.3% similar)
- [[2025-09-18/Pre-training under infinite compute_20250918|Pre-training under infinite compute]] (83.2% similar)


**ArXiv ID**: [2509.15157](https://arxiv.org/abs/2509.15157)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.15157.pdf)


**ArXiv ID**: [2509.15157](https://arxiv.org/abs/2509.15157)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.15157.pdf)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Importance Sampling, KL Penalties
**⭐ Unique Technical**: Data Rewriting Framework
**🔬 Broad Technical**: Supervised Fine-Tuning, Off-Policy Learning

## 🏷️ 추출된 키워드



`Supervised Fine-Tuning` • 

`Off-Policy Learning` • 

`Importance Sampling` • 

`Data Rewriting Framework` • 

`Two-Stage Approach`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15157v2 Announce Type: replace 
Abstract: Supervised fine-tuning (SFT) of large language models can be viewed as an off-policy learning problem, where expert demonstrations come from a fixed behavior policy while training aims to optimize a target policy. Importance sampling is the standard tool for correcting this distribution mismatch, but large policy gaps lead to skewed weights, high variance, and unstable optimization. Existing methods mitigate this issue with KL penalties or clipping, which passively restrict updates rather than actively reducing the gap. We propose a simple yet effective data rewriting framework that proactively shrinks the policy gap before training. For each problem, correct model-generated solutions are kept as on-policy data, while incorrect ones are rewritten through guided re-solving, falling back to expert demonstrations only when needed. This aligns the training distribution with the target policy, reducing variance and improving stability. To handle residual mismatch after rewriting, we additionally apply importance sampling during training, forming a two-stage approach that combines data-level alignment with lightweight optimization-level correction. Experiments on five mathematical reasoning benchmarks show consistent and significant gains over both vanilla SFT and the state-of-the-art Dynamic Fine-Tuning (DFT) approach. Data and code will be released at https://github.com/NKU-HLT/Off-Policy-SFT.

## 🔍 Abstract (한글 번역)

arXiv:2509.15157v2 발표 유형: 교체  
초록: 대규모 언어 모델의 지도 학습 조정(SFT)은 고정된 행동 정책에서 전문가 시연이 제공되고 훈련이 목표 정책을 최적화하는 것을 목표로 하는 오프 정책 학습 문제로 볼 수 있습니다. 중요도 샘플링은 이러한 분포 불일치를 수정하기 위한 표준 도구이지만, 큰 정책 격차는 왜곡된 가중치, 높은 분산, 불안정한 최적화를 초래합니다. 기존 방법은 KL 페널티나 클리핑을 통해 이 문제를 완화하지만, 이는 격차를 적극적으로 줄이기보다는 수동적으로 업데이트를 제한합니다. 우리는 훈련 전에 정책 격차를 사전에 줄이는 간단하면서도 효과적인 데이터 재작성 프레임워크를 제안합니다. 각 문제에 대해, 모델이 생성한 올바른 솔루션은 온 정책 데이터로 유지되고, 잘못된 솔루션은 안내된 재해결을 통해 재작성되며, 필요할 때만 전문가 시연으로 돌아갑니다. 이는 훈련 분포를 목표 정책과 일치시켜 분산을 줄이고 안정성을 향상시킵니다. 재작성 후 남아 있는 불일치를 처리하기 위해, 우리는 추가로 훈련 중에 중요도 샘플링을 적용하여 데이터 수준의 정렬과 경량 최적화 수준의 수정을 결합한 2단계 접근 방식을 형성합니다. 다섯 가지 수학적 추론 벤치마크 실험에서 기본 SFT와 최첨단 동적 미세 조정(DFT) 접근 방식을 모두 능가하는 일관되고 유의미한 성과 향상을 보여줍니다. 데이터와 코드는 https://github.com/NKU-HLT/Off-Policy-SFT에서 공개될 예정입니다.

## 📝 요약

이 논문은 대규모 언어 모델의 지도 학습 미세 조정을 오프 정책 학습 문제로 보고, 정책 간 격차를 줄이기 위한 데이터 재작성 프레임워크를 제안합니다. 기존 방법들은 KL 패널티나 클리핑을 사용해 업데이트를 제한하지만, 이 연구는 훈련 전 정책 격차를 능동적으로 축소합니다. 문제별로 모델이 생성한 올바른 해답은 정책 내 데이터로 유지하고, 잘못된 해답은 전문가 시연에 의존하지 않고 재해결을 통해 수정합니다. 이로 인해 훈련 분포가 목표 정책과 일치하여 분산이 줄고 안정성이 향상됩니다. 재작성 후 남은 불일치를 처리하기 위해 훈련 중 중요도 샘플링을 추가로 적용하여 데이터 정렬과 최적화 수준의 보정을 결합한 2단계 접근법을 형성합니다. 다섯 개의 수학적 추론 벤치마크 실험에서 기존 방법들보다 일관되고 유의미한 성능 향상을 보였습니다. 데이터와 코드는 공개될 예정입니다.

## 🎯 주요 포인트


- 1. 대규모 언어 모델의 지도 학습 미세 조정(SFT)은 고정된 행동 정책에서 전문가 시연을 가져와 목표 정책을 최적화하는 오프 정책 학습 문제로 볼 수 있습니다.

- 2. 기존 방법은 KL 페널티나 클리핑을 사용하여 정책 간의 차이를 수동적으로 제한하지만, 제안된 데이터 재작성 프레임워크는 훈련 전에 정책 차이를 능동적으로 줄입니다.

- 3. 문제별로 모델이 생성한 올바른 솔루션은 온 정책 데이터로 유지하고, 잘못된 솔루션은 전문가 시연으로 돌아가야 할 때만 가이드된 재해결을 통해 재작성합니다.

- 4. 데이터 재작성 후 남아 있는 불일치를 처리하기 위해 훈련 중 중요도 샘플링을 추가로 적용하여 데이터 수준의 정렬과 최적화 수준의 경량 수정이 결합된 2단계 접근 방식을 형성합니다.

- 5. 다섯 가지 수학적 추론 벤치마크 실험에서 제안된 방법은 기존의 SFT와 최신의 동적 미세 조정(DFT) 접근법보다 일관되고 유의미한 성능 향상을 보여줍니다.


---

*Generated on 2025-09-22 16:05:01*