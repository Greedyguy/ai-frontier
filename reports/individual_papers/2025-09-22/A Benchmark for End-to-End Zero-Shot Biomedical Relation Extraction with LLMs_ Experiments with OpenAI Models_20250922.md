---
keywords:
  - Zero-Shot Learning
  - Large Language Model
  - Biomedical Relation Extraction
  - OpenAI GPT-4
category: cs.CL
publish_date: 2025-09-22
arxiv_id: 2504.04083
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:43:28.950915",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Zero-Shot Learning",
    "Large Language Model",
    "Biomedical Relation Extraction",
    "OpenAI GPT-4"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Zero-Shot Learning": 0.85,
    "Large Language Model": 0.8,
    "Biomedical Relation Extraction": 0.78,
    "OpenAI GPT-4": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Zero-shot methodology",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "zero-shot",
          "zero-shot approach"
        ],
        "category": "specific_connectable",
        "rationale": "Zero-Shot Learning is a trending concept that connects to various NLP and ML tasks, enhancing cross-disciplinary insights.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Large language models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs",
          "large-scale language models"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are foundational to current NLP research, providing a broad technical base for linking.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Biomedical relation extraction",
        "canonical": "Biomedical Relation Extraction",
        "aliases": [
          "biomedical RE",
          "bio-relation extraction"
        ],
        "category": "unique_technical",
        "rationale": "This is a specialized task within NLP, crucial for linking biomedical data and enhancing domain-specific research.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "OpenAI GPT-4-turbo",
        "canonical": "OpenAI GPT-4",
        "aliases": [
          "GPT-4-turbo",
          "OpenAI turbo"
        ],
        "category": "unique_technical",
        "rationale": "This specific model variant is significant for performance benchmarking in NLP tasks, offering unique insights.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "dataset",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Zero-shot methodology",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Large language models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Biomedical relation extraction",
      "resolved_canonical": "Biomedical Relation Extraction",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "OpenAI GPT-4-turbo",
      "resolved_canonical": "OpenAI GPT-4",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# A Benchmark for End-to-End Zero-Shot Biomedical Relation Extraction with LLMs: Experiments with OpenAI Models

