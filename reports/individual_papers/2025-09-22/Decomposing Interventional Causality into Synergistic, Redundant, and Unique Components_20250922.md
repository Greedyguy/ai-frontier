---
keywords:
  - Partial Information Decomposition
  - Möbius Inversion
  - Transformer
  - Causal Power Distribution
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2501.11447
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:34:31.432982",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Partial Information Decomposition",
    "Möbius Inversion",
    "Transformer",
    "Causal Power Distribution"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Partial Information Decomposition": 0.78,
    "Möbius Inversion": 0.72,
    "Transformer": 0.85,
    "Causal Power Distribution": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Partial Information Decomposition",
        "canonical": "Partial Information Decomposition",
        "aliases": [
          "PID"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's framework and offers a unique perspective on causal analysis.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Möbius inversion",
        "canonical": "Möbius Inversion",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Möbius inversion is a mathematical technique crucial for the decomposition method proposed.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      },
      {
        "surface": "Transformer language model",
        "canonical": "Transformer",
        "aliases": [
          "Transformer model"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are widely used in AI and their inclusion helps link to broader AI concepts.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Causal power distribution",
        "canonical": "Causal Power Distribution",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Understanding how causal power is distributed is essential for analyzing complex systems.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "interventional",
      "causal effects",
      "complex systems"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Partial Information Decomposition",
      "resolved_canonical": "Partial Information Decomposition",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Möbius inversion",
      "resolved_canonical": "Möbius Inversion",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Transformer language model",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Causal power distribution",
      "resolved_canonical": "Causal Power Distribution",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Decomposing Interventional Causality into Synergistic, Redundant, and Unique Components

**Korean Title:** 중재적 인과성을 시너지, 중복, 고유 구성 요소로 분해하기

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2501.11447.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2501.11447](https://arxiv.org/abs/2501.11447)

## 🔗 유사한 논문
- [[2025-09-19/CausalPre_ Scalable and Effective Data Pre-processing for Causal Fairness_20250919|CausalPre: Scalable and Effective Data Pre-processing for Causal Fairness]] (80.7% similar)
- [[2025-09-19/The Sum Leaks More Than Its Parts_ Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration_20250919|The Sum Leaks More Than Its Parts: Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration]] (79.4% similar)
- [[2025-09-19/How Bad Is Forming Your Own Multidimensional Opinion?_20250919|How Bad Is Forming Your Own Multidimensional Opinion?]] (78.9% similar)
- [[2025-09-22/Gradient Alignment in Physics-informed Neural Networks_ A Second-Order Optimization Perspective_20250922|Gradient Alignment in Physics-informed Neural Networks: A Second-Order Optimization Perspective]] (78.8% similar)
- [[2025-09-22/Negotiated Representations to Prevent Overfitting in Machine Learning Applications_20250922|Negotiated Representations to Prevent Overfitting in Machine Learning Applications]] (78.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**⚡ Unique Technical**: [[keywords/Partial Information Decomposition|Partial Information Decomposition]], [[keywords/Möbius Inversion|Möbius Inversion]], [[keywords/Causal Power Distribution|Causal Power Distribution]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2501.11447v2 Announce Type: replace 
Abstract: We introduce a novel framework for decomposing interventional causal effects into synergistic, redundant, and unique components, building on the intuition of Partial Information Decomposition (PID) and the principle of M\"obius inversion. While recent work has explored a similar decomposition of an observational measure, we argue that a proper causal decomposition must be interventional in nature. We develop a mathematical approach that systematically quantifies how causal power is distributed among variables in a system, using a recently derived closed-form expression for the M\"obius function of the redundancy lattice. The formalism is then illustrated by decomposing the causal power in logic gates, cellular automata, chemical reaction networks, and a transformer language model. Our results reveal how the distribution of causal power can be context- and parameter-dependent. The decomposition provides new insights into complex systems by revealing how causal influences are shared and combined among multiple variables, with potential applications ranging from attribution of responsibility in legal or AI systems, to the analysis of biological networks or climate models.

## 🔍 Abstract (한글 번역)

arXiv:2501.11447v2 발표 유형: 교체  
초록: 우리는 부분 정보 분해(PID)의 직관과 뫼비우스 반전 원칙을 기반으로 하여, 중재적 인과 효과를 상호작용적, 중복적, 고유한 구성 요소로 분해하는 새로운 프레임워크를 소개합니다. 최근 연구에서는 관찰적 측정의 유사한 분해를 탐구했지만, 적절한 인과 분해는 본질적으로 중재적이어야 한다고 주장합니다. 우리는 중복 격자의 뫼비우스 함수에 대한 최근에 도출된 닫힌 형태의 표현식을 사용하여 시스템 내 변수들 간에 인과적 힘이 어떻게 분배되는지를 체계적으로 정량화하는 수학적 접근법을 개발합니다. 이 형식주의는 논리 게이트, 셀룰러 오토마타, 화학 반응 네트워크, 변환기 언어 모델에서 인과적 힘을 분해함으로써 설명됩니다. 우리의 결과는 인과적 힘의 분배가 맥락 및 매개 변수에 따라 어떻게 달라질 수 있는지를 보여줍니다. 이 분해는 여러 변수 간에 인과적 영향이 어떻게 공유되고 결합되는지를 밝혀 복잡한 시스템에 대한 새로운 통찰을 제공합니다. 이는 법적 또는 AI 시스템에서의 책임 귀속부터 생물학적 네트워크나 기후 모델의 분석에 이르기까지 다양한 응용 가능성을 가집니다.

## 📝 요약

이 논문은 중재적 인과 효과를 시너지, 중복, 고유 구성 요소로 분해하는 새로운 프레임워크를 제안합니다. 이는 부분 정보 분해(PID)와 뫼비우스 반전 원리에 기반합니다. 저자들은 최근 관찰적 측정의 유사한 분해가 연구되었지만, 적절한 인과 분해는 중재적이어야 한다고 주장합니다. 이 연구는 뫼비우스 함수의 폐쇄형 표현식을 사용하여 시스템 내 변수들 간의 인과적 영향력을 체계적으로 정량화하는 수학적 접근법을 개발했습니다. 논문은 논리 게이트, 셀룰러 오토마타, 화학 반응 네트워크, 트랜스포머 언어 모델을 통해 인과적 힘의 분포가 맥락과 매개변수에 따라 달라질 수 있음을 보여줍니다. 이 분해는 복잡한 시스템에서 인과적 영향이 어떻게 공유되고 결합되는지를 밝혀주며, 법적 책임 추적, AI 시스템 분석, 생물학적 네트워크 또는 기후 모델 분석 등 다양한 분야에 응용될 수 있습니다.

## 🎯 주요 포인트

- 1. 본 연구는 개입적 인과 효과를 시너지, 중복, 고유 성분으로 분해하는 새로운 프레임워크를 제안합니다.
- 2. 인과적 분해는 관찰적 측정이 아닌 개입적 성격을 가져야 한다고 주장합니다.
- 3. 최근 도출된 중복 격자의 뫼비우스 함수의 닫힌 형태 표현을 사용하여 인과적 힘이 시스템 내 변수들 사이에 어떻게 분배되는지를 체계적으로 정량화합니다.
- 4. 논리 게이트, 셀룰러 오토마타, 화학 반응 네트워크, 트랜스포머 언어 모델에서 인과적 힘의 분해를 통해 맥락 및 매개변수에 따라 인과적 힘의 분포가 달라질 수 있음을 보여줍니다.
- 5. 이 분해는 복잡한 시스템에서 인과적 영향을 여러 변수 간에 어떻게 공유하고 결합하는지를 밝혀 새로운 통찰을 제공합니다.


---

*Generated on 2025-09-23 09:34:31*