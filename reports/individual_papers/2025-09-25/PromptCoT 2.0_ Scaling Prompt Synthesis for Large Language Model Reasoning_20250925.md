---
keywords:
  - Large Language Model
  - Prompt Synthesis
  - Self-Play
  - Supervised Fine-Tuning
  - Expectation-Maximization
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19894
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:41:30.258019",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Prompt Synthesis",
    "Self-Play",
    "Supervised Fine-Tuning",
    "Expectation-Maximization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Prompt Synthesis": 0.88,
    "Self-Play": 0.82,
    "Supervised Fine-Tuning": 0.8,
    "Expectation-Maximization": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's focus on scaling reasoning capabilities.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Prompt Synthesis",
        "canonical": "Prompt Synthesis",
        "aliases": [
          "Prompt Generation"
        ],
        "category": "unique_technical",
        "rationale": "Core innovation in the paper, enabling scalable reasoning.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.88
      },
      {
        "surface": "Self-Play",
        "canonical": "Self-Play",
        "aliases": [
          "Autonomous Learning"
        ],
        "category": "specific_connectable",
        "rationale": "Describes a key post-training regime enhancing model performance.",
        "novelty_score": 0.6,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.82
      },
      {
        "surface": "Supervised Fine-Tuning",
        "canonical": "Supervised Fine-Tuning",
        "aliases": [
          "SFT"
        ],
        "category": "specific_connectable",
        "rationale": "Represents a critical training approach discussed in the paper.",
        "novelty_score": 0.58,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Expectation-Maximization Loop",
        "canonical": "Expectation-Maximization",
        "aliases": [
          "EM Loop"
        ],
        "category": "unique_technical",
        "rationale": "Key method for refining rationales in prompt construction.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "Olympiad mathematics",
      "competitive programming",
      "state-of-the-art results"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Prompt Synthesis",
      "resolved_canonical": "Prompt Synthesis",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Self-Play",
      "resolved_canonical": "Self-Play",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Supervised Fine-Tuning",
      "resolved_canonical": "Supervised Fine-Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Expectation-Maximization Loop",
      "resolved_canonical": "Expectation-Maximization",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# PromptCoT 2.0: Scaling Prompt Synthesis for Large Language Model Reasoning

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19894.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19894](https://arxiv.org/abs/2509.19894)

## 🔗 유사한 논문
- [[2025-09-19/PMPO_ Probabilistic Metric Prompt Optimization for Small and Large Language Models_20250919|PMPO: Probabilistic Metric Prompt Optimization for Small and Large Language Models]] (86.4% similar)
- [[2025-09-23/PromptSuite_ A Task-Agnostic Framework for Multi-Prompt Generation_20250923|PromptSuite: A Task-Agnostic Framework for Multi-Prompt Generation]] (86.3% similar)
- [[2025-09-24/PromptEnhancer_ A Simple Approach to Enhance Text-to-Image Models via Chain-of-Thought Prompt Rewriting_20250924|PromptEnhancer: A Simple Approach to Enhance Text-to-Image Models via Chain-of-Thought Prompt Rewriting]] (85.8% similar)
- [[2025-09-25/PromptSculptor_ Multi-Agent Based Text-to-Image Prompt Optimization_20250925|PromptSculptor: Multi-Agent Based Text-to-Image Prompt Optimization]] (85.6% similar)
- [[2025-09-23/Prompt-with-Me_ in-IDE Structured Prompt Management for LLM-Driven Software Engineering_20250923|Prompt-with-Me: in-IDE Structured Prompt Management for LLM-Driven Software Engineering]] (84.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Self-Play|Self-Play]], [[keywords/Supervised Fine-Tuning|Supervised Fine-Tuning]]
**⚡ Unique Technical**: [[keywords/Prompt Synthesis|Prompt Synthesis]], [[keywords/Expectation-Maximization|Expectation-Maximization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19894v1 Announce Type: new 
Abstract: Large language models (LLMs) are evolving from conversational systems into strong reasoners for tasks such as Olympiad mathematics and competitive programming. While scaling parameters and test-time computation has driven progress, a key bottleneck is the lack of high-quality training problems: human-curated datasets are costly and limited, while existing synthetic corpora are often too easy or narrow. PromptCoT 1.0 showed that injecting rationales into prompt synthesis increases problem difficulty. Building on this, we present PromptCoT 2.0, a scalable framework that replaces hand-crafted heuristics with an expectation-maximization (EM) loop, where rationales are iteratively refined to guide prompt construction. This produces problems that are both harder and more diverse than prior corpora. The synthetic prompts support two post-training regimes: (1) Self-Play, where strong models improve autonomously via verifiable feedback without stronger teachers; and (2) Supervised Fine-Tuning (SFT), where weaker models learn from teacher-distilled traces. Extensive experiments demonstrate the effectiveness of this approach. In self-play, applying PromptCoT 2.0 to Qwen3-30B-A3B-Thinking-2507 sets new state-of-the-art results at the 30B scale, with +4.4, +4.8, and +5.3 on AIME 24/25 and HMMT 25, +6.1 and +5.0 on LiveCodeBench v5/v6, and +35 Elo on Codeforces. In SFT, training Qwen2.5-7B-Instruct solely on synthetic prompts boosts accuracy to 73.1 (AIME 24), 65.6 (AIME 25), and 53.4 (LiveCodeBench v5), surpassing models trained on human or hybrid data. Analyses further confirm that PromptCoT 2.0 yields fundamentally harder and distributionally distinct problems. These results establish prompt synthesis as a new axis for scaling reasoning and position PromptCoT 2.0 as a scalable foundation for future open-source models. The implementation is available at https://github.com/inclusionAI/PromptCoT.

## 📝 요약

대형 언어 모델(LLM)의 발전을 위해 고품질 훈련 문제의 부족이 주요 장애물로 작용하고 있습니다. PromptCoT 2.0은 이러한 문제를 해결하기 위해 설계된 확장 가능한 프레임워크로, 기대-최대화(EM) 루프를 통해 문제의 난이도와 다양성을 높였습니다. 이 방법론은 두 가지 훈련 방식에 적용됩니다: (1) 자가 학습(Self-Play)에서는 강력한 모델이 자율적으로 개선되며, (2) 지도 학습(SFT)에서는 약한 모델이 강력한 모델의 학습 흔적을 통해 학습합니다. 실험 결과, PromptCoT 2.0은 자가 학습에서 새로운 최고 성능을 기록했으며, 지도 학습에서도 인간 또는 혼합 데이터로 훈련된 모델을 능가하는 정확도를 보였습니다. PromptCoT 2.0은 합성 프롬프트 생성이 추론 능력 확장의 새로운 축임을 입증하며, 향후 오픈 소스 모델의 확장 가능한 기반으로 자리매김할 것입니다.

## 🎯 주요 포인트

- 1. PromptCoT 2.0는 기대-최대화(EM) 루프를 통해 합리적 사고를 유도하여 문제의 난이도와 다양성을 증가시킵니다.
- 2. 이 프레임워크는 자가 학습(Self-Play)과 지도 학습(Supervised Fine-Tuning, SFT)의 두 가지 사후 학습 체제를 지원합니다.
- 3. PromptCoT 2.0을 적용한 자가 학습은 30B 규모에서 새로운 최첨단 성과를 달성하며, 여러 벤치마크에서 성능 향상을 보였습니다.
- 4. SFT에서는 오직 합성 프롬프트로만 훈련된 모델이 인간 또는 혼합 데이터로 훈련된 모델을 능가하는 정확도를 기록했습니다.
- 5. PromptCoT 2.0은 문제의 난이도를 근본적으로 높이고 분포적으로 독특한 문제를 생성하여 추론 확장의 새로운 축을 제공합니다.


---

*Generated on 2025-09-25 16:41:30*