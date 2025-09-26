<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:25:47.718290",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Lifelong Robot Learning",
    "Dynamic Mixture of Progressive Parameter-Efficient Expert Library",
    "Expert Coefficient Replay",
    "Parameter-Efficient Fine-Tuning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Lifelong Robot Learning": 0.78,
    "Dynamic Mixture of Progressive Parameter-Efficient Expert Library": 0.82,
    "Expert Coefficient Replay": 0.79,
    "Parameter-Efficient Fine-Tuning": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Lifelong Robot Learning",
        "canonical": "Lifelong Robot Learning",
        "aliases": [
          "Continuous Robot Learning",
          "Incremental Robot Learning"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific domain of robot learning that focuses on continuous adaptation, which is central to the paper's contributions.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Dynamic Mixture of Progressive Parameter-Efficient Expert Library",
        "canonical": "Dynamic Mixture of Progressive Parameter-Efficient Expert Library",
        "aliases": [
          "DMPEL"
        ],
        "category": "unique_technical",
        "rationale": "This is the novel method introduced in the paper, offering a new approach to lifelong learning.",
        "novelty_score": 0.9,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Expert Coefficient Replay",
        "canonical": "Expert Coefficient Replay",
        "aliases": [
          "Coefficient Replay"
        ],
        "category": "unique_technical",
        "rationale": "This technique is a key innovation for mitigating forgetting, enhancing the paper's contribution to lifelong learning.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.75,
        "link_intent_score": 0.79
      },
      {
        "surface": "Parameter-Efficient Fine-Tuning",
        "canonical": "Parameter-Efficient Fine-Tuning",
        "aliases": [
          "Efficient Fine-Tuning"
        ],
        "category": "specific_connectable",
        "rationale": "This is a relevant technique for model adaptation, linking to broader trends in machine learning.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance",
      "success rates",
      "trainable parameters"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Lifelong Robot Learning",
      "resolved_canonical": "Lifelong Robot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Dynamic Mixture of Progressive Parameter-Efficient Expert Library",
      "resolved_canonical": "Dynamic Mixture of Progressive Parameter-Efficient Expert Library",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Expert Coefficient Replay",
      "resolved_canonical": "Expert Coefficient Replay",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.75,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Parameter-Efficient Fine-Tuning",
      "resolved_canonical": "Parameter-Efficient Fine-Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Dynamic Mixture of Progressive Parameter-Efficient Expert Library for Lifelong Robot Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2506.05985.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2506.05985](https://arxiv.org/abs/2506.05985)

## 🔗 유사한 논문
- [[2025-09-18/HAM_ Hierarchical Adapter Merging for Scalable Continual Learning_20250918|HAM: Hierarchical Adapter Merging for Scalable Continual Learning]] (85.5% similar)
- [[2025-09-19/LEED_ A Highly Efficient and Scalable LLM-Empowered Expert Demonstrations Framework for Multi-Agent Reinforcement Learning_20250919|LEED: A Highly Efficient and Scalable LLM-Empowered Expert Demonstrations Framework for Multi-Agent Reinforcement Learning]] (85.4% similar)
- [[2025-09-24/Self-Evolving LLMs via Continual Instruction Tuning_20250924|Self-Evolving LLMs via Continual Instruction Tuning]] (83.7% similar)
- [[2025-09-22/Diagnostics of cognitive failures in multi-agent expert systems using dynamic evaluation protocols and subsequent mutation of the processing context_20250922|Diagnostics of cognitive failures in multi-agent expert systems using dynamic evaluation protocols and subsequent mutation of the processing context]] (83.2% similar)
- [[2025-09-22/Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control_20250922|Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control]] (83.0% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Parameter-Efficient Fine-Tuning|Parameter-Efficient Fine-Tuning]]
**⚡ Unique Technical**: [[keywords/Lifelong Robot Learning|Lifelong Robot Learning]], [[keywords/Dynamic Mixture of Progressive Parameter-Efficient Expert Library|Dynamic Mixture of Progressive Parameter-Efficient Expert Library]], [[keywords/Expert Coefficient Replay|Expert Coefficient Replay]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.05985v2 Announce Type: replace 
Abstract: A generalist agent must continuously learn and adapt throughout its lifetime, achieving efficient forward transfer while minimizing catastrophic forgetting. Previous work within the dominant pretrain-then-finetune paradigm has explored parameter-efficient fine-tuning for single-task adaptation, effectively steering a frozen pretrained model with a small number of parameters. However, in the context of lifelong learning, these methods rely on the impractical assumption of a test-time task identifier and restrict knowledge sharing among isolated adapters. To address these limitations, we propose Dynamic Mixture of Progressive Parameter-Efficient Expert Library (DMPEL) for lifelong robot learning. DMPEL progressively builds a low-rank expert library and employs a lightweight router to dynamically combine experts into an end-to-end policy, enabling flexible and efficient lifelong forward transfer. Furthermore, by leveraging the modular structure of the fine-tuned parameters, we introduce expert coefficient replay, which guides the router to accurately retrieve frozen experts for previously encountered tasks. This technique mitigates forgetting while being significantly more storage- and computation-efficient than experience replay over the entire policy. Extensive experiments on the lifelong robot learning benchmark LIBERO demonstrate that our framework outperforms state-of-the-art lifelong learning methods in success rates during continual adaptation, while utilizing minimal trainable parameters and storage.

## 📝 요약

이 논문은 일반화된 에이전트가 지속적으로 학습하고 적응하는 과정에서 효율적인 전방 전이를 이루면서도 파국적 망각을 최소화하는 방법을 제안합니다. 기존의 사전 학습 후 미세 조정 패러다임은 단일 작업 적응에 초점을 맞췄지만, 이는 테스트 시 작업 식별자가 필요하고 지식 공유가 제한되는 한계가 있습니다. 이를 해결하기 위해, 저자들은 DMPEL(Dynamic Mixture of Progressive Parameter-Efficient Expert Library)을 제안합니다. DMPEL은 저차원의 전문가 라이브러리를 구축하고, 경량 라우터를 사용해 전문가를 동적으로 결합하여 유연하고 효율적인 전방 전이를 가능하게 합니다. 또한, 전문가 계수 재생을 통해 이전 작업에 대한 전문가를 정확히 회수하여 망각을 줄입니다. LIBERO 벤치마크 실험 결과, 제안된 프레임워크는 최소한의 학습 가능한 매개변수와 저장 공간으로 최신 지속 학습 방법들보다 높은 성공률을 보였습니다.

## 🎯 주요 포인트

- 1. DMPEL은 점진적으로 저랭크 전문가 라이브러리를 구축하고 경량 라우터를 사용하여 전문가를 동적으로 결합하여 유연하고 효율적인 평생 전방 전이를 가능하게 합니다.
- 2. 전문가 계수 재생을 도입하여 라우터가 이전에 접한 작업에 대한 동결된 전문가를 정확하게 검색하도록 안내함으로써 망각을 완화합니다.
- 3. DMPEL은 전체 정책에 대한 경험 재생보다 저장 및 계산 효율성이 크게 향상되었습니다.
- 4. LIBERO 벤치마크 실험에서 DMPEL은 최소한의 학습 가능한 매개변수와 저장 공간을 사용하면서도 지속적인 적응에서 성공률 면에서 최첨단 평생 학습 방법을 능가합니다.
- 5. 기존의 사전 훈련 후 미세 조정 패러다임의 한계를 극복하기 위해 DMPEL은 테스트 시 작업 식별자 없이도 지식 공유를 가능하게 합니다.


---

*Generated on 2025-09-24 15:25:47*