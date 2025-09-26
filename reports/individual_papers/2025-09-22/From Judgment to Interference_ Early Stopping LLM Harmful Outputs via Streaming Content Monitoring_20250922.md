---
keywords:
  - Large Language Model
  - Streaming Content Monitor
  - FineHarm Dataset
  - Safety Alignment
  - Partial Detection
category: cs.CL
publish_date: 2025-09-22
arxiv_id: 2506.09996
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:48:30.898081",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Streaming Content Monitor",
    "FineHarm Dataset",
    "Safety Alignment",
    "Partial Detection"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Streaming Content Monitor": 0.8,
    "FineHarm Dataset": 0.78,
    "Safety Alignment": 0.82,
    "Partial Detection": 0.77
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
          "Language Model"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's focus on safety alignment and moderation techniques.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Streaming Content Monitor",
        "canonical": "Streaming Content Monitor",
        "aliases": [
          "SCM"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach for early stopping harmful outputs in LLMs.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "FineHarm",
        "canonical": "FineHarm Dataset",
        "aliases": [
          "FineHarm"
        ],
        "category": "unique_technical",
        "rationale": "A new dataset crucial for training models in partial detection of harmful content.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "Safety Alignment",
        "canonical": "Safety Alignment",
        "aliases": [
          "Alignment"
        ],
        "category": "specific_connectable",
        "rationale": "Key concept in ensuring LLMs produce non-harmful outputs.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "Partial Detection",
        "canonical": "Partial Detection",
        "aliases": [
          "Early Stopping"
        ],
        "category": "specific_connectable",
        "rationale": "Describes the method of detecting harmful content before full output is generated.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "moderation",
      "detection"
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
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Streaming Content Monitor",
      "resolved_canonical": "Streaming Content Monitor",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "FineHarm",
      "resolved_canonical": "FineHarm Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Safety Alignment",
      "resolved_canonical": "Safety Alignment",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Partial Detection",
      "resolved_canonical": "Partial Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# From Judgment to Interference: Early Stopping LLM Harmful Outputs via Streaming Content Monitoring

**Korean Title:** 판단에서 간섭으로: 스트리밍 콘텐츠 모니터링을 통한 LLM 유해 출력의 조기 중지

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2506.09996.pdf)
**Category**: cs.CL
**Published**: 2025-09-22
**ArXiv ID**: [2506.09996](https://arxiv.org/abs/2506.09996)

## 🔗 유사한 논문
- [[2025-09-22/Red Teaming Multimodal Language Models_ Evaluating Harm Across Prompt Modalities and Models_20250922|Red Teaming Multimodal Language Models: Evaluating Harm Across Prompt Modalities and Models]] (85.7% similar)
- [[2025-09-19/SMARTER_ A Data-efficient Framework to Improve Toxicity Detection with Explanation via Self-augmenting Large Language Models_20250919|SMARTER: A Data-efficient Framework to Improve Toxicity Detection with Explanation via Self-augmenting Large Language Models]] (85.4% similar)
- [[2025-09-22/Toxicity Red-Teaming_ Benchmarking LLM Safety in Singapore's Low-Resource Languages_20250922|Toxicity Red-Teaming: Benchmarking LLM Safety in Singapore's Low-Resource Languages]] (85.1% similar)
- [[2025-09-22/It Depends_ Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge_20250922|It Depends: Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge]] (85.0% similar)
- [[2025-09-22/AdaSteer_ Your Aligned LLM is Inherently an Adaptive Jailbreak Defender_20250922|AdaSteer: Your Aligned LLM is Inherently an Adaptive Jailbreak Defender]] (84.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Safety Alignment|Safety Alignment]], [[keywords/Partial Detection|Partial Detection]]
**⚡ Unique Technical**: [[keywords/Streaming Content Monitor|Streaming Content Monitor]], [[keywords/FineHarm Dataset|FineHarm Dataset]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.09996v2 Announce Type: replace 
Abstract: Though safety alignment has been applied to most large language models (LLMs), LLM service providers generally deploy a subsequent moderation as the external safety guardrail in real-world products. Existing moderators mainly practice a conventional full detection, which determines the harmfulness based on the complete LLM output, causing high service latency. Recent works pay more attention to partial detection where moderators oversee the generation midway and early stop the output if harmfulness is detected, but they directly apply moderators trained with the full detection paradigm to incomplete outputs, introducing a training-inference gap that lowers the performance. In this paper, we explore how to form a data-and-model solution that natively supports partial detection. For the data, we construct FineHarm, a dataset consisting of 29K prompt-response pairs with fine-grained annotations to provide reasonable supervision for token-level training. Then, we propose the streaming content monitor, which is trained with dual supervision of response- and token-level labels and can follow the output stream of LLM to make a timely judgment of harmfulness. Experiments show that SCM gains 0.95+ in macro F1 score that is comparable to full detection, by only seeing the first 18% of tokens in responses on average. Moreover, the SCM can serve as a pseudo-harmfulness annotator for improving safety alignment and lead to a higher harmlessness score than DPO.

## 🔍 Abstract (한글 번역)

arXiv:2506.09996v2 발표 유형: 교체  
초록: 안전 정렬은 대부분의 대형 언어 모델(LLM)에 적용되었지만, LLM 서비스 제공자는 일반적으로 실제 제품에서 외부 안전 가드레일로서 후속 조정(moderation)을 배치합니다. 기존의 조정자는 주로 LLM 출력 전체를 기반으로 유해성을 판단하는 전통적인 전체 탐지를 수행하여 높은 서비스 지연을 초래합니다. 최근 연구들은 조정자가 생성 중간을 감독하고 유해성이 감지되면 출력을 조기에 중단하는 부분 탐지에 더 많은 주의를 기울이고 있지만, 전체 탐지 패러다임으로 훈련된 조정자를 불완전한 출력에 직접 적용하여 성능을 저하시키는 훈련-추론 간극을 초래합니다. 이 논문에서는 부분 탐지를 본질적으로 지원하는 데이터 및 모델 솔루션을 어떻게 형성할 수 있는지 탐구합니다. 데이터 측면에서는, FineHarm이라는 데이터셋을 구축하여 29K의 프롬프트-응답 쌍과 세밀한 주석을 포함하여 토큰 수준 훈련에 합리적인 감독을 제공합니다. 그런 다음, 응답 및 토큰 수준 레이블의 이중 감독으로 훈련된 스트리밍 콘텐츠 모니터를 제안하며, 이는 LLM의 출력 스트림을 따라 유해성에 대한 적시 판단을 내릴 수 있습니다. 실험 결과, SCM은 평균적으로 응답의 첫 18%의 토큰만 보고도 전체 탐지와 비교할 때 매크로 F1 점수에서 0.95 이상의 성과를 얻었습니다. 더욱이, SCM은 안전 정렬을 개선하기 위한 의사 유해성 주석자로서 작용할 수 있으며, DPO보다 높은 무해성 점수를 이끌어낼 수 있습니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 안전성을 개선하기 위한 새로운 접근법을 제안합니다. 기존의 안전성 검사는 전체 출력물을 기반으로 유해성을 판단하여 서비스 지연을 초래하는 반면, 이 연구는 부분 검출을 통해 출력 도중 유해성을 조기에 감지하고 중단할 수 있는 방법을 탐구합니다. 이를 위해 29,000개의 프롬프트-응답 쌍으로 구성된 FineHarm 데이터셋을 구축하고, 응답 및 토큰 수준의 이중 감독을 받는 스트리밍 콘텐츠 모니터(SCM)를 제안합니다. 실험 결과, SCM은 평균적으로 응답의 첫 18%의 토큰만 보고도 높은 정확도의 유해성 판단을 가능하게 하며, 안전성 정렬을 개선하는 데 기여할 수 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. 대부분의 대형 언어 모델(LLM)에는 안전 정렬이 적용되었지만, 실제 제품에서는 외부 안전 가드레일로서 후속 조정이 필요합니다.
- 2. 기존의 조정자는 전체 탐지를 통해 유해성을 판단하여 서비스 지연을 초래합니다.
- 3. 부분 탐지에 중점을 둔 최근 연구에서는 생성 중간을 감독하고 유해성이 감지되면 출력을 조기 중단합니다.
- 4. FineHarm 데이터셋을 구축하여 토큰 수준의 훈련을 위한 세밀한 주석을 제공합니다.
- 5. 스트리밍 콘텐츠 모니터(SCM)는 응답과 토큰 수준 레이블의 이중 감독으로 훈련되어, 평균적으로 응답의 첫 18%의 토큰만 보고도 유해성을 판단할 수 있습니다.


---

*Generated on 2025-09-23 11:48:30*