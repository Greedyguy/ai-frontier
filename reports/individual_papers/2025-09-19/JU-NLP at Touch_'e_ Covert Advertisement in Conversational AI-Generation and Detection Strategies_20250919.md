---
keywords:
  - Large Language Models
  - Prompt-based Reformulation
  - Conversational AI
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14256
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:39:28.373569",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Models",
    "Prompt-based Reformulation",
    "Conversational AI"
  ],
  "rejected_keywords": [
    "Covert Advertisement"
  ],
  "similarity_scores": {
    "Large Language Models": 0.85,
    "Prompt-based Reformulation": 0.82,
    "Conversational AI": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# JU-NLP at Touch\'e: Covert Advertisement in Conversational AI-Generation and Detection Strategies

**Korean Title:** JU-NLP at Touch'é: 대화형 AI에서의 은밀한 광고 생성 및 탐지 전략

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Conversational AI|Conversational AI]]
**🔗 Specific Connectable**: [[keywords/Large Language Models|Large Language Model]]
**🚀 Evolved Concepts**: [[keywords/Prompt-based Reformulation|Prompt-based Reformulation]]

## 🔗 유사한 논문
- [[GEM-Bench A Benchmark for Ad-Injected Response Generation within Generative Engine Marketing]] (82.3% similar)
- [[AgentCTG Harnessing Multi-Agent Collaboration for Fine-Grained Precise Control in Text Generation]] (81.1% similar)
- [[$Agent^2$ An Agent-Generates-Agent Framework for Reinforcement Learning Automation]] (80.0% similar)
- [[DuetUI A Bidirectional Context Loop for Human-Agent Co-Generation of Task-Oriented Interfaces]] (79.6% similar)
- [[Language Models Identify Ambiguities and Exploit Loopholes]] (79.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14256v1 Announce Type: cross 
Abstract: This paper proposes a comprehensive framework for the generation of covert advertisements within Conversational AI systems, along with robust techniques for their detection. It explores how subtle promotional content can be crafted within AI-generated responses and introduces methods to identify and mitigate such covert advertising strategies. For generation (Sub-Task~1), we propose a novel framework that leverages user context and query intent to produce contextually relevant advertisements. We employ advanced prompting strategies and curate paired training data to fine-tune a large language model (LLM) for enhanced stealthiness. For detection (Sub-Task~2), we explore two effective strategies: a fine-tuned CrossEncoder (\texttt{all-mpnet-base-v2}) for direct classification, and a prompt-based reformulation using a fine-tuned \texttt{DeBERTa-v3-base} model. Both approaches rely solely on the response text, ensuring practicality for real-world deployment. Experimental results show high effectiveness in both tasks, achieving a precision of 1.0 and recall of 0.71 for ad generation, and F1-scores ranging from 0.99 to 1.00 for ad detection. These results underscore the potential of our methods to balance persuasive communication with transparency in conversational AI.

## 🔍 Abstract (한글 번역)

arXiv:2509.14256v1 발표 유형: 교차  
초록: 이 논문은 대화형 AI 시스템 내에서 은밀한 광고를 생성하기 위한 포괄적인 프레임워크와 이를 탐지하기 위한 견고한 기법을 제안합니다. AI 생성 응답 내에 미묘한 홍보 콘텐츠를 어떻게 제작할 수 있는지를 탐구하고, 그러한 은밀한 광고 전략을 식별하고 완화하는 방법을 소개합니다. 생성(Sub-Task~1)을 위해, 우리는 사용자 맥락과 쿼리 의도를 활용하여 맥락적으로 관련성 있는 광고를 생성하는 새로운 프레임워크를 제안합니다. 고급 프롬프트 전략을 사용하고 쌍으로 된 훈련 데이터를 큐레이션하여 대형 언어 모델(LLM)을 미세 조정하여 은밀성을 향상시킵니다. 탐지(Sub-Task~2)를 위해, 우리는 두 가지 효과적인 전략을 탐구합니다: 직접 분류를 위한 미세 조정된 CrossEncoder(\texttt{all-mpnet-base-v2})와 미세 조정된 \texttt{DeBERTa-v3-base} 모델을 사용한 프롬프트 기반 재구성. 두 접근법 모두 응답 텍스트에만 의존하여 실제 환경에서의 실용성을 보장합니다. 실험 결과는 두 작업 모두에서 높은 효과성을 보여주며, 광고 생성에서 정밀도 1.0과 재현율 0.71을 달성하고, 광고 탐지에서는 F1 점수가 0.99에서 1.00 범위에 이릅니다. 이러한 결과는 대화형 AI에서 설득력 있는 커뮤니케이션과 투명성의 균형을 맞추기 위한 우리의 방법의 잠재력을 강조합니다.

## 📝 요약

이 논문은 대화형 AI 시스템 내에서 은밀한 광고를 생성하고 이를 탐지하는 포괄적인 프레임워크를 제안합니다. 광고 생성에서는 사용자 맥락과 쿼리 의도를 활용하여 맥락에 맞는 광고를 생성하는 새로운 프레임워크를 제시하며, 고급 프롬프트 전략과 훈련 데이터를 통해 대형 언어 모델(LLM)을 미세 조정합니다. 광고 탐지에서는 CrossEncoder와 DeBERTa-v3-base 모델을 사용한 두 가지 효과적인 전략을 탐구합니다. 실험 결과, 광고 생성에서 정밀도 1.0, 재현율 0.71, 광고 탐지에서 F1 점수 0.99~1.00을 달성하여 제안된 방법의 높은 효과성을 입증했습니다. 이러한 결과는 대화형 AI에서 설득력 있는 커뮤니케이션과 투명성을 조화롭게 유지할 수 있는 가능성을 보여줍니다.

## 🎯 주요 포인트

- 1. 이 논문은 대화형 AI 시스템 내에서 은밀한 광고를 생성하고 탐지하는 포괄적인 프레임워크를 제안합니다.

- 2. 사용자 맥락과 쿼리 의도를 활용하여 맥락적으로 관련 있는 광고를 생성하는 새로운 프레임워크를 소개합니다.

- 3. 광고 탐지를 위해 CrossEncoder와 DeBERTa-v3-base 모델을 활용한 두 가지 효과적인 전략을 제안합니다.

- 4. 실험 결과, 광고 생성에서 정밀도 1.0과 재현율 0.71, 광고 탐지에서 F1-스코어 0.99에서 1.00을 달성했습니다.

- 5. 제안된 방법은 대화형 AI에서 설득력 있는 커뮤니케이션과 투명성의 균형을 맞출 수 있는 잠재력을 보여줍니다.

---

*Generated on 2025-09-19 14:51:02*