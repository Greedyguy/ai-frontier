<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:01:11.500313",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Continual Tool Usage",
    "Video Understanding",
    "Instruction Tuning",
    "VideoToolBench"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Continual Tool Usage": 0.78,
    "Video Understanding": 0.8,
    "Instruction Tuning": 0.77,
    "VideoToolBench": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the paper's focus on video understanding and tool usage.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Continual Tool Usage",
        "canonical": "Continual Tool Usage",
        "aliases": [
          "COLT"
        ],
        "category": "unique_technical",
        "rationale": "This concept is unique to the paper and represents a novel approach to tool usage in video LLMs.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Video Understanding",
        "canonical": "Video Understanding",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Video understanding is a key application area for the discussed models, linking it to broader multimedia research.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "Instruction Tuning",
        "canonical": "Instruction Tuning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Instruction tuning is crucial for adapting models to new tasks, enhancing their practical utility.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      },
      {
        "surface": "VideoToolBench",
        "canonical": "VideoToolBench",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This dataset is specifically designed for the paper's experiments, providing a unique resource for benchmarking.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
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
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Continual Tool Usage",
      "resolved_canonical": "Continual Tool Usage",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Video Understanding",
      "resolved_canonical": "Video Understanding",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Instruction Tuning",
      "resolved_canonical": "Instruction Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "VideoToolBench",
      "resolved_canonical": "VideoToolBench",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# COLT: Enhancing Video Large Language Models with Continual Tool Usage

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18754.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18754](https://arxiv.org/abs/2509.18754)

## 🔗 유사한 논문
- [[2025-09-23/Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates_20250923|Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates]] (85.6% similar)
- [[2025-09-23/Tool Preferences in Agentic LLMs are Unreliable_20250923|Tool Preferences in Agentic LLMs are Unreliable]] (84.2% similar)
- [[2025-09-23/EvoCoT_ Overcoming the Exploration Bottleneck in Reinforcement Learning_20250923|EvoCoT: Overcoming the Exploration Bottleneck in Reinforcement Learning]] (84.0% similar)
- [[2025-09-23/Generalizable End-to-End Tool-Use RL with Synthetic CodeGym_20250923|Generalizable End-to-End Tool-Use RL with Synthetic CodeGym]] (84.0% similar)
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo: Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (83.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Video Understanding|Video Understanding]], [[keywords/Instruction Tuning|Instruction Tuning]]
**⚡ Unique Technical**: [[keywords/Continual Tool Usage|Continual Tool Usage]], [[keywords/VideoToolBench|VideoToolBench]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18754v1 Announce Type: cross 
Abstract: The success of Large Language Models (LLMs) has significantly propelled the research of video understanding. To harvest the benefits of well-trained expert models (i.e., tools), video LLMs prioritize the exploration of tool usage capabilities. Existing methods either prompt closed-source LLMs or employ the instruction tuning paradigm for tool-use fine-tuning. These methods, however, assume an established repository of fixed tools and struggle to generalize to real-world environments where tool data is perpetually evolving and streaming in. To this end, we propose to enhance open-source video LLMs with COntinuaL Tool usage (termed COLT), which automatically acquires tool-use ability in a successive tool stream without suffering 'catastrophic forgetting' of the past learned tools. Specifically, our COLT incorporates a learnable tool codebook as a tool-specific memory system. Then relevant tools are dynamically selected based on the similarity between user instruction and tool features within the codebook. To unleash the tool usage potential of video LLMs, we collect a video-centric tool-use instruction tuning dataset VideoToolBench. Extensive experiments on both previous video LLM benchmarks and the tool-use-specific VideoToolBench dataset demonstrate the state-of-the-art performance of our proposed COLT.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 성공이 비디오 이해 연구를 크게 발전시켰음을 강조하며, 비디오 LLM이 도구 사용 능력을 탐색하는 데 중점을 두고 있음을 설명합니다. 기존 방법들은 폐쇄형 LLM을 사용하거나 도구 사용을 위한 미세 조정을 수행하지만, 고정된 도구 저장소를 가정하여 실제 환경에서의 일반화에 어려움을 겪습니다. 이를 해결하기 위해, 저자들은 'COLT'라는 연속적인 도구 사용 능력을 갖춘 오픈 소스 비디오 LLM을 제안합니다. COLT는 도구별 메모리 시스템으로 학습 가능한 도구 코드북을 사용하여 사용자 지침과 도구 특징 간의 유사성을 기반으로 관련 도구를 동적으로 선택합니다. 또한, 비디오 중심의 도구 사용 지침 조정 데이터셋인 VideoToolBench를 수집하여 도구 사용 잠재력을 극대화합니다. 실험 결과, COLT는 기존 비디오 LLM 벤치마크와 VideoToolBench 데이터셋에서 최첨단 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)의 성공이 비디오 이해 연구를 크게 촉진시켰습니다.
- 2. 기존 방법들은 고정된 도구 저장소를 가정하여 실제 환경에서의 일반화에 어려움을 겪습니다.
- 3. COLT는 연속적인 도구 스트림에서 자동으로 도구 사용 능력을 획득하여 과거 학습한 도구를 잊지 않도록 합니다.
- 4. COLT는 학습 가능한 도구 코드북을 도구별 메모리 시스템으로 통합하여 사용자 지시와 도구 특징 간의 유사성을 기반으로 관련 도구를 동적으로 선택합니다.
- 5. VideoToolBench 데이터셋을 통해 COLT의 최첨단 성능을 입증했습니다.


---

*Generated on 2025-09-24 14:01:11*