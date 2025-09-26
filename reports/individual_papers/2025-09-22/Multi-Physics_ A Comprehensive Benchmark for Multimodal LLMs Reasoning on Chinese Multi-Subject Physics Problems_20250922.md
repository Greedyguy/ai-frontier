---
keywords:
  - Multimodal Learning
  - Physics Reasoning
  - Chain-of-Thought Reasoning
  - Vision-Language Model
category: cs.CL
publish_date: 2025-09-22
arxiv_id: 2509.15839
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:35:00.439203",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Physics Reasoning",
    "Chain-of-Thought Reasoning",
    "Vision-Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.8,
    "Physics Reasoning": 0.72,
    "Chain-of-Thought Reasoning": 0.78,
    "Vision-Language Model": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multimodal LLMs",
        "canonical": "Multimodal Learning",
        "aliases": [
          "MLLMs"
        ],
        "category": "specific_connectable",
        "rationale": "Multimodal Learning is crucial for linking various modalities in language models, enhancing understanding across different data types.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Chinese physics reasoning",
        "canonical": "Physics Reasoning",
        "aliases": [
          "Chinese Physics"
        ],
        "category": "unique_technical",
        "rationale": "This term is specific to the paper's focus on evaluating reasoning in physics, particularly in a Chinese context.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
      },
      {
        "surface": "Chain-of-thought",
        "canonical": "Chain-of-Thought Reasoning",
        "aliases": [
          "Step-by-step reasoning"
        ],
        "category": "specific_connectable",
        "rationale": "Chain-of-Thought Reasoning is a key concept for understanding the logical process in multimodal models.",
        "novelty_score": 0.65,
        "connectivity_score": 0.82,
        "specificity_score": 0.76,
        "link_intent_score": 0.78
      },
      {
        "surface": "Visual information",
        "canonical": "Vision-Language Model",
        "aliases": [
          "Visual Data"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models are central to integrating visual information with language processing, a core aspect of the study.",
        "novelty_score": 0.6,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "evaluation benchmarks",
      "difficulty levels",
      "final answer accuracy"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multimodal LLMs",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Chinese physics reasoning",
      "resolved_canonical": "Physics Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Chain-of-thought",
      "resolved_canonical": "Chain-of-Thought Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.82,
        "specificity": 0.76,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Visual information",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Multi-Physics: A Comprehensive Benchmark for Multimodal LLMs Reasoning on Chinese Multi-Subject Physics Problems

**Korean Title:** 멀티 물리학: 중국의 다중 과목 물리 문제에 대한 다중 모달 대형 언어 모델(LLM)의 추론을 위한 종합 벤치마크

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15839.pdf)
**Category**: cs.CL
**Published**: 2025-09-22
**ArXiv ID**: [2509.15839](https://arxiv.org/abs/2509.15839)

## 🔗 유사한 논문
- [[2025-09-22/Perception-R1_ Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward_20250922|Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward]] (84.8% similar)
- [[2025-09-22/HiPhO_ How Far Are (M)LLMs from Humans in the Latest High School Physics Olympiad Benchmark?_20250922|HiPhO: How Far Are (M)LLMs from Humans in the Latest High School Physics Olympiad Benchmark?]] (84.7% similar)
- [[2025-09-22/How Good are Foundation Models in Step-by-Step Embodied Reasoning?_20250922|How Good are Foundation Models in Step-by-Step Embodied Reasoning?]] (84.3% similar)
- [[2025-09-22/DivLogicEval_ A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models_20250922|DivLogicEval: A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models]] (84.2% similar)
- [[2025-09-19/A Multi-To-One Interview Paradigm for Efficient MLLM Evaluation_20250919|A Multi-To-One Interview Paradigm for Efficient MLLM Evaluation]] (82.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]], [[keywords/Chain-of-Thought Reasoning|Chain-of-Thought Reasoning]]
**⚡ Unique Technical**: [[keywords/Physics Reasoning|Physics Reasoning]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15839v1 Announce Type: new 
Abstract: While multimodal LLMs (MLLMs) demonstrate remarkable reasoning progress, their application in specialized scientific domains like physics reveals significant gaps in current evaluation benchmarks. Specifically, existing benchmarks often lack fine-grained subject coverage, neglect the step-by-step reasoning process, and are predominantly English-centric, failing to systematically evaluate the role of visual information. Therefore, we introduce \textbf {Multi-Physics} for Chinese physics reasoning, a comprehensive benchmark that includes 5 difficulty levels, featuring 1,412 image-associated, multiple-choice questions spanning 11 high-school physics subjects. We employ a dual evaluation framework to evaluate 20 different MLLMs, analyzing both final answer accuracy and the step-by-step integrity of their chain-of-thought. Furthermore, we systematically study the impact of difficulty level and visual information by comparing the model performance before and after changing the input mode. Our work provides not only a fine-grained resource for the community but also offers a robust methodology for dissecting the multimodal reasoning process of state-of-the-art MLLMs, and our dataset and code have been open-sourced: https://github.com/luozhongze/Multi-Physics.

## 🔍 Abstract (한글 번역)

arXiv:2509.15839v1 발표 유형: 신규  
초록: 다중 모드 대형 언어 모델(Multimodal LLMs, MLLMs)이 놀라운 추론 발전을 보여주고 있지만, 물리학과 같은 전문 과학 분야에서의 적용은 현재 평가 기준에서 상당한 격차를 드러냅니다. 특히, 기존의 벤치마크는 종종 세부적인 주제 범위가 부족하고, 단계별 추론 과정을 간과하며, 주로 영어 중심적이어서 시각 정보의 역할을 체계적으로 평가하지 못합니다. 따라서 우리는 중국 물리학 추론을 위한 포괄적인 벤치마크인 \textbf{Multi-Physics}를 도입합니다. 이는 5단계의 난이도를 포함하며, 11개의 고등학교 물리학 과목에 걸쳐 1,412개의 이미지 관련 객관식 질문을 특징으로 합니다. 우리는 20개의 서로 다른 MLLMs를 평가하기 위해 이중 평가 프레임워크를 사용하여 최종 답변의 정확성과 단계별 사고 과정의 일관성을 분석합니다. 또한, 입력 모드를 변경하기 전후의 모델 성능을 비교하여 난이도 수준과 시각 정보의 영향을 체계적으로 연구합니다. 우리의 연구는 커뮤니티에 세부적인 자원을 제공할 뿐만 아니라 최첨단 MLLMs의 다중 모드 추론 과정을 해부하기 위한 강력한 방법론을 제공합니다. 우리의 데이터셋과 코드는 오픈 소스로 공개되었습니다: https://github.com/luozhongze/Multi-Physics.

## 📝 요약

이 논문은 물리학 분야에서 멀티모달 대형 언어 모델(MLLM)의 평가 기준의 한계를 극복하기 위해 중국 물리학 추론을 위한 \textbf{Multi-Physics}라는 포괄적인 벤치마크를 제안합니다. 이 벤치마크는 11개의 고등학교 물리학 과목에 걸쳐 1,412개의 이미지 연관 다지선다형 질문을 포함하며, 5단계의 난이도로 구성되어 있습니다. 20개의 MLLM을 대상으로 최종 답변 정확성과 단계별 사고 과정의 일관성을 평가하는 이중 평가 체계를 사용합니다. 또한, 입력 모드 변경 전후의 모델 성능을 비교하여 난이도와 시각 정보의 영향을 체계적으로 연구합니다. 이 연구는 커뮤니티에 세부적인 자원을 제공하고 최신 MLLM의 멀티모달 추론 과정을 분석할 수 있는 강력한 방법론을 제시합니다. 데이터셋과 코드는 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 기존 평가 벤치마크는 세부적인 주제 범위와 단계별 추론 과정을 간과하며, 주로 영어 중심으로 시각 정보의 역할을 체계적으로 평가하지 못한다.
- 2. 'Multi-Physics'는 중국어 물리학 추론을 위한 포괄적인 벤치마크로, 5단계 난이도의 1,412개의 이미지 연관 다지선다형 질문을 포함하고 있다.
- 3. 20개의 다양한 MLLM을 평가하기 위해 최종 답변 정확도와 단계별 사고 과정의 일관성을 분석하는 이중 평가 프레임워크를 사용한다.
- 4. 난이도 수준과 시각 정보의 영향을 체계적으로 연구하여 입력 모드를 변경하기 전후의 모델 성능을 비교한다.
- 5. 본 연구는 커뮤니티에 세부적인 자원을 제공할 뿐만 아니라, 최신 MLLM의 다중 모달 추론 과정을 분석하기 위한 견고한 방법론을 제시한다.


---

*Generated on 2025-09-23 11:35:00*