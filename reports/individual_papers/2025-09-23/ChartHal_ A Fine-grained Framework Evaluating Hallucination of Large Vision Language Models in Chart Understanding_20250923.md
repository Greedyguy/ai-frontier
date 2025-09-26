---
keywords:
  - Vision-Language Model
  - Chart Understanding
  - Hallucination in AI
  - Benchmarking
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17481
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:58:39.170814",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Model",
    "Chart Understanding",
    "Hallucination in AI",
    "Benchmarking"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision-Language Model": 0.85,
    "Chart Understanding": 0.78,
    "Hallucination in AI": 0.82,
    "Benchmarking": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Vision-Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "LVLMs"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models are a rapidly evolving area, crucial for understanding the intersection of visual and textual data.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.85
      },
      {
        "surface": "Chart Understanding",
        "canonical": "Chart Understanding",
        "aliases": [
          "Chart Comprehension"
        ],
        "category": "unique_technical",
        "rationale": "Chart Understanding is a specialized task that integrates visual perception and data interpretation, relevant for linking with data visualization studies.",
        "novelty_score": 0.65,
        "connectivity_score": 0.67,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Hallucination",
        "canonical": "Hallucination in AI",
        "aliases": [
          "AI Hallucination"
        ],
        "category": "specific_connectable",
        "rationale": "Understanding hallucination in AI models is critical for improving model accuracy and reliability.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.68,
        "link_intent_score": 0.82
      },
      {
        "surface": "Benchmark",
        "canonical": "Benchmarking",
        "aliases": [
          "Evaluation Benchmark"
        ],
        "category": "broad_technical",
        "rationale": "Benchmarking is essential for assessing model performance and is a common linking point in research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "accuracy"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Vision-Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Chart Understanding",
      "resolved_canonical": "Chart Understanding",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.67,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Hallucination",
      "resolved_canonical": "Hallucination in AI",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.68,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Benchmark",
      "resolved_canonical": "Benchmarking",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.5,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# ChartHal: A Fine-grained Framework Evaluating Hallucination of Large Vision Language Models in Chart Understanding

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17481.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17481](https://arxiv.org/abs/2509.17481)

## 🔗 유사한 논문
- [[2025-09-22/ORCA_ Agentic Reasoning For Hallucination and Adversarial Robustness in Vision-Language Models_20250922|ORCA: Agentic Reasoning For Hallucination and Adversarial Robustness in Vision-Language Models]] (81.8% similar)
- [[2025-09-19/METAL_ A Multi-Agent Framework for Chart Generation with Test-Time Scaling_20250919|METAL: A Multi-Agent Framework for Chart Generation with Test-Time Scaling]] (81.3% similar)
- [[2025-09-23/How Large Language Models are Designed to Hallucinate_20250923|How Large Language Models are Designed to Hallucinate]] (81.1% similar)
- [[2025-09-17/DSCC-HS_ A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models_20250917|DSCC-HS: A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models]] (80.3% similar)
- [[2025-09-22/ORIC_ Benchmarking Object Recognition in Incongruous Context for Large Vision-Language Models_20250922|ORIC: Benchmarking Object Recognition in Incongruous Context for Large Vision-Language Models]] (80.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Benchmarking|Benchmarking]]
**🔗 Specific Connectable**: [[keywords/Hallucination in AI|Hallucination in AI]]
**⚡ Unique Technical**: [[keywords/Chart Understanding|Chart Understanding]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17481v1 Announce Type: cross 
Abstract: Large Vision-Language Models (LVLMs) have recently demonstrated remarkable progress, yet hallucination remains a critical barrier, particularly in chart understanding, which requires sophisticated perceptual and cognitive abilities as well as rigorous factual accuracy. While prior work has investigated hallucinations and chart comprehension independently, their intersection remains largely unexplored. To address this gap, we present ChartHal, a benchmark that features a fine-grained taxonomy of hallucination scenarios in chart understanding, along with a human-validated dataset of 1,062 samples. Our evaluation shows that state-of-the-art LVLMs suffer from severe hallucinations on ChartHal, including proprietary models such as GPT-5 and o4-mini, which achieve only 34.46% and 22.79% accuracy, respectively. Further analysis reveals that questions involving information absent from or contradictory to charts are especially likely to trigger hallucinations, underscoring the urgent need for more robust mitigation strategies. Code and data are available at https://github.com/ymcui/ChartHal .

## 📝 요약

최근 대형 비전-언어 모델(LVLMs)은 큰 발전을 이루었지만, 특히 차트 이해에서 환각 문제가 여전히 큰 장애물로 남아 있습니다. 이에 따라, 차트 이해에서의 환각 시나리오를 세분화한 벤치마크 ChartHal을 제안하고, 1,062개의 샘플로 구성된 인간 검증 데이터셋을 제공합니다. 최신 LVLMs, 예를 들어 GPT-5와 o4-mini는 ChartHal에서 각각 34.46%와 22.79%의 정확도를 기록하며 심각한 환각 문제를 드러냈습니다. 특히 차트에 없는 정보나 모순된 정보를 포함한 질문에서 환각이 빈번하게 발생함을 확인했습니다. 이 연구는 보다 강력한 환각 완화 전략의 필요성을 강조합니다. 코드와 데이터는 https://github.com/ymcui/ChartHal 에서 확인할 수 있습니다.

## 🎯 주요 포인트

- 1. 대형 비전-언어 모델(LVLMs)은 최근 상당한 발전을 보였으나, 환각 현상이 여전히 중요한 문제로 남아 있으며, 특히 차트 이해에서 두드러진다.
- 2. ChartHal은 차트 이해에서의 환각 시나리오에 대한 세분화된 분류 체계를 제공하는 벤치마크로, 1,062개의 샘플로 구성된 인간 검증 데이터셋을 포함한다.
- 3. 최신 LVLMs는 ChartHal에서 심각한 환각 문제를 겪고 있으며, GPT-5와 o4-mini 같은 모델은 각각 34.46%와 22.79%의 정확도를 기록했다.
- 4. 차트에 없는 정보나 모순된 정보를 포함하는 질문이 환각을 유발할 가능성이 높아, 보다 강력한 완화 전략의 필요성이 강조된다.


---

*Generated on 2025-09-23 23:58:39*