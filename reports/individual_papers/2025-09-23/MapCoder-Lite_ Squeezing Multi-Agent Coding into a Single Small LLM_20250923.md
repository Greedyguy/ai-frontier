---
keywords:
  - Large Language Model
  - MapCoder-Lite
  - LoRA
  - Multi-Agent Systems
  - Trajectory Distillation
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17489
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:59:14.815739",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "MapCoder-Lite",
    "LoRA",
    "Multi-Agent Systems",
    "Trajectory Distillation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "MapCoder-Lite": 0.8,
    "LoRA": 0.78,
    "Multi-Agent Systems": 0.77,
    "Trajectory Distillation": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "This term is central to the paper's discussion and links to the broader field of AI and NLP.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.85
      },
      {
        "surface": "MapCoder-Lite",
        "canonical": "MapCoder-Lite",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is the unique model introduced in the paper, central to its contributions.",
        "novelty_score": 0.95,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "LoRA adapters",
        "canonical": "LoRA",
        "aliases": [
          "Low-Rank Adaptation",
          "LoRA adapters"
        ],
        "category": "specific_connectable",
        "rationale": "LoRA is a key technique used in the paper for model specialization, relevant to model adaptation discussions.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "multi-agent coding",
        "canonical": "Multi-Agent Systems",
        "aliases": [
          "multi-agent coding"
        ],
        "category": "specific_connectable",
        "rationale": "The concept of multi-agent systems is crucial for understanding the collaborative approach in the paper.",
        "novelty_score": 0.55,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      },
      {
        "surface": "trajectory distillation",
        "canonical": "Trajectory Distillation",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This novel technique is significant for improving model performance, as highlighted in the paper.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "code generation",
      "retriever",
      "planner",
      "coder",
      "debugger"
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
        "specificity": 0.5,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "MapCoder-Lite",
      "resolved_canonical": "MapCoder-Lite",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "LoRA adapters",
      "resolved_canonical": "LoRA",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "multi-agent coding",
      "resolved_canonical": "Multi-Agent Systems",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "trajectory distillation",
      "resolved_canonical": "Trajectory Distillation",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# MapCoder-Lite: Squeezing Multi-Agent Coding into a Single Small LLM

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17489.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17489](https://arxiv.org/abs/2509.17489)

## 🔗 유사한 논문
- [[2025-09-23/Generalizable End-to-End Tool-Use RL with Synthetic CodeGym_20250923|Generalizable End-to-End Tool-Use RL with Synthetic CodeGym]] (83.6% similar)
- [[2025-09-18/Semantic Alignment-Enhanced Code Translation via an LLM-Based Multi-Agent System_20250918|Semantic Alignment-Enhanced Code Translation via an LLM-Based Multi-Agent System]] (83.4% similar)
- [[2025-09-18/CARGO_ A Framework for Confidence-Aware Routing of Large Language Models_20250918|CARGO: A Framework for Confidence-Aware Routing of Large Language Models]] (83.3% similar)
- [[2025-09-22/Evaluating the Limitations of Local LLMs in Solving Complex Programming Challenges_20250922|Evaluating the Limitations of Local LLMs in Solving Complex Programming Challenges]] (82.9% similar)
- [[2025-09-18/AppAgent v2_ Advanced Agent for Flexible Mobile Interactions_20250918|AppAgent v2: Advanced Agent for Flexible Mobile Interactions]] (82.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/LoRA|LoRA]], [[keywords/Multi-Agent Systems|Multi-Agent Systems]]
**⚡ Unique Technical**: [[keywords/MapCoder-Lite|MapCoder-Lite]], [[keywords/Trajectory Distillation|Trajectory Distillation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17489v1 Announce Type: cross 
Abstract: Large language models (LLMs) have advanced code generation from single-function tasks to competitive-programming problems, but existing multi-agent solutions either rely on costly large-scale ($>$ 30B) models or collapse when downsized to small open-source models. We present MapCoder-Lite, which upgrades a single 7B model into four role-specialised agents-retriever, planner, coder, and debugger-using only rank-32, role-specific LoRA adapters ($<3\%$ extra parameters). Three lightweight techniques make this possible: (i) trajectory distillation from strong LLMs fixes format fragility in retrieval and debugging, (ii) supervisor-guided correction strengthens planning and coding agents, and (iii) agent-wise LoRA fine-tuning delivers memory-efficient specialisation. Comprehensive evaluation on xCodeEval, APPS, and CodeContests shows that MapCoder-Lite more than doubles xCodeEval accuracy (from $13.2\%$ to $28.3\%$), eliminates all format failures, and closes to within six points of a 32B baseline while cutting GPU memory and token-generation time by $4\times$. These results demonstrate that careful agent-wise fine-tuning unleashes high-quality multi-agent coding on a small language model.

## 📝 요약

MapCoder-Lite는 7B 크기의 단일 언어 모델을 네 가지 역할(검색자, 계획자, 코더, 디버거)로 특화된 에이전트로 업그레이드하여, 대규모 모델 없이도 효율적인 코드 생성을 가능하게 합니다. 이 모델은 랭크-32의 역할별 LoRA 어댑터를 사용하여 추가 매개변수를 3% 미만으로 유지합니다. 주요 기법으로는 강력한 언어 모델로부터의 경로 증류, 감독자 지도의 수정, 에이전트별 LoRA 미세 조정이 포함됩니다. 평가 결과, MapCoder-Lite는 xCodeEval 정확도를 두 배 이상 향상시키고, 형식 오류를 제거하며, 32B 모델 대비 GPU 메모리와 토큰 생성 시간을 4배 절감합니다. 이는 작은 언어 모델에서도 고품질의 다중 에이전트 코딩이 가능함을 보여줍니다.

## 🎯 주요 포인트

- 1. MapCoder-Lite는 단일 7B 모델을 네 가지 역할로 특화된 에이전트로 업그레이드하여 소형 오픈 소스 모델에서도 다중 에이전트 코드 생성이 가능하도록 합니다.
- 2. 역할별 LoRA 어댑터를 사용하여 추가 매개변수를 3% 미만으로 유지하면서 메모리 효율적인 특화를 달성합니다.
- 3. 강력한 LLM으로부터의 경로 증류를 통해 검색 및 디버깅의 형식 취약성을 해결합니다.
- 4. 감독자 지도의 수정으로 계획 및 코딩 에이전트를 강화합니다.
- 5. xCodeEval, APPS, CodeContests에서의 평가 결과, MapCoder-Lite는 xCodeEval 정확도를 두 배 이상 향상시키고, 형식 실패를 모두 제거하며, GPU 메모리와 토큰 생성 시간을 4배 절감합니다.


---

*Generated on 2025-09-23 23:59:14*