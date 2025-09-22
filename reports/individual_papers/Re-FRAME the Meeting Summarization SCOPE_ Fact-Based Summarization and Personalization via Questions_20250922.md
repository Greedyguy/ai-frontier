# Re-FRAME the Meeting Summarization SCOPE: Fact-Based Summarization and Personalization via Questions

**Korean Title:** 회의 요약 범위 재구성: 질문을 통한 사실 기반 요약 및 개인화

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Fact-Based Summarization

## 🔗 유사한 논문
- [[2025-09-19/LLM Agents at the Roundtable_ A Multi-Perspective and Dialectical Reasoning Framework for Essay Scoring_20250919|LLM Agents at the Roundtable A Multi-Perspective and Dialectical Reasoning Framework for Essay Scoring]] (82.3% similar)
- [[2025-09-19/Understanding the Thinking Process of Reasoning Models_ A Perspective from Schoenfeld's Episode Theory_20250919|Understanding the Thinking Process of Reasoning Models A Perspective from Schoenfeld's Episode Theory]] (81.1% similar)
- [[2025-09-19/Opening the Black Box_ Interpretable LLMs via Semantic Resonance Architecture_20250919|Opening the Black Box Interpretable LLMs via Semantic Resonance Architecture]] (80.9% similar)
- [[2025-09-17/DSCC-HS_ A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models_20250917|DSCC-HS A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models]] (80.7% similar)
- [[2025-09-19/Internalizing Self-Consistency in Language Models_ Multi-Agent Consensus Alignment_20250919|Internalizing Self-Consistency in Language Models Multi-Agent Consensus Alignment]] (80.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15901v1 Announce Type: cross 
Abstract: Meeting summarization with large language models (LLMs) remains error-prone, often producing outputs with hallucinations, omissions, and irrelevancies. We present FRAME, a modular pipeline that reframes summarization as a semantic enrichment task. FRAME extracts and scores salient facts, organizes them thematically, and uses these to enrich an outline into an abstractive summary. To personalize summaries, we introduce SCOPE, a reason-out-loud protocol that has the model build a reasoning trace by answering nine questions before content selection. For evaluation, we propose P-MESA, a multi-dimensional, reference-free evaluation framework to assess if a summary fits a target reader. P-MESA reliably identifies error instances, achieving >= 89% balanced accuracy against human annotations and strongly aligns with human severity ratings (r >= 0.70). On QMSum and FAME, FRAME reduces hallucination and omission by 2 out of 5 points (measured with MESA), while SCOPE improves knowledge fit and goal alignment over prompt-only baselines. Our findings advocate for rethinking summarization to improve control, faithfulness, and personalization.

## 🔍 Abstract (한글 번역)

arXiv:2509.15901v1 발표 유형: 교차  
초록: 대형 언어 모델(LLMs)을 사용한 회의 요약은 여전히 오류가 발생하기 쉬우며, 종종 환각, 누락, 무관한 내용이 포함된 출력을 생성합니다. 우리는 요약을 의미적 풍부화 작업으로 재구성하는 모듈식 파이프라인인 FRAME을 제안합니다. FRAME은 중요한 사실을 추출하고 점수를 매기며, 이를 주제별로 조직하여 개요를 풍부한 추상적 요약으로 발전시킵니다. 요약을 개인화하기 위해, 우리는 SCOPE라는 프로토콜을 도입하여 모델이 콘텐츠 선택 전에 아홉 가지 질문에 답함으로써 추론 과정을 구축하도록 합니다. 평가를 위해, 우리는 목표 독자에게 적합한 요약인지 평가할 수 있는 다차원, 참조 없는 평가 프레임워크인 P-MESA를 제안합니다. P-MESA는 오류 사례를 신뢰성 있게 식별하며, 인간 주석과 비교하여 89% 이상의 균형 정확도를 달성하고 인간의 심각도 평가와 강하게 일치합니다 (r >= 0.70). QMSum과 FAME에서, FRAME은 환각과 누락을 5점 만점에 2점 줄이며 (MESA로 측정), SCOPE는 프롬프트 기반 기준보다 지식 적합성과 목표 정렬을 향상시킵니다. 우리의 연구 결과는 요약을 재고하여 제어, 신뢰성, 개인화를 개선할 필요성을 제안합니다.

## 📝 요약

이 논문은 대형 언어 모델(LLMs)을 활용한 회의 요약의 문제점을 해결하기 위해 FRAME이라는 모듈형 파이프라인을 제안합니다. FRAME은 요약을 의미적 강화 작업으로 재구성하여 중요한 사실을 추출하고 주제별로 정리하여 요약을 생성합니다. 또한, SCOPE라는 프로토콜을 도입하여 모델이 콘텐츠 선택 전에 아홉 가지 질문에 답하면서 추론 과정을 구축하도록 합니다. 평가를 위해 P-MESA라는 다차원적, 참조 없는 평가 프레임워크를 제안하여 요약이 목표 독자에 적합한지를 평가합니다. P-MESA는 인간 평가와 높은 상관관계를 보이며, FRAME은 환각과 누락을 줄이고, SCOPE는 지식 적합성과 목표 정렬을 개선합니다. 연구 결과는 요약의 통제력, 신뢰성, 개인화를 개선하기 위한 새로운 접근 방식을 제안합니다.

## 🎯 주요 포인트

- 1. FRAME는 요약을 의미적 강화 작업으로 재구성하여 핵심 사실을 추출하고 테마별로 조직하여 요약의 정확성을 높입니다.

- 2. SCOPE는 요약을 개인화하기 위해 모델이 아홉 가지 질문에 답하여 추론 과정을 구축하는 프로토콜을 도입합니다.

- 3. P-MESA는 참조 없이 요약이 목표 독자에게 적합한지를 평가하는 다차원 평가 프레임워크로, 인간 평가와 높은 상관관계를 보입니다.

- 4. FRAME은 QMSum과 FAME 데이터셋에서 환각과 누락을 줄이며, SCOPE는 지식 적합성과 목표 정렬을 개선합니다.

- 5. 연구 결과는 요약의 제어, 충실성, 개인화를 개선하기 위해 요약 방식을 재고할 필요성을 제시합니다.

---

*Generated on 2025-09-22 14:16:20*