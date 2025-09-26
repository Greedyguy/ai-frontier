---
keywords:
  - Privacy-Preserving Model Merging
  - Personalization in Language Models
  - Privacy Preservation
  - Evolutionary Algorithms
category: cs.CL
publish_date: 2025-09-22
arxiv_id: 2503.18008
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:43:08.573975",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Privacy-Preserving Model Merging",
    "Personalization in Language Models",
    "Privacy Preservation",
    "Evolutionary Algorithms"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Privacy-Preserving Model Merging": 0.78,
    "Personalization in Language Models": 0.82,
    "Privacy Preservation": 0.79,
    "Evolutionary Algorithms": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Privacy-Preserving Model Merging",
        "canonical": "Privacy-Preserving Model Merging",
        "aliases": [
          "PriME"
        ],
        "category": "unique_technical",
        "rationale": "This concept introduces a novel approach to model merging with privacy considerations, which is central to the paper's contribution.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "Personalization in Language Models",
        "canonical": "Personalization in Language Models",
        "aliases": [
          "Language Model Personalization"
        ],
        "category": "specific_connectable",
        "rationale": "Personalization is a key theme of the paper, linking it to broader discussions on user-specific model adaptations.",
        "novelty_score": 0.7,
        "connectivity_score": 0.8,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      },
      {
        "surface": "Privacy Preservation",
        "canonical": "Privacy Preservation",
        "aliases": [
          "Data Privacy"
        ],
        "category": "broad_technical",
        "rationale": "Privacy preservation is a critical aspect of the proposed method, linking it to ongoing discussions in data privacy.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.79
      },
      {
        "surface": "Evolutionary Algorithms",
        "canonical": "Evolutionary Algorithms",
        "aliases": [
          "Evolutionary Computation"
        ],
        "category": "specific_connectable",
        "rationale": "The use of evolutionary algorithms is a distinctive feature of the proposed method, connecting it to optimization techniques.",
        "novelty_score": 0.6,
        "connectivity_score": 0.78,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "task-specific utility",
      "model parameters",
      "baseline"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Privacy-Preserving Model Merging",
      "resolved_canonical": "Privacy-Preserving Model Merging",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Personalization in Language Models",
      "resolved_canonical": "Personalization in Language Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.8,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Privacy Preservation",
      "resolved_canonical": "Privacy Preservation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Evolutionary Algorithms",
      "resolved_canonical": "Evolutionary Algorithms",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.78,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Personalized Language Models via Privacy-Preserving Evolutionary Model Merging

**Korean Title:** 개인화된 언어 모델을 위한 프라이버시 보호 진화적 모델 병합

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2503.18008.pdf)
**Category**: cs.CL
**Published**: 2025-09-22
**ArXiv ID**: [2503.18008](https://arxiv.org/abs/2503.18008)

## 🔗 유사한 논문
- [[2025-09-19/Communication-Efficient and Privacy-Adaptable Mechanism for Federated Learning_20250919|Communication-Efficient and Privacy-Adaptable Mechanism for Federated Learning]] (83.3% similar)
- [[2025-09-22/DP-GTR_ Differentially Private Prompt Protection via Group Text Rewriting_20250922|DP-GTR: Differentially Private Prompt Protection via Group Text Rewriting]] (82.6% similar)
- [[2025-09-17/ParaAegis_ Parallel Protection for Flexible Privacy-preserved Federated Learning_20250917|ParaAegis: Parallel Protection for Flexible Privacy-preserved Federated Learning]] (81.7% similar)
- [[2025-09-19/Learning in Context_ Personalizing Educational Content with Large Language Models to Enhance Student Learning_20250919|Learning in Context: Personalizing Educational Content with Large Language Models to Enhance Student Learning]] (81.7% similar)
- [[2025-09-19/The Sum Leaks More Than Its Parts_ Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration_20250919|The Sum Leaks More Than Its Parts: Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration]] (81.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Privacy Preservation|Privacy Preservation]]
**🔗 Specific Connectable**: [[keywords/Personalization in Language Models|Personalization in Language Models]], [[keywords/Evolutionary Algorithms|Evolutionary Algorithms]]
**⚡ Unique Technical**: [[keywords/Privacy-Preserving Model Merging|Privacy-Preserving Model Merging]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.18008v2 Announce Type: replace 
Abstract: Personalization in language models aims to tailor model behavior to individual users or user groups. Prompt-based methods incorporate user preferences into queries, while training-based methods encode them into model parameters. Model merging has also been explored for personalization under limited data. However, existing methods often fail to directly optimize task-specific utility and lack explicit mechanisms for privacy preservation. To address the limitations, we propose Privacy-Preserving Model Merging via Evolutionary Algorithms (PriME), a novel personalization approach that employs gradient-free methods to directly optimize utility while reducing privacy risks. By integrating privacy preservation into the optimization objective, PriME creates personalized modules that effectively capture target user preferences while minimizing privacy risks for data-sharing users. Experiments on the LaMP benchmark show that PriME consistently outperforms a range of baselines, achieving up to a 45% improvement in task performance. Further analysis demonstrates that PriME achieves a superior privacy-utility trade-off compared to a prior state-of-the-art, with enhanced robustness to membership inference attacks and greater utility in capturing user preferences.

## 🔍 Abstract (한글 번역)

arXiv:2503.18008v2 발표 유형: 교체  
초록: 언어 모델에서의 개인화는 개별 사용자 또는 사용자 그룹에 맞춰 모델의 동작을 조정하는 것을 목표로 합니다. 프롬프트 기반 방법은 사용자 선호도를 쿼리에 통합하고, 학습 기반 방법은 이를 모델 매개변수에 인코딩합니다. 모델 병합도 제한된 데이터 하에서 개인화를 위해 탐구되었습니다. 그러나 기존 방법들은 종종 과제별 유틸리티를 직접 최적화하지 못하고, 프라이버시 보호를 위한 명시적인 메커니즘이 부족합니다. 이러한 한계를 해결하기 위해, 우리는 진화 알고리즘을 통한 프라이버시 보호 모델 병합(PriME)을 제안합니다. 이는 유틸리티를 직접 최적화하면서 프라이버시 위험을 줄이는 새로운 개인화 접근법입니다. 최적화 목표에 프라이버시 보호를 통합함으로써, PriME는 데이터 공유 사용자에 대한 프라이버시 위험을 최소화하면서 목표 사용자 선호도를 효과적으로 포착하는 개인화 모듈을 생성합니다. LaMP 벤치마크에 대한 실험 결과, PriME는 다양한 기준선을 지속적으로 능가하며, 과제 성능에서 최대 45%의 향상을 달성합니다. 추가 분석을 통해 PriME가 이전 최첨단 방법과 비교하여 프라이버시-유틸리티 균형에서 우수함을 입증하며, 멤버십 추론 공격에 대한 강화된 강건성과 사용자 선호도 포착에서의 더 큰 유틸리티를 보여줍니다.

## 📝 요약

이 논문은 개인화된 언어 모델에서의 개인정보 보호 문제를 해결하기 위해 PriME라는 새로운 접근 방식을 제안합니다. 기존의 개인화 방법들은 주로 사용자 선호도를 쿼리에 통합하거나 모델 파라미터에 인코딩하지만, PriME는 진화 알고리즘을 사용하여 직접적인 유용성 최적화와 개인정보 보호를 동시에 달성합니다. 실험 결과, PriME는 LaMP 벤치마크에서 기존 방법들보다 최대 45% 향상된 성능을 보였으며, 개인정보 유출 위험을 줄이면서 사용자 선호도를 효과적으로 반영합니다. PriME는 특히 멤버십 추론 공격에 대한 강한 내성을 보이며, 유용성과 개인정보 보호의 균형을 잘 맞춥니다.

## 🎯 주요 포인트

- 1. PriME는 진화 알고리즘을 활용하여 개인화된 모듈을 생성하며, 프라이버시 위험을 줄이면서 직접적인 유틸리티 최적화를 목표로 한다.
- 2. PriME는 최적화 목표에 프라이버시 보존을 통합하여 데이터 공유 사용자의 프라이버시 위험을 최소화한다.
- 3. LaMP 벤치마크 실험에서 PriME는 다양한 기준선보다 최대 45% 향상된 작업 성능을 보여준다.
- 4. PriME는 기존 최첨단 방법보다 우수한 프라이버시-유틸리티 균형을 달성하며, 멤버십 추론 공격에 대한 강력한 저항성을 보인다.
- 5. PriME는 사용자 선호도를 효과적으로 포착하는 데 있어 더 큰 유틸리티를 제공한다.


---

*Generated on 2025-09-23 11:43:08*