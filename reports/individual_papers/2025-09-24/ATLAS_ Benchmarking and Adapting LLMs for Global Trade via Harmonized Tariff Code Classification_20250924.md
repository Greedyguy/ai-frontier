<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:25:15.039032",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Harmonized Tariff Schedule",
    "Large Language Model",
    "Atlas Model",
    "Customs Rulings Online Search System"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Harmonized Tariff Schedule": 0.8,
    "Large Language Model": 0.85,
    "Atlas Model": 0.78,
    "Customs Rulings Online Search System": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Harmonized Tariff Schedule",
        "canonical": "Harmonized Tariff Schedule",
        "aliases": [
          "HTS"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's focus on classification challenges in global trade.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are a key technology evaluated in the paper, linking it to broader machine learning discussions.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Atlas model",
        "canonical": "Atlas Model",
        "aliases": [
          "Atlas"
        ],
        "category": "unique_technical",
        "rationale": "The Atlas model is a specific implementation discussed in the paper, relevant for linking to model-specific discussions.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Customs Rulings Online Search System",
        "canonical": "Customs Rulings Online Search System",
        "aliases": [
          "CROSS"
        ],
        "category": "unique_technical",
        "rationale": "CROSS is the data source for the benchmark, important for discussions on data provenance and benchmarking.",
        "novelty_score": 0.68,
        "connectivity_score": 0.55,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "global trade",
      "classification",
      "accuracy"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Harmonized Tariff Schedule",
      "resolved_canonical": "Harmonized Tariff Schedule",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Atlas model",
      "resolved_canonical": "Atlas Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Customs Rulings Online Search System",
      "resolved_canonical": "Customs Rulings Online Search System",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.55,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# ATLAS: Benchmarking and Adapting LLMs for Global Trade via Harmonized Tariff Code Classification

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18400.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18400](https://arxiv.org/abs/2509.18400)

## 🔗 유사한 논문
- [[2025-09-23/From Scores to Steps_ Diagnosing and Improving LLM Performance in Evidence-Based Medical Calculations_20250923|From Scores to Steps: Diagnosing and Improving LLM Performance in Evidence-Based Medical Calculations]] (79.5% similar)
- [[2025-09-23/Quality Assessment of Tabular Data using Large Language Models and Code Generation_20250923|Quality Assessment of Tabular Data using Large Language Models and Code Generation]] (79.3% similar)
- [[2025-09-23/CEBench_ A Benchmarking Toolkit for the Cost-Effectiveness of LLM Pipelines_20250923|CEBench: A Benchmarking Toolkit for the Cost-Effectiveness of LLM Pipelines]] (78.6% similar)
- [[2025-09-22/Small LLMs with Expert Blocks Are Good Enough for Hyperparamter Tuning_20250922|Small LLMs with Expert Blocks Are Good Enough for Hyperparamter Tuning]] (78.5% similar)
- [[2025-09-19/Rationality Check! Benchmarking the Rationality of Large Language Models_20250919|Rationality Check! Benchmarking the Rationality of Large Language Models]] (78.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Harmonized Tariff Schedule|Harmonized Tariff Schedule]], [[keywords/Atlas Model|Atlas Model]], [[keywords/Customs Rulings Online Search System|Customs Rulings Online Search System]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18400v1 Announce Type: new 
Abstract: Accurate classification of products under the Harmonized Tariff Schedule (HTS) is a critical bottleneck in global trade, yet it has received little attention from the machine learning community. Misclassification can halt shipments entirely, with major postal operators suspending deliveries to the U.S. due to incomplete customs documentation. We introduce the first benchmark for HTS code classification, derived from the U.S. Customs Rulings Online Search System (CROSS). Evaluating leading LLMs, we find that our fine-tuned Atlas model (LLaMA-3.3-70B) achieves 40 percent fully correct 10-digit classifications and 57.5 percent correct 6-digit classifications, improvements of 15 points over GPT-5-Thinking and 27.5 points over Gemini-2.5-Pro-Thinking. Beyond accuracy, Atlas is roughly five times cheaper than GPT-5-Thinking and eight times cheaper than Gemini-2.5-Pro-Thinking, and can be self-hosted to guarantee data privacy in high-stakes trade and compliance workflows. While Atlas sets a strong baseline, the benchmark remains highly challenging, with only 40 percent 10-digit accuracy. By releasing both dataset and model, we aim to position HTS classification as a new community benchmark task and invite future work in retrieval, reasoning, and alignment.

## 📝 요약

이 논문은 글로벌 무역에서 중요한 병목 현상인 조화 관세 코드(HTS) 분류의 정확성을 개선하기 위해 최초의 벤치마크를 제안합니다. 미국 관세 판결 온라인 검색 시스템(CROSS)에서 데이터를 추출하여 주요 대형 언어 모델(LLM)을 평가한 결과, 미세 조정된 Atlas 모델(LLaMA-3.3-70B)이 10자리 코드에서 40%, 6자리 코드에서 57.5%의 정확도를 달성했습니다. 이는 GPT-5-Thinking과 Gemini-2.5-Pro-Thinking보다 각각 15점, 27.5점 향상된 수치입니다. 또한, Atlas는 비용 면에서 더 경제적이며, 자체 호스팅이 가능하여 데이터 프라이버시를 보장합니다. 이 연구는 HTS 분류를 새로운 커뮤니티 벤치마크 과제로 제시하고, 향후 연구를 초대합니다.

## 🎯 주요 포인트

- 1. HTS 코드 분류는 글로벌 무역에서 중요한 병목 현상이며, 기계 학습 커뮤니티에서 주목받지 못했다.
- 2. 우리는 미국 세관 판결 온라인 검색 시스템(CROSS)에서 파생된 최초의 HTS 코드 분류 벤치마크를 소개한다.
- 3. Atlas 모델은 10자리 코드에서 40% 정확도, 6자리 코드에서 57.5% 정확도를 달성하며, 이는 GPT-5-Thinking보다 15포인트, Gemini-2.5-Pro-Thinking보다 27.5포인트 향상된 결과이다.
- 4. Atlas는 GPT-5-Thinking보다 약 5배, Gemini-2.5-Pro-Thinking보다 8배 저렴하며, 데이터 프라이버시를 보장하기 위해 자체 호스팅이 가능하다.
- 5. 데이터셋과 모델을 공개함으로써 HTS 분류를 새로운 커뮤니티 벤치마크 과제로 자리매김하고, 향후 검색, 추론 및 정렬 분야의 연구를 초대한다.


---

*Generated on 2025-09-24 13:25:15*