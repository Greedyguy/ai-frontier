---
keywords:
  - Machine Translation
  - Multilingual Regression Models
  - COMET Framework
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:52:03.824732",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Machine Translation",
    "Multilingual Regression Models",
    "COMET Framework"
  ],
  "rejected_keywords": [
    "Translation Quality Evaluation",
    "Long-context Data"
  ],
  "similarity_scores": {
    "Machine Translation": 0.8,
    "Multilingual Regression Models": 0.77,
    "COMET Framework": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Long-context Reference-based MT Quality Estimation

**Korean Title:** 장문 맥락 참조 기반 기계 번역 품질 추정

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]       [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Machine Translation|Machine Translation]]
**🔗 Specific Connectable**: [[keywords/Multilingual Regression Models|Multilingual Regression Models]]
**⚡ Unique Technical**: [[keywords/COMET Framework|COMET framework]]

## 🔗 유사한 논문
- [[You Are What You Train_ Effects of Data Composition on Training Context-aware Machine Translation Models_20250917|You Are What You Train Effects of Data Composition on Training Context-aware Machine Translation Models]] (82.8% similar)
- [[Audio-Based Crowd-Sourced Evaluation of Machine Translation Quality_20250918|Audio-Based Crowd-Sourced Evaluation of Machine Translation Quality]] (82.7% similar)
- [[A Multi-To-One Interview Paradigm for Efficient MLLM Evaluation_20250919|A Multi-To-One Interview Paradigm for Efficient MLLM Evaluation]] (78.6% similar)
- [[Introducing OmniGEC_ A Silver Multilingual Dataset for Grammatical Error Correction_20250919|Introducing OmniGEC A Silver Multilingual Dataset for Grammatical Error Correction]] (78.2% similar)
- [[Ticket-Bench_ A Kickoff for Multilingual and Regionalized Agent Evaluation_20250919|Ticket-Bench A Kickoff for Multilingual and Regionalized Agent Evaluation]] (78.2% similar)

## 📋 저자 정보

**Authors:** Sami Ul Haq, Chinonso Cynthia Osuji, Sheila Castilho, Brian Davis

## 📄 Abstract (원문)

In this paper, we present our submission to the Tenth Conference on Machine
Translation (WMT25) Shared Task on Automated Translation Quality Evaluation.
  Our systems are built upon the COMET framework and trained to predict
segment-level Error Span Annotation (ESA) scores using augmented long-context
data.
  To construct long-context training data, we concatenate in-domain,
human-annotated sentences and compute a weighted average of their scores.
  We integrate multiple human judgment datasets (MQM, SQM, and DA) by
normalising their scales and train multilingual regression models to predict
quality scores from the source, hypothesis, and reference translations.
  Experimental results show that incorporating long-context information
improves correlations with human judgments compared to models trained only on
short segments.

## 🔍 Abstract (한글 번역)

이 논문에서는 제10회 기계 번역 회의(WMT25) 자동 번역 품질 평가 공동 과제에 제출한 시스템을 소개합니다. 우리의 시스템은 COMET 프레임워크를 기반으로 구축되었으며, 확장된 장문 맥락 데이터를 사용하여 세그먼트 수준의 오류 범위 주석(ESA) 점수를 예측하도록 훈련되었습니다. 장문 맥락 훈련 데이터를 구성하기 위해, 우리는 도메인 내에서 인간이 주석을 단 문장들을 연결하고, 그들의 점수에 대한 가중 평균을 계산합니다. MQM, SQM, DA와 같은 여러 인간 판단 데이터셋을 통합하여 그들의 척도를 정규화하고, 소스, 가설, 참조 번역에서 품질 점수를 예측하기 위한 다국어 회귀 모델을 훈련합니다. 실험 결과는 장문 맥락 정보를 통합하는 것이 짧은 세그먼트만으로 훈련된 모델에 비해 인간 판단과의 상관 관계를 개선함을 보여줍니다.

## 📝 요약

이 논문은 WMT25 자동 번역 품질 평가 공유 과제에 제출된 연구로, COMET 프레임워크를 기반으로 하여 세그먼트 수준의 오류 범위 주석(ESA) 점수를 예측하는 시스템을 제안합니다. 장문 맥락 데이터를 활용하여 훈련된 이 시스템은 도메인 내 인간 주석 문장을 연결하고 점수의 가중 평균을 계산하여 장문 맥락 훈련 데이터를 구성합니다. MQM, SQM, DA 등 다양한 인간 판단 데이터셋을 통합하고, 이들의 척도를 정규화하여 소스, 가설, 참조 번역으로부터 품질 점수를 예측하는 다국어 회귀 모델을 훈련합니다. 실험 결과, 장문 맥락 정보를 포함하면 짧은 세그먼트로만 훈련된 모델에 비해 인간 판단과의 상관관계가 개선됨을 보여줍니다.

## 🎯 주요 포인트

- 1. 본 연구는 WMT25 자동 번역 품질 평가 공유 과제에 대한 제출작으로, COMET 프레임워크를 기반으로 구축된 시스템을 소개합니다.

- 2. 장문 맥락 데이터를 활용하여 세그먼트 수준의 오류 범위 주석 점수를 예측하도록 시스템을 훈련했습니다.

- 3. 장문 맥락 훈련 데이터를 구축하기 위해 도메인 내 인간 주석 문장을 연결하고, 그들의 점수에 가중 평균을 계산했습니다.

- 4. 다양한 인간 판단 데이터셋(MQM, SQM, DA)을 통합하여 스케일을 정규화하고, 소스, 가설, 참조 번역에서 품질 점수를 예측하는 다국어 회귀 모델을 훈련했습니다.

- 5. 실험 결과, 장문 맥락 정보를 통합함으로써 짧은 세그먼트만으로 훈련된 모델에 비해 인간 판단과의 상관관계가 향상되었습니다.

---

*Generated on 2025-09-20 09:21:16*