---
keywords:
  - Machine Translation
  - Large Language Models
  - Transfer Learning
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14493
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:20:09.511428",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Machine Translation",
    "Large Language Models",
    "Transfer Learning"
  ],
  "rejected_keywords": [
    "Multilingual Toxicity Detection"
  ],
  "similarity_scores": {
    "Machine Translation": 0.85,
    "Large Language Models": 0.8,
    "Transfer Learning": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Translate, then Detect: Leveraging Machine Translation for Cross-Lingual Toxicity Classification

**Korean Title:** 번역 후 탐지: 기계 번역을 활용한 다국어 독성 분류

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Machine Translation|Machine Translation]], [[keywords/Transfer Learning|Cross-Lingual Transfer]]

## 🔗 유사한 논문
- [[DetectAnyLLM Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (81.5% similar)
- [[SMARTER A Data-efficient Framework to Improve Toxicity Detection with Explanation via Self-augmenting Large Language Models]] (80.7% similar)
- [[You Are What You Train Effects of Data Composition on Training Context-aware Machine Translation Models]] (80.4% similar)
- [[Semantic Alignment-Enhanced Code Translation via an LLM-Based Multi-Agent System_20250918|Semantic Alignment-Enhanced Code Translation via an LLM-Based Multi-Agent System]] (80.3% similar)
- [[Audio-Based Crowd-Sourced Evaluation of Machine Translation Quality_20250918|Audio-Based Crowd-Sourced Evaluation of Machine Translation Quality]] (79.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14493v1 Announce Type: new 
Abstract: Multilingual toxicity detection remains a significant challenge due to the scarcity of training data and resources for many languages. While prior work has leveraged the translate-test paradigm to support cross-lingual transfer across a range of classification tasks, the utility of translation in supporting toxicity detection at scale remains unclear. In this work, we conduct a comprehensive comparison of translation-based and language-specific/multilingual classification pipelines. We find that translation-based pipelines consistently outperform out-of-distribution classifiers in 81.3% of cases (13 of 16 languages), with translation benefits strongly correlated with both the resource level of the target language and the quality of the machine translation (MT) system. Our analysis reveals that traditional classifiers outperform large language model (LLM) judges, with this advantage being particularly pronounced for low-resource languages, where translate-classify methods dominate translate-judge approaches in 6 out of 7 cases. We additionally show that MT-specific fine-tuning on LLMs yields lower refusal rates compared to standard instruction-tuned models, but it can negatively impact toxicity detection accuracy for low-resource languages. These findings offer actionable guidance for practitioners developing scalable multilingual content moderation systems.

## 🔍 Abstract (한글 번역)

arXiv:2509.14493v1 발표 유형: 신규  
초록: 다국어 독성 감지 분야는 많은 언어에 대한 학습 데이터와 자원의 부족으로 인해 여전히 큰 도전 과제로 남아 있습니다. 이전 연구에서는 다양한 분류 작업에서 언어 간 전이를 지원하기 위해 번역-테스트 패러다임을 활용했지만, 대규모 독성 감지를 지원하는 번역의 유용성은 여전히 불분명합니다. 본 연구에서는 번역 기반 및 언어별/다국어 분류 파이프라인을 종합적으로 비교합니다. 번역 기반 파이프라인이 81.3%의 경우(16개 언어 중 13개)에서 분포 외 분류기보다 일관되게 우수한 성능을 보였으며, 번역의 이점은 대상 언어의 자원 수준과 기계 번역(MT) 시스템의 품질과 강한 상관 관계가 있음을 발견했습니다. 우리의 분석은 전통적인 분류기가 대형 언어 모델(LLM) 심판보다 우수한 성능을 보이며, 특히 자원이 부족한 언어에서 이 점이 두드러지며, 번역-분류 방법이 번역-심판 접근 방식을 7개 사례 중 6개에서 지배한다는 것을 보여줍니다. 또한, LLM에 대한 MT 특정 미세 조정이 표준 지침 조정 모델에 비해 거부율을 낮추지만, 자원이 부족한 언어의 독성 감지 정확성에는 부정적인 영향을 미칠 수 있음을 보여줍니다. 이러한 발견은 확장 가능한 다국어 콘텐츠 모더레이션 시스템을 개발하는 실무자에게 실질적인 지침을 제공합니다.

## 📝 요약

다언어 독성 탐지는 많은 언어에 대한 훈련 데이터와 자원의 부족으로 여전히 어려운 과제입니다. 본 연구는 번역 기반 및 언어별/다언어 분류 파이프라인을 비교하여, 번역 기반 접근법이 81.3%의 경우에서 더 우수함을 발견했습니다. 특히 번역의 이점은 대상 언어의 자원 수준과 기계 번역 시스템의 품질과 강하게 연관되어 있습니다. 전통적인 분류기가 대형 언어 모델(LLM)보다 성능이 뛰어났으며, 특히 자원이 부족한 언어에서 번역-분류 방법이 번역-판단 방법보다 우세했습니다. 또한, LLM에 대한 기계 번역(MT) 특화 미세 조정이 거부율을 낮추지만, 자원이 부족한 언어에서는 독성 탐지 정확도를 저하시킬 수 있음을 보여줍니다. 이러한 결과는 확장 가능한 다언어 콘텐츠 모더레이션 시스템 개발에 유용한 지침을 제공합니다.

## 🎯 주요 포인트

- 1. 다국어 유해성 탐지는 많은 언어에 대한 훈련 데이터와 자원의 부족으로 인해 여전히 큰 도전 과제입니다.

- 2. 번역 기반 파이프라인은 81.3%의 경우에서 번역하지 않은 분류기보다 우수한 성능을 보였습니다.

- 3. 번역의 이점은 대상 언어의 자원 수준과 기계 번역 시스템의 품질과 강하게 상관관계가 있습니다.

- 4. 전통적인 분류기가 대형 언어 모델(LLM) 판사보다 우수하며, 특히 자원이 적은 언어에서 그 차이가 두드러집니다.

- 5. 기계 번역(MT) 특화 미세 조정이 거부율을 낮출 수 있지만, 자원이 적은 언어에서는 유해성 탐지 정확도에 부정적인 영향을 미칠 수 있습니다.

---

*Generated on 2025-09-19 15:48:47*