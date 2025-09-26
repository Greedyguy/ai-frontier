---
keywords:
  - Vision-Language Model
  - Intermediate Projector
  - Transformer
  - Residual Query Alignment
  - Multimodal Learning
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2508.13739
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:26:59.430875",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Model",
    "Intermediate Projector",
    "Transformer",
    "Residual Query Alignment",
    "Multimodal Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision-Language Model": 0.85,
    "Intermediate Projector": 0.79,
    "Transformer": 0.82,
    "Residual Query Alignment": 0.77,
    "Multimodal Learning": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Vision-Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLM",
          "Vision-Language"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models are central to the paper's focus on adversarial attacks, providing strong linkage to multimodal learning discussions.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Intermediate Projector",
        "canonical": "Intermediate Projector",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The Intermediate Projector is a novel component proposed in the paper, crucial for enhancing attack granularity and transferability.",
        "novelty_score": 0.78,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      },
      {
        "surface": "Querying Transformer",
        "canonical": "Transformer",
        "aliases": [
          "Q-Former"
        ],
        "category": "broad_technical",
        "rationale": "The Querying Transformer is a key mechanism for transforming embeddings, linking to broader Transformer discussions.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "Residual Query Alignment",
        "canonical": "Residual Query Alignment",
        "aliases": [
          "RQA"
        ],
        "category": "unique_technical",
        "rationale": "Residual Query Alignment is a specialized module introduced in the paper, enhancing the specificity of fine-grained attacks.",
        "novelty_score": 0.81,
        "connectivity_score": 0.55,
        "specificity_score": 0.88,
        "link_intent_score": 0.77
      },
      {
        "surface": "Multimodal Alignment",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal"
        ],
        "category": "specific_connectable",
        "rationale": "Multimodal Alignment is essential for understanding the interaction between visual and language components in VLMs.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.68,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "black-box",
      "attack framework",
      "baseline"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Vision-Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Intermediate Projector",
      "resolved_canonical": "Intermediate Projector",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Querying Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Residual Query Alignment",
      "resolved_canonical": "Residual Query Alignment",
      "decision": "linked",
      "scores": {
        "novelty": 0.81,
        "connectivity": 0.55,
        "specificity": 0.88,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Multimodal Alignment",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.68,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Enhancing Targeted Adversarial Attacks on Large Vision-Language Models via Intermediate Projector

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2508.13739.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2508.13739](https://arxiv.org/abs/2508.13739)

## 🔗 유사한 논문
- [[2025-09-23/ADVEDM_Fine-grained Adversarial Attack against VLM-based Embodied Agents_20250923|ADVEDM:Fine-grained Adversarial Attack against VLM-based Embodied Agents]] (86.2% similar)
- [[2025-09-22/Robust Vision-Language Models via Tensor Decomposition_ A Defense Against Adversarial Attacks_20250922|Robust Vision-Language Models via Tensor Decomposition: A Defense Against Adversarial Attacks]] (85.8% similar)
- [[2025-09-25/FreezeVLA_ Action-Freezing Attacks against Vision-Language-Action Models_20250925|FreezeVLA: Action-Freezing Attacks against Vision-Language-Action Models]] (85.4% similar)
- [[2025-09-25/Semantic Representation Attack against Aligned Large Language Models_20250925|Semantic Representation Attack against Aligned Large Language Models]] (85.3% similar)
- [[2025-09-23/Sugar-Coated Poison_ Benign Generation Unlocks LLM Jailbreaking_20250923|Sugar-Coated Poison: Benign Generation Unlocks LLM Jailbreaking]] (84.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Intermediate Projector|Intermediate Projector]], [[keywords/Residual Query Alignment|Residual Query Alignment]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.13739v2 Announce Type: replace 
Abstract: The growing deployment of Large Vision-Language Models (VLMs) raises safety concerns, as adversaries may exploit model vulnerabilities to induce harmful outputs, with targeted black-box adversarial attacks posing a particularly severe threat. However, existing methods primarily maximize encoder-level global similarity, which lacks the granularity for stealthy and practical fine-grained attacks, where only specific target should be altered (e.g., modifying a car while preserving its background). Moreover, they largely neglect the projector, a key semantic bridge in VLMs for multimodal alignment. To address these limitations, we propose a novel black-box targeted attack framework that leverages the projector. Specifically, we utilize the widely adopted Querying Transformer (Q-Former) which transforms global image embeddings into fine-grained query outputs, to enhance attack effectiveness and granularity. For standard global targeted attack scenarios, we propose the Intermediate Projector Guided Attack (IPGA), which aligns Q-Former fine-grained query outputs with the target to enhance attack strength and exploits the intermediate pretrained Q-Former that is not fine-tuned for any specific Large Language Model (LLM) to improve attack transferability. For fine-grained attack scenarios, we augment IPGA with the Residual Query Alignment (RQA) module, which preserves unrelated content by constraining non-target query outputs to enhance attack granularity. Extensive experiments demonstrate that IPGA significantly outperforms baselines in global targeted attacks, and IPGA with RQA (IPGA-R) attains superior success rates and unrelated content preservation over baselines in fine-grained attacks. Our method also transfers effectively to commercial VLMs such as Google Gemini and OpenAI GPT.

## 📝 요약

이 논문은 대형 비전-언어 모델(VLM)의 안전성 문제를 다루며, 특히 블랙박스 공격의 위협을 강조합니다. 기존 방법들은 주로 인코더 수준의 전역 유사성을 극대화하지만, 이는 세밀한 공격에는 적합하지 않습니다. 이에 대해, 우리는 프로젝터를 활용한 새로운 블랙박스 공격 프레임워크를 제안합니다. 이 방법은 Q-Former를 사용하여 전역 이미지 임베딩을 세밀한 쿼리 출력으로 변환하여 공격의 효과와 세밀성을 높입니다. 또한, IPGA와 RQA 모듈을 통해 비표적 쿼리 출력을 제약하여 공격의 세밀성을 강화합니다. 실험 결과, 제안된 방법은 기존 방법들보다 높은 성공률과 비관련 콘텐츠 보존 능력을 보이며, 상업적 VLM에도 효과적으로 전이됩니다.

## 🎯 주요 포인트

- 1. 대규모 비전-언어 모델(VLM)의 보급이 증가함에 따라, 모델의 취약점을 악용하여 유해한 출력을 유도하는 공격에 대한 안전성 우려가 제기되고 있습니다.
- 2. 기존 방법들은 주로 인코더 수준의 전역 유사성을 극대화하지만, 세밀한 표적 공격에는 적합하지 않으며, 프로젝터의 역할을 간과하고 있습니다.
- 3. 우리는 Q-Former를 활용하여 공격의 효과성과 세밀함을 향상시키는 새로운 블랙박스 표적 공격 프레임워크를 제안합니다.
- 4. IPGA는 Q-Former의 세밀한 쿼리 출력을 표적과 정렬하여 공격 강도를 높이고, 특정 대형 언어 모델(LLM)에 맞춰 조정되지 않은 중간 사전 훈련된 Q-Former를 활용하여 공격 전이성을 개선합니다.
- 5. 실험 결과, IPGA는 전역 표적 공격에서 기존 방법보다 뛰어난 성능을 보였으며, IPGA-R은 세밀한 공격에서 높은 성공률과 비관련 콘텐츠 보존을 달성했습니다.


---

*Generated on 2025-09-26 09:26:59*