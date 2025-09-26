---
keywords:
  - Large Language Models
  - Confidence-Aware Routing
  - Uncertainty Quantification
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:36:37.915489",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Models",
    "Confidence-Aware Routing",
    "Uncertainty Quantification"
  ],
  "rejected_keywords": [
    "Optimization",
    "Domain-Specific Regressors"
  ],
  "similarity_scores": {
    "Large Language Models": 0.8,
    "Confidence-Aware Routing": 0.78,
    "Uncertainty Quantification": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# CARGO: A Framework for Confidence-Aware Routing of Large Language Models

**Korean Title:** CARGO: 대형 언어 모델의 신뢰 인식 라우팅을 위한 프레임워크

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Uncertainty Quantification|Uncertainty Quantification]]
**⚡ Unique Technical**: [[keywords/Confidence-Aware Routing|Confidence-Aware Routing]]
**🚀 Evolved Concepts**: [[keywords/Large Language Models|Large Language Models]]

## 🔗 유사한 논문
- [[Opening the Black Box_ Interpretable LLMs via Semantic Resonance Architecture_20250919|Opening the Black Box Interpretable LLMs via Semantic Resonance Architecture]] (84.5% similar)
- [[Adversarial Distilled Retrieval-Augmented Guarding Model for Online Malicious Intent Detection_20250919|Adversarial Distilled Retrieval-Augmented Guarding Model for Online Malicious Intent Detection]] (83.4% similar)
- [[DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (82.7% similar)
- [[{lambda}Scale_ Enabling Fast Scaling for Serverless Large Language Model Inference_20250919|{lambda}Scale Enabling Fast Scaling for Serverless Large Language Model Inference]] (82.5% similar)
- [[Select to Know_ An Internal-External Knowledge Self-Selection Framework for Domain-Specific Question Answering_20250919|Select to Know An Internal-External Knowledge Self-Selection Framework for Domain-Specific Question Answering]] (82.3% similar)

## 📋 저자 정보

**Authors:** Amine Barrak, Yosr Fourati, Michael Olchawa, Emna Ksontini, Khalil Zoghlami

## 📄 Abstract (원문)

As large language models (LLMs) proliferate in scale, specialization, and
latency profiles, the challenge of routing user prompts to the most appropriate
model has become increasingly critical for balancing performance and cost. We
introduce CARGO (Category-Aware Routing with Gap-based Optimization), a
lightweight, confidence-aware framework for dynamic LLM selection. CARGO
employs a single embedding-based regressor trained on LLM-judged pairwise
comparisons to predict model performance, with an optional binary classifier
invoked when predictions are uncertain. This two-stage design enables precise,
cost-aware routing without the need for human-annotated supervision. To capture
domain-specific behavior, CARGO also supports category-specific regressors
trained across five task groups: mathematics, coding, reasoning, summarization,
and creative writing. Evaluated on four competitive LLMs (GPT-4o, Claude 3.5
Sonnet, DeepSeek V3, and Perplexity Sonar), CARGO achieves a top-1 routing
accuracy of 76.4% and win rates ranging from 72% to 89% against individual
experts. These results demonstrate that confidence-guided, lightweight routing
can achieve expert-level performance with minimal overhead, offering a
practical solution for real-world, multi-model LLM deployments.

## 🔍 Abstract (한글 번역)

대규모 언어 모델(LLM)의 규모, 전문화, 지연 프로파일이 증가함에 따라 사용자 프롬프트를 가장 적합한 모델로 라우팅하는 문제는 성능과 비용의 균형을 맞추기 위해 점점 더 중요해지고 있습니다. 우리는 CARGO(Category-Aware Routing with Gap-based Optimization)를 소개합니다. 이는 경량의 신뢰도 인식 프레임워크로, 동적 LLM 선택을 지원합니다. CARGO는 LLM이 평가한 쌍별 비교를 기반으로 훈련된 단일 임베딩 기반 회귀 모델을 사용하여 모델 성능을 예측하며, 예측이 불확실할 경우 선택적으로 이진 분류기를 호출합니다. 이 2단계 설계는 인간이 주석을 달지 않은 감독이 필요 없이 정확하고 비용을 고려한 라우팅을 가능하게 합니다. 도메인별 행동을 포착하기 위해 CARGO는 수학, 코딩, 추론, 요약, 창의적 글쓰기의 5가지 작업 그룹에 걸쳐 훈련된 카테고리별 회귀 모델도 지원합니다. 네 가지 경쟁력 있는 LLM(GPT-4o, Claude 3.5 Sonnet, DeepSeek V3, Perplexity Sonar)에서 평가된 결과, CARGO는 76.4%의 상위 1 라우팅 정확도와 개별 전문가에 대한 72%에서 89%의 승률을 달성했습니다. 이러한 결과는 신뢰도에 기반한 경량 라우팅이 최소한의 오버헤드로 전문가 수준의 성능을 달성할 수 있음을 보여주며, 실제 다중 모델 LLM 배포를 위한 실용적인 솔루션을 제공합니다.

## 📝 요약

대형 언어 모델(LLM)의 다양성과 성능을 최적화하기 위해 사용자 프롬프트를 적절한 모델로 라우팅하는 것이 중요해졌습니다. 이를 해결하기 위해 CARGO(Categor-Aware Routing with Gap-based Optimization)를 제안합니다. CARGO는 LLM의 성능을 예측하기 위해 임베딩 기반 회귀 모델을 사용하며, 예측이 불확실할 경우 이진 분류기를 추가로 사용합니다. 이 방식은 인간의 주석 없이도 정확하고 비용 효율적인 라우팅을 가능하게 합니다. CARGO는 수학, 코딩, 추론, 요약, 창의적 글쓰기 등 5가지 작업 그룹에 대해 도메인별 회귀 모델을 지원합니다. GPT-4o, Claude 3.5 Sonnet, DeepSeek V3, Perplexity Sonar 등 4개의 LLM에서 평가한 결과, CARGO는 76.4%의 상위 1위 라우팅 정확도와 72%에서 89%의 승률을 기록했습니다. 이는 최소한의 오버헤드로 전문가 수준의 성능을 달성할 수 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. CARGO는 대규모 언어 모델(LLM) 선택을 위한 경량의 신뢰도 인식 프레임워크로, 성능과 비용의 균형을 맞추기 위해 사용자 프롬프트를 적절한 모델로 라우팅합니다.

- 2. CARGO는 LLM이 판단한 쌍별 비교를 기반으로 성능을 예측하는 단일 임베딩 기반 회귀 모델을 사용하며, 예측이 불확실할 경우 이진 분류기를 추가로 활용합니다.

- 3. CARGO는 수학, 코딩, 추론, 요약, 창의적 글쓰기의 다섯 가지 작업 그룹에 걸쳐 카테고리별 회귀 모델을 지원하여 도메인 특화 행동을 포착합니다.

- 4. 네 가지 경쟁력 있는 LLM(GPT-4o, Claude 3.5 Sonnet, DeepSeek V3, Perplexity Sonar)에서 평가된 결과, CARGO는 76.4%의 최상위 라우팅 정확도와 72%에서 89%의 승률을 기록했습니다.

- 5. CARGO는 최소한의 오버헤드로 전문가 수준의 성능을 달성할 수 있는 실용적인 솔루션을 제공하여, 실제 다중 모델 LLM 배포에 적합한 경량 라우팅을 실현합니다.

---

*Generated on 2025-09-20 02:44:54*