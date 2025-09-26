---
keywords:
  - Large Language Models
  - Metadata Extraction
  - Few-Shot Learning
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2505.19800
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:35:51.690762",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Models",
    "Metadata Extraction",
    "Few-Shot Learning"
  ],
  "rejected_keywords": [
    "Benchmark Evaluation"
  ],
  "similarity_scores": {
    "Large Language Models": 0.8,
    "Metadata Extraction": 0.75,
    "Few-Shot Learning": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# MOLE: Metadata Extraction and Validation in Scientific Papers Using LLMs

**Korean Title:** 과학 논문에서 LLM을 사용한 메타데이터 추출 및 검증: MOLE

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Large Language Models|Large Language Models]], [[keywords/Few-Shot Learning|Few-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Metadata Extraction|Metadata Extraction]]

## 🔗 유사한 논문
- [[Middo Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (83.6% similar)
- [[From Automation to Autonomy A Survey on Large Language Models in Scientific Discovery]] (83.3% similar)
- [[Modular Machine Learning An Indispensable Path towards New-Generation Large Language Models]] (82.8% similar)
- [[Decoupled Proxy Alignment Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (82.5% similar)
- [[MedVAL Toward Expert-Level Medical Text Validation with Language Models]] (82.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.19800v2 Announce Type: replace 
Abstract: Metadata extraction is essential for cataloging and preserving datasets, enabling effective research discovery and reproducibility, especially given the current exponential growth in scientific research. While Masader (Alyafeai et al.,2021) laid the groundwork for extracting a wide range of metadata attributes from Arabic NLP datasets' scholarly articles, it relies heavily on manual annotation. In this paper, we present MOLE, a framework that leverages Large Language Models (LLMs) to automatically extract metadata attributes from scientific papers covering datasets of languages other than Arabic. Our schema-driven methodology processes entire documents across multiple input formats and incorporates robust validation mechanisms for consistent output. Additionally, we introduce a new benchmark to evaluate the research progress on this task. Through systematic analysis of context length, few-shot learning, and web browsing integration, we demonstrate that modern LLMs show promising results in automating this task, highlighting the need for further future work improvements to ensure consistent and reliable performance. We release the code: https://github.com/IVUL-KAUST/MOLE and dataset: https://huggingface.co/datasets/IVUL-KAUST/MOLE for the research community.

## 🔍 Abstract (한글 번역)

arXiv:2505.19800v2 발표 유형: 교체  
초록: 메타데이터 추출은 데이터셋을 분류하고 보존하는 데 필수적이며, 특히 현재 과학 연구의 기하급수적인 성장에 비추어 효과적인 연구 발견과 재현성을 가능하게 합니다. Masader(Alyafeai et al., 2021)는 아랍어 NLP 데이터셋의 학술 논문에서 다양한 메타데이터 속성을 추출하기 위한 기초를 마련했지만, 수작업 주석에 크게 의존합니다. 이 논문에서는 아랍어 이외의 언어 데이터셋을 다루는 과학 논문에서 메타데이터 속성을 자동으로 추출하기 위해 대형 언어 모델(LLM)을 활용한 프레임워크인 MOLE을 제시합니다. 우리의 스키마 기반 방법론은 여러 입력 형식에 걸쳐 전체 문서를 처리하고 일관된 출력을 위한 강력한 검증 메커니즘을 통합합니다. 또한, 이 작업의 연구 진행을 평가하기 위한 새로운 벤치마크를 소개합니다. 문맥 길이, 소수 샷 학습, 웹 브라우징 통합의 체계적인 분석을 통해, 현대의 LLM이 이 작업을 자동화하는 데 유망한 결과를 보여주며, 일관되고 신뢰할 수 있는 성능을 보장하기 위한 향후 연구 개선의 필요성을 강조합니다. 우리는 연구 커뮤니티를 위해 코드(https://github.com/IVUL-KAUST/MOLE)와 데이터셋(https://huggingface.co/datasets/IVUL-KAUST/MOLE)을 공개합니다.

## 📝 요약

이 논문은 다양한 언어의 과학 논문에서 메타데이터를 자동으로 추출하는 프레임워크 MOLE을 소개합니다. 기존의 Masader 시스템이 아랍어 NLP 데이터셋에 대한 메타데이터 추출에 주로 수작업을 의존했던 것과 달리, MOLE은 대형 언어 모델(LLMs)을 활용하여 자동화된 추출을 가능하게 합니다. 이 방법론은 여러 입력 형식의 문서를 처리하고, 일관된 출력을 위한 검증 메커니즘을 포함합니다. 또한, 연구 진척도를 평가하기 위한 새로운 벤치마크를 제시하며, 현대 LLMs가 이 작업을 자동화하는 데 유망한 결과를 보임을 입증합니다. 연구 커뮤니티를 위해 코드와 데이터셋도 공개되었습니다.

## 🎯 주요 포인트

- 1. MOLE은 대형 언어 모델(LLMs)을 활용하여 아랍어 외의 언어 데이터셋을 다루는 학술 논문에서 메타데이터 속성을 자동으로 추출하는 프레임워크입니다.

- 2. 이 연구는 다양한 입력 형식을 처리하고 일관된 출력을 보장하기 위해 강력한 검증 메커니즘을 포함한 스키마 기반 방법론을 사용합니다.

- 3. 새로운 벤치마크를 도입하여 이 작업에 대한 연구 진척도를 평가하고, 현대 LLMs가 이 작업의 자동화에서 유망한 결과를 보임을 입증합니다.

- 4. 연구 커뮤니티를 위해 MOLE의 코드와 데이터셋을 공개하였습니다.

---

*Generated on 2025-09-19 15:58:58*