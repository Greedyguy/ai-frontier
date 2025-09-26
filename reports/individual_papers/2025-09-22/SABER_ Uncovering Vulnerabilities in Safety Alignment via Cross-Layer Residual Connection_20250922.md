---
keywords:
  - Large Language Model
  - Safety Alignment
  - Jailbreak Attack
  - Residual Connection
  - HarmBench
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.16060
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:41:21.367397",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Safety Alignment",
    "Jailbreak Attack",
    "Residual Connection",
    "HarmBench"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Safety Alignment": 0.78,
    "Jailbreak Attack": 0.8,
    "Residual Connection": 0.77,
    "HarmBench": 0.75
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
        "rationale": "As a fundamental technology, it connects to a wide range of studies in natural language processing and AI safety.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "safety alignment",
        "canonical": "Safety Alignment",
        "aliases": [
          "safety-alignment training"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's focus on vulnerabilities and is a specific area of interest in AI ethics and safety.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "jailbreak attacks",
        "canonical": "Jailbreak Attack",
        "aliases": [
          "jailbreak",
          "jailbreaks"
        ],
        "category": "unique_technical",
        "rationale": "Understanding jailbreak attacks is crucial for linking studies on AI vulnerabilities and security.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "residual connection",
        "canonical": "Residual Connection",
        "aliases": [
          "residual connections"
        ],
        "category": "specific_connectable",
        "rationale": "This is a key mechanism in neural networks that enhances model performance and is relevant to the paper's methodology.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.77
      },
      {
        "surface": "HarmBench test set",
        "canonical": "HarmBench",
        "aliases": [
          "HarmBench validation set"
        ],
        "category": "unique_technical",
        "rationale": "HarmBench is a specific benchmark used to evaluate the effectiveness of safety mechanisms in AI models.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.72,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "source code"
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
      "candidate_surface": "safety alignment",
      "resolved_canonical": "Safety Alignment",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "jailbreak attacks",
      "resolved_canonical": "Jailbreak Attack",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "residual connection",
      "resolved_canonical": "Residual Connection",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "HarmBench test set",
      "resolved_canonical": "HarmBench",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.72,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# SABER: Uncovering Vulnerabilities in Safety Alignment via Cross-Layer Residual Connection

**Korean Title:** SABER: 교차 계층 잔여 연결을 통한 안전 정렬의 취약점 발견

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16060.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.16060](https://arxiv.org/abs/2509.16060)

## 🔗 유사한 논문
- [[2025-09-22/AdaSteer_ Your Aligned LLM is Inherently an Adaptive Jailbreak Defender_20250922|AdaSteer: Your Aligned LLM is Inherently an Adaptive Jailbreak Defender]] (86.8% similar)
- [[2025-09-22/Toxicity Red-Teaming_ Benchmarking LLM Safety in Singapore's Low-Resource Languages_20250922|Toxicity Red-Teaming: Benchmarking LLM Safety in Singapore's Low-Resource Languages]] (85.2% similar)
- [[2025-09-22/From Judgment to Interference_ Early Stopping LLM Harmful Outputs via Streaming Content Monitoring_20250922|From Judgment to Interference: Early Stopping LLM Harmful Outputs via Streaming Content Monitoring]] (84.7% similar)
- [[2025-09-22/Activation Space Interventions Can Be Transferred Between Large Language Models_20250922|Activation Space Interventions Can Be Transferred Between Large Language Models]] (84.2% similar)
- [[2025-09-19/Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment: Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (83.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Residual Connection|Residual Connection]]
**⚡ Unique Technical**: [[keywords/Safety Alignment|Safety Alignment]], [[keywords/Jailbreak Attack|Jailbreak Attack]], [[keywords/HarmBench|HarmBench]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16060v1 Announce Type: new 
Abstract: Large Language Models (LLMs) with safe-alignment training are powerful instruments with robust language comprehension capabilities. These models typically undergo meticulous alignment procedures involving human feedback to ensure the acceptance of safe inputs while rejecting harmful or unsafe ones. However, despite their massive scale and alignment efforts, LLMs remain vulnerable to jailbreak attacks, where malicious users manipulate the model to produce harmful outputs that it was explicitly trained to avoid. In this study, we find that the safety mechanisms in LLMs are predominantly embedded in the middle-to-late layers. Building on this insight, we introduce a novel white-box jailbreak method, SABER (Safety Alignment Bypass via Extra Residuals), which connects two intermediate layers $s$ and $e$ such that $s < e$, through a residual connection. Our approach achieves a 51% improvement over the best-performing baseline on the HarmBench test set. Furthermore, SABER induces only a marginal shift in perplexity when evaluated on the HarmBench validation set. The source code is publicly available at https://github.com/PalGitts/SABER.

## 🔍 Abstract (한글 번역)

arXiv:2509.16060v1 발표 유형: 신규  
초록: 안전 정렬 훈련을 받은 대형 언어 모델(LLM)은 강력한 언어 이해 능력을 가진 도구입니다. 이러한 모델은 일반적으로 안전한 입력을 수용하고 유해하거나 안전하지 않은 입력을 거부하도록 인간의 피드백을 포함한 세심한 정렬 절차를 거칩니다. 그러나 대규모와 정렬 노력에도 불구하고, LLM은 악의적인 사용자가 모델을 조작하여 명시적으로 회피하도록 훈련된 유해한 출력을 생성하게 하는 탈옥 공격에 취약합니다. 본 연구에서는 LLM의 안전 메커니즘이 주로 중간에서 후반 레이어에 내장되어 있음을 발견했습니다. 이 통찰을 바탕으로, 우리는 새로운 화이트박스 탈옥 방법인 SABER(Safety Alignment Bypass via Extra Residuals)를 소개합니다. 이는 잔여 연결을 통해 두 개의 중간 레이어 $s$와 $e$를 연결하여 $s < e$가 되도록 합니다. 우리의 접근법은 HarmBench 테스트 세트에서 가장 성능이 좋은 기준선 대비 51%의 개선을 달성했습니다. 또한, SABER는 HarmBench 검증 세트에서 평가할 때 당혹도의 변화가 거의 없습니다. 소스 코드는 https://github.com/PalGitts/SABER에서 공개적으로 이용 가능합니다.

## 📝 요약

이 연구는 안전 정렬 훈련을 받은 대형 언어 모델(LLM)이 여전히 악의적인 사용자가 모델을 조작하여 유해한 출력을 생성하는 'jailbreak' 공격에 취약하다는 점을 밝힙니다. 연구진은 LLM의 안전 메커니즘이 주로 중간에서 후반부 레이어에 내재되어 있음을 발견했습니다. 이를 바탕으로, 중간 레이어 $s$와 $e$를 잉여 연결로 연결하는 새로운 화이트박스 jailbreak 방법인 SABER를 제안했습니다. SABER는 HarmBench 테스트 세트에서 기존 최고 성능 대비 51% 개선된 결과를 보였으며, 검증 세트에서 혼란도(perplexity) 변화는 미미했습니다. 소스 코드는 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)은 안전한 입력을 수용하고 유해한 입력을 거부하도록 인간 피드백을 통해 정렬 절차를 거친다.
- 2. LLM은 정렬 노력에도 불구하고 악의적인 사용자가 모델을 조작하여 유해한 출력을 생성하는 탈옥 공격에 취약하다.
- 3. 안전 메커니즘은 주로 LLM의 중간에서 후반 레이어에 내장되어 있다.
- 4. SABER라는 새로운 화이트박스 탈옥 방법을 도입하여 중간 레이어 사이에 잔여 연결을 통해 안전 정렬을 우회한다.
- 5. SABER는 HarmBench 테스트 세트에서 기존 최고 성능 대비 51% 개선을 달성했다.


---

*Generated on 2025-09-23 10:41:21*