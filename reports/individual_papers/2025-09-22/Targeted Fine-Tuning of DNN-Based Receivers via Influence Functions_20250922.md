---
keywords:
  - Deep Learning
  - Influence Functions
  - Receiver Adaptation
  - Bit Error Rate
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.15950
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:39:07.413957",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Learning",
    "Influence Functions",
    "Receiver Adaptation",
    "Bit Error Rate"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deep Learning": 0.85,
    "Influence Functions": 0.9,
    "Receiver Adaptation": 0.82,
    "Bit Error Rate": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Deep Learning",
        "canonical": "Deep Learning",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Deep Learning is a foundational concept for understanding the use of influence functions in neural networks.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.85
      },
      {
        "surface": "Influence Functions",
        "canonical": "Influence Functions",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Influence Functions are central to the paper's methodology for improving receiver performance.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.9
      },
      {
        "surface": "Receiver Adaptation",
        "canonical": "Receiver Adaptation",
        "aliases": [
          "Receiver Fine-Tuning"
        ],
        "category": "specific_connectable",
        "rationale": "Receiver Adaptation is a specific application of influence functions, linking to broader adaptation strategies.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.82
      },
      {
        "surface": "Bit Error Rate",
        "canonical": "Bit Error Rate",
        "aliases": [
          "BER"
        ],
        "category": "specific_connectable",
        "rationale": "Bit Error Rate is a key performance metric in evaluating the effectiveness of the proposed methods.",
        "novelty_score": 0.55,
        "connectivity_score": 0.68,
        "specificity_score": 0.77,
        "link_intent_score": 0.8
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
      "candidate_surface": "Deep Learning",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.5,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Influence Functions",
      "resolved_canonical": "Influence Functions",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Receiver Adaptation",
      "resolved_canonical": "Receiver Adaptation",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Bit Error Rate",
      "resolved_canonical": "Bit Error Rate",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.68,
        "specificity": 0.77,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Targeted Fine-Tuning of DNN-Based Receivers via Influence Functions

**Korean Title:** DNN 기반 수신기의 목표 지향적 미세 조정을 위한 영향 함수 활용

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15950.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.15950](https://arxiv.org/abs/2509.15950)

## 🔗 유사한 논문
- [[2025-09-22/Neural Networks for Learnable and Scalable Influence Estimation of Instruction Fine-Tuning Data_20250922|Neural Networks for Learnable and Scalable Influence Estimation of Instruction Fine-Tuning Data]] (82.5% similar)
- [[2025-09-22/Toward Efficient Influence Function_ Dropout as a Compression Tool_20250922|Toward Efficient Influence Function: Dropout as a Compression Tool]] (80.8% similar)
- [[2025-09-22/Analog In-memory Training on General Non-ideal Resistive Elements_ The Impact of Response Functions_20250922|Analog In-memory Training on General Non-ideal Resistive Elements: The Impact of Response Functions]] (78.5% similar)
- [[2025-09-22/The Alignment Bottleneck_20250922|The Alignment Bottleneck]] (78.0% similar)
- [[2025-09-22/MoE-CE_ Enhancing Generalization for Deep Learning based Channel Estimation via a Mixture-of-Experts Framework_20250922|MoE-CE: Enhancing Generalization for Deep Learning based Channel Estimation via a Mixture-of-Experts Framework]] (77.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Receiver Adaptation|Receiver Adaptation]], [[keywords/Bit Error Rate|Bit Error Rate]]
**⚡ Unique Technical**: [[keywords/Influence Functions|Influence Functions]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15950v1 Announce Type: new 
Abstract: We present the first use of influence functions for deep learning-based wireless receivers. Applied to DeepRx, a fully convolutional receiver, influence analysis reveals which training samples drive bit predictions, enabling targeted fine-tuning of poorly performing cases. We show that loss-relative influence with capacity-like binary cross-entropy loss and first-order updates on beneficial samples most consistently improves bit error rate toward genie-aided performance, outperforming random fine-tuning in single-target scenarios. Multi-target adaptation proved less effective, underscoring open challenges. Beyond experiments, we connect influence to self-influence corrections and propose a second-order, influence-aligned update strategy. Our results establish influence functions as both an interpretability tool and a basis for efficient receiver adaptation.

## 🔍 Abstract (한글 번역)

arXiv:2509.15950v1 발표 유형: 신규  
초록: 우리는 딥러닝 기반 무선 수신기에 대한 영향 함수의 첫 번째 사용을 소개합니다. 완전한 컨볼루션 수신기인 DeepRx에 적용된 영향 분석은 어떤 학습 샘플이 비트 예측에 영향을 미치는지를 밝혀내어 성능이 저조한 사례를 목표로 한 미세 조정을 가능하게 합니다. 용량과 유사한 이진 교차 엔트로피 손실과 유익한 샘플에 대한 일차 업데이트를 사용한 손실 상대적 영향이 비트 오류율을 지니 보조 성능에 가장 일관되게 향상시키며, 단일 목표 시나리오에서 무작위 미세 조정보다 뛰어남을 보여줍니다. 다중 목표 적응은 덜 효과적임이 입증되어 해결해야 할 과제를 강조합니다. 실험을 넘어, 우리는 영향을 자기 영향 수정과 연결하고, 두 번째 차수의 영향 정렬 업데이트 전략을 제안합니다. 우리의 결과는 영향 함수를 해석 가능성 도구이자 효율적인 수신기 적응의 기초로 확립합니다.

## 📝 요약

이 논문은 딥러닝 기반 무선 수신기에서 영향 함수의 첫 번째 활용을 소개합니다. DeepRx라는 완전한 합성곱 수신기에 영향 분석을 적용하여 어떤 훈련 샘플이 비트 예측에 영향을 미치는지를 밝혀내고, 이를 통해 성능이 저조한 사례를 목표로 한 미세 조정이 가능합니다. 연구 결과, 손실-상대적 영향과 용량과 유사한 이진 교차 엔트로피 손실을 사용한 유익한 샘플의 1차 업데이트가 비트 오류율을 개선하는 데 가장 효과적임을 보여주었습니다. 다중 목표 적응은 덜 효과적이었으며, 이는 해결해야 할 과제를 시사합니다. 또한, 자기 영향 수정과의 연결을 통해 2차 영향 정렬 업데이트 전략을 제안하였습니다. 이 연구는 영향 함수를 해석 가능성 도구이자 효율적인 수신기 적응의 기초로 확립했습니다.

## 🎯 주요 포인트

- 1. 딥러닝 기반 무선 수신기에 영향 함수가 처음으로 사용되었습니다.
- 2. DeepRx 수신기에 대한 영향 분석을 통해 훈련 샘플이 비트 예측에 미치는 영향을 파악하고, 성능이 저조한 사례를 대상으로 세밀한 조정이 가능해졌습니다.
- 3. 용량과 유사한 이진 교차 엔트로피 손실과 유익한 샘플에 대한 1차 업데이트를 통해 비트 오류율이 개선되었습니다.
- 4. 다중 타겟 적응은 덜 효과적이었으며, 이는 해결해야 할 과제를 남겼습니다.
- 5. 영향 함수를 해석 가능성 도구 및 효율적인 수신기 적응의 기초로 활용할 수 있음을 입증했습니다.


---

*Generated on 2025-09-23 10:39:07*