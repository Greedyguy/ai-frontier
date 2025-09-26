---
keywords:
  - Large Language Model
  - Local Differential Privacy
  - In-Context Learning
  - Privacy-Utility Trade-off
category: cs.CL
publish_date: 2025-09-22
arxiv_id: 2503.04990
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:42:00.732699",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Local Differential Privacy",
    "In-Context Learning",
    "Privacy-Utility Trade-off"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Local Differential Privacy": 0.78,
    "In-Context Learning": 0.8,
    "Privacy-Utility Trade-off": 0.77
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
        "rationale": "Central to the paper's focus on privacy in language models, linking to broader discussions in NLP.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Local Differential Privacy",
        "canonical": "Local Differential Privacy",
        "aliases": [
          "LDP"
        ],
        "category": "unique_technical",
        "rationale": "Key to the framework's approach to privacy, offering a unique angle on privacy mechanisms.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "In-Context Learning",
        "canonical": "In-Context Learning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Highlights the framework's innovative use of LLM capabilities, relevant to recent advancements in NLP.",
        "novelty_score": 0.6,
        "connectivity_score": 0.72,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "Privacy-Utility Trade-off",
        "canonical": "Privacy-Utility Trade-off",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Essential for understanding the balance achieved by the framework, crucial for privacy research.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
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
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Local Differential Privacy",
      "resolved_canonical": "Local Differential Privacy",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "In-Context Learning",
      "resolved_canonical": "In-Context Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.72,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Privacy-Utility Trade-off",
      "resolved_canonical": "Privacy-Utility Trade-off",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# DP-GTR: Differentially Private Prompt Protection via Group Text Rewriting

