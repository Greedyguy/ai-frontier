---
keywords:
  - Transformer Architecture
  - Attention Mechanism
  - Stochastic Clock Attention
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:09:02.152895",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer Architecture",
    "Attention Mechanism",
    "Stochastic Clock Attention"
  ],
  "rejected_keywords": [
    "Sequence-to-Sequence Tasks"
  ],
  "similarity_scores": {
    "Transformer Architecture": 0.78,
    "Attention Mechanism": 0.8,
    "Stochastic Clock Attention": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Stochastic Clock Attention for Aligning Continuous and Ordered Sequences

**Korean Title:** 확률적 시계 주의 메커니즘을 통한 연속적이고 순차적인 시퀀스 정렬

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]     [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Transformer Architecture|Transformer text-to-speech]], [[keywords/Attention Mechanism|attention mechanism]]
**⚡ Unique Technical**: [[keywords/Stochastic Clock Attention|stochastic clock attention]]

## 🔗 유사한 논문
- [[Fast Multipole Attention_ A Scalable Multilevel Attention Mechanism for Text and Images_20250919|Fast Multipole Attention A Scalable Multilevel Attention Mechanism for Text and Images]] (79.3% similar)
- [[Moment- and Power-Spectrum-Based Gaussianity Regularization for Text-to-Image Models_20250919|Moment- and Power-Spectrum-Based Gaussianity Regularization for Text-to-Image Models]] (76.9% similar)
- [[Hybrid Autoregressive-Diffusion Model for Real-Time Sign Language Production_20250919|Hybrid Autoregressive-Diffusion Model for Real-Time Sign Language Production]] (76.9% similar)
- [[Structure-Aware Contrastive Learning with Fine-Grained Binding Representations for Drug Discovery_20250918|Structure-Aware Contrastive Learning with Fine-Grained Binding Representations for Drug Discovery]] (76.6% similar)
- [[Beyond Marginals_ Learning Joint Spatio-Temporal Patterns for Multivariate Anomaly Detection_20250918|Beyond Marginals Learning Joint Spatio-Temporal Patterns for Multivariate Anomaly Detection]] (75.9% similar)

## 📋 저자 정보

**Authors:** Hyungjoon Soh, Junghyo Jo

## 📄 Abstract (원문)

We formulate an attention mechanism for continuous and ordered sequences that
explicitly functions as an alignment model, which serves as the core of many
sequence-to-sequence tasks. Standard scaled dot-product attention relies on
positional encodings and masks but does not enforce continuity or monotonicity,
which are crucial for frame-synchronous targets. We propose learned nonnegative
\emph{clocks} to source and target and model attention as the meeting
probability of these clocks; a path-integral derivation yields a closed-form,
Gaussian-like scoring rule with an intrinsic bias toward causal, smooth,
near-diagonal alignments, without external positional regularizers. The
framework supports two complementary regimes: normalized clocks for parallel
decoding when a global length is available, and unnormalized clocks for
autoregressive decoding -- both nearly-parameter-free, drop-in replacements. In
a Transformer text-to-speech testbed, this construction produces more stable
alignments and improved robustness to global time-scaling while matching or
improving accuracy over scaled dot-product baselines. We hypothesize
applicability to other continuous targets, including video and temporal signal
modeling.

## 🔍 Abstract (한글 번역)

연속적이고 순서가 있는 시퀀스를 위한 주의 메커니즘을 정식화하여, 이는 많은 시퀀스-투-시퀀스 작업의 핵심 역할을 하는 정렬 모델로 명시적으로 기능합니다. 표준 스케일드 닷-프로덕트 어텐션은 위치 인코딩과 마스크에 의존하지만, 프레임 동기화 대상에 중요한 연속성이나 단조성을 강제하지는 않습니다. 우리는 소스와 타겟에 대해 학습된 비음수 \emph{시계}를 제안하고, 이 시계들의 만남 확률로 어텐션을 모델링합니다. 경로 적분 유도는 외부 위치 정규화 없이 인과적이고 부드러운, 거의 대각선에 가까운 정렬에 내재된 편향을 가진 폐쇄형의 가우시안 유사 점수 규칙을 제공합니다. 이 프레임워크는 두 가지 상호 보완적인 체제를 지원합니다: 전역 길이가 주어졌을 때 병렬 디코딩을 위한 정규화된 시계와, 자회귀 디코딩을 위한 비정규화된 시계로, 둘 다 거의 매개변수가 없는, 대체 가능한 형태입니다. 트랜스포머 텍스트-투-스피치 시험 환경에서, 이 구조는 더 안정적인 정렬을 생성하고, 스케일드 닷-프로덕트 기준선보다 정확도를 유지하거나 개선하면서 전역 시간 스케일링에 대한 강건성을 향상시킵니다. 우리는 비디오 및 시간 신호 모델링을 포함한 다른 연속적 대상에 대한 적용 가능성을 가정합니다.

## 📝 요약

이 논문은 연속적이고 순서가 있는 시퀀스를 위한 주의 메커니즘을 제안하며, 이는 시퀀스-투-시퀀스 작업의 핵심 역할을 합니다. 기존의 스케일된 내적 주의 메커니즘은 위치 인코딩과 마스크에 의존하지만 연속성이나 단조성을 보장하지 못합니다. 저자들은 소스와 타겟에 학습된 비음수 '클록'을 도입하고, 이 클록의 만남 확률로 주의를 모델링하여 외부 위치 정규화 없이 인과적이고 부드러운 정렬을 유도하는 가우시안 유사 점수 규칙을 제안합니다. 이 프레임워크는 병렬 디코딩을 위한 정규화 클록과 자가회귀 디코딩을 위한 비정규화 클록을 지원하며, 거의 매개변수가 필요 없는 대체물로 사용될 수 있습니다. 텍스트-투-스피치 테스트에서 이 방법은 안정적인 정렬과 시간 확장에 대한 강건성을 제공하면서 정확도를 유지하거나 개선합니다. 이 방법은 비디오 및 시간 신호 모델링과 같은 다른 연속 타겟에도 적용 가능할 것으로 예상됩니다.

## 🎯 주요 포인트

- 1. 연속적이고 순서가 있는 시퀀스를 위한 주의 메커니즘을 정식화하여 정렬 모델로 기능하도록 설계했습니다.

- 2. 기존의 스케일된 내적 주의는 위치 인코딩과 마스크에 의존하지만, 연속성과 단조성을 보장하지 못합니다.

- 3. 제안된 모델은 소스와 타겟에 학습된 비음수 '시계'를 사용하여 주의를 시계의 만남 확률로 모델링합니다.

- 4. 제안된 프레임워크는 병렬 디코딩을 위한 정규화된 시계와 자가회귀 디코딩을 위한 비정규화된 시계를 지원합니다.

- 5. 텍스트-음성 변환 실험에서 제안된 모델은 더 안정적인 정렬과 향상된 전역 시간 스케일링에 대한 강건성을 보여주었습니다.

---

*Generated on 2025-09-20 05:45:36*