**Korean Title:** 엔드-투-엔드 제로-샷 생물의학 관계 추출을 위한 벤치마크: OpenAI 모델을 사용한 실험

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2504.04083.pdf)
**Category**: cs.CL
**Published**: 2025-09-22
**ArXiv ID**: [2504.04083](https://arxiv.org/abs/2504.04083)

## 🔗 유사한 논문
- [[2025-09-19/LLM-OREF_ An Open Relation Extraction Framework Based on Large Language Models_20250919|LLM-OREF: An Open Relation Extraction Framework Based on Large Language Models]] (82.9% similar)
- [[2025-09-22/Data-Efficient Learning for Generalizable Surgical Video Understanding_20250922|Data-Efficient Learning for Generalizable Surgical Video Understanding]] (81.2% similar)
- [[2025-09-22/Predicting Language Models' Success at Zero-Shot Probabilistic Prediction_20250922|Predicting Language Models' Success at Zero-Shot Probabilistic Prediction]] (81.0% similar)
- [[2025-09-22/Can Large Language Models Infer Causal Relationships from Real-World Text?_20250922|Can Large Language Models Infer Causal Relationships from Real-World Text?]] (80.8% similar)
- [[2025-09-22/A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages_20250922|A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages]] (80.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Biomedical Relation Extraction|Biomedical Relation Extraction]], [[keywords/OpenAI GPT-4|OpenAI GPT-4]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2504.04083v2 Announce Type: replace 
Abstract: Objective: Zero-shot methodology promises to cut down on costs of dataset annotation and domain expertise needed to make use of NLP. Generative large language models trained to align with human goals have achieved high zero-shot performance across a wide variety of tasks. As of yet, it is unclear how well these models perform on biomedical relation extraction (RE). To address this knowledge gap, we explore patterns in the performance of OpenAI LLMs across a diverse sampling of RE tasks.
  Methods: We use OpenAI GPT-4-turbo and OpenAI's reasoning models o1 and GPT-OSS to conduct end-to-end RE experiments on seven datasets. We use the JSON generation capabilities of GPT models to generate structured output in two ways: (1) by defining an explicit schema describing the structure of relations, and (2) using a setting that infers the structure from the prompt language.
  Results: Our work is the first to study and compare the performance of the GPT-4, o1 and GPT-OSS for the end-to-end zero-shot biomedical RE task across a broad array of datasets. We found the zero-shot performances to be proximal to that of fine-tuned methods. The limitations of this approach are that it performs poorly on instances containing many relations and errs on the boundaries of textual mentions.
  Conclusion: LLMs exhibit promising zero-shot capabilities in complex biomedical RE tasks, offering competitive performance with reduced dataset curation costs and NLP modeling needs but with increased perpetual compute costs. Addressing the limitations we identify could further boost reliability. The code, data, and prompts for all our experiments are publicly available for additional benchmarking by the community: https://github.com/bionlproc/ZeroShotRE

## 🔍 Abstract (한글 번역)

arXiv:2504.04083v2 발표 유형: 교체  
초록: 목표: 제로샷 방법론은 NLP를 활용하는 데 필요한 데이터셋 주석 및 도메인 전문 지식의 비용을 절감할 수 있는 가능성을 제시합니다. 인간의 목표에 맞춰 훈련된 생성적 대형 언어 모델은 다양한 작업에서 높은 제로샷 성능을 달성했습니다. 그러나 이러한 모델이 생물의학적 관계 추출(RE)에서 얼마나 잘 수행되는지는 아직 명확하지 않습니다. 이러한 지식 격차를 해결하기 위해, 우리는 다양한 RE 작업 샘플링에서 OpenAI LLM의 성능 패턴을 탐색합니다.  
방법: 우리는 OpenAI GPT-4-turbo와 OpenAI의 추론 모델 o1 및 GPT-OSS를 사용하여 7개의 데이터셋에서 엔드 투 엔드 RE 실험을 수행합니다. GPT 모델의 JSON 생성 기능을 사용하여 두 가지 방법으로 구조화된 출력을 생성합니다: (1) 관계의 구조를 설명하는 명시적 스키마를 정의하는 방법, (2) 프롬프트 언어에서 구조를 추론하는 설정을 사용하는 방법.  
결과: 우리의 연구는 다양한 데이터셋에서 엔드 투 엔드 제로샷 생물의학 RE 작업을 위해 GPT-4, o1 및 GPT-OSS의 성능을 연구하고 비교한 최초의 연구입니다. 우리는 제로샷 성능이 미세 조정된 방법과 근접하다는 것을 발견했습니다. 이 접근법의 한계는 많은 관계를 포함하는 인스턴스에서 성능이 저조하고 텍스트 언급의 경계에서 오류가 발생한다는 점입니다.  
결론: LLM은 복잡한 생물의학 RE 작업에서 유망한 제로샷 기능을 보여주며, 데이터셋 큐레이션 비용과 NLP 모델링 요구를 줄이면서 경쟁력 있는 성능을 제공합니다. 그러나 지속적인 컴퓨팅 비용은 증가합니다. 우리가 식별한 한계를 해결하면 신뢰성을 더욱 높일 수 있습니다. 모든 실험에 대한 코드, 데이터 및 프롬프트는 커뮤니티의 추가 벤치마킹을 위해 공개되어 있습니다: https://github.com/bionlproc/ZeroShotRE

## 📝 요약

이 논문은 제로샷 방법론을 활용하여 바이오메디컬 관계 추출(RE)에서의 성능을 평가합니다. OpenAI의 GPT-4-turbo, o1, GPT-OSS 모델을 사용하여 7개의 데이터셋에서 실험을 수행하였으며, JSON 생성 기능을 통해 구조화된 출력을 생성했습니다. 연구 결과, 제로샷 성능이 미세 조정된 방법과 유사하게 나타났으나, 많은 관계를 포함한 경우와 텍스트 경계에서의 오류가 한계로 지적되었습니다. 이러한 제로샷 능력은 데이터셋 제작 비용과 NLP 모델링 필요성을 줄이는 데 기여할 수 있습니다. 연구의 코드와 데이터는 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 본 연구는 OpenAI의 GPT-4-turbo, o1, GPT-OSS 모델을 사용하여 다양한 생의학적 관계 추출(RE) 작업에서의 성능을 비교한 최초의 연구입니다.
- 2. 제로샷 성능은 미세 조정된 방법과 유사한 수준으로 나타났으나, 많은 관계를 포함한 경우와 텍스트 언급의 경계에서 성능이 저하되었습니다.
- 3. LLMs는 복잡한 생의학적 RE 작업에서 유망한 제로샷 능력을 보이며, 데이터셋 큐레이션 비용과 NLP 모델링 필요성을 줄일 수 있습니다.
- 4. 연구의 한계점을 해결하면 신뢰성을 더욱 높일 수 있으며, 모든 실험의 코드, 데이터 및 프롬프트는 공개되어 추가 벤치마킹이 가능합니다.


---

*Generated on 2025-09-23 11:43:28*