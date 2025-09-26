---
keywords:
  - Large Language Models
  - Behavioral Finance
  - Personal Finance
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:45:04.867585",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Models",
    "Behavioral Finance",
    "Personal Finance"
  ],
  "rejected_keywords": [
    "Data-Generation Framework"
  ],
  "similarity_scores": {
    "Large Language Models": 0.8,
    "Behavioral Finance": 0.7,
    "Personal Finance": 0.65
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Synthesizing Behaviorally-Grounded Reasoning Chains: A Data-Generation Framework for Personal Finance LLMs

**Korean Title:** 행동 기반 추론 체인 합성: 개인 금융 대형 언어 모델을 위한 데이터 생성 프레임워크

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]    [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Large Language Models|Large Language Models]]
**⚡ Unique Technical**: [[keywords/Behavioral Finance|Behavioral Finance]], [[keywords/Personal Finance|Personal Finance]]

## 🔗 유사한 논문
- [[MAFA_ A multi-agent framework for annotation_20250918|MAFA A multi-agent framework for annotation]] (80.8% similar)
- [[(P)rior(D)yna(F)low_ A Priori Dynamic Workflow Construction via Multi-Agent Collaboration_20250919|(P)rior(D)yna(F)low A Priori Dynamic Workflow Construction via Multi-Agent Collaboration]] (79.5% similar)
- [[WebCoT_ Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback_20250919|WebCoT Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback]] (79.4% similar)
- [[From Patterns to Predictions_ A Shapelet-Based Framework for Directional Forecasting in Noisy Financial Markets_20250918|From Patterns to Predictions A Shapelet-Based Framework for Directional Forecasting in Noisy Financial Markets]] (79.1% similar)
- [[An LLM Agentic Approach for Legal-Critical Software_ A Case Study for Tax Prep Software_20250918|An LLM Agentic Approach for Legal-Critical Software A Case Study for Tax Prep Software]] (78.4% similar)

## 📋 저자 정보

**Authors:** Akhil Theerthala

## 📄 Abstract (원문)

Personalized financial advice requires consideration of user goals,
constraints, risk tolerance, and jurisdiction. Prior LLM work has focused on
support systems for investors and financial planners. Simultaneously, numerous
recent studies examine broader personal finance tasks, including budgeting,
debt management, retirement, and estate planning, through agentic pipelines
that incur high maintenance costs, yielding less than 25% of their expected
financial returns. In this study, we introduce a novel and reproducible
framework that integrates relevant financial context with behavioral finance
studies to construct supervision data for end-to-end advisors. Using this
framework, we create a 19k sample reasoning dataset and conduct a comprehensive
fine-tuning of the Qwen-3-8B model on the dataset. Through a held-out test
split and a blind LLM-jury study, we demonstrate that through careful data
curation and behavioral integration, our 8B model achieves performance
comparable to significantly larger baselines (14-32B parameters) across factual
accuracy, fluency, and personalization metrics while incurring 80% lower costs
than the larger counterparts.

## 🔍 Abstract (한글 번역)

개인화된 재무 조언은 사용자 목표, 제약 조건, 위험 수용도, 그리고 관할권을 고려해야 합니다. 이전의 대규모 언어 모델(LLM) 연구는 투자자와 재무 계획자를 위한 지원 시스템에 중점을 두었습니다. 동시에, 최근의 여러 연구들은 예산 관리, 부채 관리, 은퇴, 그리고 유산 계획을 포함한 더 넓은 개인 재무 과제를 에이전트 파이프라인을 통해 조사하고 있으며, 이는 높은 유지 비용을 초래하고 기대 수익의 25% 미만을 실현하고 있습니다. 본 연구에서는 관련 재무 맥락과 행동 재무 연구를 통합하여 종단 간 자문가를 위한 감독 데이터를 구축하는 새로운 재현 가능한 프레임워크를 소개합니다. 이 프레임워크를 사용하여 19,000개의 샘플 추론 데이터셋을 생성하고, Qwen-3-8B 모델을 데이터셋에 맞추어 종합적인 미세 조정을 수행합니다. 보류된 테스트 분할과 블라인드 LLM-배심원 연구를 통해, 신중한 데이터 큐레이션과 행동 통합을 통해 우리의 8B 모델이 사실적 정확성, 유창성, 개인화 지표에서 훨씬 더 큰 기준 모델(14-32B 파라미터)과 비교 가능한 성능을 달성하면서도 더 큰 모델에 비해 80% 낮은 비용을 발생시킨다는 것을 입증합니다.

## 📝 요약

이 연구는 개인 맞춤형 금융 조언을 제공하기 위해 사용자 목표, 제약 조건, 위험 수용도 및 관할권을 고려하는 새로운 프레임워크를 제안합니다. 기존 연구는 투자자와 금융 계획자를 위한 지원 시스템에 중점을 두었으나, 본 연구는 행동 금융학을 통합하여 감독 데이터를 구축하고, 이를 통해 Qwen-3-8B 모델을 미세 조정했습니다. 19,000개의 샘플 데이터셋을 활용하여, 사실 정확성, 유창성, 개인화 측면에서 더 큰 모델(14-32B 파라미터)과 유사한 성능을 보이면서도 비용을 80% 절감할 수 있음을 입증했습니다.

## 🎯 주요 포인트

- 1. 개인화된 금융 조언은 사용자 목표, 제약, 위험 수용도 및 관할권을 고려해야 합니다.

- 2. 기존 연구는 투자자 및 금융 계획자를 위한 지원 시스템에 중점을 두었습니다.

- 3. 본 연구에서는 행동 금융 연구와 관련 금융 맥락을 통합하여 엔드 투 엔드 조언자를 위한 감독 데이터를 구축하는 새로운 프레임워크를 제안합니다.

- 4. 제안된 프레임워크를 통해 19,000개의 샘플 추론 데이터셋을 생성하고 Qwen-3-8B 모델을 정교하게 튜닝했습니다.

- 5. 우리의 8B 모델은 데이터 큐레이션과 행동 통합을 통해 더 큰 모델들에 비해 80% 낮은 비용으로 사실 정확성, 유창성 및 개인화 측면에서 유사한 성능을 달성했습니다.

---

*Generated on 2025-09-20 07:44:26*