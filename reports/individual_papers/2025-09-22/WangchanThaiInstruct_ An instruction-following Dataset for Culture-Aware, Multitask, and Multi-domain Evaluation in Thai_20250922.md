---
keywords:
  - Large Language Model
  - Zero-Shot Learning
  - Instruction Tuning
  - Culturally Grounded Instruction Data
category: cs.CL
publish_date: 2025-09-22
arxiv_id: 2508.15239
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:50:23.904369",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Zero-Shot Learning",
    "Instruction Tuning",
    "Culturally Grounded Instruction Data"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Zero-Shot Learning": 0.8,
    "Instruction Tuning": 0.75,
    "Culturally Grounded Instruction Data": 0.78
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
        "rationale": "Connects to a broad range of studies in natural language processing and machine learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Zero-Shot Evaluation",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-Shot Evaluation"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights the evaluation method used, which is a trending topic in machine learning.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "Instruction Tuning",
        "canonical": "Instruction Tuning",
        "aliases": [
          "Instruction Fine-Tuning"
        ],
        "category": "unique_technical",
        "rationale": "Represents a unique approach to improving model alignment with specific tasks.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      },
      {
        "surface": "Culturally Grounded Instruction Data",
        "canonical": "Culturally Grounded Instruction Data",
        "aliases": [
          "Cultural Instruction Data"
        ],
        "category": "unique_technical",
        "rationale": "Emphasizes the importance of cultural context in data for low-resource languages.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "performance",
      "method",
      "evaluation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Zero-Shot Evaluation",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Instruction Tuning",
      "resolved_canonical": "Instruction Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Culturally Grounded Instruction Data",
      "resolved_canonical": "Culturally Grounded Instruction Data",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# WangchanThaiInstruct: An instruction-following Dataset for Culture-Aware, Multitask, and Multi-domain Evaluation in Thai

**Korean Title:** WangchanThaiInstruct: 태국어에서 문화 인식을 고려한 다중 작업 및 다중 도메인 평가를 위한 지침 준수 데이터셋

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2508.15239.pdf)
**Category**: cs.CL
**Published**: 2025-09-22
**ArXiv ID**: [2508.15239](https://arxiv.org/abs/2508.15239)

## 🔗 유사한 논문
- [[2025-09-22/A method for improving multilingual quality and diversity of instruction fine-tuning datasets_20250922|A method for improving multilingual quality and diversity of instruction fine-tuning datasets]] (83.1% similar)
- [[2025-09-22/CultureScope_ A Dimensional Lens for Probing Cultural Understanding in LLMs_20250922|CultureScope: A Dimensional Lens for Probing Cultural Understanding in LLMs]] (82.8% similar)
- [[2025-09-22/Enhancing LLM Language Adaption through Cross-lingual In-Context Pre-training_20250922|Enhancing LLM Language Adaption through Cross-lingual In-Context Pre-training]] (81.7% similar)
- [[2025-09-19/Ticket-Bench_ A Kickoff for Multilingual and Regionalized Agent Evaluation_20250919|Ticket-Bench: A Kickoff for Multilingual and Regionalized Agent Evaluation]] (81.5% similar)
- [[2025-09-22/Toxicity Red-Teaming_ Benchmarking LLM Safety in Singapore's Low-Resource Languages_20250922|Toxicity Red-Teaming: Benchmarking LLM Safety in Singapore's Low-Resource Languages]] (81.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Instruction Tuning|Instruction Tuning]], [[keywords/Culturally Grounded Instruction Data|Culturally Grounded Instruction Data]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.15239v2 Announce Type: replace 
Abstract: Large language models excel at instruction-following in English, but their performance in low-resource languages like Thai remains underexplored. Existing benchmarks often rely on translations, missing cultural and domain-specific nuances needed for real-world use. We present WangchanThaiInstruct, a human-authored Thai dataset for evaluation and instruction tuning, covering four professional domains and seven task types. Created through a multi-stage quality control process with annotators, domain experts, and AI researchers, WangchanThaiInstruct supports two studies: (1) a zero-shot evaluation showing performance gaps on culturally and professionally specific tasks, and (2) an instruction tuning study with ablations isolating the effect of native supervision. Models fine-tuned on WangchanThaiInstruct outperform those using translated data in both in-domain and out-of-domain benchmarks. These findings underscore the need for culturally and professionally grounded instruction data to improve LLM alignment in low-resource, linguistically diverse settings.

## 🔍 Abstract (한글 번역)

arXiv:2508.15239v2 발표 유형: 교체  
초록: 대형 언어 모델은 영어에서의 지시 수행에 뛰어나지만, 태국어와 같은 자원이 부족한 언어에서는 그 성능이 충분히 탐구되지 않았습니다. 기존의 벤치마크는 종종 번역에 의존하여, 실제 사용에 필요한 문화적 및 도메인 특유의 뉘앙스를 놓치고 있습니다. 우리는 평가 및 지시 조정을 위한 인간 작성 태국어 데이터셋인 WangchanThaiInstruct를 제시하며, 이는 네 가지 전문 도메인과 일곱 가지 작업 유형을 포함합니다. 이 데이터셋은 주석자, 도메인 전문가, AI 연구자와 함께 다단계 품질 관리 과정을 통해 제작되었습니다. WangchanThaiInstruct는 두 가지 연구를 지원합니다: (1) 문화적 및 전문적으로 특화된 작업에서의 성능 격차를 보여주는 제로샷 평가, (2) 원어 감독의 효과를 분리하는 소거 연구를 포함한 지시 조정 연구. WangchanThaiInstruct로 미세 조정된 모델은 번역 데이터를 사용하는 모델보다 도메인 내 및 도메인 외 벤치마크에서 더 우수한 성능을 보입니다. 이러한 결과는 자원이 부족하고 언어적으로 다양한 환경에서 대형 언어 모델의 정렬을 개선하기 위해 문화적 및 전문적으로 기반이 된 지시 데이터의 필요성을 강조합니다.

## 📝 요약

이 논문은 대규모 언어 모델이 영어에서는 뛰어난 성능을 보이지만, 태국어와 같은 저자원 언어에서는 성능이 부족하다는 점을 지적합니다. 이를 해결하기 위해 WangchanThaiInstruct라는 태국어 데이터셋을 개발하였으며, 이는 네 가지 전문 분야와 일곱 가지 작업 유형을 포함합니다. 데이터셋은 다단계 품질 관리 과정을 통해 제작되었으며, 두 가지 연구에 활용되었습니다. 첫째, 문화적 및 전문적 특수성을 반영한 작업에서 성능 격차를 보여주는 제로샷 평가, 둘째, 원어 감독의 효과를 분리한 명령어 튜닝 연구입니다. WangchanThaiInstruct로 미세 조정된 모델은 번역 데이터를 사용한 모델보다 더 나은 성능을 보였으며, 이는 저자원 언어 환경에서 문화적, 전문적 맥락을 반영한 데이터의 필요성을 강조합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델은 영어에서는 뛰어난 성능을 보이지만, 태국어와 같은 저자원 언어에서는 성능이 충분히 탐구되지 않았다.
- 2. 기존 벤치마크는 번역에 의존하여 실제 사용에 필요한 문화적, 도메인 특유의 뉘앙스를 놓치는 경우가 많다.
- 3. WangchanThaiInstruct는 태국어 평가 및 지시 조정을 위한 인간 작성 데이터셋으로, 네 가지 전문 도메인과 일곱 가지 작업 유형을 포함한다.
- 4. WangchanThaiInstruct로 미세 조정된 모델은 번역 데이터를 사용한 모델보다 도메인 내외 벤치마크에서 더 나은 성능을 보인다.
- 5. 연구 결과는 저자원 언어 환경에서 문화적, 전문적으로 기반이 된 지시 데이터의 필요성을 강조한다.


---

*Generated on 2025-09-23 11:50:23*