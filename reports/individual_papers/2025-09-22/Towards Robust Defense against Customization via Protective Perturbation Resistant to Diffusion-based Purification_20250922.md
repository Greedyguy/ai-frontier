---
keywords:
  - Diffusion Models
  - Protective Perturbation
  - Purification-Customization Workflow
  - AntiPure
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.13922
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:40:17.605136",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion Models",
    "Protective Perturbation",
    "Purification-Customization Workflow",
    "AntiPure"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Diffusion Models": 0.82,
    "Protective Perturbation": 0.78,
    "Purification-Customization Workflow": 0.77,
    "AntiPure": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Diffusion Models",
        "canonical": "Diffusion Models",
        "aliases": [
          "Stable Diffusion"
        ],
        "category": "specific_connectable",
        "rationale": "Diffusion models are central to the paper's focus on visual synthesis and security risks, making them a key concept for linking.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Protective Perturbation",
        "canonical": "Protective Perturbation",
        "aliases": [
          "Adversarial Noise"
        ],
        "category": "unique_technical",
        "rationale": "This concept is unique to the paper's proposed solution for safeguarding images, offering a novel approach to link.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Purification-Customization Workflow",
        "canonical": "Purification-Customization Workflow",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This workflow is a specific process discussed in the paper, providing a unique context for linking related research.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      },
      {
        "surface": "AntiPure",
        "canonical": "AntiPure",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "AntiPure is the novel method introduced in the paper, essential for understanding its contributions.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Diffusion Models",
      "resolved_canonical": "Diffusion Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Protective Perturbation",
      "resolved_canonical": "Protective Perturbation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Purification-Customization Workflow",
      "resolved_canonical": "Purification-Customization Workflow",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "AntiPure",
      "resolved_canonical": "AntiPure",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Towards Robust Defense against Customization via Protective Perturbation Resistant to Diffusion-based Purification

**Korean Title:** 확산 기반 정화를 저항하는 보호적 섭동을 통한 맞춤화에 대한 강력한 방어를 향하여

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.13922.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.13922](https://arxiv.org/abs/2509.13922)

## 🔗 유사한 논문
- [[2025-09-19/Controllable Localized Face Anonymization Via Diffusion Inpainting_20250919|Controllable Localized Face Anonymization Via Diffusion Inpainting]] (80.7% similar)
- [[2025-09-19/End4_ End-to-end Denoising Diffusion for Diffusion-Based Inpainting Detection_20250919|End4: End-to-end Denoising Diffusion for Diffusion-Based Inpainting Detection]] (80.7% similar)
- [[2025-09-17/Defending Diffusion Models Against Membership Inference Attacks via Higher-Order Langevin Dynamics_20250917|Defending Diffusion Models Against Membership Inference Attacks via Higher-Order Langevin Dynamics]] (79.9% similar)
- [[2025-09-22/RespoDiff_ Dual-Module Bottleneck Transformation for Responsible & Faithful T2I Generation_20250922|RespoDiff: Dual-Module Bottleneck Transformation for Responsible & Faithful T2I Generation]] (79.4% similar)
- [[2025-09-22/Personalized Language Models via Privacy-Preserving Evolutionary Model Merging_20250922|Personalized Language Models via Privacy-Preserving Evolutionary Model Merging]] (79.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Diffusion Models|Diffusion Models]]
**⚡ Unique Technical**: [[keywords/Protective Perturbation|Protective Perturbation]], [[keywords/Purification-Customization Workflow|Purification-Customization Workflow]], [[keywords/AntiPure|AntiPure]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13922v2 Announce Type: replace 
Abstract: Diffusion models like Stable Diffusion have become prominent in visual synthesis tasks due to their powerful customization capabilities, which also introduce significant security risks, including deepfakes and copyright infringement. In response, a class of methods known as protective perturbation emerged, which mitigates image misuse by injecting imperceptible adversarial noise. However, purification can remove protective perturbations, thereby exposing images again to the risk of malicious forgery. In this work, we formalize the anti-purification task, highlighting challenges that hinder existing approaches, and propose a simple diagnostic protective perturbation named AntiPure. AntiPure exposes vulnerabilities of purification within the "purification-customization" workflow, owing to two guidance mechanisms: 1) Patch-wise Frequency Guidance, which reduces the model's influence over high-frequency components in the purified image, and 2) Erroneous Timestep Guidance, which disrupts the model's denoising strategy across different timesteps. With additional guidance, AntiPure embeds imperceptible perturbations that persist under representative purification settings, achieving effective post-customization distortion. Experiments show that, as a stress test for purification, AntiPure achieves minimal perceptual discrepancy and maximal distortion, outperforming other protective perturbation methods within the purification-customization workflow.

