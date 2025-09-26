---
keywords:
  - Diffusion Models
  - Generative Models
  - Anti-Memorization Strategies
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14934
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:34:09.151693",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion Models",
    "Generative Models",
    "Anti-Memorization Strategies"
  ],
  "rejected_keywords": [
    "Stable Audio Open"
  ],
  "similarity_scores": {
    "Diffusion Models": 0.82,
    "Generative Models": 0.75,
    "Anti-Memorization Strategies": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Mitigating data replication in text-to-audio generative diffusion models through anti-memorization guidance

**Korean Title:** 텍스트-오디오 생성 확산 모델에서 데이터 복제를 완화하기 위한 반기억화 유도

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Diffusion Models|text-to-audio diffusion models]], [[keywords/Generative Models|generative audio models]]
**⚡ Unique Technical**: [[keywords/Anti-Memorization Strategies|anti-memorization strategies]]

## 🔗 유사한 논문
- [[Diffusion-Based_Unsupervised_Audio-Visual_Speech_Separation_in_Noisy_Environments_with_Noise_Prior_20250919|Diffusion-Based Unsupervised Audio-Visual Speech Separation in Noisy Environments with Noise Prior]] (80.2% similar)
- [[Mixture of Low-Rank Adapter Experts in Generalizable Audio Deepfake Detection]] (79.4% similar)
- [[Cross-Modal_Knowledge_Distillation_for_Speech_Large_Language_Models_20250919|Cross-Modal Knowledge Distillation for Speech Large Language Models]] (78.7% similar)
- [[Omni-CLST Error-aware Curriculum Learning with guided Selective chain-of-Thought for audio question answering]] (78.2% similar)
- [[SpeechOp Inference-Time Task Composition for Generative Speech Processing]] (77.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14934v1 Announce Type: cross 
Abstract: A persistent challenge in generative audio models is data replication, where the model unintentionally generates parts of its training data during inference. In this work, we address this issue in text-to-audio diffusion models by exploring the use of anti-memorization strategies. We adopt Anti-Memorization Guidance (AMG), a technique that modifies the sampling process of pre-trained diffusion models to discourage memorization. Our study explores three types of guidance within AMG, each designed to reduce replication while preserving generation quality. We use Stable Audio Open as our backbone, leveraging its fully open-source architecture and training dataset. Our comprehensive experimental analysis suggests that AMG significantly mitigates memorization in diffusion-based text-to-audio generation without compromising audio fidelity or semantic alignment.

## 🔍 Abstract (한글 번역)

arXiv:2509.14934v1 발표 유형: 교차  
초록: 생성적 오디오 모델에서 지속적인 문제는 데이터 복제이며, 이는 모델이 추론 중에 의도치 않게 훈련 데이터를 생성하는 경우를 말합니다. 본 연구에서는 텍스트-오디오 확산 모델에서 이 문제를 해결하기 위해 반기억화 전략의 사용을 탐구합니다. 우리는 사전 훈련된 확산 모델의 샘플링 과정을 수정하여 기억화를 방지하는 기술인 Anti-Memorization Guidance (AMG)를 채택합니다. 본 연구는 AMG 내에서 세 가지 유형의 가이던스를 탐구하며, 각각은 생성 품질을 유지하면서 복제를 줄이도록 설계되었습니다. 우리는 완전한 오픈 소스 아키텍처와 훈련 데이터셋을 활용하는 Stable Audio Open을 백본으로 사용합니다. 우리의 포괄적인 실험 분석은 AMG가 오디오 충실도나 의미적 정렬을 손상시키지 않으면서 확산 기반 텍스트-오디오 생성에서 기억화를 크게 완화한다는 것을 시사합니다.

## 📝 요약

이 논문은 텍스트-오디오 변환 확산 모델에서 발생하는 데이터 복제 문제를 해결하기 위해 반기억화 전략을 탐구합니다. Anti-Memorization Guidance(AMG) 기법을 사용하여 사전 학습된 확산 모델의 샘플링 과정을 수정함으로써 기억화를 방지하고자 합니다. 세 가지 유형의 AMG 가이드를 연구하여 복제를 줄이면서도 생성 품질을 유지합니다. Stable Audio Open의 오픈 소스 아키텍처와 데이터셋을 활용하여 실험한 결과, AMG가 오디오 생성의 기억화를 효과적으로 완화하면서도 음질이나 의미적 일치를 저해하지 않음을 확인했습니다.

## 🎯 주요 포인트

- 1. 생성 오디오 모델에서의 데이터 복제 문제를 해결하기 위해 반기억화 전략을 탐구했습니다.

- 2. Anti-Memorization Guidance(AMG)를 채택하여 사전 훈련된 확산 모델의 샘플링 과정을 수정했습니다.

- 3. AMG 내에서 복제를 줄이면서 생성 품질을 유지하기 위한 세 가지 유형의 가이던스를 탐구했습니다.

- 4. 실험 분석 결과, AMG가 오디오 충실도나 의미적 정렬을 손상시키지 않으면서 기억화를 크게 완화함을 확인했습니다.

- 5. Stable Audio Open의 완전한 오픈 소스 아키텍처와 훈련 데이터셋을 활용했습니다.

---

*Generated on 2025-09-19 15:36:32*