**Korean Title:** DP-GTR: 그룹 텍스트 재작성을 통한 차등 프라이버시 프롬프트 보호

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2503.04990.pdf)
**Category**: cs.CL
**Published**: 2025-09-22
**ArXiv ID**: [2503.04990](https://arxiv.org/abs/2503.04990)

## 🔗 유사한 논문
- [[2025-09-18/SynBench_ A Benchmark for Differentially Private Text Generation_20250918|SynBench: A Benchmark for Differentially Private Text Generation]] (85.0% similar)
- [[2025-09-19/The Sum Leaks More Than Its Parts_ Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration_20250919|The Sum Leaks More Than Its Parts: Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration]] (82.7% similar)
- [[2025-09-22/Personalized Language Models via Privacy-Preserving Evolutionary Model Merging_20250922|Personalized Language Models via Privacy-Preserving Evolutionary Model Merging]] (82.6% similar)
- [[2025-09-19/GRADA_ Graph-based Reranking against Adversarial Documents Attack_20250919|GRADA: Graph-based Reranking against Adversarial Documents Attack]] (82.5% similar)
- [[2025-09-19/Enterprise AI Must Enforce Participant-Aware Access Control_20250919|Enterprise AI Must Enforce Participant-Aware Access Control]] (81.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/In-Context Learning|In-Context Learning]]
**⚡ Unique Technical**: [[keywords/Local Differential Privacy|Local Differential Privacy]], [[keywords/Privacy-Utility Trade-off|Privacy-Utility Trade-off]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.04990v2 Announce Type: replace 
Abstract: Prompt privacy is crucial, especially when using online large language models (LLMs), due to the sensitive information often contained within prompts. While LLMs can enhance prompt privacy through text rewriting, existing methods primarily focus on document-level rewriting, neglecting the rich, multi-granular representations of text. This limitation restricts LLM utilization to specific tasks, overlooking their generalization and in-context learning capabilities, thus hindering practical application. To address this gap, we introduce DP-GTR, a novel three-stage framework that leverages local differential privacy (DP) and the composition theorem via group text rewriting. DP-GTR is the first framework to integrate both document-level and word-level information while exploiting in-context learning to simultaneously improve privacy and utility, effectively bridging local and global DP mechanisms at the individual data point level. Experiments on CommonSense QA and DocVQA demonstrate that DP-GTR outperforms existing approaches, achieving a superior privacy-utility trade-off. Furthermore, our framework is compatible with existing rewriting techniques, serving as a plug-in to enhance privacy protection. Our code is publicly available at github.com/ResponsibleAILab/DP-GTR.

## 🔍 Abstract (한글 번역)

arXiv:2503.04990v2 발표 유형: 교체  
초록: 프롬프트 프라이버시는 특히 온라인 대형 언어 모델(LLM)을 사용할 때 프롬프트에 종종 포함된 민감한 정보 때문에 매우 중요합니다. LLM은 텍스트 재작성을 통해 프롬프트 프라이버시를 강화할 수 있지만, 기존 방법은 주로 문서 수준의 재작성에 초점을 맞추어 텍스트의 풍부하고 다중 세분화된 표현을 간과하고 있습니다. 이 제한은 LLM의 활용을 특정 작업으로 제한하여 일반화 및 문맥 내 학습 능력을 간과하게 하여 실용적인 적용을 저해합니다. 이 격차를 해소하기 위해, 우리는 DP-GTR이라는 새로운 3단계 프레임워크를 소개합니다. 이는 로컬 차등 프라이버시(DP)와 그룹 텍스트 재작성을 통한 합성 정리를 활용합니다. DP-GTR은 문서 수준과 단어 수준의 정보를 모두 통합하면서 문맥 내 학습을 활용하여 프라이버시와 유용성을 동시에 향상시키는 최초의 프레임워크로, 개별 데이터 포인트 수준에서 로컬 및 글로벌 DP 메커니즘을 효과적으로 연결합니다. CommonSense QA와 DocVQA에 대한 실험은 DP-GTR이 기존 접근 방식을 능가하여 우수한 프라이버시-유용성 균형을 달성함을 보여줍니다. 또한, 우리의 프레임워크는 기존의 재작성 기술과 호환되어 프라이버시 보호를 강화하는 플러그인으로 작동할 수 있습니다. 우리의 코드는 github.com/ResponsibleAILab/DP-GTR에서 공개적으로 이용 가능합니다.

## 📝 요약

이 논문은 온라인 대형 언어 모델(LLM) 사용 시 중요한 프롬프트 프라이버시 문제를 다룹니다. 기존 방법들은 주로 문서 수준의 재작성을 다루며, 텍스트의 다양한 표현을 충분히 활용하지 못했습니다. 이를 해결하기 위해, 저자들은 DP-GTR이라는 새로운 프레임워크를 제안합니다. 이 프레임워크는 로컬 차등 프라이버시(DP)와 그룹 텍스트 재작성을 통해 문서 및 단어 수준 정보를 통합하여 프라이버시와 유용성을 동시에 개선합니다. CommonSense QA와 DocVQA 실험에서 DP-GTR은 기존 방법들보다 뛰어난 프라이버시-유용성 균형을 보여주었으며, 기존 재작성 기술과도 호환됩니다. 코드도 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 온라인 대형 언어 모델(LLM) 사용 시 프롬프트에 포함된 민감한 정보를 보호하기 위해 프롬프트 프라이버시가 중요합니다.
- 2. 기존 방법은 문서 수준의 재작성에 중점을 두어 LLM의 일반화 및 맥락 내 학습 기능을 충분히 활용하지 못합니다.
- 3. DP-GTR은 로컬 차등 프라이버시(DP)와 그룹 텍스트 재작성을 통한 조합 정리를 활용하여 프라이버시와 유틸리티를 동시에 개선하는 새로운 프레임워크입니다.
- 4. DP-GTR은 문서 수준과 단어 수준의 정보를 통합하여 개인 데이터 포인트 수준에서 로컬 및 글로벌 DP 메커니즘을 연결합니다.
- 5. CommonSense QA와 DocVQA 실험에서 DP-GTR은 기존 접근법보다 우수한 프라이버시-유틸리티 균형을 달성하며, 기존 재작성 기술과 호환 가능합니다.


---

*Generated on 2025-09-23 11:42:00*