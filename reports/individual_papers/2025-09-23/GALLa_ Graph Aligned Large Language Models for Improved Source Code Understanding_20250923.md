---
keywords:
  - Graph Aligned Large Language Models
  - Graph Neural Network
  - Large Language Model
  - Cross-modal Alignment
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2409.04183
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:39:18.520412",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Aligned Large Language Models",
    "Graph Neural Network",
    "Large Language Model",
    "Cross-modal Alignment"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Aligned Large Language Models": 0.78,
    "Graph Neural Network": 0.82,
    "Large Language Model": 0.75,
    "Cross-modal Alignment": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Graph Aligned Large Language Models",
        "canonical": "Graph Aligned Large Language Models",
        "aliases": [
          "GALLa"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel framework combining graph neural networks with large language models, enhancing source code understanding.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Graph Neural Networks",
        "canonical": "Graph Neural Network",
        "aliases": [
          "GNN"
        ],
        "category": "specific_connectable",
        "rationale": "Graph neural networks are crucial for encoding structural information in source code, linking to existing graph-based methods.",
        "novelty_score": 0.4,
        "connectivity_score": 0.88,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Large language models are central to the study, providing a basis for integrating graph-based enhancements.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "Cross-modal alignment",
        "canonical": "Cross-modal Alignment",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Cross-modal alignment is essential for integrating structural graph information with language models.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "source code",
      "baseline LLM",
      "training time"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Graph Aligned Large Language Models",
      "resolved_canonical": "Graph Aligned Large Language Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Graph Neural Networks",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.88,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Cross-modal alignment",
      "resolved_canonical": "Cross-modal Alignment",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# GALLa: Graph Aligned Large Language Models for Improved Source Code Understanding

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2409.04183.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2409.04183](https://arxiv.org/abs/2409.04183)

## 🔗 유사한 논문
- [[2025-09-23/Generalizable End-to-End Tool-Use RL with Synthetic CodeGym_20250923|Generalizable End-to-End Tool-Use RL with Synthetic CodeGym]] (85.1% similar)
- [[2025-09-23/Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates_20250923|Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates]] (84.6% similar)
- [[2025-09-22/A Survey of Large Language Models for Data Challenges in Graphs_20250922|A Survey of Large Language Models for Data Challenges in Graphs]] (84.2% similar)
- [[2025-09-23/MapCoder-Lite_ Squeezing Multi-Agent Coding into a Single Small LLM_20250923|MapCoder-Lite: Squeezing Multi-Agent Coding into a Single Small LLM]] (84.0% similar)
- [[2025-09-19/Automated and Context-Aware Code Documentation Leveraging Advanced LLMs_20250919|Automated and Context-Aware Code Documentation Leveraging Advanced LLMs]] (83.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]], [[keywords/Cross-modal Alignment|Cross-modal Alignment]]
**⚡ Unique Technical**: [[keywords/Graph Aligned Large Language Models|Graph Aligned Large Language Models]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2409.04183v3 Announce Type: replace-cross 
Abstract: Programming languages possess rich semantic information - such as data flow - that is represented by graphs and not available from the surface form of source code. Recent code language models have scaled to billions of parameters, but model source code solely as text tokens while ignoring any other structural information. Conversely, models that do encode structural information of code make modifications to the Transformer architecture, limiting their scale and compatibility with pretrained LLMs. In this work, we take the best of both worlds with GALLa - Graph Aligned Large Language Models. GALLa utilizes graph neural networks and cross-modal alignment technologies to inject the structural information of code into LLMs as an auxiliary task during finetuning. This framework is both model-agnostic and task-agnostic, as it can be applied to any code LLM for any code downstream task, and requires the structural graph data only at training time from a corpus unrelated to the finetuning data, while incurring no cost at inference time over the baseline LLM. Experiments on five code tasks with seven different baseline LLMs ranging in size from 350M to 14B validate the effectiveness of GALLa, demonstrating consistent improvement over the baseline, even for powerful models such as LLaMA3 and Qwen2.5-Coder.

## 📝 요약

이 논문에서는 프로그래밍 언어의 구조적 정보를 활용하는 GALLa(그래프 정렬 대형 언어 모델)를 제안합니다. 기존의 코드 언어 모델은 소스 코드를 텍스트 토큰으로만 처리하지만, GALLa는 그래프 신경망과 교차 모달 정렬 기술을 사용해 코드의 구조적 정보를 대형 언어 모델에 주입합니다. 이 방법은 모델과 작업에 구애받지 않으며, 학습 시에만 구조적 그래프 데이터를 필요로 하고 추론 시에는 추가 비용이 발생하지 않습니다. 350M에서 14B까지 다양한 크기의 7개 기본 LLM을 사용한 5가지 코드 작업 실험에서 GALLa는 일관된 성능 향상을 보여주며, LLaMA3와 Qwen2.5-Coder와 같은 강력한 모델에서도 효과적임을 입증했습니다.

## 🎯 주요 포인트

- 1. 프로그래밍 언어의 풍부한 의미 정보를 그래프 형태로 표현하여 코드의 구조적 정보를 활용하는 GALLa 모델을 제안합니다.
- 2. GALLa는 그래프 신경망과 크로스 모달 정렬 기술을 사용하여 코드의 구조적 정보를 LLM에 주입합니다.
- 3. 이 프레임워크는 모델 및 작업에 구애받지 않으며, 코드 LLM의 다운스트림 작업에 적용할 수 있습니다.
- 4. GALLa는 학습 시에만 구조적 그래프 데이터를 필요로 하며, 추론 시에는 추가 비용이 들지 않습니다.
- 5. 실험 결과, GALLa는 다양한 크기의 LLM을 사용한 다섯 가지 코드 작업에서 일관된 성능 향상을 보여줍니다.


---

*Generated on 2025-09-24 00:39:18*