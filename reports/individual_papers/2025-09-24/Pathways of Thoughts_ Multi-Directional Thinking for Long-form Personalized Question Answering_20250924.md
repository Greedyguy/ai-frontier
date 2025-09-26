<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:11:36.940631",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Personalized Question Answering",
    "Pathways of Thoughts",
    "Reasoning Trajectories"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.8,
    "Personalized Question Answering": 0.75,
    "Pathways of Thoughts": 0.78,
    "Reasoning Trajectories": 0.7
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
        "rationale": "Central to the proposed method, connecting it to existing LLM research.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      },
      {
        "surface": "Personalized Question Answering",
        "canonical": "Personalized Question Answering",
        "aliases": [
          "Personalized QA"
        ],
        "category": "unique_technical",
        "rationale": "Focus of the paper, highlighting a niche area in QA systems.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Pathways of Thoughts",
        "canonical": "Pathways of Thoughts",
        "aliases": [
          "PoT"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel inference-stage method specific to this research.",
        "novelty_score": 0.85,
        "connectivity_score": 0.55,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Reasoning Trajectories",
        "canonical": "Reasoning Trajectories",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Describes the diverse reasoning paths explored by the method.",
        "novelty_score": 0.65,
        "connectivity_score": 0.5,
        "specificity_score": 0.75,
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
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Personalized Question Answering",
      "resolved_canonical": "Personalized Question Answering",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Pathways of Thoughts",
      "resolved_canonical": "Pathways of Thoughts",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.55,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Reasoning Trajectories",
      "resolved_canonical": "Reasoning Trajectories",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.5,
        "specificity": 0.75,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Pathways of Thoughts: Multi-Directional Thinking for Long-form Personalized Question Answering

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19094.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.19094](https://arxiv.org/abs/2509.19094)

## 🔗 유사한 논문
- [[2025-09-23/LaMP-QA_ A Benchmark for Personalized Long-form Question Answering_20250923|LaMP-QA: A Benchmark for Personalized Long-form Question Answering]] (90.1% similar)
- [[2025-09-23/QA-prompting_ Improving Summarization with Large Language Models using Question-Answering_20250923|QA-prompting: Improving Summarization with Large Language Models using Question-Answering]] (85.2% similar)
- [[2025-09-23/RephQA_ Evaluating Readability of Large Language Models in Public Health Question Answering_20250923|RephQA: Evaluating Readability of Large Language Models in Public Health Question Answering]] (84.2% similar)
- [[2025-09-23/A Survey of Personalized Large Language Models_ Progress and Future Directions_20250923|A Survey of Personalized Large Language Models: Progress and Future Directions]] (84.1% similar)
- [[2025-09-22/MMAPG_ A Training-Free Framework for Multimodal Multi-hop Question Answering via Adaptive Planning Graphs_20250922|MMAPG: A Training-Free Framework for Multimodal Multi-hop Question Answering via Adaptive Planning Graphs]] (84.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Personalized Question Answering|Personalized Question Answering]], [[keywords/Pathways of Thoughts|Pathways of Thoughts]], [[keywords/Reasoning Trajectories|Reasoning Trajectories]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19094v1 Announce Type: cross 
Abstract: Personalization is essential for adapting question answering (QA) systems to user-specific information needs, thereby improving both accuracy and user satisfaction. However, personalized QA remains relatively underexplored due to challenges such as inferring preferences from long, noisy, and implicit contexts, and generating responses that are simultaneously correct, contextually appropriate, and aligned with user expectations and background knowledge. To address these challenges, we propose Pathways of Thoughts (PoT), an inference-stage method that applies to any large language model (LLM) without requiring task-specific fine-tuning. The approach models the reasoning of an LLM as an iterative decision process, where the model dynamically selects among cognitive operations such as reasoning, revision, personalization, and clarification. This enables exploration of multiple reasoning trajectories, producing diverse candidate responses that capture different perspectives. PoT then aggregates and reweights these candidates according to inferred user preferences, yielding a final personalized response that benefits from the complementary strengths of diverse reasoning paths. Experiments on the LaMP-QA benchmark for personalized QA show that PoT consistently outperforms competitive baselines, achieving up to a 13.1% relative improvement. Human evaluation corroborates these results, with annotators preferring outputs from PoT in 66% of cases and reporting ties in only 15% of cases.

## 📝 요약

이 논문은 개인화된 질문 응답 시스템(QA)의 발전을 위해 'Pathways of Thoughts (PoT)'라는 방법론을 제안합니다. PoT는 대형 언어 모델(LLM)의 추론 과정을 반복적 의사 결정 과정으로 모델링하여, 추론, 수정, 개인화, 명확화 등의 인지적 작업을 동적으로 선택합니다. 이를 통해 다양한 추론 경로를 탐색하고, 사용자 선호에 맞춘 개인화된 응답을 생성합니다. LaMP-QA 벤치마크 실험에서 PoT는 기존 방법들보다 최대 13.1% 더 나은 성능을 보였으며, 인간 평가에서도 66%의 선호도를 얻었습니다.

## 🎯 주요 포인트

- 1. 개인화된 질문 응답 시스템은 사용자 맞춤형 정보 요구에 적응하여 정확성과 사용자 만족도를 향상시킨다.
- 2. Pathways of Thoughts (PoT)는 대규모 언어 모델에 적용 가능한 추론 단계 방법으로, 특정 작업에 대한 미세 조정 없이 개인화된 응답을 생성한다.
- 3. PoT는 다양한 인지 작업을 통해 여러 추론 경로를 탐색하고, 사용자 선호에 따라 후보 응답을 집계 및 재가중하여 최종 개인화된 응답을 제공한다.
- 4. LaMP-QA 벤치마크 실험에서 PoT는 최대 13.1%의 상대적 개선을 보이며 경쟁력 있는 기준 모델들을 능가한다.
- 5. 인간 평가에서 PoT의 결과물이 66%의 사례에서 선호되었으며, 15%의 사례에서 동점으로 평가되었다.


---

*Generated on 2025-09-24 14:11:36*