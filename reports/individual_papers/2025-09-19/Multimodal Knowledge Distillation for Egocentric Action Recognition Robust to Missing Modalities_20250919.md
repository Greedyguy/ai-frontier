---
keywords:
  - Multi-Modal Learning
  - Egocentric Action Recognition
  - Epic-Kitchens
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2504.08578
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:32:44.113560",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multi-Modal Learning",
    "Egocentric Action Recognition",
    "Epic-Kitchens"
  ],
  "rejected_keywords": [
    "Missing Modalities"
  ],
  "similarity_scores": {
    "Multi-Modal Learning": 0.82,
    "Egocentric Action Recognition": 0.79,
    "Epic-Kitchens": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Multimodal Knowledge Distillation for Egocentric Action Recognition Robust to Missing Modalities

**Korean Title:** 자가 결손 모달리티에 강인한 자가중심 행동 인식을 위한 다중 모달 지식 증류

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**⚡ Unique Technical**: [[keywords/Egocentric Action Recognition|Egocentric Action Recognition]], [[keywords/Epic-Kitchens|Epic-Kitchens]]
**🚀 Evolved Concepts**: [[keywords/Multi-Modal Learning|Multimodal Knowledge Distillation]]

## 🔗 유사한 논문
- [[MOCHA Multi-modal Objects-aware Cross-arcHitecture Alignment]] (84.9% similar)
- [[Cross-Modal Knowledge Distillation for Speech Large Language Models_20250919|Cross-Modal Knowledge Distillation for Speech Large Language Models]] (82.1% similar)
- [[Delta Knowledge Distillation for Large Language Models_20250919|Delta Knowledge Distillation for Large Language Models]] (81.4% similar)
- [[From Correction to Mastery Reinforced Distillation of Large Language Model Agents]] (80.0% similar)
- [[A Knowledge-driven Adaptive Collaboration of LLMs for Enhancing Medical Decision-making_20250919|A Knowledge-driven Adaptive Collaboration of LLMs for Enhancing Medical Decision-making]] (79.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2504.08578v2 Announce Type: replace 
Abstract: Existing methods for egocentric action recognition often rely solely on RGB videos, while additional modalities, e.g., audio, can improve accuracy in challenging scenarios. However, most prior multimodal approaches assume all modalities are available at inference, leading to significant accuracy drops, or even failure, when inputs are missing. To address this, we introduce KARMMA, a multimodal Knowledge distillation approach for egocentric Action Recognition robust to Missing ModAlities that requires no modality alignment across all samples during training or inference. KARMMA distills knowledge from a multimodal teacher into a multimodal student that benefits from all available modalities while remaining robust to missing ones, making it suitable for diverse multimodal scenarios without retraining. Our student uses approximately 50% fewer computational resources than our teacher, resulting in a lightweight and fast model. Experiments on Epic-Kitchens and Something-Something show that our student achieves competitive accuracy while significantly reducing accuracy drops under missing modality conditions.

## 🔍 Abstract (한글 번역)

arXiv:2504.08578v2 발표 유형: 교체  
초록: 기존의 자아중심 행동 인식 방법은 종종 RGB 비디오에만 의존하는 반면, 오디오와 같은 추가적인 모달리티는 어려운 상황에서 정확성을 향상시킬 수 있습니다. 그러나 대부분의 기존 다중 모달 접근법은 추론 시 모든 모달리티가 사용 가능하다고 가정하여 입력이 누락될 경우 상당한 정확도 저하 또는 실패를 초래합니다. 이를 해결하기 위해, 우리는 KARMMA를 소개합니다. KARMMA는 자아중심 행동 인식을 위한 다중 모달 지식 증류 접근법으로, 훈련이나 추론 동안 모든 샘플에 대해 모달리티 정렬이 필요하지 않으면서도 누락된 모달리티에 강인합니다. KARMMA는 다중 모달 교사로부터 다중 모달 학생에게 지식을 증류하여, 사용 가능한 모든 모달리티의 이점을 누리면서도 누락된 모달리티에 대해 강인성을 유지하여, 재훈련 없이 다양한 다중 모달 시나리오에 적합합니다. 우리의 학생 모델은 교사 모델에 비해 약 50% 적은 계산 자원을 사용하여 경량화되고 빠른 모델을 제공합니다. Epic-Kitchens와 Something-Something에 대한 실험 결과, 우리의 학생 모델은 누락된 모달리티 조건에서 정확도 저하를 크게 줄이면서도 경쟁력 있는 정확도를 달성합니다.

## 📝 요약

기존의 자아 중심 행동 인식 방법은 주로 RGB 비디오에 의존하지만, 오디오와 같은 추가 모달리티는 정확성을 높일 수 있습니다. 그러나 대부분의 다중 모달 접근법은 모든 모달리티가 제공된다는 가정 하에 작동하여, 입력이 누락될 경우 정확도가 크게 떨어집니다. 이를 해결하기 위해, 우리는 KARMMA라는 다중 모달 지식 증류 방법을 제안합니다. KARMMA는 훈련 및 추론 시 모든 샘플에 대해 모달리티 정렬이 필요 없으며, 누락된 모달리티에 대해 강건성을 유지합니다. 이 방법은 다중 모달 교사 모델의 지식을 다중 모달 학생 모델에 증류하여, 모든 사용 가능한 모달리티를 활용하면서도 누락된 모달리티에 대해 강건성을 유지합니다. KARMMA는 재훈련 없이 다양한 다중 모달 시나리오에 적합하며, 학생 모델은 교사 모델보다 약 50% 적은 계산 자원을 사용하여 경량화되고 빠릅니다. Epic-Kitchens와 Something-Something 데이터셋 실험에서, 학생 모델은 경쟁력 있는 정확성을 유지하면서도 누락된 모달리티 조건에서의 정확도 감소를 크게 줄였습니다.

## 🎯 주요 포인트

- 1. KARMMA는 egocentric action recognition에서 모달리티가 누락된 상황에서도 강력한 성능을 발휘하는 멀티모달 지식 증류 방법입니다.

- 2. KARMMA는 훈련이나 추론 시 모든 샘플에 대해 모달리티 정렬이 필요하지 않으며, 다양한 멀티모달 시나리오에 적합합니다.

- 3. KARMMA의 학생 모델은 교사 모델보다 약 50% 적은 계산 자원을 사용하여 경량화 및 빠른 모델을 제공합니다.

- 4. Epic-Kitchens와 Something-Something 데이터셋 실험에서 KARMMA의 학생 모델은 누락된 모달리티 조건에서도 경쟁력 있는 정확도를 유지합니다.

---

*Generated on 2025-09-19 16:17:21*