## 🔍 Abstract (한글 번역)

arXiv:2509.13922v2 발표 유형: 교체  
초록: Stable Diffusion과 같은 확산 모델은 강력한 맞춤화 기능 덕분에 시각적 합성 작업에서 두각을 나타내고 있습니다. 그러나 이러한 기능은 딥페이크 및 저작권 침해와 같은 중대한 보안 위험도 초래합니다. 이에 대응하여, 보호적 섭동(protective perturbation)이라는 방법이 등장했으며, 이는 인지할 수 없는 적대적 노이즈를 주입하여 이미지 남용을 완화합니다. 그러나 정화(purification)는 보호적 섭동을 제거할 수 있어 이미지를 다시 악의적인 위조의 위험에 노출시킬 수 있습니다. 본 연구에서는 반정화(anti-purification) 작업을 공식화하고 기존 접근 방식을 방해하는 문제를 강조하며, AntiPure라는 간단한 진단 보호 섭동을 제안합니다. AntiPure는 "정화-맞춤화" 워크플로 내에서 정화의 취약점을 드러내며, 두 가지 안내 메커니즘 덕분에 효과를 발휘합니다: 1) 패치 단위 주파수 안내(Patch-wise Frequency Guidance)는 정화된 이미지의 고주파 성분에 대한 모델의 영향을 줄이고, 2) 잘못된 시간 단계 안내(Erroneous Timestep Guidance)는 다양한 시간 단계에 걸쳐 모델의 노이즈 제거 전략을 방해합니다. 추가 안내와 함께, AntiPure는 대표적인 정화 설정에서도 지속되는 인지할 수 없는 섭동을 내재화하여 효과적인 맞춤화 후 왜곡을 달성합니다. 실험 결과, AntiPure는 정화에 대한 스트레스 테스트로서 최소한의 지각적 불일치와 최대의 왜곡을 달성하여 정화-맞춤화 워크플로 내에서 다른 보호적 섭동 방법을 능가합니다.

## 📝 요약

이 논문은 이미지 합성 작업에서 보안 위험을 줄이기 위한 보호적 섭동 기법을 다룹니다. 기존의 보호적 섭동은 이미지 오용을 방지하지만, 정화 과정에서 제거될 수 있어 이미지가 다시 위조 위험에 노출됩니다. 이를 해결하기 위해 저자들은 '정화 방지' 작업을 공식화하고, 'AntiPure'라는 진단적 보호 섭동 방법을 제안합니다. AntiPure는 두 가지 가이드 메커니즘을 통해 정화-맞춤화 워크플로우의 취약점을 드러냅니다: 1) 패치 기반 주파수 가이드, 2) 오류 타임스텝 가이드. 실험 결과, AntiPure는 정화 후에도 섭동을 유지하며, 기존 방법보다 더 효과적인 왜곡을 달성합니다.

## 🎯 주요 포인트

- 1. 확산 모델은 강력한 커스터마이징 기능으로 인해 시각적 합성 작업에서 두각을 나타내지만, 보안 위험도 함께 증가시킵니다.
- 2. 보호적 섭동은 이미지 오용을 방지하기 위해 미세한 적대적 노이즈를 주입하는 방법으로 등장했습니다.
- 3. 정화 과정은 보호적 섭동을 제거할 수 있어 이미지가 다시 악의적인 위조에 노출될 위험이 있습니다.
- 4. AntiPure는 정화-커스터마이징 워크플로우 내에서 정화의 취약점을 드러내기 위해 설계된 진단적 보호 섭동입니다.
- 5. 실험 결과, AntiPure는 정화-커스터마이징 워크플로우 내에서 다른 보호적 섭동 방법보다 뛰어난 왜곡 효과를 발휘합니다.


---

*Generated on 2025-09-23 12:40:17*