<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:29:41.369507",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Retrieval Augmented Generation",
    "Temporal Governance",
    "Memory Quadruple",
    "Model Editing"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Retrieval Augmented Generation": 0.82,
    "Temporal Governance": 0.78,
    "Memory Quadruple": 0.77,
    "Model Editing": 0.8
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
        "rationale": "Central to the paper's theme, linking to foundational concepts in NLP.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Retrieval Augmented Generation",
        "canonical": "Retrieval Augmented Generation",
        "aliases": [
          "RAG"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to trending techniques in LLMs for enhancing information retrieval.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Temporal Governance",
        "canonical": "Temporal Governance",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Introduces a novel concept for managing model updates over time.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Memory Quadruple",
        "canonical": "Memory Quadruple",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Defines a unique framework for understanding memory in LLMs.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.77
      },
      {
        "surface": "Model Editing",
        "canonical": "Model Editing",
        "aliases": [
          "ROME",
          "MEND",
          "MEMIT",
          "SERAC"
        ],
        "category": "specific_connectable",
        "rationale": "Relevant for linking to techniques in modifying model behavior post-training.",
        "novelty_score": 0.55,
        "connectivity_score": 0.82,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "mechanism",
      "evaluation",
      "governance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Model",
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
      "candidate_surface": "Retrieval Augmented Generation",
      "resolved_canonical": "Retrieval Augmented Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Temporal Governance",
      "resolved_canonical": "Temporal Governance",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Memory Quadruple",
      "resolved_canonical": "Memory Quadruple",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Model Editing",
      "resolved_canonical": "Model Editing",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.82,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Memory in Large Language Models: Mechanisms, Evaluation and Evolution

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18868.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18868](https://arxiv.org/abs/2509.18868)

## 🔗 유사한 논문
- [[2025-09-23/Synthetic POMDPs to Challenge Memory-Augmented RL_ Memory Demand Structure Modeling_20250923|Synthetic POMDPs to Challenge Memory-Augmented RL: Memory Demand Structure Modeling]] (86.1% similar)
- [[2025-09-23/EG-MLA_ Embedding-Gated Multi-head Latent Attention for Scalable and Efficient LLMs_20250923|EG-MLA: Embedding-Gated Multi-head Latent Attention for Scalable and Efficient LLMs]] (86.0% similar)
- [[2025-09-23/SEDM_ Scalable Self-Evolving Distributed Memory for Agents_20250923|SEDM: Scalable Self-Evolving Distributed Memory for Agents]] (83.7% similar)
- [[2025-09-23/Mitigating Forgetting in LLM Fine-Tuning via Low-Perplexity Token Learning_20250923|Mitigating Forgetting in LLM Fine-Tuning via Low-Perplexity Token Learning]] (83.7% similar)
- [[2025-09-22/It Depends_ Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge_20250922|It Depends: Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge]] (83.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Retrieval Augmented Generation|Retrieval Augmented Generation]], [[keywords/Model Editing|Model Editing]]
**⚡ Unique Technical**: [[keywords/Temporal Governance|Temporal Governance]], [[keywords/Memory Quadruple|Memory Quadruple]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18868v1 Announce Type: new 
Abstract: Under a unified operational definition, we define LLM memory as a persistent state written during pretraining, finetuning, or inference that can later be addressed and that stably influences outputs. We propose a four-part taxonomy (parametric, contextual, external, procedural/episodic) and a memory quadruple (location, persistence, write/access path, controllability). We link mechanism, evaluation, and governance via the chain write -> read -> inhibit/update. To avoid distorted comparisons across heterogeneous setups, we adopt a three-setting protocol (parametric only, offline retrieval, online retrieval) that decouples capability from information availability on the same data and timeline. On this basis we build a layered evaluation: parametric (closed-book recall, edit differential, memorization/privacy), contextual (position curves and the mid-sequence drop), external (answer correctness vs snippet attribution/faithfulness), and procedural/episodic (cross-session consistency and timeline replay, E MARS+). The framework integrates temporal governance and leakage auditing (freshness hits, outdated answers, refusal slices) and uncertainty reporting via inter-rater agreement plus paired tests with multiple-comparison correction. For updating and forgetting, we present DMM Gov: coordinating DAPT/TAPT, PEFT, model editing (ROME, MEND, MEMIT, SERAC), and RAG to form an auditable loop covering admission thresholds, rollout, monitoring, rollback, and change audits, with specs for timeliness, conflict handling, and long-horizon consistency. Finally, we give four testable propositions: minimum identifiability; a minimal evaluation card; causally constrained editing with verifiable forgetting; and when retrieval with small-window replay outperforms ultra-long-context reading. This yields a reproducible, comparable, and governable coordinate system for research and deployment.

## 📝 요약

이 논문은 대규모 언어 모델(LLM)의 메모리를 정의하고 이를 평가하기 위한 체계를 제안합니다. LLM 메모리는 사전 학습, 미세 조정, 추론 중에 기록되어 이후 출력에 영향을 미치는 지속적인 상태로 정의됩니다. 저자들은 메모리를 네 가지 유형(파라메트릭, 컨텍스추얼, 외부, 절차적/에피소드)으로 분류하고, 메모리의 위치, 지속성, 접근 경로, 제어 가능성을 포함한 메모리 사중주를 제안합니다. 또한, 메모리의 메커니즘, 평가, 관리 방식을 연결하여 일관된 평가 시스템을 구축합니다. 이 시스템은 파라메트릭, 컨텍스추얼, 외부, 절차적/에피소드 평가를 포함하며, 업데이트 및 망각을 위한 DMM Gov 프레임워크를 제시합니다. 마지막으로, 최소 식별성, 최소 평가 카드, 인과적으로 제한된 편집, 소규모 재생이 초장기 문맥 읽기를 능가하는 경우 등 네 가지 검증 가능한 제안을 제시합니다. 이를 통해 연구 및 배포를 위한 재현 가능하고 비교 가능하며 관리 가능한 시스템을 제공합니다.

## 🎯 주요 포인트

- 1. LLM 메모리를 사전 훈련, 미세 조정, 추론 중에 기록된 지속적인 상태로 정의하고, 이를 네 가지 분류(매개변수적, 맥락적, 외부적, 절차적/삽화적)와 메모리 4중주(위치, 지속성, 쓰기/접근 경로, 제어 가능성)로 제안합니다.
- 2. 이 연구는 세 가지 설정 프로토콜(매개변수적, 오프라인 검색, 온라인 검색)을 채택하여 동일한 데이터와 타임라인에서 정보 가용성과 능력을 분리합니다.
- 3. 평가 프레임워크는 매개변수적, 맥락적, 외부적, 절차적/삽화적 측면에서 계층화된 평가를 구축하며, 시간적 거버넌스와 누출 감사, 불확실성 보고를 통합합니다.
- 4. DMM Gov를 통해 업데이트와 망각을 조정하며, 이는 입학 임계값, 롤아웃, 모니터링, 롤백, 변경 감사 등을 포함하는 감사 가능한 루프를 형성합니다.
- 5. 최소 식별성, 최소 평가 카드, 인과적으로 제한된 편집과 검증 가능한 망각, 소창 재생을 통한 검색이 초장기 문맥 읽기를 능가하는 경우 등 네 가지 검증 가능한 명제를 제시합니다.


---

*Generated on 2025-09-24 13:29:41*