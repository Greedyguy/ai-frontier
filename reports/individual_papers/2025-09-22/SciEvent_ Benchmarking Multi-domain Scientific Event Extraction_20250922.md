---
keywords:
  - Scientific Event Extraction
  - Large Language Model
  - Multi-domain Benchmark
  - Event Extraction Schema
category: cs.CL
publish_date: 2025-09-22
arxiv_id: 2509.15620
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:31:29.512591",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Scientific Event Extraction",
    "Large Language Model",
    "Multi-domain Benchmark",
    "Event Extraction Schema"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Scientific Event Extraction": 0.8,
    "Large Language Model": 0.85,
    "Multi-domain Benchmark": 0.78,
    "Event Extraction Schema": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Scientific Event Extraction",
        "canonical": "Scientific Event Extraction",
        "aliases": [
          "SciEvent"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a new benchmark for event extraction across multiple scientific domains, enhancing interdisciplinary research connections.",
        "novelty_score": 0.85,
        "connectivity_score": 0.7,
        "specificity_score": 0.88,
        "link_intent_score": 0.8
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Connects to the existing concept of large language models, which are pivotal in processing and extracting scientific information.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Multi-domain Benchmark",
        "canonical": "Multi-domain Benchmark",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Represents a novel approach to benchmarking across various scientific fields, fostering cross-domain insights.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Event Extraction Schema",
        "canonical": "Event Extraction Schema",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Defines a structured approach to capturing scientific events, crucial for improving information extraction accuracy.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "entity-relation extraction",
      "performance gap",
      "manual annotations"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Scientific Event Extraction",
      "resolved_canonical": "Scientific Event Extraction",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.7,
        "specificity": 0.88,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Multi-domain Benchmark",
      "resolved_canonical": "Multi-domain Benchmark",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Event Extraction Schema",
      "resolved_canonical": "Event Extraction Schema",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# SciEvent: Benchmarking Multi-domain Scientific Event Extraction

**Korean Title:** 과학 이벤트: 다중 도메인 과학 이벤트 추출의 벤치마킹

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15620.pdf)
**Category**: cs.CL
**Published**: 2025-09-22
**ArXiv ID**: [2509.15620](https://arxiv.org/abs/2509.15620)

## 🔗 유사한 논문
- [[2025-09-19/SNaRe_ Domain-aware Data Generation for Low-Resource Event Detection_20250919|SNaRe: Domain-aware Data Generation for Low-Resource Event Detection]] (82.8% similar)
- [[2025-09-19/An Evaluation-Centric Paradigm for Scientific Visualization Agents_20250919|An Evaluation-Centric Paradigm for Scientific Visualization Agents]] (80.0% similar)
- [[2025-09-19/DiCoRe_ Enhancing Zero-shot Event Detection via Divergent-Convergent LLM Reasoning_20250919|DiCoRe: Enhancing Zero-shot Event Detection via Divergent-Convergent LLM Reasoning]] (77.7% similar)
- [[2025-09-19/SPICE_ An Automated SWE-Bench Labeling Pipeline for Issue Clarity, Test Coverage, and Effort Estimation_20250919|SPICE: An Automated SWE-Bench Labeling Pipeline for Issue Clarity, Test Coverage, and Effort Estimation]] (77.5% similar)
- [[2025-09-17/Combining Evidence and Reasoning for Biomedical Fact-Checking_20250917|Combining Evidence and Reasoning for Biomedical Fact-Checking]] (77.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Scientific Event Extraction|Scientific Event Extraction]], [[keywords/Multi-domain Benchmark|Multi-domain Benchmark]], [[keywords/Event Extraction Schema|Event Extraction Schema]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15620v1 Announce Type: new 
Abstract: Scientific information extraction (SciIE) has primarily relied on entity-relation extraction in narrow domains, limiting its applicability to interdisciplinary research and struggling to capture the necessary context of scientific information, often resulting in fragmented or conflicting statements. In this paper, we introduce SciEvent, a novel multi-domain benchmark of scientific abstracts annotated via a unified event extraction (EE) schema designed to enable structured and context-aware understanding of scientific content. It includes 500 abstracts across five research domains, with manual annotations of event segments, triggers, and fine-grained arguments. We define SciIE as a multi-stage EE pipeline: (1) segmenting abstracts into core scientific activities--Background, Method, Result, and Conclusion; and (2) extracting the corresponding triggers and arguments. Experiments with fine-tuned EE models, large language models (LLMs), and human annotators reveal a performance gap, with current models struggling in domains such as sociology and humanities. SciEvent serves as a challenging benchmark and a step toward generalizable, multi-domain SciIE.

## 🔍 Abstract (한글 번역)

arXiv:2509.15620v1 발표 유형: 신규  
초록: 과학 정보 추출(SciIE)은 주로 좁은 분야에서의 엔티티-관계 추출에 의존해 왔으며, 이는 학제 간 연구에의 적용 가능성을 제한하고 과학 정보의 필수적인 맥락을 포착하는 데 어려움을 겪어 종종 단편적이거나 상충되는 진술을 초래합니다. 본 논문에서는 과학 콘텐츠의 구조적이고 맥락을 고려한 이해를 가능하게 하기 위해 통합된 이벤트 추출(EE) 스키마를 통해 주석이 달린 과학 초록의 새로운 다중 도메인 벤치마크인 SciEvent를 소개합니다. 이는 다섯 개의 연구 분야에 걸쳐 500개의 초록을 포함하며, 이벤트 세그먼트, 트리거 및 세부적인 인수에 대한 수동 주석이 포함되어 있습니다. 우리는 SciIE를 다단계 EE 파이프라인으로 정의합니다: (1) 초록을 핵심 과학 활동--배경, 방법, 결과, 결론으로 세분화하고; (2) 해당 트리거와 인수를 추출합니다. 세밀하게 조정된 EE 모델, 대형 언어 모델(LLM), 인간 주석자와의 실험은 사회학 및 인문학과 같은 분야에서 현재 모델이 어려움을 겪고 있음을 보여주는 성능 격차를 드러냅니다. SciEvent는 도전적인 벤치마크로서 일반화 가능하고 다중 도메인에 걸친 SciIE로 나아가는 한 걸음이 됩니다.

## 📝 요약

이 논문은 과학 정보 추출(SciIE)의 한계를 극복하기 위해 SciEvent라는 새로운 다중 도메인 벤치마크를 제안합니다. SciEvent는 통합된 이벤트 추출(EE) 스키마를 통해 과학적 내용을 구조적이고 맥락적으로 이해할 수 있도록 설계되었습니다. 5개 연구 분야에서 500개의 초록을 수집하고, 이벤트 세그먼트, 트리거, 세부적인 인자를 수작업으로 주석 처리했습니다. SciIE는 (1) 초록을 배경, 방법, 결과, 결론의 핵심 과학 활동으로 세분화하고, (2) 해당 트리거와 인자를 추출하는 다단계 EE 파이프라인으로 정의됩니다. 실험 결과, 현재 모델들이 사회학 및 인문학 분야에서 어려움을 겪고 있음을 보여주며, SciEvent는 일반화 가능한 다중 도메인 SciIE로 나아가는 중요한 발판이 됩니다.

## 🎯 주요 포인트

- 1. SciEvent는 과학 정보 추출을 위한 새로운 다중 도메인 벤치마크로, 통합된 이벤트 추출 스키마를 통해 과학 콘텐츠의 구조적이고 맥락적인 이해를 가능하게 합니다.
- 2. SciEvent는 5개 연구 분야의 500개 초록을 포함하며, 이벤트 세그먼트, 트리거, 세부적인 인수에 대한 수작업 주석을 제공합니다.
- 3. SciIE는 배경, 방법, 결과, 결론으로 초록을 세분화하고, 해당 트리거와 인수를 추출하는 다단계 이벤트 추출 파이프라인으로 정의됩니다.
- 4. 실험 결과, 현재 모델은 사회학 및 인문학 분야에서 성능 격차를 보이며, SciEvent는 일반화 가능한 다중 도메인 과학 정보 추출을 위한 도전적인 벤치마크로 작용합니다.


---

*Generated on 2025-09-23 11:31:29*