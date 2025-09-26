---
keywords:
  - Virtual Screening
  - Subgraph-Driven Dynamic Propagation
  - Zero-Shot Learning
  - False Discovery Rate
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16273
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:10:54.514866",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Virtual Screening",
    "Subgraph-Driven Dynamic Propagation",
    "Zero-Shot Learning",
    "False Discovery Rate"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Virtual Screening": 0.78,
    "Subgraph-Driven Dynamic Propagation": 0.85,
    "Zero-Shot Learning": 0.82,
    "False Discovery Rate": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Virtual Screening",
        "canonical": "Virtual Screening",
        "aliases": [
          "VS"
        ],
        "category": "unique_technical",
        "rationale": "Virtual Screening is a specific technique central to the paper's focus, providing a unique link to bioinformatics and cheminformatics fields.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Subgraph-Driven Dynamic Propagation",
        "canonical": "Subgraph-Driven Dynamic Propagation",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is a novel method introduced in the paper, crucial for understanding the proposed framework's mechanism.",
        "novelty_score": 0.9,
        "connectivity_score": 0.68,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "Zero-Shot Conditions",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-Shot"
        ],
        "category": "specific_connectable",
        "rationale": "Zero-Shot Learning is a trending concept that aligns with the paper's evaluation conditions, facilitating connections to machine learning contexts.",
        "novelty_score": 0.5,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "False Discovery Rate",
        "canonical": "False Discovery Rate",
        "aliases": [
          "FDR"
        ],
        "category": "broad_technical",
        "rationale": "False Discovery Rate is a statistical measure relevant to the paper's methodology, linking to broader statistical analysis discussions.",
        "novelty_score": 0.4,
        "connectivity_score": 0.75,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
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
      "candidate_surface": "Virtual Screening",
      "resolved_canonical": "Virtual Screening",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Subgraph-Driven Dynamic Propagation",
      "resolved_canonical": "Subgraph-Driven Dynamic Propagation",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.68,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Zero-Shot Conditions",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "False Discovery Rate",
      "resolved_canonical": "False Discovery Rate",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.75,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# SubDyve: Subgraph-Driven Dynamic Propagation for Virtual Screening Enhancement Controlling False Positive

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16273.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16273](https://arxiv.org/abs/2509.16273)

## 🔗 유사한 논문
- [[2025-09-18/Structure-Aware Contrastive Learning with Fine-Grained Binding Representations for Drug Discovery_20250918|Structure-Aware Contrastive Learning with Fine-Grained Binding Representations for Drug Discovery]] (81.0% similar)
- [[2025-09-22/Monte Carlo Tree Diffusion with Multiple Experts for Protein Design_20250922|Monte Carlo Tree Diffusion with Multiple Experts for Protein Design]] (77.1% similar)
- [[2025-09-19/jXBW_ Fast Substructure Search for Large-Scale JSONL Datasets with LLM Applications_20250919|jXBW: Fast Substructure Search for Large-Scale JSONL Datasets with LLM Applications]] (76.6% similar)
- [[2025-09-22/DPC-QA Net_ A No-Reference Dual-Stream Perceptual and Cellular Quality Assessment Network for Histopathology Images_20250922|DPC-QA Net: A No-Reference Dual-Stream Perceptual and Cellular Quality Assessment Network for Histopathology Images]] (76.5% similar)
- [[2025-09-22/A Multi-Scale Graph Neural Process with Cross-Drug Co-Attention for Drug-Drug Interactions Prediction_20250922|A Multi-Scale Graph Neural Process with Cross-Drug Co-Attention for Drug-Drug Interactions Prediction]] (76.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/False Discovery Rate|False Discovery Rate]]
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Virtual Screening|Virtual Screening]], [[keywords/Subgraph-Driven Dynamic Propagation|Subgraph-Driven Dynamic Propagation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16273v1 Announce Type: cross 
Abstract: Virtual screening (VS) aims to identify bioactive compounds from vast chemical libraries, but remains difficult in low-label regimes where only a few actives are known. Existing methods largely rely on general-purpose molecular fingerprints and overlook class-discriminative substructures critical to bioactivity. Moreover, they consider molecules independently, limiting effectiveness in low-label regimes. We introduce SubDyve, a network-based VS framework that constructs a subgraph-aware similarity network and propagates activity signals from a small known actives. When few active compounds are available, SubDyve performs iterative seed refinement, incrementally promoting new candidates based on local false discovery rate. This strategy expands the seed set with promising candidates while controlling false positives from topological bias and overexpansion. We evaluate SubDyve on ten DUD-E targets under zero-shot conditions and on the CDK7 target with a 10-million-compound ZINC dataset. SubDyve consistently outperforms existing fingerprint or embedding-based approaches, achieving margins of up to +34.0 on the BEDROC and +24.6 on the EF1% metric.

## 📝 요약

Virtual screening(VS)은 방대한 화학 라이브러리에서 생리활성 화합물을 식별하는 것을 목표로 하지만, 알려진 활성 화합물이 적은 경우 어려움을 겪습니다. 기존 방법은 일반적인 분자 지문에 의존하며, 생리활성에 중요한 클래스 구별적 부분구조를 간과합니다. 우리는 SubDyve라는 네트워크 기반 VS 프레임워크를 소개합니다. 이는 부분 그래프 인식 유사성 네트워크를 구축하고, 소수의 알려진 활성 화합물로부터 활동 신호를 전파합니다. SubDyve는 적은 활성 화합물이 있을 때, 지역적 허위 발견율에 기반하여 새로운 후보를 점진적으로 촉진하는 반복적인 시드 정제 전략을 사용합니다. 이는 유망한 후보로 시드 집합을 확장하면서 위상적 편향과 과도한 확장을 제어합니다. SubDyve는 DUD-E의 10개 표적과 1천만 개의 ZINC 데이터셋을 사용한 CDK7 표적에서 기존 방법을 일관되게 능가하며, BEDROC에서 최대 +34.0, EF1%에서 +24.6의 성능 향상을 보였습니다.

## 🎯 주요 포인트

- 1. SubDyve는 소수의 알려진 활성 화합물로부터 활동 신호를 전파하는 서브그래프 인식 유사성 네트워크를 구축하는 네트워크 기반 가상 스크리닝(VS) 프레임워크입니다.
- 2. SubDyve는 로컬 허위 발견율을 기반으로 새로운 후보를 점진적으로 승격시키는 반복적인 시드 정제 과정을 수행하여 시드 세트를 확장합니다.
- 3. SubDyve는 DUD-E 타겟과 1천만 개의 화합물이 포함된 ZINC 데이터셋의 CDK7 타겟에서 기존 방법보다 최대 +34.0(BEDROC) 및 +24.6(EF1%)의 성능 향상을 보였습니다.
- 4. 기존 방법들은 일반적인 분자 지문에 의존하며, 생물활성에 중요한 클래스 구별적 하위 구조를 간과합니다.
- 5. SubDyve는 위상적 편향과 과도한 확장을 제어하면서 유망한 후보를 포함하여 시드 세트를 확장합니다.


---

*Generated on 2025-09-23 23:10:54*