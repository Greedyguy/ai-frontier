<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:07:17.590153",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Model",
    "Optimal Transport",
    "Data Poisoning",
    "Zero-Shot Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision-Language Model": 0.85,
    "Optimal Transport": 0.78,
    "Data Poisoning": 0.8,
    "Zero-Shot Learning": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "CLIP",
        "canonical": "Vision-Language Model",
        "aliases": [
          "Contrastive Language-Image Pre-training"
        ],
        "category": "evolved_concepts",
        "rationale": "CLIP is a foundational model in vision-language tasks, linking it enhances understanding of multimodal learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Optimal Transport",
        "canonical": "Optimal Transport",
        "aliases": [
          "OT"
        ],
        "category": "unique_technical",
        "rationale": "Optimal Transport is a specialized mathematical approach crucial for the proposed framework, enhancing technical depth.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Data Poisoning",
        "canonical": "Data Poisoning",
        "aliases": [
          "Poisoning Attacks"
        ],
        "category": "unique_technical",
        "rationale": "Data poisoning is a critical threat in machine learning, and understanding it is vital for security-focused research.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "Zero-Shot Learning",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "ZSL"
        ],
        "category": "specific_connectable",
        "rationale": "Zero-shot learning is a key performance metric for CLIP, linking it supports exploration of model capabilities.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "CLIP",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Optimal Transport",
      "resolved_canonical": "Optimal Transport",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Data Poisoning",
      "resolved_canonical": "Data Poisoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Zero-Shot Learning",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Pre-training CLIP against Data Poisoning with Optimal Transport-based Matching and Alignment

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18717.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18717](https://arxiv.org/abs/2509.18717)

## 🔗 유사한 논문
- [[2025-09-23/Neural Antidote_ Class-Wise Prompt Tuning for Purifying Backdoors in CLIP_20250923|Neural Antidote: Class-Wise Prompt Tuning for Purifying Backdoors in CLIP]] (86.0% similar)
- [[2025-09-22/CLIPTTA_ Robust Contrastive Vision-Language Test-Time Adaptation_20250922|CLIPTTA: Robust Contrastive Vision-Language Test-Time Adaptation]] (85.0% similar)
- [[2025-09-23/CLIP-IN_ Enhancing Fine-Grained Visual Understanding in CLIP via Instruction Editing Data and Long Captions_20250923|CLIP-IN: Enhancing Fine-Grained Visual Understanding in CLIP via Instruction Editing Data and Long Captions]] (84.8% similar)
- [[2025-09-23/Test-Time Multimodal Backdoor Detection by Contrastive Prompting_20250923|Test-Time Multimodal Backdoor Detection by Contrastive Prompting]] (84.7% similar)
- [[2025-09-22/RegionMed-CLIP_ A Region-Aware Multimodal Contrastive Learning Pre-trained Model for Medical Image Understanding_20250922|RegionMed-CLIP: A Region-Aware Multimodal Contrastive Learning Pre-trained Model for Medical Image Understanding]] (83.5% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Optimal Transport|Optimal Transport]], [[keywords/Data Poisoning|Data Poisoning]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18717v1 Announce Type: new 
Abstract: Recent studies have shown that Contrastive Language-Image Pre-training (CLIP) models are threatened by targeted data poisoning and backdoor attacks due to massive training image-caption pairs crawled from the Internet. Previous defense methods correct poisoned image-caption pairs by matching a new caption for each image. However, the matching process relies solely on the global representations of images and captions, overlooking fine-grained features of visual and textual features. It may introduce incorrect image-caption pairs and harm the CLIP pre-training. To address their limitations, we propose an Optimal Transport-based framework to reconstruct image-caption pairs, named OTCCLIP. We propose a new optimal transport-based distance measure between fine-grained visual and textual feature sets and re-assign new captions based on the proposed optimal transport distance. Additionally, to further reduce the negative impact of mismatched pairs, we encourage the inter- and intra-modality fine-grained alignment by employing optimal transport-based objective functions. Our experiments demonstrate that OTCCLIP can successfully decrease the attack success rates of poisoning attacks. Also, compared to previous methods, OTCCLIP significantly improves CLIP's zero-shot and linear probing performance trained on poisoned datasets.

## 📝 요약

최근 연구에 따르면, 대규모 이미지-캡션 쌍을 활용하는 CLIP 모델이 데이터 중독 및 백도어 공격에 취약하다는 문제가 제기되었습니다. 기존 방어 방법은 이미지에 새로운 캡션을 매칭하여 중독된 쌍을 수정하지만, 이는 이미지와 캡션의 전역 표현에만 의존하여 세부 특징을 간과합니다. 이러한 한계를 극복하기 위해, 우리는 OTCCLIP이라는 최적 수송 기반 프레임워크를 제안합니다. 이 방법은 세부적인 시각 및 텍스트 특징 세트 간의 최적 수송 거리 측정을 통해 새로운 캡션을 재할당합니다. 또한, 최적 수송 기반 목표 함수를 사용하여 모달리티 간 및 내에서 세부 정렬을 촉진합니다. 실험 결과, OTCCLIP은 중독 공격의 성공률을 감소시키고, 이전 방법에 비해 CLIP의 제로샷 및 선형 탐색 성능을 크게 향상시킵니다.

## 🎯 주요 포인트

- 1. 대규모 인터넷 이미지-캡션 쌍으로 인해 CLIP 모델이 데이터 중독 및 백도어 공격에 취약하다는 최근 연구 결과가 있습니다.
- 2. 기존 방어 방법은 이미지에 새로운 캡션을 매칭하여 중독된 이미지-캡션 쌍을 수정하지만, 이는 이미지와 캡션의 전역 표현에만 의존하여 세밀한 특징을 간과합니다.
- 3. OTCCLIP은 최적 수송 기반의 거리 측정을 통해 세밀한 시각 및 텍스트 특징 세트 간의 새로운 캡션을 재할당하는 프레임워크입니다.
- 4. OTCCLIP은 최적 수송 기반의 목표 함수를 사용하여 모달리티 간 및 모달리티 내 세밀한 정렬을 촉진하여 잘못 매칭된 쌍의 부정적 영향을 줄입니다.
- 5. 실험 결과, OTCCLIP은 중독 공격의 성공률을 감소시키고, 이전 방법에 비해 CLIP의 제로샷 및 선형 탐색 성능을 크게 향상시킵니다.


---

*Generated on 2025-09-24 16:07:17*