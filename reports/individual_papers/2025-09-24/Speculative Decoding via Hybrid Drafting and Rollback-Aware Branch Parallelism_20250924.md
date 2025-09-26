<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:35:16.055684",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Speculative Decoding",
    "Large Language Model",
    "Branch Parallelism",
    "Token Rollback"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Speculative Decoding": 0.8,
    "Large Language Model": 0.85,
    "Branch Parallelism": 0.78,
    "Token Rollback": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Speculative Decoding",
        "canonical": "Speculative Decoding",
        "aliases": [
          "SD"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel technique central to the paper's contribution, offering a unique approach to LLM inference acceleration.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are a fundamental component of the study, providing context for the speculative decoding technique.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Branch Parallelism",
        "canonical": "Branch Parallelism",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Branch parallelism is a key innovation in the proposed framework, enhancing the speculative decoding process.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Token Rollback",
        "canonical": "Token Rollback",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Token rollback is a critical challenge addressed by the paper, impacting the efficiency of speculative decoding.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Speculative Decoding",
      "resolved_canonical": "Speculative Decoding",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Branch Parallelism",
      "resolved_canonical": "Branch Parallelism",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Token Rollback",
      "resolved_canonical": "Token Rollback",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Speculative Decoding via Hybrid Drafting and Rollback-Aware Branch Parallelism

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2506.01979.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2506.01979](https://arxiv.org/abs/2506.01979)

## 🔗 유사한 논문
- [[2025-09-22/CARD_ A Cache-Assisted Parallel Speculative Decoding Framework via Query-and-Correct Paradigm for Accelerating LLM Inference_20250922|CARD: A Cache-Assisted Parallel Speculative Decoding Framework via Query-and-Correct Paradigm for Accelerating LLM Inference]] (89.1% similar)
- [[2025-09-23/SpecVLM_ Fast Speculative Decoding in Vision-Language Models_20250923|SpecVLM: Fast Speculative Decoding in Vision-Language Models]] (85.8% similar)
- [[2025-09-23/Spiffy_ Multiplying Diffusion LLM Acceleration via Lossless Speculative Decoding_20250923|Spiffy: Multiplying Diffusion LLM Acceleration via Lossless Speculative Decoding]] (85.7% similar)
- [[2025-09-22/ViSpec_ Accelerating Vision-Language Models with Vision-Aware Speculative Decoding_20250922|ViSpec: Accelerating Vision-Language Models with Vision-Aware Speculative Decoding]] (84.3% similar)
- [[2025-09-23/Spec-VLA_ Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance_20250923|Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance]] (83.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Speculative Decoding|Speculative Decoding]], [[keywords/Branch Parallelism|Branch Parallelism]], [[keywords/Token Rollback|Token Rollback]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.01979v2 Announce Type: replace-cross 
Abstract: Speculative decoding (SD) has emerged as a promising technique to accelerate LLM inference by employing a small draft model to propose draft tokens in advance, and validating them in parallel with the large target model. However, the existing SD methods still remain constrained by their serialized execution, which causes the mutual waiting bubbles between the draft and target models. To address this challenge, we draw inspiration from branch prediction in modern processors and propose a novel framework \textbf{SpecBranch} to unlock branch parallelism in SD. Specifically, we first take an in-depth analysis of the potential of branch parallelism in SD, and recognize that the key challenge lies in the trade-offs between parallelization and token rollback. Based on the analysis, we introduce parallel speculative branches to preemptively hedge against likely rejections. Meanwhile, to enhance parallelism, we jointly orchestrate adaptive draft lengths with a hybrid combination of the implicit draft model confidence and explicit reusing of target model features. Extensive experiments across various models and benchmarks show that SpecBranch achieves over \textbf{1.8}$\times \sim$ \textbf{4.5}$\times$ speedups against the auto-regressive decoding and reduces rollback tokens by $\textbf{50}$\% for poorly aligned models, while maintaining an identical sampling distribution.

## 📝 요약

이 논문은 LLM 추론을 가속화하기 위한 새로운 기법인 Speculative Decoding(SD)의 한계를 극복하고자 제안된 \textbf{SpecBranch}라는 프레임워크를 소개합니다. 기존 SD 방법은 직렬 실행으로 인해 초안 모델과 대상 모델 간의 상호 대기 시간이 발생하는 문제가 있었습니다. 이를 해결하기 위해, 현대 프로세서의 분기 예측에서 영감을 받아 SD에서 분기 병렬성을 구현했습니다. 주요 기여는 병렬 분기를 통해 예상되는 거부를 사전에 대비하고, 초안 모델의 신뢰도와 대상 모델의 특징을 결합하여 적응형 초안 길이를 조정함으로써 병렬성을 향상시킨 것입니다. 다양한 모델과 벤치마크에서 실험한 결과, SpecBranch는 기존 자동 회귀 디코딩 대비 1.8배에서 4.5배의 속도 향상을 이루었고, 잘 맞지 않는 모델에서 롤백 토큰을 50% 줄이면서도 동일한 샘플링 분포를 유지했습니다.

## 🎯 주요 포인트

- 1. Speculative decoding(추론 가속화 기법)은 초안 모델과 대형 목표 모델의 병렬 검증을 통해 LLM 추론을 가속화하지만, 기존 방법은 직렬 실행의 제약을 받습니다.
- 2. SpecBranch라는 새로운 프레임워크는 현대 프로세서의 분기 예측에서 영감을 받아 SD에서의 분기 병렬성을 구현하여 이 문제를 해결합니다.
- 3. SpecBranch는 병렬화를 통한 토큰 롤백의 균형을 맞추기 위해 잠재적인 분기 병렬성을 분석하고, 사전 방어를 위한 병렬 추측 분기를 도입합니다.
- 4. 다양한 모델과 벤치마크에서 SpecBranch는 자동 회귀 디코딩에 비해 1.8배에서 4.5배의 속도 향상을 달성하고, 잘못 정렬된 모델에서 롤백 토큰을 50% 줄이면서 동일한 샘플링 분포를 유지합니다.


---

*Generated on 2025-09-24 14:35:16*