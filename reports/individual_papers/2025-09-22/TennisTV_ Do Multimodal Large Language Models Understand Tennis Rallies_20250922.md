---
keywords:
  - Multimodal Learning
  - Sports Video Understanding
  - Temporal Reasoning
  - Frame Sampling Techniques
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.15602
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:02:26.911574",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Sports Video Understanding",
    "Temporal Reasoning",
    "Frame Sampling Techniques"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.82,
    "Sports Video Understanding": 0.79,
    "Temporal Reasoning": 0.8,
    "Frame Sampling Techniques": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multimodal large language models",
        "canonical": "Multimodal Learning",
        "aliases": [
          "MLLMs"
        ],
        "category": "specific_connectable",
        "rationale": "Links to the trending concept of integrating multiple data modalities, crucial for understanding complex video content.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Tennis video understanding",
        "canonical": "Sports Video Understanding",
        "aliases": [
          "TennisTV"
        ],
        "category": "unique_technical",
        "rationale": "Represents a niche application of video understanding, providing a unique context for evaluating MLLMs.",
        "novelty_score": 0.72,
        "connectivity_score": 0.68,
        "specificity_score": 0.81,
        "link_intent_score": 0.79
      },
      {
        "surface": "Temporal grounding",
        "canonical": "Temporal Reasoning",
        "aliases": [
          "Temporal alignment"
        ],
        "category": "specific_connectable",
        "rationale": "Critical for improving reasoning in sequential video tasks, linking to broader temporal analysis techniques.",
        "novelty_score": 0.58,
        "connectivity_score": 0.77,
        "specificity_score": 0.82,
        "link_intent_score": 0.8
      },
      {
        "surface": "Frame-sampling density",
        "canonical": "Frame Sampling Techniques",
        "aliases": [
          "Sampling density"
        ],
        "category": "unique_technical",
        "rationale": "Key for optimizing video analysis, offering a specific technical approach within video processing.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.79,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "benchmark",
      "assessment",
      "evaluation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multimodal large language models",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Tennis video understanding",
      "resolved_canonical": "Sports Video Understanding",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.68,
        "specificity": 0.81,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Temporal grounding",
      "resolved_canonical": "Temporal Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.77,
        "specificity": 0.82,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Frame-sampling density",
      "resolved_canonical": "Frame Sampling Techniques",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.79,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# TennisTV: Do Multimodal Large Language Models Understand Tennis Rallies?

**Korean Title:** 테니스TV: 다중모달 대형 언어 모델은 테니스 랠리를 이해하는가?

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15602.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.15602](https://arxiv.org/abs/2509.15602)

## 🔗 유사한 논문
- [[2025-09-19/BST_ Badminton Stroke-type Transformer for Skeleton-based Action Recognition in Racket Sports_20250919|BST: Badminton Stroke-type Transformer for Skeleton-based Action Recognition in Racket Sports]] (81.3% similar)
- [[2025-09-22/Predicting Language Models' Success at Zero-Shot Probabilistic Prediction_20250922|Predicting Language Models' Success at Zero-Shot Probabilistic Prediction]] (80.3% similar)
- [[2025-09-19/Ticket-Bench_ A Kickoff for Multilingual and Regionalized Agent Evaluation_20250919|Ticket-Bench: A Kickoff for Multilingual and Regionalized Agent Evaluation]] (80.1% similar)
- [[2025-09-19/A Multi-To-One Interview Paradigm for Efficient MLLM Evaluation_20250919|A Multi-To-One Interview Paradigm for Efficient MLLM Evaluation]] (80.1% similar)
- [[2025-09-19/Unleashing the Potential of Multimodal LLMs for Zero-Shot Spatio-Temporal Video Grounding_20250919|Unleashing the Potential of Multimodal LLMs for Zero-Shot Spatio-Temporal Video Grounding]] (80.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]], [[keywords/Temporal Reasoning|Temporal Reasoning]]
**⚡ Unique Technical**: [[keywords/Sports Video Understanding|Sports Video Understanding]], [[keywords/Frame Sampling Techniques|Frame Sampling Techniques]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15602v1 Announce Type: new 
Abstract: Multimodal large language models (MLLMs) excel at general video understanding but struggle with fast, high-frequency sports like tennis, where rally clips are short yet information-dense. To systematically evaluate MLLMs in this challenging domain, we present TennisTV, the first and most comprehensive benchmark for tennis video understanding. TennisTV models each rally as a temporal-ordered sequence of consecutive stroke events, using automated pipelines for filtering and question generation. It covers 8 tasks at rally and stroke levels and includes 2,500 human-verified questions. Evaluating 16 representative MLLMs, we provide the first systematic assessment of tennis video understanding. Results reveal substantial shortcomings and yield two key insights: (i) frame-sampling density should be tailored and balanced across tasks, and (ii) improving temporal grounding is essential for stronger reasoning.

## 🔍 Abstract (한글 번역)

arXiv:2509.15602v1 발표 유형: 신규  
초록: 다중 모달 대형 언어 모델(MLLMs)은 일반적인 비디오 이해에서 뛰어난 성능을 보이지만, 테니스와 같은 빠르고 고주파의 스포츠에서는 어려움을 겪습니다. 테니스의 랠리 클립은 짧지만 정보가 밀집되어 있기 때문입니다. 이 어려운 분야에서 MLLMs를 체계적으로 평가하기 위해, 우리는 테니스 비디오 이해를 위한 최초이자 가장 포괄적인 벤치마크인 TennisTV를 제시합니다. TennisTV는 각 랠리를 연속적인 스트로크 이벤트의 시간 순서로 모델링하며, 필터링과 질문 생성을 위한 자동화된 파이프라인을 사용합니다. 이 벤치마크는 랠리 및 스트로크 수준에서 8개의 과제를 다루며, 2,500개의 인간 검증 질문을 포함하고 있습니다. 16개의 대표적인 MLLMs를 평가하여 테니스 비디오 이해에 대한 최초의 체계적인 평가를 제공합니다. 결과는 상당한 단점을 드러내며 두 가지 주요 통찰을 제공합니다: (i) 프레임 샘플링 밀도는 과제 전반에 걸쳐 맞춤화되고 균형 잡혀야 하며, (ii) 더 강력한 추론을 위해 시간적 기반을 개선하는 것이 필수적입니다.

## 📝 요약

이 논문은 고속 스포츠인 테니스의 비디오 이해에 어려움을 겪는 다중모달 대형 언어 모델(MLLMs)의 성능을 평가하기 위해 TennisTV라는 벤치마크를 제시합니다. TennisTV는 각 랠리를 연속적인 스트로크 이벤트의 시간 순서로 모델링하며, 자동화된 파이프라인을 통해 필터링과 질문 생성을 수행합니다. 총 8개의 랠리 및 스트로크 수준의 과제를 포함하고, 2,500개의 인간 검증 질문을 제공합니다. 16개의 대표적인 MLLMs를 평가한 결과, 테니스 비디오 이해에서의 주요 문제점을 밝혀냈으며, 두 가지 주요 통찰을 제공합니다: (i) 프레임 샘플링 밀도는 과제에 맞게 조정되어야 하며, (ii) 더 강력한 추론을 위해 시간적 기반 개선이 필수적입니다.

## 🎯 주요 포인트

- 1. MLLMs는 일반적인 비디오 이해에서는 뛰어나지만, 테니스와 같은 빠르고 고빈도의 스포츠에서는 어려움을 겪는다.
- 2. TennisTV는 테니스 비디오 이해를 위한 최초이자 가장 포괄적인 벤치마크로, 랠리를 시간 순서대로 연속적인 스트로크 이벤트로 모델링한다.
- 3. TennisTV는 랠리 및 스트로크 수준에서 8개의 과제를 다루며, 2,500개의 인간 검증 질문을 포함한다.
- 4. 16개의 대표적인 MLLMs를 평가한 결과, 프레임 샘플링 밀도를 과제에 맞게 조정하고 균형을 맞춰야 하며, 시간적 근거를 개선하는 것이 중요하다는 두 가지 주요 통찰을 얻었다.


---

*Generated on 2025-09-23 12:02:26*