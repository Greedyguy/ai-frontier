---
keywords:
  - Large Language Model
  - Think-Verbalize-Speak Framework
  - ReVerT Verbalizer
  - Spoken Dialogue System
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.16028
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:27:10.854013",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Think-Verbalize-Speak Framework",
    "ReVerT Verbalizer",
    "Spoken Dialogue System"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Think-Verbalize-Speak Framework": 0.8,
    "ReVerT Verbalizer": 0.78,
    "Spoken Dialogue System": 0.7
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
        "rationale": "Large Language Models are central to the paper's framework and connect well with existing NLP concepts.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Think-Verbalize-Speak",
        "canonical": "Think-Verbalize-Speak Framework",
        "aliases": [
          "TVS"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel framework introduced in the paper, crucial for understanding the proposed methodology.",
        "novelty_score": 0.95,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "ReVerT",
        "canonical": "ReVerT Verbalizer",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "ReVerT is a newly introduced component that enhances the framework's efficiency, making it a key concept.",
        "novelty_score": 0.92,
        "connectivity_score": 0.55,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "Spoken Dialogue Systems",
        "canonical": "Spoken Dialogue System",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This is a specific application area for the framework, linking it to broader NLP and AI systems.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "spoken communication",
      "speech-friendly outputs"
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
      "candidate_surface": "Think-Verbalize-Speak",
      "resolved_canonical": "Think-Verbalize-Speak Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "ReVerT",
      "resolved_canonical": "ReVerT Verbalizer",
      "decision": "linked",
      "scores": {
        "novelty": 0.92,
        "connectivity": 0.55,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Spoken Dialogue Systems",
      "resolved_canonical": "Spoken Dialogue System",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Think, Verbalize, then Speak: Bridging Complex Thoughts and Comprehensible Speech

**Korean Title:** 생각하고, 말로 표현한 후, 말하기: 복잡한 사고와 이해 가능한 언어의 연결

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16028.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.16028](https://arxiv.org/abs/2509.16028)

## 🔗 유사한 논문
- [[2025-09-19/ThinkAct_ Vision-Language-Action Reasoning via Reinforced Visual Latent Planning_20250919|ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning]] (85.1% similar)
- [[2025-09-19/WebCoT_ Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback_20250919|WebCoT: Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback]] (85.1% similar)
- [[2025-09-22/Temporal Reasoning with Large Language Models Augmented by Evolving Knowledge Graphs_20250922|Temporal Reasoning with Large Language Models Augmented by Evolving Knowledge Graphs]] (84.8% similar)
- [[2025-09-22/REFER_ Mitigating Bias in Opinion Summarisation via Frequency Framed Prompting_20250922|REFER: Mitigating Bias in Opinion Summarisation via Frequency Framed Prompting]] (84.3% similar)
- [[2025-09-22/Efficient Real-time Refinement of Language Model Text Generation_20250922|Efficient Real-time Refinement of Language Model Text Generation]] (84.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Spoken Dialogue System|Spoken Dialogue System]]
**⚡ Unique Technical**: [[keywords/Think-Verbalize-Speak Framework|Think-Verbalize-Speak Framework]], [[keywords/ReVerT Verbalizer|ReVerT Verbalizer]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16028v1 Announce Type: cross 
Abstract: Spoken dialogue systems increasingly employ large language models (LLMs) to leverage their advanced reasoning capabilities. However, direct application of LLMs in spoken communication often yield suboptimal results due to mismatches between optimal textual and verbal delivery. While existing approaches adapt LLMs to produce speech-friendly outputs, their impact on reasoning performance remains underexplored. In this work, we propose Think-Verbalize-Speak, a framework that decouples reasoning from spoken delivery to preserve the full reasoning capacity of LLMs. Central to our method is verbalizing, an intermediate step that translates thoughts into natural, speech-ready text. We also introduce ReVerT, a latency-efficient verbalizer based on incremental and asynchronous summarization. Experiments across multiple benchmarks show that our method enhances speech naturalness and conciseness with minimal impact on reasoning. The project page with the dataset and the source code is available at https://yhytoto12.github.io/TVS-ReVerT

## 🔍 Abstract (한글 번역)

arXiv:2509.16028v1 발표 유형: 교차  
초록: 음성 대화 시스템은 점점 더 고급 추론 능력을 활용하기 위해 대형 언어 모델(LLM)을 사용합니다. 그러나 LLM을 음성 통신에 직접 적용할 경우 최적의 텍스트 전달과 음성 전달 간의 불일치로 인해 종종 최적이 아닌 결과를 초래합니다. 기존 접근 방식은 LLM을 조정하여 음성 친화적인 출력을 생성하지만, 이러한 조정이 추론 성능에 미치는 영향은 충분히 탐구되지 않았습니다. 본 연구에서는 LLM의 완전한 추론 능력을 보존하기 위해 추론과 음성 전달을 분리하는 Think-Verbalize-Speak라는 프레임워크를 제안합니다. 우리의 방법의 핵심은 생각을 자연스럽고 음성 준비가 된 텍스트로 변환하는 중간 단계인 '구두화'입니다. 또한, 점진적이고 비동기적인 요약을 기반으로 한 지연 효율적인 구두화 도구인 ReVerT를 소개합니다. 여러 벤치마크에 걸친 실험은 우리의 방법이 추론에 거의 영향을 미치지 않으면서도 음성의 자연스러움과 간결성을 향상시킨다는 것을 보여줍니다. 데이터셋과 소스 코드를 포함한 프로젝트 페이지는 https://yhytoto12.github.io/TVS-ReVerT에서 확인할 수 있습니다.

## 📝 요약

이 연구는 대화형 시스템에서 대형 언어 모델(LLM)의 추론 능력을 유지하면서도 음성 전달의 자연스러움을 개선하기 위한 새로운 프레임워크인 Think-Verbalize-Speak를 제안합니다. 이 방법은 추론과 음성 전달을 분리하여 LLM의 추론 능력을 최대한 활용하고자 합니다. 핵심은 'Verbalizing'이라는 중간 단계를 도입하여 생각을 자연스럽고 음성에 적합한 텍스트로 변환하는 것입니다. 또한, ReVerT라는 지연 효율적인 음성 변환기를 소개하여 점진적이고 비동기적인 요약을 통해 이를 구현합니다. 여러 벤치마크 실험 결과, 이 방법이 추론 성능에 거의 영향을 주지 않으면서도 음성의 자연스러움과 간결성을 향상시킴을 확인했습니다.

## 🎯 주요 포인트

- 1. 대화형 시스템에서 대형 언어 모델(LLM)의 추론 능력을 활용하기 위해 Think-Verbalize-Speak 프레임워크를 제안합니다.
- 2. 제안된 프레임워크는 추론과 발화를 분리하여 LLM의 추론 능력을 최대한 보존합니다.
- 3. ReVerT라는 비동기 요약 기반의 효율적인 발화 도구를 도입하여 발화의 자연스러움과 간결성을 향상시킵니다.
- 4. 여러 벤치마크 실험에서 제안된 방법이 추론 성능에 거의 영향을 주지 않으면서 발화의 자연스러움과 간결성을 개선하는 것으로 나타났습니다.
- 5. 데이터셋과 소스 코드는 프로젝트 페이지(https://yhytoto12.github.io/TVS-ReVerT)에서 제공됩니다.


---

*Generated on 2025-09-23 09:27:10*