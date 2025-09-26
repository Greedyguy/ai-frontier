---
keywords:
  - Large Language Models
  - Attention Mechanism
  - Graph Neural Networks
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:46:12.638844",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Models",
    "Attention Mechanism",
    "Graph Neural Networks"
  ],
  "rejected_keywords": [
    "Spatially-Enhanced Attention",
    "Spatio-Temporal Forecasting"
  ],
  "similarity_scores": {
    "Large Language Models": 0.78,
    "Attention Mechanism": 0.77,
    "Graph Neural Networks": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# ST-LINK: Spatially-Aware Large Language Models for Spatio-Temporal Forecasting

**Korean Title:** ST-LINK: 시공간 예측을 위한 공간 인식 대형 언어 모델

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]       [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]], [[keywords/Graph Neural Networks|Graph-Structured Spatial Data]]
**🚀 Evolved Concepts**: [[keywords/Large Language Models|Large Language Models]]

## 🔗 유사한 논문
- [[Improving Internet Traffic Matrix Prediction via Time Series Clustering_20250919|Improving Internet Traffic Matrix Prediction via Time Series Clustering]] (82.3% similar)
- [[Unleashing the Potential of Multimodal LLMs for Zero-Shot Spatio-Temporal Video Grounding_20250919|Unleashing the Potential of Multimodal LLMs for Zero-Shot Spatio-Temporal Video Grounding]] (82.1% similar)
- [[Traffic Co-Simulation Framework Empowered by Infrastructure Camera Sensing and Reinforcement Learning_20250919|Traffic Co-Simulation Framework Empowered by Infrastructure Camera Sensing and Reinforcement Learning]] (82.0% similar)
- [[LLM-I_ LLMs are Naturally Interleaved Multimodal Creators_20250918|LLM-I LLMs are Naturally Interleaved Multimodal Creators]] (80.2% similar)
- [[CARGO_ A Framework for Confidence-Aware Routing of Large Language Models_20250918|CARGO A Framework for Confidence-Aware Routing of Large Language Models]] (80.1% similar)

## 📋 저자 정보

**Authors:** Hyotaek Jeon, Hyunwook Lee, Juwon Kim, Sungahn Ko

## 📄 Abstract (원문)

Traffic forecasting represents a crucial problem within intelligent
transportation systems. In recent research, Large Language Models (LLMs) have
emerged as a promising method, but their intrinsic design, tailored primarily
for sequential token processing, introduces notable challenges in effectively
capturing spatial dependencies. Specifically, the inherent limitations of LLMs
in modeling spatial relationships and their architectural incompatibility with
graph-structured spatial data remain largely unaddressed. To overcome these
limitations, we introduce ST-LINK, a novel framework that enhances the
capability of Large Language Models to capture spatio-temporal dependencies.
Its key components are Spatially-Enhanced Attention (SE-Attention) and the
Memory Retrieval Feed-Forward Network (MRFFN). SE-Attention extends rotary
position embeddings to integrate spatial correlations as direct rotational
transformations within the attention mechanism. This approach maximizes spatial
learning while preserving the LLM's inherent sequential processing structure.
Meanwhile, MRFFN dynamically retrieves and utilizes key historical patterns to
capture complex temporal dependencies and improve the stability of long-term
forecasting. Comprehensive experiments on benchmark datasets demonstrate that
ST-LINK surpasses conventional deep learning and LLM approaches, and
effectively captures both regular traffic patterns and abrupt changes.

## 🔍 Abstract (한글 번역)

교통 예측은 지능형 교통 시스템에서 중요한 문제를 나타냅니다. 최근 연구에서는 대형 언어 모델(LLM)이 유망한 방법으로 부상했지만, 주로 순차적인 토큰 처리에 맞춰진 이들의 본질적인 설계는 공간적 종속성을 효과적으로 포착하는 데 있어 상당한 도전을 제기합니다. 구체적으로, LLM의 공간적 관계를 모델링하는 데 있어서의 내재적 한계와 그래프 구조의 공간 데이터를 다루는 데 있어서의 구조적 비호환성은 대부분 해결되지 않은 상태로 남아 있습니다. 이러한 한계를 극복하기 위해, 우리는 대형 언어 모델의 시공간적 종속성 포착 능력을 강화하는 새로운 프레임워크인 ST-LINK를 소개합니다. ST-LINK의 주요 구성 요소는 공간 강화 주의 메커니즘(SE-Attention)과 메모리 검색 피드포워드 네트워크(MRFFN)입니다. SE-Attention은 회전 위치 임베딩을 확장하여 주의 메커니즘 내에서 공간 상관관계를 직접적인 회전 변환으로 통합합니다. 이 접근 방식은 LLM의 고유한 순차 처리 구조를 유지하면서 공간 학습을 극대화합니다. 한편, MRFFN은 주요 역사적 패턴을 동적으로 검색하고 활용하여 복잡한 시간적 종속성을 포착하고 장기 예측의 안정성을 향상시킵니다. 벤치마크 데이터셋에 대한 종합적인 실험 결과, ST-LINK는 기존의 딥러닝 및 LLM 접근 방식을 능가하며, 규칙적인 교통 패턴과 급격한 변화를 모두 효과적으로 포착함을 보여줍니다.

## 📝 요약

교통 예측은 지능형 교통 시스템에서 중요한 문제입니다. 최근 연구에서는 대형 언어 모델(LLM)이 유망한 방법으로 떠올랐지만, 주로 순차적 토큰 처리에 맞춰진 설계로 인해 공간적 의존성을 효과적으로 포착하는 데 어려움이 있습니다. 이를 해결하기 위해 ST-LINK라는 새로운 프레임워크를 제안합니다. ST-LINK는 공간-시간 의존성을 포착하기 위해 공간 강화 주의(SE-Attention)와 메모리 검색 피드포워드 네트워크(MRFFN)를 도입합니다. SE-Attention은 회전 위치 임베딩을 확장하여 주의 메커니즘 내에서 공간 상관관계를 직접 회전 변환으로 통합합니다. MRFFN은 주요 역사적 패턴을 동적으로 검색하여 복잡한 시간적 의존성을 포착하고 장기 예측의 안정성을 향상시킵니다. 벤치마크 데이터셋에 대한 실험 결과, ST-LINK는 기존의 심층 학습 및 LLM 접근 방식을 능가하며, 규칙적인 교통 패턴과 급격한 변화를 효과적으로 포착합니다.

## 🎯 주요 포인트

- 1. LLMs는 순차적 토큰 처리에 최적화되어 있어 공간적 의존성을 효과적으로 포착하는 데 어려움이 있다.

- 2. ST-LINK는 LLM의 시공간 의존성 포착 능력을 강화하는 새로운 프레임워크로, SE-Attention과 MRFFN을 핵심 구성 요소로 한다.

- 3. SE-Attention은 회전 위치 임베딩을 확장하여 주의 메커니즘 내에서 공간 상관관계를 직접 회전 변환으로 통합한다.

- 4. MRFFN은 주요 역사적 패턴을 동적으로 검색 및 활용하여 복잡한 시간적 의존성을 포착하고 장기 예측의 안정성을 향상시킨다.

- 5. ST-LINK는 벤치마크 데이터셋에서 기존의 딥러닝 및 LLM 접근 방식을 능가하며, 규칙적인 교통 패턴과 급격한 변화를 효과적으로 포착한다.

---

*Generated on 2025-09-20 09:36:24*