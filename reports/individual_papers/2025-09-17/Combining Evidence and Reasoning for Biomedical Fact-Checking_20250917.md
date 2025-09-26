---
keywords:
  - Large Language Models
  - Natural Language Processing
  - Supervised Veracity Prediction
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:58:53.012283",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Models",
    "Natural Language Processing",
    "Supervised Veracity Prediction"
  ],
  "rejected_keywords": [
    "Biomedical Fact-Checking",
    "Scientific Evidence Retrieval"
  ],
  "similarity_scores": {
    "Large Language Models": 0.88,
    "Natural Language Processing": 0.85,
    "Supervised Veracity Prediction": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Combining Evidence and Reasoning for Biomedical Fact-Checking

**Korean Title:** 증거와 추론의 결합을 통한 생물의학적 사실 검증

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Natural Language Processing|Natural Language Processing]]
**⚡ Unique Technical**: [[keywords/Supervised Veracity Prediction|Supervised Veracity Prediction]]

## 🔗 유사한 논문
- [[Combating Biomedical Misinformation through Multi-modal Claim Detection and Evidence-based Verification_20250917|Combating Biomedical Misinformation through Multi-modal Claim Detection and Evidence-based Verification]] (99.0% similar)
- [[MedFact-R1_ Towards Factual Medical Reasoning via Pseudo-Label Augmentation_20250919|MedFact-R1 Towards Factual Medical Reasoning via Pseudo-Label Augmentation]] (84.4% similar)
- [[MedVAL_ Toward Expert-Level Medical Text Validation with Language Models_20250919|MedVAL Toward Expert-Level Medical Text Validation with Language Models]] (81.0% similar)
- [[Causal-Counterfactual RAG_ The Integration of Causal-Counterfactual Reasoning into RAG_20250919|Causal-Counterfactual RAG The Integration of Causal-Counterfactual Reasoning into RAG]] (78.4% similar)
- [[Listening, Imagining & Refining_ A Heuristic Optimized ASR Correction Framework with LLMs_20250919|Listening, Imagining & Refining A Heuristic Optimized ASR Correction Framework with LLMs]] (78.0% similar)

## 📋 저자 정보

**Authors:** Mariano Barone, Antonio Romano, Giuseppe Riccio, Marco Postiglione, Vincenzo Moscato

## 📄 Abstract (원문)

Misinformation in healthcare, from vaccine hesitancy to unproven treatments,
poses risks to public health and trust in medical systems. While machine
learning and natural language processing have advanced automated fact-checking,
validating biomedical claims remains uniquely challenging due to complex
terminology, the need for domain expertise, and the critical importance of
grounding in scientific evidence. We introduce CER (Combining Evidence and
Reasoning), a novel framework for biomedical fact-checking that integrates
scientific evidence retrieval, reasoning via large language models, and
supervised veracity prediction. By integrating the text-generation capabilities
of large language models with advanced retrieval techniques for high-quality
biomedical scientific evidence, CER effectively mitigates the risk of
hallucinations, ensuring that generated outputs are grounded in verifiable,
evidence-based sources. Evaluations on expert-annotated datasets (HealthFC,
BioASQ-7b, SciFact) demonstrate state-of-the-art performance and promising
cross-dataset generalization. Code and data are released for transparency and
reproducibility: https: //github.com/PRAISELab-PicusLab/CER.

## 🔍 Abstract (한글 번역)

의료 분야에서의 잘못된 정보는 백신 주저에서부터 입증되지 않은 치료법에 이르기까지 공중 보건과 의료 시스템에 대한 신뢰에 위험을 초래합니다. 기계 학습과 자연어 처리 기술이 자동화된 사실 확인을 발전시켰지만, 생의학적 주장 검증은 복잡한 용어, 분야 전문 지식의 필요성, 과학적 증거에 기반해야 하는 중요성 때문에 여전히 독특하게 어려운 과제로 남아 있습니다. 우리는 과학적 증거 검색, 대형 언어 모델을 통한 추론, 감독된 진위 예측을 통합하는 새로운 생의학적 사실 확인 프레임워크인 CER(Combining Evidence and Reasoning)를 소개합니다. 대형 언어 모델의 텍스트 생성 능력을 고품질 생의학적 과학 증거를 위한 고급 검색 기술과 통합함으로써, CER은 생성된 출력이 검증 가능한 증거 기반 출처에 근거하도록 하여 환각의 위험을 효과적으로 완화합니다. 전문가가 주석을 단 데이터셋(HealthFC, BioASQ-7b, SciFact)에 대한 평가에서 최첨단 성능과 유망한 데이터셋 간 일반화가 입증되었습니다. 투명성과 재현성을 위해 코드와 데이터가 공개되었습니다: https://github.com/PRAISELab-PicusLab/CER.

## 📝 요약

이 논문은 의료 분야에서의 잘못된 정보 문제를 해결하기 위해 새로운 프레임워크인 CER(Combining Evidence and Reasoning)를 제안합니다. CER는 과학적 증거 검색, 대형 언어 모델을 통한 추론, 감독된 진위 예측을 통합하여 생의학적 사실 검증을 수행합니다. 특히 대형 언어 모델의 텍스트 생성 능력과 고품질 생의학적 증거 검색 기술을 결합하여 잘못된 정보 생성 위험을 줄이고, 생성된 결과가 검증 가능한 증거에 기반하도록 합니다. HealthFC, BioASQ-7b, SciFact와 같은 전문가 주석 데이터셋에서 최첨단 성능과 데이터셋 간 일반화 가능성을 입증하였으며, 코드와 데이터를 공개하여 투명성과 재현성을 보장합니다.

## 🎯 주요 포인트

- 1. 의료 분야의 허위 정보는 공중 보건과 의료 시스템에 대한 신뢰에 위험을 초래합니다.

- 2. 생의학적 주장 검증은 복잡한 용어와 과학적 증거의 중요성 때문에 도전적입니다.

- 3. CER은 과학적 증거 검색과 대형 언어 모델을 통한 추론을 결합한 새로운 생의학적 사실 검증 프레임워크입니다.

- 4. CER은 고품질의 생의학적 증거를 활용하여 생성된 출력이 검증 가능한 증거 기반 소스에 근거하도록 합니다.

- 5. CER은 전문가 주석 데이터셋에서 최첨단 성능과 데이터셋 간 일반화 가능성을 보여줍니다.

---

*Generated on 2025-09-20 09:27:05*